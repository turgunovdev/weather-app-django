from django.shortcuts import render
import requests
from .models import City
from .forms import Cityform

def index(request):
    appid = '9e444d4dd3aa5730772cebde5f340fc8'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=Metric&appid=' + appid

    if (request.method == 'POST'):
        form = Cityform(request.POST)
        form.save()
    form = Cityform()
    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        cityinfo = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(cityinfo)
        context = {'all_info': all_cities, 'form': form}

    return render(request, 'weatherapp/index.html', context)