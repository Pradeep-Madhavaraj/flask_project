from flask import Blueprint, render_template, request, flash
from Project.weather.forms import WeatherForm
import requests


weather = Blueprint('weather',__name__)


def get_data(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=4dff3bbc561ffeb5f1a85a5a1003c3ed'
    data = requests.get(url.format(city)).json()
    if 'name' not in data:
        return None
    values = {
                'city' : data['name'],
                'temperature' : data['main']['temp'],
                'description' : data['weather'][0]['description'],
                'icon' : data['weather'][0]['icon']
            }
    return values


@weather.route('/home/weather', methods=['GET' , 'POST'])
def get_weather():
    form = WeatherForm()
    weather = None
    if request.method == 'POST':
        city = form.city.data
        weather = get_data(city)
        if weather is None:
            flash(message='City not found. Please enter a valid city name.',category= 'danger')
    return render_template('weath.html', form=form, weather=weather)