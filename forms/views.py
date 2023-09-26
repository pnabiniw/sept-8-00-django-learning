from django.shortcuts import render, redirect
from tables.models import Student


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
