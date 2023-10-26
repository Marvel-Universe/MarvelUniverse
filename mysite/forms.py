from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Import user model


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    firstname = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Firstname'}))
    lastname = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Lastname'}))
    username =  forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder':'password'}),)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}),)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'firstname', 'lastname')
