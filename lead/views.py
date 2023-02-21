from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages import success

from lead.forms import LeadCreateForm
from lead.models import Lead
# Create your views here.


class LeadCreateView(LoginRequiredMixin,CreateView):
    form_class = LeadCreateForm
    template_name = "lead/leadCreate.html"
    success_url = reverse_lazy("dashboard:dashboard")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        success(self.request, "Lead Added Successfully")
        return super().form_valid(form)


class LeadListView(LoginRequiredMixin, ListView):
    model = Lead
    context_object_name = "leads"
    template_name = "lead/leadList.html"

    def get_queryset(self):
        return Lead.objects.filter(created_by = self.request.user)
