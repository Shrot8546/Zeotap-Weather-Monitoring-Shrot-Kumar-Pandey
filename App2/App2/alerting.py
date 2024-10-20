# alerting.py
import smtplib
from email.mime.text import MIMEText

def send_email_alert(subject, body, to_email):
    """Send an email alert."""
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'your_email@example.com'
    smtp_password = 'your_password'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = smtp_username
    msg['To'] = to_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, msg.as_string())

def check_alerts_and_notify(weather_summary, temp_threshold=35):
    """Check for alerts and send notifications if thresholds are breached."""
    if weather_summary['maximum_temperature'] > temp_threshold:
        alert_message = f"Temperature exceeded {temp_threshold}°C! Current Max: {weather_summary['maximum_temperature']}°C."
        send_email_alert("Weather Alert", alert_message, "recipient@example.com")
        return alert_message
    return "No alerts"
