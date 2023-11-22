from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Import user model


class SignupForm(UserCreationForm):
    """
    Form for user registration.

    Fields:
    - email (str): User's email address.
    - firstname (str): User's first name.
    - lastname (str): User's last name.
    - username (str): User's chosen username.
    - password1 (str): User's chosen password.
    - password2 (str): Confirmation of the user's chosen password.

    """
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    firstname = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Firstname'}))
    lastname = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Lastname'}))
    username =  forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder':'password'}),)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}),)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'firstname', 'lastname')
