from flask import Flask, render_template
import requests
import re

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # getting the current time in moscow using WorldTimeAPI
        moscowTimeZoneParam = 'Europe/Moscow'
        time_api_url = f'https://timeapi.io/api/Time/current/zone?timeZone={moscowTimeZoneParam}'
        response = requests.get(time_api_url, timeout=5) # limit up to 5 seconds
        response.raise_for_status()

        # parse the response to JSON
        data = response.json()
        moscow_time = data['dateTime']

        # validate time format (YYYY-MM-DDTHH:MM:SS.sss)
        if not re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", moscow_time):
            raise ValueError("Invalid time format")

        # format the time
        formatted_time = moscow_time.replace('T', ' ').split('.')[0]

    except Exception as e:
        # display if there is any error
        formatted_time = f'error: {e}'

    return render_template('index.html', time=formatted_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
