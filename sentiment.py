"""This file will handle our sentimental API"""
import os
import paralleldots
from paralleldots import config
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# set the key
config.set_api_key(os.getenv("SENTIMENT_KEY"))

# get the emotion of the text
def get_emotion(entry):
    """This method will get the emotion for an individual journal entry"""
    tones = []
    emotions = paralleldots.emotion(entry)

    # access data of each emotion
    emotions = emotions["emotion"].items()
    print(emotions)

    maximum = {"emotion": "None", "data": -1}  # hold highest emotion
    for data in emotions:
        # find maximum emotion value in case there is no value higher than 0.25
        if data[1] > maximum["data"]:
            maximum["emotion"] = data[0]
            maximum["data"] = data[1]
        # threshold for possible emotions conveyed
        if data[1] > 0.25:
            tones.append(data[0])
    # case to make sure a tone is shown
    if len(tones) == 0:
        try:
            tones.append(maximum["emotion"])
        except:
            tones.append("Bored")

    # correcting the 'fear' to 'fearful' for a better sound
    for tone in tones:
        if tone == "Fear":
            tone = "Fearful"

    return tones
