from django.shortcuts import redirect, get_object_or_404, render

from django.views.generic.edit import CreateView
from django.views import View

from django.contrib.auth.views import LoginView as GenericLoginView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin

from accounts.forms import LoginForm, SignUpForm
from accounts.models import Profile
# Create your views here.

User = get_user_model()

class SignUpView(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    template_name = "auth/signup.html"
    success_url = reverse_lazy("account:login")
    success_message = "User signed up successfull"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("core:index")
        return super().dispatch(request, *args, **kwargs)

class LoginView(GenericLoginView):
    form_class = LoginForm
    template_name = "auth/login.html"
    success_url = reverse_lazy("core:index")
    
    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(LoginView, self).form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("core:index")
        return super().dispatch(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, View):
    template_name = "auth/profile.html"
    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, user=request.user)
        context = {
            "profile":profile,
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        pass