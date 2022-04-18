# pylint: skip-file
import unittest
from unittest import mock
from unittest.mock import MagicMock, patch
from openweather import get_weather
from twitter import get_trends
import json
import os

# testing the weather API response
class WeatherTest(unittest.TestCase):
    def test_get_weather(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "coord": {"lon": -84.388, "lat": 33.749},
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n",
                }
            ],
            "base": "stations",
            "main": {
                "temp": 282.55,
                "feels_like": 280.89,
                "temp_min": 279.96,
                "temp_max": 284.11,
                "pressure": 1011,
                "humidity": 53,
            },
            "visibility": 10000,
            "wind": {"speed": 3.09, "deg": 270},
            "clouds": {"all": 75},
            "dt": 1649399895,
            "sys": {
                "type": 2,
                "id": 2006620,
                "country": "US",
                "sunrise": 1649416533,
                "sunset": 1649462566,
            },
            "timezone": -14400,
            "id": 4180439,
            "name": "Atlanta",
            "cod": 200,
        }

        with patch("openweather.requests.get") as mock_requests_get:
            mock_requests_get.return_value = mock_response

            self.assertEqual(
                get_weather(),
                {
                    "weather": "Clouds",
                    "city": "Atlanta",
                    "fahrenheit": "48.92 F°",
                    "country": "US",
                },
            )


# Checking for Twitter API response
class TwitterTests(unittest.TestCase):
    """We'll test our twitter api"""

    def test_twitter_api(self):
        """This is where we test the api and see if the response are the values
        we expect"""
        mock_reponse_api = MagicMock()
        mock_reponse_api.return_value = [
            {
                "trends": [
                    {"name": "a"},
                    {"name": "b"},
                    {"name": "c"},
                    {"name": "d"},
                    {"name": "e"},
                ]
            }
        ]
        mock_response_auth = MagicMock()

        mock_response_auth.return_value = "92879e737e983748308748374987y489y8gf8wgef8ub"

        with patch("twitter.tweepy.OAuthHandler") as mock_auth:
            with patch("twitter.tweepy.API.get_place_trends") as mock_api:
                mock_auth.return_value = mock_response_auth

                mock_api.return_value = mock_reponse_api.return_value

                self.assertEqual(get_trends(), ["a", "b", "c", "d", "e"])


class NasaTests(unittest.TestCase):
    """We'll test our Nasa api"""

    def test_Nasa_API(self):
        mock_response_api = MagicMock()
        mock_response_api.json.return_value = {
            "hdurl": "https://apod.nasa.gov/apod/image/2204/HaleBoppSeip_c4096.jpg",
            "explanation": "amazing explanation",
        }
        with patch("nasa.requests.get") as mock_requests_get:
            mock_requests_get.return_value = mock_response_api
            self.assertEqual(
                nasa_picture()["picture"],
                "https://apod.nasa.gov/apod/image/2204/HaleBoppSeip_c4096.jpg",
            )


if __name__ == "__main__":
    unittest.main()
