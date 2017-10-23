from django import forms
from django.core.exceptions import ValidationError
from django.conf import settings

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout

from decimal import Decimal

from .models import Account

class SendCoins(forms.Form):
    recipient = forms.RegexField(
            regex="^[a-zA-Z0-9]{16,35}$",
            label="Address or local account")
    amount = forms.DecimalField(label="amount",
            min_value=Decimal("0.01"),
            max_value=Decimal("2000000"))

        
    def clean_recipient(self):
        """Validate recipient"""
        data = self.cleaned_data["recipient"]

        if (len(data) == 34 or len(data) == 35) and data.startswith("G"):
            """Valid GST address"""
            return data
        elif len(data) == 16:
            """Account name"""
            try:
                a = Account.objects.get(name=data)
            except Account.DoesNotExist:
                raise ValidationError("Invalid account name", code="invalid")
        else:
            raise ValidationError("Incorrect recipient address/account name", 
                    code="invalid")

        return data

    def clean(self):
        """Check balance"""
        if self.user and self.is_valid():
            if len(self.cleaned_data["recipient"]) == 16:
                total_amount = self.cleaned_data["amount"]
            else:
                total_amount = self.cleaned_data["amount"] + \
                        settings.GST_NETWORK_FEE + settings.SERVICE_FEE
            if self.user.account.balance < total_amount:
                raise ValidationError("Not enough coins on balance")

        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(SendCoins, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Send'))
