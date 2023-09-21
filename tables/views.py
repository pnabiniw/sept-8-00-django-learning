from django.shortcuts import render
from .models import Student, StudentProfile


def student(request):
    students = Student.objects.all()   # [obj1, obj2, obj3]  [{}, {}, {}]
    return render(request, template_name="tables/student.html", context={"infos": students})


def profile(request):
    return render(request, template_name="tables/profile.html",
                  context={"profiles": StudentProfile.objects.all()})
