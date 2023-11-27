from django.shortcuts import redirect

def handle_invalid_url(request, path):
    return redirect('MarvelUniverse:home')
