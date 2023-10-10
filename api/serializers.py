from rest_framework import serializers
from crud.models import ClassRoom, Student, StudentProfile


class ClassRoomSerializer(serializers.Serializer):
    name = serializers.CharField()


class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ["id", "name"]


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name", "email", "age", "classroom"]

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method.lower() == 'get':
            fields['classroom'] = ClassRoomModelSerializer()
        return fields


class StudentProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ["student", "profile_picture", "contact", "address"]

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method.lower() == 'get':
            fields["student"] = StudentModelSerializer()
        return fields

