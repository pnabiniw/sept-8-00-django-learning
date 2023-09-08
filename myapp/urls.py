from django.urls import path
from .views import home, python


urlpatterns = [
    path("world/", home),
    path("python/", python),
]
