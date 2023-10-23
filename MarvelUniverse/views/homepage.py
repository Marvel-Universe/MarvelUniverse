from django.shortcuts import render


def homepage(requests):
    return render(requests, 'base.html')
