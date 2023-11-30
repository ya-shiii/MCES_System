from django.shortcuts import render
from django.http import *
from .models import *

def login(request):
    return render(request, 'qr_system/login.html')

def home(request):
    return render(request, 'qr_system/index.html')

def analytics(request):
    return render(request, 'qr_system/analytics.html')

def log_book(request):
    return render(request, 'qr_system/log-book.html')

def tracking(request):
    items = Item.objects.all()
    return render(request, 'qr_system/tracking.html', {'items': items})

def user_management(request):
    return render(request, 'qr_system/user_management.html')

def account(request):
    return render(request, 'qr_system/account.html')


