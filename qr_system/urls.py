from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login, name='login-page'),
    path('login-api/', views.login_api, name='login-api'),

    path('analytics/', views.analytics, name='analytics-page'),
    path('log-book/', views.log_book, name='logbook-page'),
    path('logs/', views.log_book, name='logs-page'),
    path('tracking/', views.tracking, name='tracking-page'),
    path('user-management/', views.user_management, name='users-page'),
    path('account/<str:username>', views.account, name='account-page'),
    path('', views.home, name='home-page'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)