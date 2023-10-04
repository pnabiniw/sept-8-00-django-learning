from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inherit/", include('temp_inheritance.urls')),
    path("tables/", include('tables.urls')),
    path("forms/", include('forms.urls')),
    path("classbased/", include('classbased.urls')),
    path("", include('crud.urls')),
    path("", include("myapp.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

