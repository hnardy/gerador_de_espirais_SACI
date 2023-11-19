import pygame
from random import randint
def pmusic(file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def stopmusic():
    pygame.mixer.music.stop()

def getmixerargs():
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan

def initMixer():
    BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
    FREQ, SIZE, CHAN = getmixerargs()
    pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)



def play():
    playlist = ["one.mp3", "two.mp3", "three.mp3", "four.mp3"]
    initMixer()
    file = playlist[randint(0,len(playlist)-1)]
    pmusic(file)



