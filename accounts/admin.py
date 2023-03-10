from django.contrib import admin
from accounts.forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as GetUserAdmin

from accounts.models import Profile
# Register your models here.

User = get_user_model()

class ProfileIncline(admin.StackedInline):
    model = Profile
@admin.register(User)
class UserAdmin(GetUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username','email','is_staff']
    fieldsets = GetUserAdmin.fieldsets + (
        (None, {
            "fields":("date_of_birth",)
        }),
    )
    add_fieldsets = (
        ("Create User", {
            "classes":("wide",),
            "fields":("username","email","password1","password2"),
        }),
    )
    
    def get_inlines(self, request, obj=None):
        if obj:
            return [ProfileIncline]
        return []

