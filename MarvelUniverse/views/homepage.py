from django.http import HttpResponse

def homepage(requests):
    return HttpResponse('welcome to marvel')
