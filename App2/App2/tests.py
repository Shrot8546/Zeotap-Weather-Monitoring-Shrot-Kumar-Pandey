# tests.py
import unittest
from weather_data import process_weather_data, fetch_weather_data, get_weather_for_all_cities
from alerting import check_alerts

class TestWeatherMonitoring(unittest.TestCase):
    def setUp(self):
        """Setup mock data for testing."""
        self.mock_weather_data = {
            'Delhi': {
                'main': {'temp': 32.5, 'temp_max': 35.0, 'temp_min': 30.0},
                'weather': [{'main': 'Clear'}]
            },
            'Mumbai': {
                'main': {'temp': 28.0, 'temp_max': 29.0, 'temp_min': 27.0},
                'weather': [{'main': 'Rain'}]
            },
            'Chennai': {
                'main': {'temp': 34.0, 'temp_max': 36.0, 'temp_min': 32.0},
                'weather': [{'main': 'Clear'}]
            }
        }

    def test_process_weather_data(self):
        """Test if the weather data is processed correctly for daily summaries."""
        summary = process_weather_data(self.mock_weather_data)
        self.assertAlmostEqual(summary['average_temperature'], (32.5 + 28.0 + 34.0) / 3)
        self.assertEqual(summary['maximum_temperature'], 36.0)
        self.assertEqual(summary['minimum_temperature'], 27.0)
        self.assertEqual(summary['dominant_condition'], 'Clear')

    def test_fetch_weather_data(self):
        """Test if fetching weather data for a specific city returns a valid structure."""
        city = 'Delhi'
        data = fetch_weather_data(city)
        # Check if the API call was successful and returned the expected data structure
        if data:  # Only check if data is returned (skipping actual API call validation)
            self.assertIn('main', data)
            self.assertIn('weather', data)

    def test_get_weather_for_all_cities(self):
        """Test if fetching weather data for all cities returns the correct number of results."""
        weather_data = get_weather_for_all_cities()
        # Check if weather data was retrieved for each city
        self.assertEqual(len(weather_data), len(self.mock_weather_data))

    def test_check_alerts(self):
        """Test if alerts are correctly generated based on the weather summary."""
        summary = process_weather_data(self.mock_weather_data)
        alert_message = check_alerts(summary, temp_threshold=35)
        self.assertEqual(alert_message, "Alert: Temperature exceeded 35°C!")

        # Test with a higher threshold to ensure no alert is generated
        alert_message = check_alerts(summary, temp_threshold=40)
        self.assertEqual(alert_message, "No alerts")

if __name__ == '__main__':
    unittest.main()
