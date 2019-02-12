import os
import glob
import pygame
pygame.init()
ecran = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
list = []
for root, dirs, files in os.walk("song", topdown=False):
    for name in dirs:
        for filename in glob.glob(os.path.join(os.path.join(root, name), '*.mp3')):
            list.append(filename)
print("c'est la liste : {}".format(list))

pygame.mixer.music.load("/home/jonathan/Bureau/musiquegroove/pokemon/pokemon-b2w2-remix-champion-iris-battle-music-mashup-hq.mp3")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            pygame.mixer.music.rewind()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            pygame.mixer.music.unpause()
