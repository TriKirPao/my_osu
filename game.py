import pygame
from parser import *

def check_click(event):
    pass

def load_pause_menu(play):
    while pause:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.mixer.music.pause()
            pause = True
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z or event.key == pygame.K_e:
                check_click(event)

def load_game(play, name):
    circle_list = parser(name)
    screen = play.screen
    launch = True
    play.blit_back()
    clock = pygame.time.Clock()
    pygame.time.tick(60)
    path = "song/" + name + "/" + name + ".mp3"
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()
    image = "song/" + name + "/" + name + ".jpg"
    pygame.image.load(image)
    screen.blit(image, (0, 0))
    while launch:
        event = load_pause_menu()
