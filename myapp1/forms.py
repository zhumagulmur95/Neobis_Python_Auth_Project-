from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.forms import ModelForm, ValidationError
from .models import Profile

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Этот логин уже занят.")
        return username

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


class MyPasswordResetForm(PasswordResetForm):
    class Meta:
        model = User
        fields = ("email",)
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not User.objects.filter(email=email).exists():
            raise ValidationError("Пользователь с таким адресом электронной почты не найден")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class CustomPasswordResetForm(MyPasswordResetForm):
    # Пользовательские изменения или дополнения, если необходимо
    pass