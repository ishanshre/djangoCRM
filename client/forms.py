from django import forms

from client.models import Client

class ClientUpdateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name','email','description']
        