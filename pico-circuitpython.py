import board
import busio
import sdcardio
import storage
import os
import digitalio
import audiomp3, audiopwmio
import time
import random

spi = busio.SPI(board.GP10, MOSI=board.GP11, MISO=board.GP8)
cs = board.GP9
sdcard = sdcardio.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd", readonly=True)
mp3files = ['/sd/' + f for f in os.listdir('/sd/') if f.endswith('.mp3')]
print(f'found {len(mp3files)} files on SD')

audio = audiopwmio.PWMAudioOut(board.GP0)

button = digitalio.DigitalInOut(board.GP7)
button.switch_to_input(pull=digitalio.Pull.UP)


while True:
    if not button.value:
        index = random.randint(0, len(mp3files) - 1)
        file = mp3files[index]
        print(f'playing file {index} of {len(mp3files)}, {file}')
        decoder = audiomp3.MP3Decoder(open(file, "rb"))
        audio.play(decoder)
        print('playing', decoder.file)
        time.sleep(1)
        # This allows you to do other things while the audio plays!
        while audio.playing:
            if not button.value:
                print('stopping')
                audio.stop()
                time.sleep(1)
        print('done')
print('shutdown')        

