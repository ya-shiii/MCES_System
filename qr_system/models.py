# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group

class Item(models.Model):
    item_id = models.CharField(max_length=50, unique=True)
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    available = models.PositiveIntegerField(default=0)
    borrowed = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.item_name} (ID: {self.item_id}) (Quantity: {self.quantity} | Available: {self.available} | Borrowed: {self.borrowed})"

class Logs(models.Model):
    log_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    item_id = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log ID: {self.log_id} | User ID: {self.username} | Item ID: {self.item_id} | Event: {self.event} | Date/Time: {self.date_time}"

class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('admin', 'Administrator'),
        ('teacher', 'Teacher'),
    ]
    VALIDATION_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
    ]

    usertype = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='Teacher')
    validation = models.CharField(max_length=50, choices=VALIDATION_CHOICES, default='Pending')
    
    # Set a unique related_name for groups
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='qr_system_user_groups',
    )

    # Set a unique related_name for user_permissions
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='user_permissions',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} (ID: {self.username}, UserType: {self.usertype})"


