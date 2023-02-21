from django.urls import path

from core import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("about-us/", views.about_us, name='about_us'),
    path("contact-us/", views.contact_us, name='contact_us'),
]