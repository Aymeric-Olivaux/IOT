#!/usr/bin/env python3

import asyncio
import configparser
import json
import pyloudnorm as pyln
import requests
import soundfile as sf
import sounddevice as sd
import soundfile as sf


from light import *

config = configparser.ConfigParser()

def sound():
    # Read configuration
    config.read('config.ini')

    # Set variable with configuration file
    url_data = config['ambizen.tryhard.fr']['UrlData']
    config_id = int(config['DEFAULT']['ConfigID'])
    threshold = int(config['DEFAULT']['threshold'])

    # Mesure Loudness
    data, rate = sf.read("output.wav")
    meter = pyln.Meter(rate) 
    loudness = meter.integrated_loudness(data)

    # 0 LUFS = 120 db
    # -42 LUFS = 0 db
    # Convert Loudness to decibel
    db = 120 + (loudness / 60 * 120)

    print("loudness: " + str(loudness))
    print("db: " + str(db))

    # Light
    if db > threshold:
        filename = 'alerte.wav'
        # Extract data and sampling rate from file
        data, fs = sf.read(filename, dtype='int16')
        sd.play(data, fs)
        status = sd.wait()  # Wait until file is done playing
        asyncio.run(light_on())


    # Post
    r = requests.post(url = url_data, json = {'device_id': config_id, 'decibels': int(db)})

if __name__ == "__main__":
    sound()


#!/usr/bin/env python3



