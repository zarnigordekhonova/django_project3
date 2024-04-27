from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def get_car_info1(request):
    return HttpResponse('<h1>Car make--> BMW<hr/>')

def get_car_info2(request):
    return HttpResponse('<h1>Car model--> BMW X8<hr/>')