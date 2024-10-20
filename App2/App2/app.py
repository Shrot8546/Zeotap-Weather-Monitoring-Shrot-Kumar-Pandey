# app.py
from flask import Flask, jsonify, render_template
from weather_data import get_weather_for_all_cities, process_weather_data
from alerting import check_alerts
from database import init_db
# app.py
from apscheduler.schedulers.background import BackgroundScheduler
from weather_data import get_weather_for_all_cities, process_weather_data
from database import insert_weather_data, insert_daily_summary
from datetime import datetime


app = Flask(__name__)
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather_summary')
def weather_summary():
    weather_data = get_weather_for_all_cities()
    summary = process_weather_data(weather_data)
    return jsonify(summary)

@app.route('/alerts')
def alerts():
    weather_data = get_weather_for_all_cities()
    summary = process_weather_data(weather_data)
    alert_message = check_alerts(summary)
    return jsonify({'message': alert_message})

if __name__ == '__main__':
    app.run(debug=True)
def fetch_and_store_weather():
    """Fetch weather data for all cities and store the results in the database."""
    weather_data = get_weather_for_all_cities()
    for city, data in weather_data.items():
        insert_weather_data(
            city, data['main']['temp'], data['main']['temp_max'], data['main']['temp_min'], data['weather'][0]['main']
        )
    # Process the weather data for daily summary and store it
    summary = process_weather_data(weather_data)
    date = datetime.now().date()
    insert_daily_summary(date, summary['average_temperature'], summary['maximum_temperature'], summary['minimum_temperature'], summary['dominant_condition'])

# Schedule the job
scheduler = BackgroundScheduler()
scheduler.add_job(fetch_and_store_weather, 'interval', minutes=5)  # Fetch data every 5 minutes
scheduler.start()
