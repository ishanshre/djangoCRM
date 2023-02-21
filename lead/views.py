from django.shortcuts import render

from django.urls import reverse_lazy, reverse

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.messages import success
from django.contrib.messages.views import SuccessMessageMixin

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


class LeadDetailView(LoginRequiredMixin, DetailView):
    model = Lead
    context_object_name = "lead"
    template_name = "lead/leadDetail.html"


class LeadUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin ,UpdateView):
    model = Lead
    form_class = LeadCreateForm
    context_object_name = "lead"
    template_name = "lead/leadUpdate.html"
    success_message = "Lead Updated Successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    def test_func(self):
        self.object = self.get_object()
        return self.object.created_by == self.request.user
    

class LeadDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Lead
    template_name = "lead/leadDelete.html"
    context_object_name = "lead"
    success_message = "Lead Deleted Successfully"
    success_url = reverse_lazy("lead:leadList")

    def test_func(self):
        self.object = self.get_object()
        return self.object.created_by == self.request.user