from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Get free API key from https://openweathermap.org/api
API_KEY = 'e9d3d92b6181494530fd969689e7bddf'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'Bangalore')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    response = requests.get(url)
    response = requests.get(url)

    print("API URL:", url)
    print("Status Code:", response.status_code)
    print("Response:", response.text)

    if response.status_code != 200:
        return jsonify({
            "error": "City not found or API error",
            "status_code": response.status_code,
            "details": response.text
        }), response.status_code

    data = response.json()
    formatted = {
        "city": data['name'],
        "temperature": data['main']['temp'],
        "feels_like": data['main']['feels_like'],
        "humidity": data['main']['humidity'],
        "description": data['weather'][0]['description'],
        "wind_speed": data['wind']['speed']
    }
    return jsonify(formatted)

if __name__ == '__main__':
    app.run(debug=True)
