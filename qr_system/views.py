from django.shortcuts import render, get_object_or_404, redirect
from django.http import *
from .models import Logs, Item, User
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_or_register(request):
    if request.method == 'POST':
        # Assuming that the 'username' field is used for both login and registration
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if 'register' in request.POST:
            # Registration logic
            first_name = request.POST.get('first-name')
            last_name = request.POST.get('last-name')
            email = request.POST.get('new-email')

            # You might want to add more validation logic here

            # Create a new user
            user = User.objects.create_user(username=username, password=password,
                                            first_name=first_name, last_name=last_name, email=email)
            
            # Log in the new user
            login(request, user)
            
            return JsonResponse({'status': 'success', 'message': 'Registration successful', 'username': username})
        elif 'login' in request.POST:
            # Login logic
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({'status': 'success', 'message': 'Login successful', 'username': username})
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid credentials', 'username': username})

    # Render login page if not a POST request or if there's an issue
    return render(request, 'qr_system/login.html')  # Update with your actual template path


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


