Heroku Link: https://my-daily-cup-polished.herokuapp.com/
# My-Daily-Cup
A personalized blog-based web application.

![My Daily Cup Image](https://github.com/AtilG/My-Daily-Cup-Polished/blob/main/static/readme.png)

# Openweather API DOC
'https://openweathermap.org/current'

To ensure Openweather works, request an API Key from here
'https://openweathermap.org/'

After recieving an API Key, create a .env file in the directory (if you have not done so already)
and paste `OPENWEATHER_KEY = "<YOUR_API_KEY_HERE>"`

Next install 
pip install geocoder

# Fun Fact API
Displays a random fun fact!
https://aakhilv.notion.site/fun-bea0f2ca5aaa411f93a3a9fa1699ce39


# Flask_Login
To use this library in your app, you must make sure to generate a secret key to store in your .env file and/or Heroku config variables.

To generate your key, run:

`python3 -c 'import secrets; print(secrets.token_hex())`


# Twitter API
https://developer.twitter.com/en/docs
To use this API with your own app, you would first have to set up a twitter developer account.
There you will be given your own api_key and secret_key.
You will also need to upgrade your account to "Elevated" which will give you access to the "trends" that we use in our app.
Store the keys somewhere safe where you can retrieve them for your requests to to the twitter API.
Note, in order to use the Twitter API in the same manner as us, you must use the command: "pip install tweepy"

# Sentiment Analysis API 
To use ParallelDots' APIs, you must obtain a key by signing up at https://dashboard.komprehend.io/signUp. Once you get your key, place it in your `.env` file and Heroku config variables.

In your .env:
`SENTIMENT_KEY = "<YOUR_API_KEY_HERE>"`

Another thing to know before using this API is that you need to install their library for Python by running:

`pip install paralleldots`

# Linting

Disabled linter for the `tests.py` as this is just for testing logic in our API
Disabled linting in `models.py` which is our database model due to multiple false positives such as no member and too few classes.
Disabled nomember error in `database_functions.py` and `app.py`. This can also be resolved by adding loading the installed plugin to your `settings.json` file using
` "python.linting.pylintArgs": ["--load-plugins", "pylint_flask_sqlalchemy", "pylint_flask"]`


