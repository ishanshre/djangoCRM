from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View

from client.models import Client
from lead.models import Lead
from team.models import Team
# Create your views here.

class DashboardView(LoginRequiredMixin, View):
    template_name = "dashboard/dashboard.html"
    def get(self, request, *args, **kwargs):
        teams = Team.objects.filter(created_by=request.user).order_by('-created_at')[0:5]
        clients = Client.objects.filter(created_by=request.user).order_by('-created_at')[0:5]
        leads = Lead.objects.filter(created_by=request.user, converted_into_clients=False).order_by('-created_at')[0:5]
        context = {
            "teams":teams,
            "clients":clients,
            "leads":leads,
        }
        return render(request, self.template_name, context)