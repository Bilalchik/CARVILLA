from django.shortcuts import render
from django.views.generic import ListView
from .models import Car


def index_view(request):
    cars = Car.objects.order_by('-created_date').reverse()[:8]
    return render(request, 'product/index.html', {'cars': cars})


