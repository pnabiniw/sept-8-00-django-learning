from django.urls import path
from .views import crud_classroom, classroom_delete, classroom_update, crud_student, \
    add_student, student_detail, update_student


urlpatterns = [
    path("classroom/delete/<int:id>/", classroom_delete, name="classroom_delete"),
    path("classroom/update/<int:id>/", classroom_update, name="classroom_update"),
    path("student/", crud_student, name="crud_student"),
    path("add-student/", add_student, name="add_student"),
    path("student/<int:id>/", student_detail, name="student_detail"),
    path("update-student/<int:id>/", update_student, name="update_student"),
    path("", crud_classroom, name="crud_classroom")
]
