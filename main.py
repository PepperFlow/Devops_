from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

@app.route('/')
def weather():
    
    city = request.args.get('city', 'Stockholm')
    lang = "se"  
    api_key = os.environ.get("API_KEY", "b38ecf570c462b01c29a466698374f46")  
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang={lang}&units=metric"

    try:
        
        result = requests.get(api)
        result.raise_for_status()  
        data = result.json()
    except requests.exceptions.HTTPError:
        
        return render_template('index.html', error="Staden hittades inte. Försök igen.")
    except requests.exceptions.RequestException as e:
        
        return render_template('index.html', error="Kunde inte hämta väderdata. Försök senare.")

    
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

    
    return render_template('index.html', weather=weather_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
