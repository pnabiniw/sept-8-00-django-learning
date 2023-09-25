from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inherit/", include('temp_inheritance.urls')),
    path("tables/", include('tables.urls')),
    path("forms/", include('forms.urls')),
    path("", include("myapp.urls")),
]
