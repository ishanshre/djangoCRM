from django.urls import path

from team import views

app_name = "team"

urlpatterns  =[
    path("create/", views.TeamCreateView.as_view(), name="teamCreate"),
    path("", views.TeamListView.as_view(), name="teamList"),
    path("<int:pk>/detail/", views.TeamDetailView.as_view(), name="teamDetail"),
    path("<int:pk>/update/", views.TeamUpdateView.as_view(), name="teamUpdate"),
    path("<int:pk>/delete/", views.TeamDeleteView.as_view(), name="teamDelete"),
]