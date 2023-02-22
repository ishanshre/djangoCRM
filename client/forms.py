from django import forms

from client.models import Client
from team.models import Team
class ClientUpdateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name','email','description']


class ClientCreateForm(forms.ModelForm):
    team = forms.ModelChoiceField(Team.objects.all())
    def __init__(self, user=None, *args, **kwargs):
        super(ClientCreateForm, self).__init__(*args, **kwargs)
        if not user:
            self.fields["team"].queryset = Team.objects.filter(created_by=user)
        
    class Meta:
        model = Client
        fields = ['name','email','description','team']