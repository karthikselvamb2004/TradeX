from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = user

        fields = ['name','contact']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'contact': forms.NumberInput(attrs={'placeholder': 'Enter your contact number'}),
        }
class LoginForm(forms.ModelForm):
    class Meta:
       model = login
       fields = ['email','password']
       widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'password':forms.PasswordInput(attrs={'placeholder':'enter your password'})

       }

class LoginCheck(forms.Form):
    email=forms.CharField(max_length=200,widget=forms.EmailInput(attrs={'placeholder': 'Enter your E-mail'}))
    password=forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'placeholder': 'Enter your passwordd'}))

class StockMarketNewsForm(forms.ModelForm):
    class Meta:
        model = StockMarketNews
        fields = ['title', 'content', 'source']
