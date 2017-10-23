from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from captcha.fields import CaptchaField

class PasswordSignUpForm(UserCreationForm):
    password1 = None
    password2 = None
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(PasswordSignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Continue'))

class PasswordSignInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(PasswordSignInForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Sign in'))

