import django_filters
from .models import Car


class CarFilters(django_filters.FilterSet):
    car_model = django_filters.ModelChoiceFilter(
        queryset=Car.objects.all(),
        empty_label = 'Выберите модель автомобиля'

    )
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    release_year__gt = django_filters.NumberFilter(field_name='year_of_release', lookup_expr='year__gt')
    release_year__lt = django_filters.NumberFilter(field_name='year_of_release', lookup_expr='year__lt')

    class Meta:
        model = Car
        fields = (
            'brands',
            'car_model',
            'engine_volume',
            'engine_type',
            'color',
            'condition',
            'mileage',
            'gearbox',
            'rudder_position',
            'wheel_drive',
            'car_body',
        )
