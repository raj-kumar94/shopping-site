from django import forms
from django.contrib.auth.models import User

from .models import Cart,Customer,BankDetail


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'password']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class BankForm(forms.ModelForm):

    class Meta:
        model = BankDetail
        fields = ['name','card_no']
