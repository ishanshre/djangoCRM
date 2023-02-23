from django.shortcuts import get_object_or_404, redirect, HttpResponse

import csv

from django.urls import reverse

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.messages import success

from django.urls import reverse_lazy

from client.models import Client
from client.forms import ClientUpdateForm, ClientCreateForm, AddCommentForm, AddFileForm
# Create your views here.

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    context_object_name = "clients"
    template_name = "client/clientList.html"

    def get_queryset(self):
        return Client.objects.filter(created_by=self.request.user)


class GetComment(DetailView):
    model = Client
    context_object_name = "client"
    template_name = "client/clientDetail.html"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["comment_form"] = AddCommentForm()
        kwargs["file_form"] = AddFileForm()
        return kwargs

    def get_queryset(self):
        return Client.objects.filter(created_by=self.request.user, pk=self.kwargs["pk"])

class PostComment(SingleObjectMixin, LoginRequiredMixin, FormView):
    model = Client
    form_class = AddCommentForm
    context_object_name = "client"
    template_name = "client/clientDetail.html"

    def get_queryset(self):
        return Client.objects.filter(created_by=self.request.user, pk=self.kwargs["pk"])
    
    def post(self, request, *args, **kwargs): # from SingleObjectMixin returns url paramater
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.client = self.object
        comment.team = self.object.team
        comment.created_by = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("client:clientDetail", args=[self.object.id])

class ClientDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = GetComment.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostComment.as_view()
        return view(request, *args, **kwargs)


class ClientDetailFileView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        fileUpload = AddFileForm(request.POST, request.FILES)
        if fileUpload.is_valid():
            client = Client.objects.get(created_by=request.user, pk=self.kwargs["pk"])
            file = fileUpload.save(commit=False)
            file.created_by = request.user
            file.team = client.team
            file.client = client
            file.save()
            success(request, "Client file uploaded")
        return redirect("client:clientDetail", pk=self.kwargs['pk'])  

class ClientUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Client
    form_class = ClientUpdateForm
    template_name = "client/clientUpdate.html"
    success_message = "client updated successfully"

    def test_func(self):
        self.object = self.get_object()
        return self.object.created_by == self.request.user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class ClientDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Client
    template_name = "client/clientDelete.html"
    success_url = reverse_lazy("client:clientList")
    success_message = "Client successfully deleted"

    def test_func(self):
        self.object = self.get_object()
        return self.object.created_by == self.request.user


class ClientCreateView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    form_class = ClientCreateForm
    template_name = "client/clientCreate.html"
    success_url = reverse_lazy("client:clientList")
    success_message = "New Client Created"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        """
        Passing authenticated user to the create form of client
        """
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs



class ClientExportView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        clients = Client.objects.filter(created_by=request.user)
        response = HttpResponse(
            content_type = "text/csv",
            headers = {
            "Content-Disposition":"attachment; filename='client.csv'",
            }
        )
        writer = csv.writer(response)
        writer.writerow(['Client', 'Description','Created at','Created by',"Modified at"])
        for client in clients:
            writer.writerow([client.name, client.description, client.created_at, client.created_by, client.modified_at])
        return response            
        