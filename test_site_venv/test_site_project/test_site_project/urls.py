from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("index/", include("test_site_app.urls")),
    path('admin/', admin.site.urls),
]
