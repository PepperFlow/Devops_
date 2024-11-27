from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

@app.route('/')
def weather():
    # Hämta stad från användarens inmatning eller använd Stockholm som standard
    city = request.args.get('city', 'Stockholm')
    lang = "se"  # Svenska som språk
    api_key = os.environ.get("API_KEY", "b38ecf570c462b01c29a466698374f46")  # Din API-nyckel
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang={lang}&units=metric"

    try:
        # Anropa OpenWeather API
        result = requests.get(api)
        result.raise_for_status()  # Kontrollera om svaret innehåller ett fel
        data = result.json()
    except requests.exceptions.HTTPError:
        # Om API:et svarar med ett HTTP-fel, t.ex. 404 för ogiltig stad
        return render_template('index.html', error="Staden hittades inte. Försök igen.")
    except requests.exceptions.RequestException as e:
        # Fångar andra nätverksrelaterade fel
        return render_template('index.html', error="Kunde inte hämta väderdata. Försök senare.")

    # Skapa väderdata från API-svaret
    weather_data = {
        "city": data.get('name', 'N/A'),
        "description": data['weather'][0]['description'],
        "temperature": data['main']['temp'],
        "feels_like": data['main']['feels_like'],
        "temp_min": data['main']['temp_min'],
        "temp_max": data['main']['temp_max'],
        "humidity": data['main']['humidity'],
        "pressure": data['main']['pressure'],
        "wind_speed": data['wind']['speed'],
        "wind_deg": data['wind']['deg']
    }

    # Rendera HTML-mallen och skicka väderdata
    return render_template('index.html', weather=weather_data)

# Kör Flask-applikationen
if __name__ == "__main__":
    app.run(debug=True)
