from django.shortcuts import render

# Create your views here.
# app/views.py

def home(request):
    return HttpResponse("Hello Django Inventory V2")
