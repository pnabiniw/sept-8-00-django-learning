from django.shortcuts import render
from .models import Student


def student(request):
    students = Student.objects.all()   # [obj1, obj2, obj3]  [{}, {}, {}]
    return render(request, template_name="tables/student.html", context={"infos": students})
