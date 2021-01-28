import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=c05f9a60c3350fc7044c8d73958bd224'

    err_msg = ''

    message = ''

    message_class = '' 

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city = City.objects.filter(name=new_city)

            if (existing_city.count() == 0) and not None:
    
                r = requests.get(url.format(new_city)).json()
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'City does not exist!'

            else:
                err_msg = 'City already exists in the database!'

        if err_msg:
            message = err_msg
            message_class = 'is-danger'

        else:
            message = 'City added successfully!'
            message_class = 'is-success'

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        weather_data.append( city_weather )

    print( weather_data )

    print(city_weather)
    context = {
        'weather_data' : weather_data,
        
        'form' : form,

        'message' : message,

        'message_class' : message_class
    }
    
    return render(request, 'weather/weather.html', context)
