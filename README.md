# My-Daily-Cup
A personalized blog-based web application.

Please be patient, this application is still under development.

Make sure to create your own branch so we can avoid issues with conflicting code!

# Openweather API DOC
'https://openweathermap.org/current'

To ensure Openweather works, request an API Key from here
'https://openweathermap.org/'

After recieving an API Key, create a .env file in the directory (if you have not done so already)
and paste 'OPENWEATHER_KEY = "<YOUR_API_KEY_HERE>"'

# Fun Fact API
Displays a random fun fact!
https://aakhilv.notion.site/fun-bea0f2ca5aaa411f93a3a9fa1699ce39


# Flask_Login
To use this library in your app, you must make sure to generate a secret key to store in your .env file and/or Heroku config variables.

To generate your key, run:

python3 -c 'import secrets; print(secrets.token_hex())'

#   Twitter API
    https://developer.twitter.com/en/docs
    To use this API with your own app, you would first have to set up a twitter developer account.
    There you will be given your own api_key and secret_key.
    You will also need to upgrade your account to "Elevated" which will give you access to the "trends" that we use in our app.
    Store the keys somewhere safe where you can retrieve them for your requests to to the twitter API.
