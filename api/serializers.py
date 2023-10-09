from rest_framework import serializers
from crud.models import ClassRoom, Student


class ClassRoomSerializer(serializers.Serializer):
    name = serializers.CharField()


class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ["name"]


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name", "email", "age", "classroom"]
