
# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    
    # related_name для избежания конфликта
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='myapp1_user_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='myapp1_user_permissions')

    class Meta:
        db_table = 'myapp1_user'  # Добавьте этот атрибут

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
