from django.urls import path
from cardescription.views import get_car_price, car_appearance

urlpatterns = [
    path('price', get_car_price),
    path('color', car_appearance)
]