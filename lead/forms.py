from django import forms

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
