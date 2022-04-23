Heroku Link: https://my-daily-cup-polished.herokuapp.com/
# My-Daily-Cup
A personalized blog-based web application. This application is a blog where you can create journal entries with sentient analysis, a task list and interact with various widgets such as daily pictures from NASA, Twitters top trending, a fun fact of the day and more!

![My Daily Cup Image](https://github.com/AtilG/My-Daily-Cup-Polished/blob/main/static/readme.png)

# Openweather API DOC

Openweather API will fetch the weather for your location and return you various data about the current weather.
'https://openweathermap.org/current'

To ensure Openweather works, request an API Key from here
'https://openweathermap.org/'

After recieving an API Key, create a .env file in the directory (if you have not done so already)
and paste `OPENWEATHER_KEY = "<YOUR_API_KEY_HERE>"`

Next install 
pip install geocoder

# Fun Fact API
Displays a random fun fact! The fun fact is randomly generated from a list of amazing fun facts.
https://aakhilv.notion.site/fun-bea0f2ca5aaa411f93a3a9fa1699ce39

# New York Times API
New York Times API to fetch various NYT Articles. Request a key from https://developer.nytimes.com/apis and insert `NYT_KEY = <INSERT KEY HERE>` into .env file.
# NASA API
NASA API that provides various information such as an image of the day, weather service for mars and other features. Request an API key here https://api.nasa.gov/ after create 
`NASA_KEY = <INSERT KEY HERE> ` in your `.env` file.
# Flask_Login
To use this library in your app, you must make sure to generate a secret key to store in your .env file and/or Heroku config variables.

To generate your key, run:

`python3 -c 'import secrets; print(secrets.token_hex())`


# Twitter API
https://developer.twitter.com/en/docs
This API fetches twitters top trending tags based of whatever you set your paramters as.
To use this API with your own app, you would first have to set up a twitter developer account.
There you will be given your own api_key and secret_key.
You will also need to upgrade your account to "Elevated" which will give you access to the "trends" that we use in our app.
Store the keys somewhere safe where you can retrieve them for your requests to to the twitter API.
Note, in order to use the Twitter API in the same manner as us, you must use the command: "pip install tweepy"

# Sentiment Analysis API 
The sentiment analysis API returns results based off of your input attempting to read the emotion behind the words it recieves.
To use ParallelDots' APIs, you must obtain a key by signing up at https://dashboard.komprehend.io/signUp. Once you get your key, place it in your `.env` file and Heroku config variables.

In your .env:
`SENTIMENT_KEY = "<YOUR_API_KEY_HERE>"`

Another thing to know before using this API is that you need to install their library for Python by running:

`pip install paralleldots`

# Linting

Disabled linting in `models.py` which is our database model due to multiple false positives such as no member and too few classes.
Disabled nomember error in `database_functions.py` and `app.py`. This can also be resolved by adding loading the installed plugin to your `settings.json` file using
` "python.linting.pylintArgs": ["--load-plugins", "pylint_flask_sqlalchemy", "pylint_flask"]`
Disabled pylint error C0301, Which essentially tells us that the line is too long. It was disabled because all of the urls and uris in the tests.py file were too long, and the file would be thousands of lines long if we broke the links down into seperate lines.


