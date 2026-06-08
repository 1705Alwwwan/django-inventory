from django.shortcuts import render


def home (request):
    retrun render(request, 'inventory/home.html')
