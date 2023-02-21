from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View
# Create your views here.

class DashboardView(LoginRequiredMixin, View):
    template_name = "dashboard/dashboard.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)