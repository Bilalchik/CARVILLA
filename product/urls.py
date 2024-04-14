from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('index/<slug:slug>/', views.car_detail_view, name='car_detail'),
    path('car_list/', views.CarListView.as_view(), name='car_list'),
]
