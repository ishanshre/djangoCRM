from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

from django import forms

from accounts.models import Profile

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username","email"]

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email"
        ]

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username','password','remember_me']

class SignUpForm(CustomUserCreationForm):
    class Meta(CustomUserCreationForm.Meta):
        model = User
        fiedls = ['username','email','password1','password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar","bio","country"]

class UserUpdateForm(CustomUserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','date_of_birth']        