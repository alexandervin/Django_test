from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def show(request):
    return HttpResponse('Hello ----------- Django+Deploy!!!!!!!!!!!')
