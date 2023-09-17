from django.shortcuts import render


def main(request):
    people = [
        {"name": "Ram", "age": 30, "address": "KTM"},
        {"name": "Hari", "age": 24, "address": "KTM"},
        {"name": "Sita", "age": 45, "address": "BKT"},
    ]
    return render(request, template_name='temp_inheritance/home.html', context={"people": people})


def features(request):
    items = [
        {"name": "laptop", "feature": "A portable computer that can be used anywhere"},
        {"name": "Mouse", "feature": "A clicking input device of a computer"},
        {"name": "Keyboard", "feature": "An input device with keys"},
    ]
    return render(request, template_name='temp_inheritance/features.html', context={"items": items})


def pricing(request):
    items = [
        {"name": "laptop", "price": "5000"},
        {"name": "Mouse", "price": 120000},
        {"name": "Keyboard", "price": 12000},
    ]
    return render(request, 'temp_inheritance/pricing.html', {"goods": items})
