from django.urls import path
from .views import hello_world, HelloWorldView, SimpleStudentView


urlpatterns = [
    path("hello-world/", hello_world),
    path("message/", HelloWorldView.as_view()),
    path("simple-student/", SimpleStudentView.as_view())
]
