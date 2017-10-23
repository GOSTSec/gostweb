from django.conf.urls import url, include
from django.urls import reverse_lazy

from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import user_passes_test

from . import views
app_name = "integral_auth"

anon_only = user_passes_test(
        lambda u: u.is_anonymous(), reverse_lazy('site_index'))

urlpatterns = [
    url(r'^$', views.PasswordSignUp.as_view(), name='signup'),
    url(r'^signin$', views.PasswordSignIn.as_view(), name='signin'),
    url(r'^url/(?P<username>\w{1,150})/(?P<password>\w+)$',
        anon_only(views.signin_url), name='signin_url'),

    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]

