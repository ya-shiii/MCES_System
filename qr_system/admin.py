# admin.py

from django.contrib import admin
from .models import Logs, User, Item

admin.site.register(Logs)
admin.site.register(User)
admin.site.register(Item)
