#!/usr/bin/env python

import pygame

pygame.init()
window_resolution = (1920, 1080)
blue = [0, 60, 155]
black = [0, 0, 0]
white = [255, 255, 255]

pygame.display.set_caption("Rectangle test")
window_surface = pygame.display.set_mode(window_resolution, pygame.FULLSCREEN)

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

def second_screen():
    launched = True
    start = 0
    while launched:
        for event in pygame.event.get():
            window_surface.fill((black))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4 and start > 0:
                    start -= 1
                elif event.button == 5 and start < len(music) - 8:
                    start += 1
            music_list = list_creation(music, start)
            if event.type == pygame.QUIT:
                launched = False
            i = 0
            for rec in my_rec:
                pygame.draw.rect(window_surface, blue, rec.rect_creation(), 2)
                window_surface.blit(text_creation(music_list[i]), [rec.x + 40, rec.y + rec.height / 2 - 30])
                i += 1
            pygame.display.flip()

second_screen()
