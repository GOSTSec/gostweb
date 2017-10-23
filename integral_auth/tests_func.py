from django.test import TestCase, RequestFactory, Client
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.sessions.backends.db import SessionStore
from django.http import Http404
from django.conf import settings

import os.path
from unittest.mock import MagicMock

import integral_auth.views as views
from integral_auth.utils import rand_string

import captcha
captcha.conf.settings.CAPTCHA_TEST_MODE = True

views.conn = MagicMock()
views.conn.getnewaddress = lambda: "G" + rand_string(33)

class SignupTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("sophia", password="qweqweqwe")
        self.page_url = reverse_lazy("integral_auth:signup")
        self.factory = RequestFactory()

    def test_page(self):
        request = self.factory.get(self.page_url)
        request.user = AnonymousUser()
        resp = views.PasswordSignUp.as_view()(request)
        self.assertEqual(resp.status_code, 200)

        request = self.factory.get(self.page_url)
        request.user = self.user
        resp = views.PasswordSignUp.as_view()(request)
        self.assertEqual(resp.status_code, 302)


    def test_invalid_signup(self):

        resp = Client().post(self.page_url, {})
        self.assertIs(resp.status_code, 200)
        self.assertFalse(resp.context["form"].is_valid())

        resp = Client().post(self.page_url, {
            "username": "sophia",  
            'captcha_0': 'abc', "captcha_1": "passed"})
        self.assertFalse(resp.context["form"].is_valid())

        resp = Client().post(self.page_url, {
            "username": "test11", 
            'captcha_0': 'abc', "captcha_1": "wrong"})
        self.assertFalse(resp.context["form"].is_valid())


    def test_success_signup(self):

        resp = Client().post(self.page_url, {
            "username": "testuser",  
            'captcha_0': 'abc', "captcha_1": "passed"})

        self.assertEqual(resp.status_code, 302)

class SigninTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("sophia", password="qweqweqwe")
        self.page_url = reverse_lazy("integral_auth:signin")
        self.factory = RequestFactory()

    def post_request(self, data):
        request = self.factory.post(self.page_url)
        request.user, request.session = AnonymousUser(), SessionStore()
        request.POST = data
        return request

    def test_page(self):
        request = self.factory.get(self.page_url)
        request.user, request.session = AnonymousUser(), SessionStore()
        resp = views.PasswordSignIn.as_view()(request)
        self.assertEqual(resp.status_code, 200)

        request = self.factory.get(self.page_url)
        request.user = self.user
        resp = views.PasswordSignIn.as_view()(request)
        self.assertEqual(resp.status_code, 302)

    def test_signin_incorrect(self):
        request = self.post_request({"username": "", "password": ""})
        resp = views.PasswordSignIn.as_view()(request)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(request.user.is_anonymous)

        request = self.post_request({"username": "hacker", "password": "qweqweqwe"})
        resp = views.PasswordSignIn.as_view()(request)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(request.user.is_anonymous)

        request = self.post_request({"username": "sophia", "password": ""})
        resp = views.PasswordSignIn.as_view()(request)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(request.user.is_anonymous)

        request = self.post_request({"username": "sophia", "password": "aiosoidsoaas"})
        resp = views.PasswordSignIn.as_view()(request)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(request.user.is_anonymous)

    def test_signin_success(self):
        request = self.post_request({"username": "sophia", "password": "qweqweqwe"})
        resp = views.PasswordSignIn.as_view()(request)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(request.user.username, "sophia")

class SigninUrlTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("sophia", password="qweqweqwe")
        self.user1 = User.objects.create_user("hacker", password="qweqweqwe")
        self.factory = RequestFactory()

    def test_signin_incorrect(self):
        creds = {"username": "sophia", "password": "qweqweqw"}
        page_url = reverse("integral_auth:signin_url", kwargs=creds)
        request = self.factory.get(page_url)
        request.session, request.user = SessionStore(), AnonymousUser()
        with self.assertRaises(Http404):
            views.signin_url(request, **creds)
        self.assertTrue(request.user.is_anonymous)
        # it redirects instead of 404 if user is logged in
        c = Client()
        c.login(username="hacker", password="qweqweqwe")
        resp = c.get(page_url)
        self.assertEqual(resp.status_code, 302)

    def test_signin_success(self):
        creds = {"username": "sophia", "password": "qweqweqwe"}
        page_url = reverse("integral_auth:signin_url", kwargs=creds)
        request = self.factory.get(page_url)
        request.session, request.user = SessionStore(), AnonymousUser()
        resp = views.signin_url(request, **creds)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(request.user.username, "sophia")

