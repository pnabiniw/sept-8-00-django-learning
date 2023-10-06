from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response


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
