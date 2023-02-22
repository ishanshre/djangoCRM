from django import forms

from team.models import Team


class TeamCreateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name','members']


class TeamUpdateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name','members']