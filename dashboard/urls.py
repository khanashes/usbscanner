from django.urls import path, include
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.index,name="dashboard"),
    path("manage/", views.manage, name="manage"),
    path("feed/", views.feed, name="feed"),
    path("scan_info/", views.scan_info, name="scan_info"),
    path("file/", views.file_post, name="file_post"),
    path("delete/", views.file_delete, name="file_delete")
]
