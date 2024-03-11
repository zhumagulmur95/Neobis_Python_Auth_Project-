from django.contrib import admin
from ..models import Profile

class ProfileAdmin(admin.ModelAdmin):
    # Добавьте здесь поля для отображения
    list_display = ('user', 'bio', 'avatar')
    # ... (добавьте другие настройки)

admin.site.register(Profile, ProfileAdmin)
