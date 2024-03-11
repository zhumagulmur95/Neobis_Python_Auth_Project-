import logging
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from .forms import RegistrationForm, LoginForm, MyPasswordResetForm

@login_required
def home(request):
    return render(request, 'myapp1/home.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()

            logger = logging.getLogger(__name__)
            logger.info(f"User registered: {user.username}")
            # Добавьте логика отправки письма с подтверждением по почте
            
            return redirect("/")
    else:
        form = RegistrationForm()
    return render(request, "myapp1/registration.html", {"form": form})

def custom_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
    else:
        form = LoginForm()
    return render(request, "myapp1/login.html", {"form": form})

def custom_logout(request):
    logout(request)
    return redirect("/")

class CustomPasswordResetView(PasswordResetView):
    template_name = 'myapp1/password_reset_form.html'
    email_template_name = 'myapp1/password_reset_email.html'
    success_url = '/password-reset/done/'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'myapp1/password_reset_confirm.html'
    success_url = '/password-reset/complete/'

def my_view1(request):
    # ... ваш код обработки запроса ...
    return render(request, 'myapp1/index.html')

def my_view2(request):
    # ... ваш код обработки запроса ...
    return render(request, 'myapp1/about.html')