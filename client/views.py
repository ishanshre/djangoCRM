from django.shortcuts import get_object_or_404

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy

from client.models import Client
from client.forms import ClientUpdateForm
# Create your views here.

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    context_object_name = "clients"
    template_name = "client/clientList.html"

    def get_queryset(self):
        return Client.objects.filter(created_by=self.request.user)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    context_object_name = "client"
    template_name = "client/clientDetail.html"

    def get_queryset(self):
        return Client.objects.filter(created_by=self.request.user, pk=self.kwargs["pk"])


class ClientUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Client
    form_class = ClientUpdateForm
    template_name = "client/clientUpdate.html"
    success_message = "client updated successfully"

    def test_func(self):
        self.object = self.get_object()
        return self.object.created_by == self.request.user


class ClientDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Client
    template_name = "client/clientDelete.html"
    success_url = reverse_lazy("client:clientList")
    success_message = "Client successfully deleted"

    def test_func(self):
        self.object = self.get_object()
        return self.object.created_by == self.request.user



