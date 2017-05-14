from django import forms

class SigninForm(forms.Form):
    phone_number= forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput)