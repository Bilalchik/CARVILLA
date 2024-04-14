from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView

from user.models import MyUser
from .models import Car, Basket
from .forms import CarUpdateForm
from .filters import CarFilters


def index_view(request):
    cars = Car.objects.order_by('-created_date').reverse()[:8]
    return render(request, 'product/index.html', {'cars': cars})


class IndexView(ListView):
    model = Car
    template_name = 'product/index.html'
    context_object_name = 'cars'
    queryset = Car.objects.order_by('-created_date').reverse()[:8]


def car_detail_view(request, slug):
    car = Car.objects.filter(slug=slug).first()

    if request.method == 'POST':
        print(request.POST)
        if 'buy' in request.POST:
            buying = Basket(
                user=MyUser.objects.filter(id=request.user.id).first(),
                car=car
            )
            buying.save()
        else:
            form = CarUpdateForm(request.POST, request.FILES, instance=car)

            if form.is_valid():
                form.save()
                return redirect('car_detail', slug=car.slug)
            else:
                print(form.errors)

    form = CarUpdateForm(instance=car)
    return render(request, 'product/car_detail.html', {'car': car, 'form': form})



class CarListView(ListView):
    model = Car
    template_name = 'product/car_list.html'
    context_object_name = 'cars'
    filterset_class = CarFilters

    # def get_queryset(self):
    #     search = self.request.GET.get('q')
    #     if search:
    #         return Car.objects.filter(Q(brands__title__icontains=search) | Q(car_model__icontains=search))
    #     else:
    #         return Car.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CarFilters(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context



