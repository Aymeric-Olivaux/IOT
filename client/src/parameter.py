#!/usr/bin/env python3

import speech_recognition as sr
import configparser
import requests

r = sr.Recognizer()
config = configparser.ConfigParser()

def recognition():
    # Read configuration
    config.read('config.ini')


    # Set variable with configuration file
    url_config = config['ambizen.tryhard.fr']['UrlConfig']
    config_id = int(config['DEFAULT']['ConfigID'])


    # Get config file from the backend and modify threshold in config file
    response = requests.get(url_config + str(config_id))
    jsonResponse = response.json()
    print(jsonResponse)
    threshold = jsonResponse['threshold']
    config['DEFAULT']['Threshold'] = str(threshold)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    # Set threshold with voice recognition
    with sr.WavFile("output.wav") as source:              # use "output.wav" as the audio source
        audio = r.record(source)                        # extract audio data from the file
        try:
            text = r.recognize_google(audio, language="fr-FR")
            print("\ntext: " +  text)

            list = text.split(" ")
            if list[0] == "db" or list[0] == "décibel" or list[0] == "décibels":
                try:
                    respond = requests.post(url = url_config + str(config_id), json = {'threshold': int(list[1])})
                    print("\n" + respond)
                except:
                    print("Pas réussi à post")



        except:
            print('Sorry.. run again...')

if __name__ == "__main__":
    recognition()
