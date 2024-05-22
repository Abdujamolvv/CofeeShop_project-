from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffee


def home(request):
    coffee_objects = Coffee.objects.all()  # Adjust the queryset according to your requirements
    return render(request, 'home.html', {'coffee_objects': coffee_objects})

