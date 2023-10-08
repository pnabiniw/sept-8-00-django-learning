from django.urls import path
from .views import hello_world, HelloWorldView, SimpleStudentView, \
    StudentFromDBView, StudentFromDBListView

urlpatterns = [
    path("hello-world/", hello_world),
    path("message/", HelloWorldView.as_view()),
    path("simple-student/", SimpleStudentView.as_view()),
    path("student-from-db/", StudentFromDBListView.as_view()),
    path("student-from-db/<int:id>/", StudentFromDBView.as_view()),
]
