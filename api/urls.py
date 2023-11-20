from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import hello_world, HelloWorldView, SimpleStudentView, \
    StudentFromDBView, StudentFromDBListView, ClassRoomFromDBView, \
    ClassRoomFromDBListView, StudentDetailView, StudentListView, \
    StudentProfileListView, ClassRoomAPIView, ClassRoomCreateAPIView, \
    ClassRoomUpdateAPIView, ClassRoomDetailAPIView, ClassRoomDeleteAPIView, \
    ClassRoomListCreateAPIView, ClassRoomObjectAPIView, ClassRoomViewSet, ClassRoomListUpdateViewSet

router = DefaultRouter()
router.register("classroom-viewset", ClassRoomViewSet)
router.register("classroom-list-update-viewset", ClassRoomListUpdateViewSet)

# List
# Create
# Retrieve / Detail
# Update
# Delete


urlpatterns = [
    path("hello-world/", hello_world),
    path("message/", HelloWorldView.as_view()),
    path("simple-student/", SimpleStudentView.as_view()),
    path("student-from-db/", StudentFromDBListView.as_view()),
    path("classroom-from-db/", ClassRoomFromDBListView.as_view()),
    path("student-list/", StudentListView.as_view()),
    path("student-profile-list/", StudentProfileListView.as_view()),
    path("student-detail/<int:id>/", StudentDetailView.as_view()),
    path("student-from-db/<int:id>/", StudentFromDBView.as_view()),
    path("classroom-from-db/<int:id>/", ClassRoomFromDBView.as_view()),
]


generic_urls = [
    path("generic-classroom-list/", ClassRoomAPIView.as_view()),
    path("generic-classroom-create/", ClassRoomCreateAPIView.as_view()),
    path("generic-classroom-update/<int:pk>/", ClassRoomUpdateAPIView.as_view()),
    path("generic-classroom-detail/<int:pk>/", ClassRoomDetailAPIView.as_view()),
    path("generic-classroom-delete/<int:pk>/", ClassRoomDeleteAPIView.as_view()),
    path("generic-classroom/", ClassRoomListCreateAPIView.as_view()),
    path("generic-classroom/<int:pk>/", ClassRoomObjectAPIView.as_view()),
    path("login/", obtain_auth_token)
]

urlpatterns += generic_urls + router.urls
