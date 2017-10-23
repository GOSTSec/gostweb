from django.conf import settings 
from bitcoinrpc.authproxy import AuthServiceProxy

def select_inputs(conn, amount):
    """Select unspent inputs to craft tx"""
    unspent_inputs = conn.listunspent(0)
    unspent_inputs.sort(key=lambda u: u['amount'] * u['confirmations'], 
            reverse=True)

    inputs, total = [], 0
    for usin in unspent_inputs:
        inputs.append(usin)
        total += usin["amount"]
        if total >= amount: break

    if total < amount:
        raise GostCoinException("Not enough coins on the server")

    return inputs, total

def create_raw_tx(conn, address, amount):
    """Prepare raw transaction and return with output amount"""
    # TODO calculate fee per kB
    output_amount = amount + settings.GST_NETWORK_FEE
    inputs, total = select_inputs(conn, output_amount)

    change_amount = total - output_amount
    outputs = {address: amount}
    if change_amount > settings.GST_DUST:
        outputs[settings.GST_CHANGE_ADDRESS] = change_amount

    return conn.createrawtransaction(inputs, outputs)


class GostCoinException(Exception):
    """
    Raised when something is wrong with account balance
    """
    pass


GOSTCOIN_CONNECTION = AuthServiceProxy(settings.COIN_CONNECTION)
