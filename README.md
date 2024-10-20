

# Real-Time Weather Monitoring System

## Overview

The Real-Time Weather Monitoring System is designed to fetch, store, and analyze weather data from multiple cities. It provides daily summaries, alerts based on specific weather conditions, and a user-friendly web interface for data visualization.

## Features

- **Data Storage**: Fetch and store weather data in a SQLite database.
- **Periodic Data Fetching**: Automatically retrieves weather data at regular intervals.
- **Alert Notification System**: Sends email alerts when specific weather conditions are met (e.g., temperature thresholds).
- **Data Visualization**: Displays temperature trends using charts.
- **Unit Testing**: Comprehensive tests for functionalities including data storage and alert notifications.
- **Documentation and Packaging**: Instructions for setup and deployment using Docker.

## Requirements

- Python 3.6+
- SQLite
- APScheduler
- Flask (for web interface)
- Chart.js (for data visualization)
- smtplib (for email notifications)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/weather-monitoring-system.git
   cd weather-monitoring-system
2.	Install the required packages:
bash
Copy code
pip install -r requirements.txt
3.	Create the SQLite database:
Run the following Python script to create the necessary tables in the database.
python
Copy code
import sqlite3

conn = sqlite3.connect('weather.db')
cursor = conn.cursor()

# Create weather table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY,
        city TEXT,
        temperature REAL,
        max_temp REAL,
        min_temp REAL,
        condition TEXT
    )
''')

# Create daily_summary table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS daily_summary (
        id INTEGER PRIMARY KEY,
        date TEXT,
        average_temperature REAL,
        maximum_temperature REAL,
        minimum_temperature REAL,
        dominant_condition TEXT
    )
''')

conn.commit()
conn.close()
4.	Configure Email Settings:
Update the alerting.py file with your SMTP server details, including your email, password, and the recipient's email.
python
Copy code
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'your_email@example.com'
smtp_password = 'your_password'
5.	Run the Application:
You can start the application using:
bash
Copy code
python app.py
Scheduling Data Fetching
The application uses APScheduler to periodically fetch and store weather data. The default interval is set to 5 minutes. You can modify this interval in the app.py file.
python
Copy code
scheduler.add_job(fetch_and_store_weather, 'interval', minutes=5)  # Modify interval here
Email Alerts
The alert notification system checks if the maximum temperature exceeds a specified threshold (default is 35°C). You can customize this threshold in the check_alerts_and_notify function in alerting.py.
python
Copy code
def check_alerts_and_notify(weather_summary, temp_threshold=35):
Data Visualization
The web interface uses Chart.js to display temperature trends. Ensure you include Chart.js in your HTML file. The index.html file should contain:
html
Copy code
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<canvas id="temperatureChart" width="400" height="200"></canvas>
Testing
To run unit tests for the application, execute:
bash
Copy code
python -m unittest tests.py
Docker Deployment
To containerize the application, create a Dockerfile in the root directory:
dockerfile
Copy code
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
Build and run the Docker container:
bash
Copy code
docker build -t weather-monitoring-system .
docker run -d -p 5000:5000 weather-monitoring-system
License
This project is licensed under the MIT License. See the LICENSE file for more details.
Acknowledgments
•	Flask for the web framework.
•	APScheduler for scheduling tasks.
•	Chart.js for data visualization.

