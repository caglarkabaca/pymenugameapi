import pygame
from pygame.locals import *
pygame.init()

SIZE = (640, 640)

# RENKLER

SIYAH = (0, 0, 0)
BEYAZ = (255, 255, 255)
YESIL = (0, 255, 0)
KIRMIZI = (255, 0, 0)
MAVI = (0, 0, 255)

CURRENT_COLOR = SIYAH
TITLE = "test pythonu"

screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption(TITLE)


from cacapi.modules import Button, Text, Color_Pallette, InputBox

i = InputBox((320,320),size=(125,25),screen=screen)
i.set_Text('text')


while 1:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print('Exiting.. ')
            exit()
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            i.listen_clicks()

        if event.type == pygame.KEYDOWN:

            if event.key == K_UP:

                i.is_Writable = True

            if event.key == K_DOWN:

                i.is_Writable = False

            i.listen_text(event)

            


    screen.fill(CURRENT_COLOR)

    i.Show()

    pygame.display.update() # Ekranı yeniliyor