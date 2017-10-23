from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .forms import SendCoins
from .models import Account, WithdrawalTransaction
from .gostcoin import GostCoinException, create_raw_tx
from .gostcoin import GOSTCOIN_CONNECTION as conn

import logging
logger = logging.getLogger("django")

@login_required
def index(request):
    form = SendCoins(request.POST or None, user=request.user)

    if request.method == "POST" and form.is_valid():
        recipient, amount = form.cleaned_data["recipient"], \
                form.cleaned_data["amount"]
        local_transfer = len(recipient) == 16
        if local_transfer:
            total_amount = amount
        else:
            if not conn.validateaddress(recipient)["isvalid"]:
                raise GostCoinException("Invalid address")

            total_amount = amount + settings.GST_NETWORK_FEE + \
                    settings.SERVICE_FEE

        # TODO: check if address exists, then transfer locally
        with transaction.atomic():
            a = Account.objects.select_for_update().get(user=request.user)
            if recipient == a.name:
                raise GostCoinException("Can't transfer to yourself")
            if total_amount > a.balance:
                raise GostCoinException("Not enough coins on balance")

            if local_transfer:
                n = Account.objects.select_for_update().get(name=recipient)
                a.balance -= total_amount
                a.save()
                n.balance += total_amount
                n.save()
                messages.success(request, "Transfer succeeded")
                form = SendCoins()
            else:
                a.balance -= total_amount
                a.save()
                form = SendCoins()

        if not local_transfer:
            rawtx = create_raw_tx(conn, recipient, amount)
            txid = conn.sendrawtransaction(
                    conn.signrawtransaction(rawtx)["hex"])
            messages.success(request, 
                    "Transfer succeeded. Transaction id: {}".format(txid))
            WithdrawalTransaction.objects.create(account=request.user.account, 
                txid=txid, address=recipient, amount=amount, confirmed=False)

        request.user.account.refresh_from_db()

    context = {
        "fees": {"network": settings.GST_NETWORK_FEE,
                "service": settings.SERVICE_FEE},
        "address": request.user.account.address_set.filter(used=False).first().address,
        "balance": request.user.account.balance,
        "deposit_transactions": request.user.account.deposittransaction_set.all(),
        "withdrawal_transactions": request.user.account.withdrawaltransaction_set.all(),
        "form": form
    }

    return render(request, "wallet/index_page.html", context)

