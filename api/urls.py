from django.urls import path
from .views import hello_world, HelloWorldView, SimpleStudentView, \
    StudentFromDBView, StudentFromDBListView, ClassRoomFromDBView, \
    ClassRoomFromDBListView, StudentDetailView, StudentListView

urlpatterns = [
    path("hello-world/", hello_world),
    path("message/", HelloWorldView.as_view()),
    path("simple-student/", SimpleStudentView.as_view()),
    path("student-from-db/", StudentFromDBListView.as_view()),
    path("classroom-from-db/", ClassRoomFromDBListView.as_view()),
    path("student-list/", StudentListView.as_view()),
    path("student-detail/<int:id>/", StudentDetailView.as_view()),
    path("student-from-db/<int:id>/", StudentFromDBView.as_view()),
    path("classroom-from-db/<int:id>/", ClassRoomFromDBView.as_view()),
]
