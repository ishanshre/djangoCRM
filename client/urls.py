from django.urls import path

from client import views


app_name = "client"

urlpatterns = [
    path("", views.ClientListView.as_view(), name="clientList"),
    path("<int:pk>/detail/", views.ClientDetailView.as_view(), name='clientDetail'),
    path("<int:pk>/update/", views.ClientUpdateView.as_view(), name="clientUpdate"),
    path("<int:pk>/delete/", views.ClientDeleteView.as_view(), name="clientDelete"),
]