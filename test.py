import unittest
from datetime import datetime

import pandas as pd

from Analyze_Data import Highest_Wind, Temperatur_Operation, humidity_trend


class TestWeatherAnalysis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load a sample dataset for testing
        cls.data = pd.DataFrame({
            'Date': pd.date_range(start='2016-01-03', periods=10, freq='D'),
            'Temp': [24.3, 26.9, 23.4, 15.5, 16.1, 16.9, 18.2, 17, 19.5, 22.8],
            'Humidity': [68, 80, 82, 62, 68, 70, 63, 65, 70, 82],
            'WindGustSpeed': [30, 39, 85, 54, 50, 44, 43, 41, 48, 31]
        })

    def test_temperature_operation(self):
        # Test the Temperatur_Operation function
        start_date = datetime(2016, 1, 3)
        end_date = datetime(2016, 1, 7)

        result = Temperatur_Operation(self.data, start_date, end_date)
        expected_result = {
            "Maximum Temperature": 26.9,
            "Average Temperature": 21.24,
            "Minimum Temperature": 15.5
        }

        self.assertEqual(result, expected_result)

    def test_humidity_trend(self):
        # Test the humidity_trend function
        start_date = datetime(2016, 1, 3)
        end_date = datetime(2016, 1, 7)

        result = humidity_trend(self.data, start_date, end_date)
        expected_result = 20

        self.assertEqual(result['Humidty increase by'], expected_result)

    def test_highest_wind(self):
        # Test the Highest_Wind function
        start_date = datetime(2016, 1, 3)
        end_date = datetime(2016, 1, 7)

        result = Highest_Wind(self.data, start_date, end_date)
        expected_result = pd.Timestamp('2016-01-05 00:00:00')

        self.assertEqual(result['Date with Highest Wind Speed'], expected_result)

if __name__ == '__main__':
    unittest.main()
