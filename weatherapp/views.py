from django.shortcuts import render
# import url library for the requests
import urllib.request
# for python to convert the json file to python
import json

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city'] # name of the city
        # contains json data from the API
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city + '&units=metric&appid=12b4e42bc63538922b069586e9126b37').read()
        # holds all the data that we requested about the city
        list_of_data = json.loads(source)
        # data dictionary: holds everything that will be entered on html page
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure" : str(list_of_data['main']['pressure']),
            "humidity" : str(list_of_data['main']['humidity']),
            "main" : str(list_of_data['weather'][0]['main']),
            "description" : str(list_of_data['weather'][0]['description']),
            "icon" : str(list_of_data['weather'][0]['icon']),
        }
        print(data)
    else:
        # data will be an empty dict
        data ={}
    return render(request, "main/index.html", data)
