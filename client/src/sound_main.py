#!/usr/bin/env python3

import numpy as np
import sounddevice as sd
import requests
import configparser

config = configparser.ConfigParser()

while True:
    
    # Read configuration
    config.read('config.ini')

    # Set variable with configuration file
    duration = int(config['DEFAULT']['Duration'])
    sd.default.device = int(config['DEFAULT']['Device'])
    sd.default.samplerate = int(config['DEFAULT']['Samplerate'])
    url_data = config['iot.tryhard.fr']['UrlData']

    # Capture sound
    list = []
    def audio_callback(indata, frames, time, status):
        volume_norm = int(np.linalg.norm(indata) * 10)
        list.append(volume_norm)
        #print("|" * int(volume_norm))

    stream = sd.InputStream(callback=audio_callback)
    with stream:
        sd.sleep(duration * 1000)
   
    # Calcul mean
    mean = int(sum(list) / len(list))
    print(mean)

    # Send Data
    #data = {
     #  'device_id':'1',
     #  'decibels': mean
    #}
    #r = requests.post(url = url, data = data)
