from django.shortcuts import render
from .models import Car
import requests
from requests.auth import HTTPBasicAuth
# Create your views here.
PI = 3.14

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars(request):
    all_cars = Car.objects.all
    return render(request, 'cars.html', {'all_cars':all_cars})

def trains(request):
    
    
    arrivalTimes = []
    departureTimes = []
    destinations = []
    
    data = requests.get("https://api-v3.mbta.com/schedules?filter[stop]=place-north").json()
    for x in range(10):
        train = data["data"][x]
        AT = train["attributes"]["arrival_time"]
        DT = train["attributes"]["departure_time"]
        dest_id = train["relationships"]["route"]["data"]["id"]
        dir_id = train["attributes"]["direction_id"]

        route = requests.get("https://api-v3.mbta.com/routes/"+ dest_id).json()
        dest = route["data"]["attributes"]["direction_destinations"][dir_id]
        arrivalTimes.append(AT)
        departureTimes.append(DT)
        destinations.append(dest)

    
    return render(request, 'trains.html', {'arrivals':arrivalTimes,'departures':departureTimes,'destinations':destinations})