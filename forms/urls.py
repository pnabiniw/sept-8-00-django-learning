from django.urls import path
from .views import student_view, classroom, model_classroom, model_student

urlpatterns = [
    path("classroom/", classroom, name="forms_classroom"),
    path("model-classroom/", model_classroom, name="model_classroom"),
    path("model-student/", model_student, name="model_student"),
    path('', student_view, name="student_view")
]
