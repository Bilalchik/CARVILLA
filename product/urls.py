from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('index/<slug:slug>/', views.car_detail_view, name='car_detail')
]
