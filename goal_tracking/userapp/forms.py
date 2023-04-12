from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import MyUser



class RegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password1', 'password2')