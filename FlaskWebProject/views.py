"""
Routes and views for the flask application.
"""
import requests
from datetime import datetime
from flask import render_template, request
from FlaskWebProject import app



@app.route('/', methods=['GET', 'POST'])
@app.route('/home')

def home():
    """Renders the home page."""
    #initialise city list
    cities = ['London']
    if request.method == 'POST':
        #new_city = request.form.get('city')
        city = request.form.get('city')
        cities.append(city)
    #http://api.openweathermap.org/data/2.5/weather?q=paris&units=imperial&appid=ba55f7979e7823f5404600a5d1f983eb
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=ba55f7979e7823f5404600a5d1f983eb'
    #city = 'London'
    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()

        weather = {
                        'city' : city,
                        'temperature' : r['main']['temp'],
                        'description' : r['weather'][0]['description'],
                        'icon' : r['weather'][0]['icon']
                        }

        print(weather, r)
        weather_data.append(weather)





    return render_template(
        'index2.html',
        title='Home Page',
        year=datetime.now().year,
        weather_data=weather_data
    )
