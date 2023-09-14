from django.shortcuts import render


def main(request):
    return render(request, template_name='temp_inheritance/home.html')
