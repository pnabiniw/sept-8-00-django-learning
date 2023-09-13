from django.urls import path
from .views import home, python, test, portfolio


urlpatterns = [
    path("python/", python),
    path("test/", test),
    path("portfolio/", portfolio),
    path("", home)
]
