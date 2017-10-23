from django.test import TestCase, RequestFactory, Client
from django.urls import reverse_lazy, reverse
from django.contrib.sessions.backends.db import SessionStore
from unittest.mock import MagicMock

from django.contrib.auth.models import User
from decimal import Decimal
from wallet.models import Account, Address

import wallet.views as wv

from wallet.tests.fake_data import DEMO_TRANSACTIONS, DEMO_UNSPENT, DEMO_DATA_1

class SendCoinsFormTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("tester", password="asdasdasd")
        account = Account.objects.create(user=self.user, 
                name="A2aac03D5F5Adae0")
        Address.objects.create(account=account, 
                address="GPem1MVc49r7dxsUDL4sKFvq79rCtqs5Sx", used=False)
        self.factory = RequestFactory()

    def test_view_wallet(self):
        wv.conn = MagicMock()
        wv.conn.getnewaddress.return_value = "GPem1MVc49r7dxsUDL4sKFvq79rCtqs5Sx"
        self.user.account.balance = Decimal("0.998")
        self.user.account.save()
        request = self.factory.get("/")
        request.user, request.session = self.user, SessionStore()
        resp = wv.index(request)
        self.assertEqual(resp.status_code, 200)

    def test_send_coins_not_enough_on_balance(self):
        wv.conn = MagicMock()
        wv.conn.getnewaddress.return_value = "GPem1MVc49r7dxsUDL4sKFvq79rCtqs5Sx"
        self.user.account.balance = Decimal("1")
        self.user.account.save()
        request = self.factory.post("/")
        request.user, request.session = self.user, SessionStore()
        request.POST = {"recipient": "GPem1MVc49r7dxsUDL4sKFvq79rCtqs5Sx",
                "amount": "999"}

        resp = wv.index(request)
        self.assertIn("Not enough", str(resp.content))

    def test_send_coins_locally(self):
        wv.conn = MagicMock()
        wv.conn.getnewaddress.return_value = "GPem1MVc49r7dxsUDL4sKFvq79rCtqs5Sx"
        wv.messages = MagicMock()

        user2 = User.objects.create_user("second", password="asdasdasd")
        Account.objects.create(user=user2, name="B1bbd03D5F5Adae0")

        self.user.account.balance = Decimal("10")
        self.user.account.save()

        request = self.factory.post("/")
        request.user, request.session = self.user, SessionStore()
        request.POST = {"recipient": user2.account.name,
                "amount": "1"}

        resp = wv.index(request)

        user2.account.refresh_from_db()
        self.user.account.refresh_from_db()
        self.assertEqual(user2.account.balance, 1)
        self.assertEqual(self.user.account.balance, 9)

    def test_send_coins_locally_not_enough(self):
        wv.conn = MagicMock()
        wv.conn.getnewaddress.return_value = "GPem1MVc49r7dxsUDL4sKFvq79rCtqs5Sx"
        wv.messages = MagicMock()

        user2 = User.objects.create_user("second", password="asdasdasd")
        Account.objects.create(user=user2, name="B1bbd03D5F5Adae0")

        self.user.account.balance = Decimal("10")
        self.user.account.save()

        request = self.factory.post("/")
        request.user, request.session = self.user, SessionStore()
        request.POST = {"recipient": user2.account.name,
                "amount": "100"}

        resp = wv.index(request)
        self.assertIn("Not enough", str(resp.content))



    def test_send_coins_to_address(self):
        wv.conn = MagicMock()
        wv.conn.getnewaddress.return_value = "GPem1MVc49r7dxsUDL4sKFvq79rCtqs5Sx"
        wv.conn.listunspent.return_value = DEMO_UNSPENT
        wv.conn.listunspent.return_value = DEMO_DATA_1["listunspent"]
        wv.conn.sendrawtransaction.return_value = "71ea479aca93b1fb6f44b2081c711b54b1261711462ab6b7121b39763b19f328"
        wv.messages = MagicMock()

        self.user.account.balance = Decimal("10")
        self.user.account.save()
        request = self.factory.post("/")
        request.user, request.session = self.user, SessionStore()
        request.POST = {"recipient": "GPem1MVc49r7dxsUDL4sKFvq79rCtqs5Sx",
                "amount": "1"}

        resp = wv.index(request)
        self.assertIs(resp.status_code, 200)
        self.assertTrue(wv.messages.success.called)


