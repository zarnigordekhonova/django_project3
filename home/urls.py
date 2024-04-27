from django.urls import path
from home.views import get_car_info1, get_car_info2

urlpatterns = [
    path('make', get_car_info1),
    path('model', get_car_info2)
]