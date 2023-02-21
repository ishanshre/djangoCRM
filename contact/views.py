from django.shortcuts import render

from django.views.generic.edit import CreateView

from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy

from contact.forms import ContactForm
# Create your views here.

class ContactView(SuccessMessageMixin, CreateView):
    form_class = ContactForm
    template_name = "contact/contact_us.html"
    success_url = reverse_lazy("core:index")
    success_message = "Message Sent"
