import pygame
from pygame.locals import *

pygame.init()

SCREEN = pygame.display.set_mode((640, 640))
pygame.display.set_caption('Test')

import cacapi.modules as cacapi

editor = cacapi.Editor_Mode('o', screen=SCREEN)

d_Button = cacapi.Button(160, 160, screen=SCREEN)
d_InputBox = cacapi.InputBox((320, 320), screen=SCREEN)
d_InputBox.set_Type('dynamic')
d_Text = cacapi.Text('Test', color = (255, 255, 255), screen=SCREEN, pos=(480, 480))

while 1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT: exit()

        if event.type == pygame.KEYDOWN:

            editor.check(event)
            d_InputBox.listen_text(event)

            if event.key == pygame.K_s and editor.open :
                
                import time
                editor.save_Status((d_Button, d_InputBox))
                time.sleep(1)
                print('saved')


        if event.type == pygame.MOUSEBUTTONUP:
            editor.drop()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if d_Button.isClicked(): editor.drag(d_Button)
            if d_InputBox.listen_clicks(): editor.drag(d_InputBox)

    SCREEN.fill((0, 0, 0))    
    editor.Show()

    d_Button.Show()
    d_InputBox.Show()
    d_Text.Show()

    pygame.display.update()