import pygame
from parser import *

def load_pause_menu(play):
    pigame.mixer.music.pause()
    pause = True
    while pause:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            launch = False
            pygame.mixer.music.unpause()
            return 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            pygame.mixer.music.rewind()
            launch = False
            return 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            launch = False
            pygame.mixer.music.stop()
            return 2

def check_game_event():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == 27:
            return load_pause_menu(play)

def load_game(play, name):
    circle_list = parser(name)
    screen = play.screen
    launch = True
    play.blit_back()
    while launch:
        event = check_game_event()
