from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse_lazy, reverse

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.messages import success, error
from django.contrib.messages.views import SuccessMessageMixin

from django.db.models import Q

from lead.forms import LeadCreateForm, LeadUpdateForm
from lead.models import Lead

from client.models import Client
# Create your views here.


class LeadCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    form_class = LeadCreateForm
    template_name = "lead/leadCreate.html"
    success_url = reverse_lazy("lead:leadList")
    success_message = "New Lead Created"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class LeadListView(LoginRequiredMixin, ListView):
    model = Lead
    context_object_name = "leads"
    template_name = "lead/leadList.html"

    def get_queryset(self):
        return Lead.objects.filter(Q(created_by = self.request.user) & Q(converted_into_clients=False))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["conv_leads"] = Lead.objects.filter(Q(created_by = self.request.user) & Q(converted_into_clients=True))
        return context


class LeadDetailView(LoginRequiredMixin, DetailView):
    model = Lead
    context_object_name = "lead"
    template_name = "lead/leadDetail.html"


class LeadUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin ,UpdateView):
    model = Lead
    form_class = LeadUpdateForm
    context_object_name = "lead"
    template_name = "lead/leadUpdate.html"
    success_message = "Lead Updated Successfully"

    def test_func(self):
        self.object = self.get_object()
        return self.object.created_by == self.request.user and self.object.converted_into_clients == False

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
    

class LeadDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Lead
    template_name = "lead/leadDelete.html"
    context_object_name = "lead"
    success_message = "Lead Deleted Successfully"
    success_url = reverse_lazy("lead:leadList")

    def test_func(self):
        self.object = self.get_object()
        return self.object.created_by == self.request.user


class ConvertToClient(LoginRequiredMixin, SuccessMessageMixin, View):
    def get(self, request, *args, **kwargs):
        lead = get_object_or_404(Lead, created_by=request.user, pk=self.kwargs['pk'])
        if lead.team.plan.max_clients <= lead.team.clients.count():
            error(request, "Client Limit already reached")
            return redirect("lead:leadDetail", pk=lead.id)
        client = Client.objects.create(
            name=lead.name,
            email=lead.email,
            description=lead.description,
            created_by = request.user,
            team=lead.team
        )
        lead.converted_into_clients = True
        lead.save()
        success(request, f"successfully converted lead: {lead.name.title()} into client")
        return redirect("lead:leadList")