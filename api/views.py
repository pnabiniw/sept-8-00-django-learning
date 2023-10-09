from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from crud.models import Student, ClassRoom

from .serializers import ClassRoomSerializer, ClassRoomModelSerializer, StudentModelSerializer


def hello_world(request):
    response = {
        "message": "Hello World. I'm learning API"
    }
    return JsonResponse(response)


class HelloWorldView(APIView):
    def get(self, *args, **kwargs):
        response = {
            "message": "Hello World from APIView"
        }
        return Response(response)


class SimpleStudentView(APIView):
    def get(self, *args, **kwargs):
        students = [
            {"name": "Jon", "age": 30, "address": "KTM"},
            {"name": "Jane", "age": 30, "address": "KTM"},
            {"name": "Alex", "age": 30, "address": "KTM"},
        ]
        return Response(students)


class StudentFromDBView(APIView):
    def get(self, *args, **kwargs):
        id = kwargs["id"]  # name, email, age, classroom
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({
                "detail": "Invalid Student ID"
            })
        response = {
            "name": student.name,
            "email": student.email,
            "age": student.age,
            "classroom": student.classroom.name
        }
        return Response(response)


class StudentFromDBListView(APIView):
    def get(self, *args, **kwargs):
        """
                [
                {"name": "Jon", "age": 30, "email": "a@a.com", "classroom": "One"},
                {"name": "Jon", "age": 30, "email": "a@a.com", "classroom": "One"},
                {"name": "Jon", "age": 30, "email": "a@a.com", "classroom": "One"}
                ]
        """
        students = Student.objects.all()
        response = [{"name": student.name, "age": student.age} for student in students]
        return Response(response)

    def post(self, *args, **kwargs):
        # name = request.POST.get("name")
        print(self.request.data)
        name = self.request.data.get("name")
        email = self.request.data.get("email")
        age = self.request.data.get("age")
        classroom = self.request.data.get("classroom")
        Student.objects.create(name=name, email=email, age=age, classroom_id=classroom)
        return Response({
            "detail": "Student Created Successfully !!"
        })


class ClassRoomFromDBView(APIView):
    def get(self, *args, **kwargs):
        id = kwargs['id']
        try:
            classroom = ClassRoom.objects.get(id=id)
        except ClassRoom.DoesNotExist:
            return Response({
                "detail": "Invalid Classroom ID"
            })
        # response = {
        #     "name": classroom.name
        # }
        serializer = ClassRoomSerializer(classroom)
        return Response(serializer.data)


class ClassRoomFromDBListView(APIView):
    def get(self, *args, **kwargs):
        classrooms = ClassRoom.objects.all()
        serializer = ClassRoomSerializer(classrooms, many=True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        # serializer = ClassRoomSerializer(data=self.request.data)
        serializer = ClassRoomModelSerializer(data=self.request.data)
        if serializer.is_valid():
            # name = serializer.validated_data.get("name")
            # ClassRoom.objects.create(name=name)
            serializer.save()
            return Response({
                "detail": "Classroom Created Successfully !!"
            })
        return Response({
            "detail": "Invalid Request Data !!"
        })


# StudentDetailView, StudentView

class StudentDetailView(APIView):
    def get(self, *args, **kwargs):
        id = kwargs['id']
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({
                "detail": "Invalid Student ID"
            })
        serializer = StudentModelSerializer(student)
        return Response(serializer.data)


class StudentListView(APIView):
    def get(self, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentModelSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        serializer = StudentModelSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "detail": "Student Added Successfully !!"
            })
        return Response({
            "detail": "Invalid request data"
        })
