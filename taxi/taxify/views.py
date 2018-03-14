from django.shortcuts import render
import googlemaps
from datetime import datetime
from .models import Location

gmaps=googlemaps.Client(key='AIzaSyCs-25pls4eMU-ikbwk8NsOe-3-M3ChXP0')
def index(request):
    
    geocode_result = gmaps.geocode('Nakuru')
    geo = geocode_result[0]['geometry']
    name=geocode_result[0]['address_components']
    location=geo['location']
    address=name[0]['long_name']
    lat = location['lat']
    log = location['lng']
   
    location = Location(lat=lat,log=log,name=address)
    location.save()

    print(address)
    
    
    return render(request,'temps/index.html')