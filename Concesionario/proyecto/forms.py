from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class User_registration_form(UserCreationForm):
    email = forms.EmailField(widget= forms.EmailInput(attrs={"placeholder":"Email"}))
    password1 = forms.CharField(label="Password", widget= forms.PasswordInput(attrs={"placeholder":"Password"}))
    password2 = forms.CharField(label="Repeat the password", widget= forms.PasswordInput(attrs={"placeholder":"Repeat your password"}))
    
    class Meta:
        model = User
        fields = ["first_name","last_name","username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}