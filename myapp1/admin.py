from django.contrib import admin  # Импорт модуля admin
from django.contrib.auth.admin import UserAdmin
from myapp1.models import User, Profile

admin.site.register(User, UserAdmin)
admin.site.register(Profile)

