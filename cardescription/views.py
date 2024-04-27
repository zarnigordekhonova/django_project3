from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_car_price(request):
    return HttpResponse('<h1>Car price--> $170.000<hr/>')

def car_appearance(request):
    return HttpResponse('<h1>Car color--> Bright silver<hr/>')