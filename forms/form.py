from django import forms
from crud.models import ClassRoom, Student


class ClassRoomForm(forms.Form):
    name = forms.CharField(max_length=20)


class ClassRoomModelForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ["name", ]


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "age", "classroom"]
