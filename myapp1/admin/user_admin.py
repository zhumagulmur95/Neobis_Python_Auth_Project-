from django.contrib import admin
from django.contrib.auth.models import User

class MyUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_active")
    list_filter = ("is_staff", "is_active")
    search_fields = ("username", "email")
    ordering = ("-date_joined",)

admin.site.register(User, MyUserAdmin)


