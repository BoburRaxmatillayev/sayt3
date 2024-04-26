from django.shortcuts import render
from django.contrib import messages

def home_view(request):
    return render(request, "index.html")

def about_view(request):
    return render(request, "about.html")

def contact_view(request):
    return render(request, "contact.html")

def guard_view(request):
    return render(request, "guard.html")

def service_view(request):
    return render(request,"service.html")
