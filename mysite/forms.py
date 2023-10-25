from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Import user model


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField(max_length=30, required=True)
    lastname = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'firstname', 'lastname')
