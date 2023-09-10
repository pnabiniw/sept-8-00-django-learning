from django.urls import path
from .views import home, python, test


urlpatterns = [
    path("python/", python),
    path("test/", test),
    path("", home)
]
