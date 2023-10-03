from django.urls import path
from .views import student_view, classroom, model_classroom

urlpatterns = [
    path("classroom/", classroom, name="forms_classroom"),
    path("model-classroom/", model_classroom, name="model_classroom"),
    path('', student_view, name="student_view")
]
