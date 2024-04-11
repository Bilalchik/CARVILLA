from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Car
from .forms import CarUpdateForm


def index_view(request):
    cars = Car.objects.order_by('-created_date').reverse()[:8]
    return render(request, 'product/index.html', {'cars': cars})


def car_detail_view(request, slug):
    car = Car.objects.filter(slug=slug).first()

    if request.method == 'POST':
        form = CarUpdateForm(request.POST, request.FILES, instance=car)

        if form.is_valid():
            form.save()
            return redirect('car_detail', slug=car.slug)
        else:
            print(form.errors)
    form = CarUpdateForm(instance=car)
    return render(request, 'product/car_detail.html', {'car': car, 'form': form})
