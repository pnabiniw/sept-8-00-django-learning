from django import forms
from crud.models import ClassRoom


class ClassRoomForm(forms.Form):
    name = forms.CharField(max_length=20)


class ClassRoomModelForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ["name", ]

