from django.urls import path
from . import views

app_name = "test_site_app"

urlpatterns = [
    path("sample/", views.index, name="index"),
]
