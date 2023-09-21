from django.urls import path
from .views import student, profile

urlpatterns = [
    path("student/", student, name="student"),
    path("profile/", profile, name="profile"),
]
