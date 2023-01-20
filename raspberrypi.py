import random
import time

import vlc
from os import listdir
from os.path import isfile, join
import RPi.GPIO as GPIO

button_pin = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN)

mp3s = [f for f in listdir('mp3s') if isfile(join('mp3s', f)) and f.endswith('.mp3')]
vlc.MediaPlayer('startup.wav').play()
while True:
    if GPIO.input(button_pin):
        chosen = random.randint(0, len(mp3s))
        player = vlc.MediaPlayer(f'mp3s/{mp3s[chosen]}')
        player.play()
        time.sleep(2)
        while player.is_playing():
            if GPIO.input(button_pin):
                player.stop()
                break
            time.sleep(0.1)
    time.sleep(0.1)