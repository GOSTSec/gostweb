from django.test import TestCase, SimpleTestCase
from unittest.mock import MagicMock

from django.contrib.auth.models import User
from django.conf import settings
from decimal import Decimal

from wallet.models import Account, Address, DepositTransaction
from wallet.forms import SendCoins
from wallet.tasks import check_received_transactions, check_confirmed_transactions

from wallet.tests.fake_data import DEMO_TRANSACTIONS, DEMO_UNSPENT, DEMO_DATA_1
from wallet import gostcoin

from integral_auth.utils import rand_string

class SendCoinsFormTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("tester", password="asdasdasd")
        Account.objects.create(user=self.user, name="A2aac03D5F5Adae0")

    def test_valid_data(self):
        form = SendCoins({"recipient": "GPem1MVc49r7dxsUDL4sKFvq79rCtqs5Sx", 
            "amount": "0.1"})
        self.assertTrue(form.is_valid())
        form = SendCoins({"recipient": self.user.account.name, "amount": "1"})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = SendCoins({})
        self.assertFalse(form.is_valid())

        form = SendCoins({"recipient": self.user.account.name})
        self.assertFalse(form.is_valid())

        form = SendCoins({"recipient": self.user.account.name, "amount": ""})
        self.assertFalse(form.is_valid())

        form = SendCoins({"amount": "1"})
        self.assertFalse(form.is_valid())

        form = SendCoins({"recipient": "GPem1MVc49r7dxsUDL4sKFvq79rCtqs5Sx", 
            "amount": "aaaa"})
        self.assertFalse(form.is_valid())

        form = SendCoins({"recipient": "GPem1MVc49r7dxsUDL4sKFvq79rCtqs5Sx", 
            "amount": "0.000000001"})
        self.assertFalse(form.is_valid())

        form = SendCoins({"recipient": "GPem1MVc49r7dxsUDL4sKFvq79rCtqs5Sx", 
            "amount": "0.0099"})
        self.assertFalse(form.is_valid())

        form = SendCoins({"recipient": "GPem1MVc49r7dxsUDL4sKFvq79rCtqs5Sx",
            "amount": "-0.1"})
        self.assertFalse(form.is_valid())


        form = SendCoins({"recipient": "GPem1MVc49r7dxsUDL4sKFvq79rCtqs5Sx00", 
            "amount": "0.1"})
        self.assertFalse(form.is_valid())

        form = SendCoins({"recipient": "aaa", 
            "amount": "0.1"})
        self.assertFalse(form.is_valid())

        form = SendCoins({"recipient": ")%$#", 
            "amount": "0.1"})
        self.assertFalse(form.is_valid())

        form = SendCoins({"recipient": "abcdEFGH123456780", "amount": "1"})
        self.assertFalse(form.is_valid())

        form = SendCoins({"recipient": "APem1MVc49r7dxsUDL4sKFvq79rCtqs5Sx", 
            "amount": "0.1"})
        self.assertFalse(form.is_valid())

    def test_valid_cleaned_data(self):
        form = SendCoins({"recipient": "GPem1MVc49r7dxsUDL4sKFvq79rCtqs5Sx", 
            "amount": "0.1"})
        form.is_valid()

        self.assertEqual(form.cleaned_data["amount"], Decimal("0.1"))

    def test_with_balance(self):
        self.user.account.balance = 100
        self.user.account.save()
        form = SendCoins({"recipient": "GPem1MVc49r7dxsUDL4sKFvq79rCtqs5Sx", 
            "amount": "1"}, user=self.user)
        self.assertTrue(form.is_valid())

    def test_without_balance(self):
        self.user.account.balance = 1
        self.user.account.save()
        form = SendCoins({"recipient": "GPem1MVc49r7dxsUDL4sKFvq79rCtqs5Sx", 
            "amount": "100"}, user=self.user)
        self.assertFalse(form.is_valid())

    def test_without_fee_balance(self):
        with self.settings(GST_NETWORK_FEE=Decimal('0.02'), 
                           SERVICE_FEE=Decimal('0.0')):
            self.user.account.balance = 100
            self.user.account.save()
            form = SendCoins({"recipient": "GPem1MVc49r7dxsUDL4sKFvq79rCtqs5Sx",
                "amount": "100"}, user=self.user)
            self.assertFalse(form.is_valid())

class AccountModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("tester", password="asdasdasd")
        Account.objects.create(user=self.user, name="A2aac03D5F5Adae0")
        self.user2 = User.objects.create_user("tester2", password="asdasdasd")
        Account.objects.create(user=self.user2, name="B6cac03D5F5Adae0")


class GostcoinTests(TestCase):

    def test_select_inputs(self):
        conn = MagicMock()
        conn.listunspent.return_value = DEMO_UNSPENT

        inputs, total = gostcoin.select_inputs(conn, Decimal("212"))
        self.assertEquals(total, Decimal("233.06"))
        self.assertEquals(len(inputs), 3)

    def test_create_raw_tx(self):
        conn = MagicMock()
        conn.listunspent.return_value = DEMO_DATA_1["listunspent"]
        conn.createrawtransaction.return_value = DEMO_DATA_1["createrawtransaction"]
        rawtx = gostcoin.create_raw_tx(conn,
                "GXaNvzURu4fRAkjSodybjcXnwwUPKxB6rQ", Decimal("212"))
        self.assertEquals(rawtx, DEMO_DATA_1["createrawtransaction"])


class CeleryTaskTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("tester", password="asdasdasd")
        Account.objects.create(user=self.user, name="A2aac03D5F5Adae0")
        self.user2 = User.objects.create_user("tester2", password="asdasdasd")
        Account.objects.create(user=self.user2, name="B6cac03D5F5Adae0")


    def test_check_received_transactions(self):
        Address.objects.create(account=self.user.account, used=False,
                address="GXaNvzURu4fRAkjSodybjcXnwwUPKxB6rQ")
        Address.objects.create(account=self.user2.account, used=False,
                address="GHwVSdza9QB5zPa9kZWjFdByynTAtDb6M9")

        conn = MagicMock()
        conn.listtransactions.return_value = DEMO_TRANSACTIONS
        conn.getnewaddress = lambda: "G" + rand_string(33)

        result = check_received_transactions(conn)

        tx = DepositTransaction.objects.get(
            txid='3c03439fab4f53c97185e66217fe5fe61cdc4e80b25dfe5a0d19bf0b8c77f994')
        self.assertEqual(tx.account, self.user.account)
        self.assertEqual(tx.address.used, True)

        self.assertEqual(self.user.account.address_set.filter(used=True).first().used, True)

        tx = DepositTransaction.objects.get(
            txid='a94b83eec4f267aa503cc9ec65a229350cae60799ff73c28283a7aa5dad15435')
        self.assertEqual(tx.account, self.user2.account)
        self.assertEqual(tx.address.used, True)

    def test_check_confirmed_transactions(self):
        Address.objects.create(account=self.user.account, used=False,
                address="GXaNvzURu4fRAkjSodybjcXnwwUPKxB6rQ")

        conn = MagicMock()
        conn.listtransactions.return_value = DEMO_TRANSACTIONS
        conn.gettransaction.return_value = {'time': 1491951811, 'blocktime': 1491951914, 'txid': '3c03439fab4f53c97185e66217fe5fe61cdc4e80b25dfe5a0d19bf0b8c77f994', 'amount': Decimal('616.00000000'), 'confirmations': 7430, 'blockindex': 1, 'blockhash': '0000004d184d3df898180937bd22c2717543706443b33ec7e16e369fa9d8c334', 'timereceived': 1491951811, 'details': [{'account': '', 'amount': Decimal('616.00000000'), 'address': 'GXaNvzURu4fRAkjSodybjcXnwwUPKxB6rQ', 'category': 'receive'}]}
        conn.getreceivedbyaddress.return_value = Decimal('616.00000000')
        conn.getnewaddress = lambda: "G" + rand_string(33)

        check_received_transactions(conn)
        check_confirmed_transactions(conn)

        tx = DepositTransaction.objects.get(
            txid='3c03439fab4f53c97185e66217fe5fe61cdc4e80b25dfe5a0d19bf0b8c77f994')
        self.assertEqual(tx.confirmed, True)
        self.assertEqual(tx.account.balance, 616)

        check_confirmed_transactions(conn)

        tx = DepositTransaction.objects.get(
            txid='3c03439fab4f53c97185e66217fe5fe61cdc4e80b25dfe5a0d19bf0b8c77f994')
        self.assertEqual(tx.account.balance, 616)
