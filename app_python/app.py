from flask import Flask, render_template
import requests
import re
import os

app = Flask(__name__)

VISITS = "visits.txt"

if not os.path.exists(VISITS):
    with open(VISITS, "w") as f:
        f.write("0")

def increment_visits():
    # increase the visit counter and save it to the file
    with open(VISITS, "r+") as f:
        visits = int(f.read().strip() or 0)
        visits += 1
        f.seek(0)
        f.write(str(visits))
        f.truncate()
    return visits

@app.route('/')
def home():
    try:
        # increase visits
        increment_visits()
        
        # getting the current time in moscow using the WorldTimeAPI
        moscowTimeZoneParam = 'Europe/Moscow'
        time_api_url = (
            f'https://timeapi.io/api/Time/current/zone?'
            f'timeZone={moscowTimeZoneParam}'
        )
        response = requests.get(time_api_url, timeout=5)  # limit to 5 seconds
        response.raise_for_status()

        # parse the response to JSON
        data = response.json()
        moscow_time = data['dateTime']

        # validate time format (YYYY-MM-DDTHH:MM:SS.sss)
        if not re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", moscow_time):
            raise ValueError("Invalid time format")

        # format the time
        formatted_time = moscow_time.replace('T', ' ').split('.')[0]

        return render_template('index.html', time=formatted_time)
    except Exception as e:
        # log if there is any error for debugging
        app.logger.error(f"an error occurred: {e}")

        # return a generic error message to the user
        return 'an error occurred, please try again later', 500


@app.route('/visits')
def visits():
    """Endpoint to display the number of visits."""
    try:
        with open(VISITS, "r") as f:
            visits = f.read().strip()
        return f"total visits: {visits}"
    except Exception as e:
        app.logger.error(f"error while reading visits: {e}")
        return "unable to retrieve visits count", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
