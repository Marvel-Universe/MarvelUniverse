# MarvelUniverse/views/handle.py

from django.shortcuts import redirect

def handle_invalid_url(request, *args, **kwargs):
    return redirect('MarvelUniverse:home')
