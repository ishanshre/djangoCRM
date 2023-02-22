from django import forms

from django.core.exceptions import ValidationError

from lead.models import Lead

from team.models import Team


class LeadCreateForm(forms.ModelForm):
    team = forms.ModelChoiceField(Team.objects.all())

    def __init__(self, user, *args, **kwargs):
        super(LeadCreateForm, self).__init__(*args, **kwargs)
        self.fields["team"].queryset = Team.objects.filter(created_by=user)
    class Meta:
        model = Lead
        fields = [
            'name',
            'email',
            'team',
            'description',
            'priority',
            'status'
        ]
    
    def clean_team(self):
        data = self.cleaned_data['team']
        if data.plan.max_leads <= data.leads.count():
            raise ValidationError(f"Lead limit Reached for team: {data}")
        return data

class LeadUpdateForm(forms.ModelForm):
    team = forms.ModelChoiceField(Team.objects.all())

    def __init__(self, user, *args, **kwargs):
        super(LeadUpdateForm, self).__init__(*args, **kwargs)
        self.fields["team"].queryset = Team.objects.filter(created_by=user)
    class Meta:
        model = Lead
        fields = [
            'name',
            'email',
            'team',
            'description',
            'priority',
            'status'
        ]

