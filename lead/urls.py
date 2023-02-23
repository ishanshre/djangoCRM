from django.urls import path

from lead import views

app_name = "lead"

urlpatterns  =[
    path("create/", views.LeadCreateView.as_view(), name="leadCreate"),
    path("export/", views.LeadExportView.as_view(), name="leadExport"),
    path("", views.LeadListView.as_view(), name="leadList"),
    path("<int:pk>/detail/", views.LeadDetailView.as_view(), name="leadDetail"),
    path("<int:pk>/update/", views.LeadUpdateView.as_view(), name="leadUpdate"),
    path("<int:pk>/delete/", views.LeadDeleteView.as_view(), name="leadDelete"),
    path("<int:pk>/upload/", views.LeadDetailFileView.as_view(), name="leadUpload"),
    path("<int:pk>/convert-to-client", views.ConvertToClient.as_view(), name="leadToClient"),
]