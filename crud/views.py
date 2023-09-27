from django.shortcuts import render, redirect
from .models import ClassRoom


def crud_classroom(request):
    if request.method == "POST":
        name = request.POST.get("name")
        ClassRoom.objects.create(name=name)
        return redirect('crud_classroom')
    classrooms = ClassRoom.objects.all()
    return render(request, template_name='crud/classroom.html',
                  context={"classrooms": classrooms, "title": "Classroom"})

