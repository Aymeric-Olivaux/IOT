#!/usr/bin/env python3

import numpy as np
import sounddevice as sd

duration = 10 #in seconds
sd.default.samplerate = 44100
sd.default.device = 1

def audio_callback(indata, frames, time, status):
   volume_norm = np.linalg.norm(indata) * 10
   print("|" * int(volume_norm))


stream = sd.InputStream(callback=audio_callback)
with stream:
   sd.sleep(duration * 1000)

#import subprocess
#import sys

#result = subprocess.run(['soundmeter', '-c', '-s', '3', '|', 'grep', 'avg', '|', 'awk', '\'{print $2}\''], capture_output=True)
#result = subprocess.run(['soundmeter -c -s 3 | grep avg | awk \'{print $2}\''], capture_output=True)
