from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import widgets

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text", 
        "name": "register-form-name", 
        "placeholder": "Имя пользователя"
    }))

    phone = forms.CharField(label="Номер телефона", widget=forms.NumberInput(attrs={
        "placeholder": "Номер",
        "type": "tel", 
        "name": "register-form-phone", 
        
    }))

    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={
        "placeholder": "Пароль",
        "type": "password", 
        "name": "register-form-password", 
    }))

    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={
        "placeholder": "Повтор пароля",
        "type": "password", 
        "name": "register-form-repassword", 
    }))
    
    class Meta:
        model = User
        fields = ("username", "phone", "password1", "password2")
    
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "type": "login", 
        "name": "login",
        "placeholder": "Имя пользователя",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "type": "password",
        "name": "pass", 
        "placeholder": "Пароль",
    }))