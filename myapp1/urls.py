from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from myapp1.views import my_view1, my_view2, register, custom_login, custom_logout, CustomPasswordResetView, CustomPasswordResetConfirmView

urlpatterns = [
    path('', my_view1, name='my_view1'),
    path('about/', my_view2, name='my_view2'),
    path('register/', register, name='register'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    
    path("favicon.ico",
         RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
]