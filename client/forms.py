from django import forms
from django.contrib.messages import error
from django.core.exceptions import ValidationError

from client.models import Client, Comment
from team.models import Team

class ClientUpdateForm(forms.ModelForm):
    team = forms.ModelChoiceField(Team.objects.all())

    def __init__(self, user, *args, **kwargs):
        super(ClientUpdateForm, self).__init__(*args, **kwargs)
        self.fields["team"].queryset = Team.objects.filter(created_by=user)
    class Meta:
        model = Client
        fields = ['name','email','description','team']


class ClientCreateForm(forms.ModelForm):
    team = forms.ModelChoiceField(Team.objects.all())
    def __init__(self, user, *args, **kwargs):
        super(ClientCreateForm, self).__init__(*args, **kwargs)
        self.fields["team"].queryset = Team.objects.filter(created_by=user)
        
    class Meta:
        model = Client
        fields = ['name','email','description','team']
    
    def clean_team(self):
        data = self.cleaned_data["team"]
        if data.plan.max_clients <= data.clients.count():
            raise ValidationError(f"Client Limit Reached for team: {data}")
        return data


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
