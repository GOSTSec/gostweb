from celery import shared_task
from django.db import transaction
from django.conf import settings

from decimal import Decimal

from .models import Account, Address, DepositTransaction, WithdrawalTransaction

from .gostcoin import GOSTCOIN_CONNECTION as conn

@shared_task
def check_transactions_task():
    check_received_transactions(conn)
    check_confirmed_transactions(conn)

def check_received_transactions(conn):
    for t in conn.listtransactions("", 100):
        if "txid" not in t:
            continue
        elif t["category"] == "receive":
            try:
                tx = DepositTransaction.objects.get(txid=t["txid"])
            except DepositTransaction.DoesNotExist:
                try:
                    address = Address.objects.get(address=t["address"])
                    if not address.used:
                        address.used = True
                        address.save()
                        # create new address
                        Address.objects.create(account=address.account,
                                address=conn.getnewaddress(), used=False)
                    DepositTransaction.objects.create(account=address.account, 
                        txid=t["txid"], address=address, confirmed=False)
                except Address.DoesNotExist:
                    continue

def check_confirmed_transactions(conn):
    """
    Looks for unconfirmed transactions in the database
    checks if they are confirmed in gostd
    add received coins to balance
    """
    unconfirmed_recv = DepositTransaction.objects.filter(confirmed=False)
    for t in unconfirmed_recv:
        result = conn.gettransaction(t.txid)
        if result["confirmations"] >= 6:
            amount = Decimal("0")

            for d in result["details"]:
                if d["category"] == "receive" and d["address"] == t.address.address:
                    amount += d["amount"]

            with transaction.atomic():
                t.amount = amount
                t.confirmed = True
                t.save()
                t.account.balance += amount
                t.account.save()

    unconfirmed_send = WithdrawalTransaction.objects.filter(confirmed=False)
    for t in unconfirmed_send:
        result = conn.gettransaction(t.txid)
        if result["confirmations"] >= 6:
            t.confirmed = True
            t.save()

