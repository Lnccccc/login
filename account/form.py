from django import forms

class LoginForn(forms.Form):
    username= forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

