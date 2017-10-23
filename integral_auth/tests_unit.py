from django.test import TestCase
from django.contrib.auth.models import User

from integral_auth import forms

import captcha
captcha.conf.settings.CAPTCHA_TEST_MODE = True


class PasswordSignUpFormTests(TestCase):

    def setUp(self):
        self.form = forms.PasswordSignUpForm
        self.user = User.objects.create_user("sophia", password="qweqweqwe")

    def test_signup_valid(self):
        data = {'username': 'paul', 
                'captcha_0':'abc', 'captcha_1': 'passed'}
        form = self.form(data)
        self.assertTrue(form.is_valid())

    def test_signup_invalid_username(self):
        data = {'username': 'sophia', 
                'captcha_0':'abc', 'captcha_1': 'passed'}
        form = self.form(data)
        self.assertFalse(form.is_valid())

    def test_signup_invalid_input(self):
        data = {}
        form = self.form(data)
        self.assertFalse(form.is_valid())

        data = {'username': 'sophia3'}
        form = self.form(data)
        self.assertFalse(form.is_valid())

        data = {'username': 'sophia3', 
                'captcha_0':'abc', 'captcha_1': 'wtf'}
        form = self.form(data)
        self.assertFalse(form.is_valid())

