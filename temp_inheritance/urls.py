from django.urls import path
from .views import main, features

urlpatterns = [
    path('features/', features, name='features'),
    path('', main, name='home')
]
