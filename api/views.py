from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, \
    DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from crud.models import Student, ClassRoom, StudentProfile

from .serializers import ClassRoomSerializer, ClassRoomModelSerializer, StudentModelSerializer, \
    StudentProfileModelSerializer
from .permissions import IsAdminUser


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
            }, status=status.HTTP_400_BAD_REQUEST)
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
        }, status=status.HTTP_201_CREATED)


class ClassRoomFromDBView(APIView):
    def get(self, *args, **kwargs):
        id = kwargs['id']
        try:
            classroom = ClassRoom.objects.get(id=id)
        except ClassRoom.DoesNotExist:
            return Response({
                "detail": "Invalid Classroom ID"
            }, status=status.HTTP_400_BAD_REQUEST)
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
            }, status=201)
        return Response({
            "detail": "Invalid Request Data !!"
        }, status=status.HTTP_400_BAD_REQUEST)


# StudentDetailView, StudentView

class StudentDetailView(APIView):
    def get(self, *args, **kwargs):
        id = kwargs['id']
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({
                "detail": "Invalid Student ID"
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer = StudentModelSerializer(student)
        return Response(serializer.data)


class StudentListView(APIView):
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ["classroom_id", "classroom__name"]
    permission_classes = [AllowAny, ]
    def get(self, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentModelSerializer(students, many=True, context={"request": self.request})
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        serializer = StudentModelSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "detail": "Student Added Successfully !!"
            }, status=201)
        return Response({
            "detail": "Invalid request data"
        }, status=status.HTTP_400_BAD_REQUEST)


class StudentProfileListView(APIView):
    search_fields = ["contact", "student__name"]
    def get(self, *args, **kwargs):
        profiles = StudentProfile.objects.all()
        ser = StudentProfileModelSerializer(profiles, many=True, context={"request": self.request})
        return Response(ser.data)

    def post(self, *args, **kwargs):
        ser = StudentProfileModelSerializer(data=self.request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)


class ClassRoomAPIView(ListAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomCreateAPIView(CreateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomUpdateAPIView(UpdateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomDetailAPIView(RetrieveAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomDeleteAPIView(DestroyAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomListCreateAPIView(ListCreateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomObjectAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomViewSet(ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["name", ]
    filterset_fields = []
    # permission_classes = [IsAuthenticated, ]
    # authentication_classes = [TokenAuthentication, ]

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        return [IsAdminUser(), ]
