from django.shortcuts import render
from django.http import HttpResponse


# def home(request):
#     content = """
#     <h1>Hello World</h1>
#     <h2>I'm learning Python</h2>
#     <p>Python is awesome !! </p>
#     """
#     return HttpResponse(content)

def home(request):
    # return render(request, template_name="home.html")
    return render(request, template_name="myapp/test.html")


def python(request):
    name = request.GET.get("name")
    print(name)
    return HttpResponse("<h1>I'm Learning Python</h1>")


def test(request):
    # We can send query strings / query parameters in the urls
    # Everything sent after "?" in the url is querystring
    # Query strings can be multiple and are separated by ampersand (&).
    name = request.GET.get("name")
    age = request.GET.get("age")
    return HttpResponse(f"<h1>Hello my name is {name}. I'm {age}</h1>")
