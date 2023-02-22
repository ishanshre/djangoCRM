from django import forms

from lead.models import Lead


class LeadCreateForm(forms.ModelForm):
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
