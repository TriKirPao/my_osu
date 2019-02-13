#!/usr/bin/env python

import pygame, os, glob

pygame.init()
window_resolution = (1920, 1080)
black = [255, 255, 255]

pygame.display.set_caption("Rectangle test")
window_surface = pygame.display.set_mode(window_resolution, pygame.FULLSCREEN)

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
    color = (255, 255, 255, 128)
    music_name = arial_font.render(music, True, color)
    return (music_name)

music = []
for root, dirs, files in os.walk("Songs", topdown=False):
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

def second_screen():
    launched = True
    start = 0
    while launched:
        os.system('clear')
        screen = pygame.image.load("pic/six.jpg")
        window_surface.blit(screen, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    pygame.quit()
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4 and start > 0:
                    start -= 1
                elif event.button == 5 and start < len(music) - 8:
                    start += 1
            if event.type == pygame.QUIT:
                    launched = False
        music_list = list_creation(music, start)
        i = 0
        j = 0
        for rec in my_rec:
            window_surface.blit(my_rec[j].rect_creation(), [my_rec[j].x, my_rec[j].y])
            if i < len(music_list):
                window_surface.blit(text_creation(music_list[i]), [rec.x + 85, rec.y + rec.height / 2 - 15])
                i += 1
            j += 1
        pygame.display.flip()

second_screen()
