from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect




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
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def custom_login_view(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # other login logic
            return HttpResponseRedirect('/success')
        else:
            error_message = "Username or password is incorrect."

    return render(request, 'login.html', {'error_message': error_message})
