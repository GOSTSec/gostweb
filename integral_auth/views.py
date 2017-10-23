from django.shortcuts import redirect
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.db import IntegrityError

from integral_auth.utils import rand_string

from .forms import PasswordSignUpForm, PasswordSignInForm

from wallet.models import Account, Address
from wallet.gostcoin import GOSTCOIN_CONNECTION as conn

class PasswordAuth(UserPassesTestMixin, FormView):
    login_url = reverse_lazy("site_index")
    def test_func(self):
        return self.request.user.is_anonymous()

class PasswordSignUp(PasswordAuth):
    template_name = "integral_auth/signup.html"
    form_class = PasswordSignUpForm

    def form_valid(self, form):
        addr = conn.getnewaddress()

        while True:
            try:
                username, password = rand_string(16), rand_string(32)
                user = User.objects.create_user(username, password=password)
                break
            except IntegrityError:
                pass

        name = rand_string(16)
        account = Account.objects.create(user=user, name=name)
        Address.objects.create(account=account, address=addr, used=False)

        signin_url = self.request.build_absolute_uri(
                reverse('integral_auth:signin_url', kwargs={
                        "username": username, "password": password}))

        messages.success(self.request, 
                "Success! Username: {}, password: {}".format(
                    username, password))
        messages.success(self.request, 
                "You can login by visiting this link: {}".format(signin_url))
        messages.warning(self.request,
                """Save username/password RIGHT NOW in a secure place. There is
                NO WAY to recover them!""")

        login(self.request, user)
        return redirect("site_index")

class PasswordSignIn(PasswordAuth):
    template_name = "integral_auth/signin.html"
    form_class = PasswordSignInForm

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data["username"], 
                            password=form.cleaned_data["password"])
        if user is not None and user.is_active:
            login(self.request, user)
            return redirect("site_index")

def signin_url(request, username, password):
    """Handle sign in by url"""
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
    else:
        raise Http404

    return redirect("site_index")
