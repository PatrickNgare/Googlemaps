from django.shortcuts import render

def welcome(request):
    return HttpResponse('Welcome to the taxify')