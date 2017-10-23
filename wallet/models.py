from django.db import models, IntegrityError
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from integral_auth.utils import rand_string

import logging
logger = logging.getLogger("django")

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=16, unique=True)
    balance = models.DecimalField(default=0, decimal_places=8, max_digits=15)

    def __str__(self):
        return self.name

class Address(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    address = models.CharField(max_length=35, unique=True)
    used = models.BooleanField(default=False)

class Transaction(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    txid = models.CharField(max_length=64, unique=True)
    confirmed = models.BooleanField(default=False)
    amount = models.DecimalField(default=0, decimal_places=8, max_digits=15)

    class Meta:
        abstract = True

class DepositTransaction(Transaction):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

class WithdrawalTransaction(Transaction):
    address = models.CharField(max_length=35)
