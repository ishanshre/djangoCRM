from django.urls import path

from django.contrib.auth.views import LogoutView

from django.urls import reverse_lazy
from accounts import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy("accounts:login")), name='logout'),
    path("", views.ProfileView.as_view(), name="profile"),
]