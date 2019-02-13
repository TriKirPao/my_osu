#!/usr/bin/env python

import pygame

pygame.init()
blue = [0, 60, 155]
black = [0, 0, 0]
white = [255, 255, 255]

##arial_font = pygame.font.SysFont("arial", 20, True)
##hello_text = arial_font.render("Bonjour", False, blue)

class rectangle:

    def __init__(self, y):
        self.x = 1220
        self._y = y
        self.width = 700
        self.height = 135
        self.rec = 0

    def y_getage(self):
        return self._y

    def y_setage(self, new_y):
        if  new_y < 0 - self.height:
            self._y = 0 - self.height
        else:
            self._y = new_y

    y = property(y_getage, y_setage)

    def rect_creation(self):
        self.rec = pygame.Rect(self.x, self.y, self.width, self.height)
        return (self.rec)


my_rec = []
for i in range(0, 8):
    my_rec.append(rectangle(i * 135))

def text_creation(music):
    arial_font = pygame.font.SysFont('police/police.ttf', 60, True)
    music_name = arial_font.render(music, True, white)
    return (music_name)

music = ["Yes", "No", "Yah", "Hey", "Bah", "Hello", "zfz", "fzfz", "ve", "ffzs", "fefe"]

def list_creation(music, start):
    m_list = []
    for i in range(start, start + 8):
        m_list.append(music[i])
    return (m_list)

def second_screen(play):
    launched = True
    start = 0
    while launched:
        play.blit_back()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4 and start > 0:
                    start -= 1
                elif event.button == 5 and start < len(music) - 8:
                    start += 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                launched = False
            music_list = list_creation(music, start)
            if event.type == pygame.QUIT:
                launched = False
            i = 0
            for rec in my_rec:
                pygame.draw.rect(play.screen, blue, rec.rect_creation(), 2)
                play.screen.blit(text_creation(music_list[i]), [rec.x + 40, rec.y + rec.height / 2 - 30])
                i += 1
            pygame.display.flip()
    return
            
""" 
------------------------------------------


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
 """