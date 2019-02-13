#!/usr/bin/env python

import pygame
import os
import glob
from song_menu import *
from game import *

pygame.init()
blue = [0, 60, 155]
black = [0, 0, 0]
white = [255, 255, 255]

##arial_font = pygame.font.SysFont("arial", 20, True)
##hello_text = arial_font.render("Bonjour", False, blue)

class rectangle:

    def __init__(self, y):
        self.x = 1000
        self._y = y
        self.width = 700
        self.height = 135
        self.img = 0

    def y_getage(self):
        return self._y

    def y_setage(self, new_y):
        if  new_y < 0 - self.height:
            self._y = 0 - self.height
        else:
            self._y = new_y

    y = property(y_getage, y_setage)

    def rect_creation(self):
        self.img = pygame.image.load("texture/selection.png")
        return (self.img)


my_rec = []
for i in range(0, 8):
    my_rec.append(rectangle(i * 135))

def text_creation(music):
    arial_font = pygame.font.SysFont('police/police.ttf', 60, True)
    color = (0, 0, 0, 128)
    music_name = arial_font.render(music, True, color)
    return (music_name)

music = []
for root, dirs, files in os.walk("song", topdown=False):
    for name in dirs:
        music.append(name)

def list_creation(music, start):
    m_list = []
    if (len(music) < 8):
        size = len(music)
    else:
        size = 8
    for i in range(start, start + size):
        m_list.append(music[i])
    return (m_list)

def check_event(start):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == 27:
                return 3
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4 and start > 0:
                return 2
            elif event.button == 5 and start < len(music) - 8:
                return 1
            elif event.button == 1:
                return 4
        if event.type == pygame.QUIT:
            return 0

def choice_map():
    Mx = pygame.mouse.get_pos()[0]
    My = pygame.mouse.get_pos()[1]
    i = 0
    for rect in my_rec:
        if (Mx >= rect.x and Mx <= rect.x + rect.width) and (My >= rect.y and My <= rect.y + rect.height):
            return i
        i += 1

def blit_map(idx, music_list, screen):
    path = "song/" + music_list[idx]
    for filename in glob.glob(os.path.join(path, '*.jpg')):
        path_png = filename
        bgn = pygame.image.load(path_png)
        return bgn

def second_screen(play):
    launched = True
    start = 0
    bol_game = 0
    screen = play.screen
    while launched:
        event = check_event(start)
        if event == 0:
            launched = False
        elif event == 1:
            start += 1
        elif event == 2:
            start -= 1
        elif event == 3:
            return
        play.blit_back()
        music_list = list_creation(music, start)
        i = 0
        j = 0
        for rec in my_rec:
            screen.blit(my_rec[j].rect_creation(), [my_rec[j].x, my_rec[j].y])
            if i < len(music_list):
                screen.blit(text_creation(music_list[i]), [rec.x + 85, rec.y + rec.height / 2 - 15])
                i += 1
            j += 1
        if event == 4:
            idx = choice_map()
            if idx != None and idx < len(music_list):
                bol_game = 1
                play.bgrnd = blit_map(idx, music_list, screen)
                pygame.mixer.music.stop()
                selec_music(music_list[idx])
            if idx == None:
                bol_game = 0
        if bol_game == 1:
            if event == 4:
                idx_nd = choice_map()
                if idx_nd == idx:
                    load_game(play, music_list[idx])
                if idx_nd == None:
                    bol_game = 0

        pygame.display.flip()
    return
