from django.urls import path

from lead import views

app_name = "lead"

urlpatterns  =[
    path("create/", views.LeadCreateView.as_view(), name="leadCreate"),
    path("list/", views.LeadListView.as_view(), name="leadList"),
    path("<int:pk>/detail/", views.LeadDetailView.as_view(), name="leadDetail")
]