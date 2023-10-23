from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import SignupForm


def signup(request):
    """Register a new user."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_passwd = form.cleaned_data.get('password1')
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_passwd, email=email, firstname=firstname,
                                lastname=lastname)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})
