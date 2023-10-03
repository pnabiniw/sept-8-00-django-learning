from django.shortcuts import render, redirect
from tables.models import Student
from crud.models import ClassRoom
from .form import ClassRoomForm, ClassRoomModelForm


def student_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        address = request.POST.get('address')
        bio = request.POST.get('bio')
        Student.objects.create(name=name, age=age, email=email, address=address, bio=bio)
        return redirect('student')
    return render(request, template_name='forms/student_view.html')


def classroom(request):
    if request.method == "POST":
        form = ClassRoomForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            ClassRoom.objects.create(name=name)
            return redirect("forms_classroom")
    form = ClassRoomForm()
    classrooms = ClassRoom.objects.all()
    return render(request, template_name="forms/classroom.html",
                  context={"classrooms": classrooms, "form": form})


def model_classroom(request):
    if request.method == "POST":
        form = ClassRoomModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("forms_classroom")
    form = ClassRoomModelForm()
    classrooms = ClassRoom.objects.all()
    return render(request, template_name="forms/classroom.html",
                  context={"form": form, "classrooms": classrooms})
