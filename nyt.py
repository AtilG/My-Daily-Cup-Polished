import os
import requests
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

NYT_KEY = os.getenv("NYT_KEY")

def nyt_results():
    """Displays most popular NYT Articles from past day"""
    article_name = []
    article_url = []
    responses = requests.get(f"https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key={NYT_KEY}")
    responses_json = responses.json()
    for x in range(5):
        article_name.append(responses_json["results"][x]["title"])
        article_url.append(responses_json["results"][x]["url"])
    return zip(article_name, article_url)
