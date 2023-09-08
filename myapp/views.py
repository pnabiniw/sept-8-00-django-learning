from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    content = """
    <h1>Hello World</h1>
    <h2>I'm learning Python</h2>
    <p>Python is awesome !! </p>
    """
    return HttpResponse(content)


def python(request):
    return HttpResponse("<h1>I'm Leanring Python</h1>")