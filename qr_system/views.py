from django.shortcuts import render, get_object_or_404, redirect
from django.http import *
from .models import Logs, Item, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success', 'message': 'Login successful', 'username': username})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid credentials'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@login_required
def protected_view(request):
    return JsonResponse({'status': 'success', 'message': 'You are authenticated'})

@login_required
def logout_view(request):
    logout(request)
    return JsonResponse({'status': 'success', 'message': 'Logout successful'})

# Example of a protected view that requires authentication
@login_required
def protected_view(request):
    return JsonResponse({'status': 'success', 'message': 'You are authenticated'})

def login(request):
    return render(request, 'qr_system/login.html')

def home(request):
    return render(request, 'qr_system/index.html')

def analytics(request):
    return render(request, 'qr_system/analytics.html')

def log_book(request):
    logs = Logs.objects.all()
    return render(request, 'qr_system/log-book.html', {'logs': logs})

def tracking(request):
    items = Item.objects.all()
    return render(request, 'qr_system/tracking.html', {'items': items})

def user_management(request):
    users = User.objects.all()
    return render(request, 'qr_system/user-management.html', {'users': users})

def account(request, username):
    users = get_object_or_404(User, username=username)
    return render(request, 'qr_system/account.html', {'users': users})




