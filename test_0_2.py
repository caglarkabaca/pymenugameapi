"""
0.2 için login ekranı 
"""

import pygame
from pygame.locals import *
from cacapi.modules import Button, Text, InputBox

SIZE = (480, 320)

USERNAME = 'admin'
PASSWORD = 'admin'

#region COlORS

M_BUTTON = (228,249,245)
M_BACK = (48,227,202)
M_SHADOW = (17,153,158)
M_TEXT = (64,81,78)

#endregion

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Login page | v0.2')


# --------------------

login_text = Text('cacapi login ekranı v0.2', (240, 50), color = M_TEXT, size = 28, screen=screen )

kullanici_adi_text = Text('Kullanıcı adı : ', (140, 120), color = M_TEXT, screen=screen)
kullanici_adi_input = InputBox((300, 120), size = (180,30), color= M_BUTTON, screen=screen)

password_text = Text('Şifre : ', (175, 175), color = M_TEXT, screen=screen)
password_input = InputBox((300, 175), size = (180,30), color= M_BUTTON, screen=screen)

submit_button = Button(240, 240, color = M_BUTTON, size = (150, 40), screen=screen)
submit_button.set_Text('Giriş yap', 18, color = M_TEXT)

status_text = Text('', (240, 280), color = M_TEXT, size = 24, screen=screen)

while 1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print('Exiting.. ')
            exit()
            break

        if event.type == pygame.MOUSEBUTTONDOWN:

            kullanici_adi_input.listen_clicks()
            password_input.listen_clicks()

            if submit_button.isClicked():

                if kullanici_adi_input.text == USERNAME and password_input.text == PASSWORD:
                    
                    print('Giriş başarılı')
                    status_text.set_Text('Giriş Başarılı')

                else:

                    print('Giriş başarısız')
                    status_text.set_Text('Giriş Başarısız')

        if event.type == pygame.KEYDOWN:

            kullanici_adi_input.listen_text(event)
            password_input.listen_text(event)

    screen.fill(M_BACK)
    
    login_text.Show()

    kullanici_adi_text.Show()
    kullanici_adi_input.Show()

    password_text.Show()
    password_input.Show()

    submit_button.Show()

    status_text.Show()

    pygame.display.update()