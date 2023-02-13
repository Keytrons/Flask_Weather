from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def weather():
    # ваш ключ API придет сюда
    if request.method == 'POST':
        city = request.form['city']

    else:
        # для имени по умолчанию 
        city = 'Gomel'

    appid = 'b910f32618d13f8c9f37d22ec9ca7560'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={appid}'  # .format(city, appid)

    # данные для переменной res
    res = requests.get(url.format(city)).json()

    data = {
        'city_name': city,
        'temp_min': res['main']['temp_min'],
        'temp_max': res['main']['temp_max'],
        'clouds_all': res['clouds']['all'],
        "temp": res['main']['temp'],
        'fiels_like': res["main"]["feels_like"],
        'speed': res["wind"]["speed"],
        "pressure": res['main']['pressure'],
        "humidity": res['main']['humidity'],
        'icon': res["weather"][0]["icon"],
    }
    print(data)
    return render_template('weather.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
