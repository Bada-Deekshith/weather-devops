from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "your_openweather_api_key_here"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": city.title(),
                "temp": data["main"]["temp"],
                "desc": data["weather"][0]["description"].title(),
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"]
            }
    return render_template("index.html", weather=weather_data)
