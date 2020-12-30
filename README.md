# Birb Box
Plays a random episode of the BBC Radio 4 program "Tweet of the Day" when the button is pressed. 

Implemented with Raspberry Pi Zero, MAX98357A amplifier and small 1W speaker

Video of it in action: https://youtu.be/RF9HhtpWjfE

## Prerequisites
A device to run this on should have VLC installed along with python 3.7 or greater. 
You will also need to install the python bindings for vlc `python-vlc`

### scrape.py

Downloads all tweet of the day episodes from the BBC website https://www.bbc.co.uk/programmes/b01s6xyk/episodes/downloads
Tweak the line `for page in range(1, 24):` to determine how many pages of episodes to download. If more episodes are added later more than 24 pages may exist.
This script only needs run once to get the mp3 files and is simply intended to automate the download process.

### tweet-of-the-day.py

Simple script that waits for the press of a button connected to GPIO pin 5 and when pressed will play a random episode. 
On my raspberry pi I run this as a service using systemd.
