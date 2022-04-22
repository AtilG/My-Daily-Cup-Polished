# pylint: skip-file
import unittest
from unittest import mock
from unittest.mock import MagicMock, patch
from openweather import get_weather
from nasa import nasa_picture
from nyt import nyt_results
from useful_functions import formation, sort_emotions
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

class nytTests(unittest.TestCase):
    '''We'll test our NYT API and make sure we are retireving the data that's important to us'''
    def test_NYT_API_Names(self):
        mock_response_api = MagicMock()
        mock_response_api.json.return_value = {
            "status":"OK",
            "results":[
                {
                    "uri":"nyt://article/aec25509-ec2e-591d-b1ab-d2229cdaadcf",
                    "url":"https://www.nytimes.com/2022/04/21/us/politics/trump-mitch-mcconnell-kevin-mccarthy.html",
                    "id":100000008311870,
                    "asset_id":100000008311870,
                    "source":"New York Times",
                    "published_date":"2022-04-21",
                    "updated":"2022-04-22 09:53:24",
                    "section":"U.S.",
                    "subsection":"Politics",
                    "nytdsection":"u.s.",
                    "adx_keywords":"Presidential Election of 2020;United States Politics and Government;Storming of the US Capitol (Jan, 2021);Impeachment;Books and Literature;McConnell, Mitch;McCarthy, Kevin (1965- );Trump, Donald J;Republican Party;House of Representatives;Senate",
                    "column":"None",
                    "byline":"By Alexander Burns and Jonathan Martin",
                    "type":"Article",
                    "title":"‘I’ve Had It With This Guy’: G.O.P. Leaders Privately Blasted Trump After Jan. 6",
                    "abstract":"In the days after the attack, Representative Kevin McCarthy planned to tell Mr. Trump to resign. Senator Mitch McConnell told allies impeachment was warranted. But their fury faded fast.",
                    
                },
                {
                    "uri":"nyt://article/6869e94d-ea6a-57a0-a182-3348b23f7330",
                    "url":"https://www.nytimes.com/2022/04/21/business/cnn-plus-shutting-down.html",
                    "id":100000008311767,
                    "asset_id":100000008311767,
                    "source":"New York Times",
                    "published_date":"2022-04-21",
                    "updated":"2022-04-22 00:10:23",
                    "section":"Business",
                    "subsection":"",
                    "nytdsection":"business",
                    "adx_keywords":"News and News Media;Shutdowns (Institutional);Television;Cable Television;Media;Video Recordings, Downloads and Streaming;Licht, Christopher A (1971- );Morse, Andrew (1974- );CNN;Warner Bros Discovery",
                    "column":"None",
                    "byline":"By Michael M. Grynbaum, John Koblin and Benjamin Mullin",
                    "type":"Article",
                    "title":"CNN+ Streaming Service Will Shut Down Weeks After Its Start",
                    "abstract":"A major investment by CNN, which poached big-name anchors and threw a splashy launch party, ends abruptly at the hands of a new corporate leadership team.",
                    
                },
                {
                    "uri":"nyt://article/6ecd01e4-f917-50b4-9734-9b8b073efd8a",
                    "url":"https://www.nytimes.com/2022/04/21/arts/johnny-depp-amber-heard-trial.html",
                    "id":100000008313582,
                    "asset_id":100000008313582,
                    "source":"New York Times",
                    "published_date":"2022-04-21",
                    "updated":"2022-04-21 12:45:34",
                    "section":"Arts",
                    "subsection":"",
                    "nytdsection":"arts",
                    "adx_keywords":"Movies;Actors and Actresses;Domestic Violence;Suits and Litigation (Civil);Libel and Slander;Depp, Johnny;Heard, Amber;Washington Post;Fairfax County (Va)",
                    "column":"None",
                    "byline":"By Julia Jacobs",
                    "type":"Article",
                    "title":"Johnny Depp v. Amber Heard: What We Know",
                    "abstract":"Mr. Depp has sued Ms. Heard, his ex-wife, on grounds that she defamed him in an op-ed she wrote for The Washington Post.",
                    
                },
                {
                    "uri":"nyt://article/5268f1e7-fe23-5bb0-b4cf-29cb3f621774",
                    "url":"https://www.nytimes.com/2022/04/21/business/disney-florida-special-tax-status.html",
                    "id":100000008313466,
                    "asset_id":100000008313466,
                    "source":"New York Times",
                    "published_date":"2022-04-21",
                    "updated":"2022-04-21 23:28:04",
                    "section":"Business",
                    "subsection":"",
                    "nytdsection":"business",
                    "adx_keywords":"Taxation;Corporate Taxes;Amusement and Theme Parks;Homosexuality and Bisexuality;DeSantis, Ron;Disney, Walt, World (Lake Buena Vista, Fla);Walt Disney Company;Florida",
                    "column":"None",
                    "byline":"By Brooks Barnes",
                    "type":"Article",
                    "title":"Disney to Lose Special Tax Status in Florida Amid ‘Don’t Say Gay’ Clash",
                    "abstract":"Lawmakers in the state voted to revoke the company’s special designation after a dispute with Gov. Ron DeSantis over a new education law.",
                },
                {   "uri":"nyt://article/79e7977f-a4c6-51fb-bb43-e7d1ac11493e",
                    "url":"https://www.nytimes.com/2022/04/21/arts/johnny-depp-amber-heard-texts.html",
                    "id":100000008314141,
                    "asset_id":100000008314141,
                    "source":"New York Times",
                    "published_date":"2022-04-21",
                    "updated":"2022-04-21 23:15:07",
                    "section":"Arts",
                    "subsection":"",
                    "nytdsection":"arts",
                    "adx_keywords":"Libel and Slander;Bettany, Paul;Depp, Johnny;Franco, James;Heard, Amber;Manson, Marilyn;Fairfax County (Va)",
                    "column":"None",
                    "byline":"By Julia Jacobs",
                    "type":"Article",
                    "title":"Johnny Depp Confronted With Texts and Audio at Libel Trial",
                    "abstract":"Mr. Depp was questioned on the stand by lawyers for his ex-wife Amber Heard, whom he is suing for defamation.",
                }
            ]
        }
        with patch('nyt.requests.get') as mock_requests_get:
            mock_requests_get.return_value = mock_response_api
            self.assertEqual(
                ([item[0] for item in nyt_results()]),
                [   "‘I’ve Had It With This Guy’: G.O.P. Leaders Privately Blasted Trump After Jan. 6", 
                    "CNN+ Streaming Service Will Shut Down Weeks After Its Start", 
                    "Johnny Depp v. Amber Heard: What We Know",
                    "Disney to Lose Special Tax Status in Florida Amid ‘Don’t Say Gay’ Clash",
                    "Johnny Depp Confronted With Texts and Audio at Libel Trial"
                ]

            ) 

    def test_NYT_API_URLs(self):
        mock_response_api = MagicMock()
        mock_response_api.json.return_value = {
            "status":"OK",
            "results":[
                {
                    "uri":"nyt://article/aec25509-ec2e-591d-b1ab-d2229cdaadcf",
                    "url":"https://www.nytimes.com/2022/04/21/us/politics/trump-mitch-mcconnell-kevin-mccarthy.html",
                    "id":100000008311870,
                    "asset_id":100000008311870,
                    "source":"New York Times",
                    "published_date":"2022-04-21",
                    "updated":"2022-04-22 09:53:24",
                    "section":"U.S.",
                    "subsection":"Politics",
                    "nytdsection":"u.s.",
                    "adx_keywords":"Presidential Election of 2020;United States Politics and Government;Storming of the US Capitol (Jan, 2021);Impeachment;Books and Literature;McConnell, Mitch;McCarthy, Kevin (1965- );Trump, Donald J;Republican Party;House of Representatives;Senate",
                    "column":"None",
                    "byline":"By Alexander Burns and Jonathan Martin",
                    "type":"Article",
                    "title":"‘I’ve Had It With This Guy’: G.O.P. Leaders Privately Blasted Trump After Jan. 6",
                    "abstract":"In the days after the attack, Representative Kevin McCarthy planned to tell Mr. Trump to resign. Senator Mitch McConnell told allies impeachment was warranted. But their fury faded fast.",
                    
                },
                {
                    "uri":"nyt://article/6869e94d-ea6a-57a0-a182-3348b23f7330",
                    "url":"https://www.nytimes.com/2022/04/21/business/cnn-plus-shutting-down.html",
                    "id":100000008311767,
                    "asset_id":100000008311767,
                    "source":"New York Times",
                    "published_date":"2022-04-21",
                    "updated":"2022-04-22 00:10:23",
                    "section":"Business",
                    "subsection":"",
                    "nytdsection":"business",
                    "adx_keywords":"News and News Media;Shutdowns (Institutional);Television;Cable Television;Media;Video Recordings, Downloads and Streaming;Licht, Christopher A (1971- );Morse, Andrew (1974- );CNN;Warner Bros Discovery",
                    "column":"None",
                    "byline":"By Michael M. Grynbaum, John Koblin and Benjamin Mullin",
                    "type":"Article",
                    "title":"CNN+ Streaming Service Will Shut Down Weeks After Its Start",
                    "abstract":"A major investment by CNN, which poached big-name anchors and threw a splashy launch party, ends abruptly at the hands of a new corporate leadership team.",
                    
                },
                {
                    "uri":"nyt://article/6ecd01e4-f917-50b4-9734-9b8b073efd8a",
                    "url":"https://www.nytimes.com/2022/04/21/arts/johnny-depp-amber-heard-trial.html",
                    "id":100000008313582,
                    "asset_id":100000008313582,
                    "source":"New York Times",
                    "published_date":"2022-04-21",
                    "updated":"2022-04-21 12:45:34",
                    "section":"Arts",
                    "subsection":"",
                    "nytdsection":"arts",
                    "adx_keywords":"Movies;Actors and Actresses;Domestic Violence;Suits and Litigation (Civil);Libel and Slander;Depp, Johnny;Heard, Amber;Washington Post;Fairfax County (Va)",
                    "column":"None",
                    "byline":"By Julia Jacobs",
                    "type":"Article",
                    "title":"Johnny Depp v. Amber Heard: What We Know",
                    "abstract":"Mr. Depp has sued Ms. Heard, his ex-wife, on grounds that she defamed him in an op-ed she wrote for The Washington Post.",
                    
                },
                {
                    "uri":"nyt://article/5268f1e7-fe23-5bb0-b4cf-29cb3f621774",
                    "url":"https://www.nytimes.com/2022/04/21/business/disney-florida-special-tax-status.html",
                    "id":100000008313466,
                    "asset_id":100000008313466,
                    "source":"New York Times",
                    "published_date":"2022-04-21",
                    "updated":"2022-04-21 23:28:04",
                    "section":"Business",
                    "subsection":"",
                    "nytdsection":"business",
                    "adx_keywords":"Taxation;Corporate Taxes;Amusement and Theme Parks;Homosexuality and Bisexuality;DeSantis, Ron;Disney, Walt, World (Lake Buena Vista, Fla);Walt Disney Company;Florida",
                    "column":"None",
                    "byline":"By Brooks Barnes",
                    "type":"Article",
                    "title":"Disney to Lose Special Tax Status in Florida Amid ‘Don’t Say Gay’ Clash",
                    "abstract":"Lawmakers in the state voted to revoke the company’s special designation after a dispute with Gov. Ron DeSantis over a new education law.",
                },
                {   "uri":"nyt://article/79e7977f-a4c6-51fb-bb43-e7d1ac11493e",
                    "url":"https://www.nytimes.com/2022/04/21/arts/johnny-depp-amber-heard-texts.html",
                    "id":100000008314141,
                    "asset_id":100000008314141,
                    "source":"New York Times",
                    "published_date":"2022-04-21",
                    "updated":"2022-04-21 23:15:07",
                    "section":"Arts",
                    "subsection":"",
                    "nytdsection":"arts",
                    "adx_keywords":"Libel and Slander;Bettany, Paul;Depp, Johnny;Franco, James;Heard, Amber;Manson, Marilyn;Fairfax County (Va)",
                    "column":"None",
                    "byline":"By Julia Jacobs",
                    "type":"Article",
                    "title":"Johnny Depp Confronted With Texts and Audio at Libel Trial",
                    "abstract":"Mr. Depp was questioned on the stand by lawyers for his ex-wife Amber Heard, whom he is suing for defamation.",
                }
            ]
        }
        with patch('nyt.requests.get') as mock_requests_get:
            mock_requests_get.return_value = mock_response_api
            self.assertEqual(
                ([item[1] for item in nyt_results()]),
                [   "https://www.nytimes.com/2022/04/21/us/politics/trump-mitch-mcconnell-kevin-mccarthy.html", 
                    "https://www.nytimes.com/2022/04/21/business/cnn-plus-shutting-down.html", 
                    "https://www.nytimes.com/2022/04/21/arts/johnny-depp-amber-heard-trial.html",
                    "https://www.nytimes.com/2022/04/21/business/disney-florida-special-tax-status.html",
                    "https://www.nytimes.com/2022/04/21/arts/johnny-depp-amber-heard-texts.html"
                ]
            ) 


class algorithms_tests:

    def test_sort_emotions(self):
        ''' This will directly test our algorithm for sorting the entries by emotions '''
        




if __name__ == "__main__":
    unittest.main()