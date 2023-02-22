from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from team.models import Team
from team.forms import TeamCreateForm, TeamUpdateForm

from django.http import Http404
# Create your views here.


class TeamListView(LoginRequiredMixin, ListView):
    model = Team
    template_name = "team/teamList.html"
    context_object_name = "teams"

    def get_queryset(self):
        return Team.objects.filter(created_by=self.request.user)


class TeamDetailView(LoginRequiredMixin, DetailView):
    model = Team
    template_name = "team/teamDetail.html"
    context_object_name = "team"

    def get_queryset(self):
        try:
            return Team.objects.filter(created_by=self.request.user, pk=self.kwargs["pk"])
        except Team.DoesNotExist:
            raise Http404("match not found")


class TeamCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = TeamCreateForm
    template_name = "team/teamCreate.html"
    context_object_name = "team"
    success_message = "Team created successfull"
    success_url = reverse_lazy("team:teamList")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response =  super().form_valid(form)
        self.object.members.add(self.request.user)
        return response



class TeamUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Team
    form_class = TeamUpdateForm
    template_name = "team/teamUpdate.html"
    success_message = "Team updated Successfull"

    def test_func(self):
        self.object = self.get_object()
        return self.object.created_by == self.request.user


class TeamDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Team
    template_name = "team/teamDelete.html"
    context_object_name = "team"
    success_message = "Team Deleted Successfully"
    success_url = reverse_lazy("team:teamList")

    def test_func(self):
        self.object = self.get_object()
        return self.object.created_by == self.request.user