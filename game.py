import pygame
from parser import *
import math

def check_click(event, circle_list, play):
    x,y = pygame.mouse.get_pos()
    for i in range(0, len(circle_list)):
        print("nbr en cours : {}, number qui apparait: {}, booleen du cercle: {}, valeur de la gauche {}, valeur de la droite :{}".format(play.number, circle_list[i].number, circle_list[i].bool, math.pow((x - int(circle_list[i].x) - 40), 2) + math.pow((y - int(circle_list[i].y) - 40), 2), math.pow((1200), 2)))
        if int(circle_list[i].bool) == 1 and math.pow((x - int(circle_list[i].x) - 40), 2) + math.pow((y - int(circle_list[i].y) - 40), 2) <= math.pow((50), 2) and play.number == int(circle_list[i].number):
            print("salut")
            circle_list[i].bool = 0
            try:
                play.number = circle_list[i + 1].number
            except:
                pass

def load_pause_menu(play, circle_list):
    resume = pygame.image.load("pic/continue.png")
    retry = pygame.image.load("pic/retry.png")
    backmenu = pygame.image.load("pic/backmenu.png")
    for mainevent in pygame.event.get():
        if (mainevent.type == pygame.KEYDOWN and mainevent.key == pygame.K_ESCAPE):
            pygame.mixer.music.pause()
            play.screen.blit(resume, (700, 300))
            play.screen.blit(retry, (700, 500))
            play.screen.blit(backmenu, (700, 700))
            pygame.display.flip()
            while 1:
                Mx = pygame.mouse.get_pos()[0]
                My = pygame.mouse.get_pos()[1]
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and Mx >= 700 and Mx <= 700 + 530 and My >= 300 and My <= 300 + 124:
                        pygame.mixer.music.unpause()
                        return 0
                    if event.type == pygame.MOUSEBUTTONDOWN and Mx >= 700 and Mx <= 700 + 530 and My >= 500 and My <= 500 + 124:
                        pygame.mixer.music.rewind()
                        return 1
                    if event.type == pygame.MOUSEBUTTONDOWN and Mx >= 700 and Mx <= 700 + 530 and My >= 700 and My <= 700 + 124:
                        pygame.mixer.music.stop()
                        return 2
        if mainevent.type == pygame.KEYDOWN and (mainevent.key == pygame.K_z or mainevent.key == pygame.K_e):
            check_click(mainevent, circle_list, play)

def print_number(screen, circle):
    name = "texture/default-" + circle.number + ".png"
    number = pygame.image.load(name)
    screen.blit(number, (int(circle.x) + 40, int(circle.y) + 40))

def load_game(play, name):
    circle_list = parser(name)
    screen = play.screen
    launch = True
    play.blit_back()
    clock = pygame.time.Clock()
    path = "song/" + name + "/" + name + ".mp3"
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    image = "song/" + name + "/" + name + ".jpg"
    timage = pygame.image.load(image)
    time = 0
    toblit = []
    while launch:
        clock.tick(60)
        time += clock.get_time()
        screen.blit(timage, (0, 0))
        event = load_pause_menu(play, circle_list)
        if event == 2 or pygame.mixer.music.get_busy() == False:
            launch = False
        for circle in circle_list:
            if circle.time * 1000 <= time and circle.bool == 2:
                circle.bool = 1
            if circle.bool == 1 and circle.time * 1000 + 2000 <= time:
                circle.bool = 0
        for circle in circle_list:
            if circle.bool == 1:
                circlepic = pygame.image.load("texture/hitcircle.png")
                screen.blit(circlepic, (int(circle.x), int(circle.y)))
                print_number(screen, circle)
        pygame.display.flip()
    play.number = 0
