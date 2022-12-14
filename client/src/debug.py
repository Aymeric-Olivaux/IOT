#!/usr/bin/env python3

import numpy as np
import sounddevice as sd
import requests
import configparser
import json
import asyncio
from pixel_ring import pixel_ring
from gpiozero import LED


config = configparser.ConfigParser()
power = LED(5)


while True:

    # Read configuration
    config.read('config.ini')

    # Set variable with configuration file
    duration = int(config['DEFAULT']['Duration'])
    sd.default.device = int(config['DEFAULT']['SoundDeviceID'])
    sd.default.samplerate = int(config['DEFAULT']['Samplerate'])
    url_data = config['ambizen.tryhard.fr']['UrlData']
    config_id = int(config['DEFAULT']['ConfigID'])
    threshold = int(config['DEFAULT']['threshold'])
    # Capture sound
    list = []
    def audio_callback(indata, frames, time, status):
        volume_norm = int(np.linalg.norm(indata) * 10)
        list.append(volume_norm)
        print("|" * int(volume_norm))

    stream = sd.InputStream(callback=audio_callback)
    with stream:
        sd.sleep(duration * 1000)

