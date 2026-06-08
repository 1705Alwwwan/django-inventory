from django.shortcuts import render


def home (request):
    retrun render(request, 'home.html')
