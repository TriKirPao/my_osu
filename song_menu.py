import os
import glob
import random
import pygame

def create_list():
    list= []
    for root, dirs, files in os.walk("song", topdown=False):
        for name in dirs:
            for filename in glob.glob(os.path.join(os.path.join(root, name), '*.mp3')):
                list.append(filename)
    pygame.mixer.music.load(random.choice(list))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.30)
    return list

def launch_music(list):
    if pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.load(random.choice(list))
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.30)
