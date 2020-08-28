"""
0.2 için login ekranı 
"""

import pygame
from pygame.locals import *
from cacapi.modules import Button, Text, InputBox, Editor_Mode

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

editor = Editor_Mode(pygame.locals.K_F1, screen=screen)

screen_objects = [login_text, kullanici_adi_text, kullanici_adi_input, password_text, password_input, 
submit_button, status_text]

while 1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print('Exiting.. ')
            exit()
            break
        
        if event.type == pygame.MOUSEBUTTONUP: editor.drop()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if kullanici_adi_input.listen_clicks(): editor.drag(kullanici_adi_input)
            if password_input.listen_clicks(): editor.drag(password_input)

            if kullanici_adi_text.isClicked(): editor.drag(kullanici_adi_text)
            if password_text.isClicked(): editor.drag(password_text)

            if status_text.isClicked(): editor.drag(status_text)
            if login_text.isClicked(): editor.drag(login_text)

            if submit_button.isClicked():
                
                editor.drag(submit_button)

                if kullanici_adi_input.text == USERNAME and password_input.text == PASSWORD:
                    
                    print('Giriş başarılı')
                    status_text.set_Text('Giriş Başarılı')

                else:

                    print('Giriş başarısız')
                    status_text.set_Text('Giriş Başarısız')

        if event.type == pygame.KEYDOWN:

            editor.check(event)
            kullanici_adi_input.listen_text(event)
            password_input.listen_text(event)

            if event.key == pygame.locals.K_F12:

                editor.save_Status(screen_objects)

    screen.fill(M_BACK)

    editor.Show()
    
    login_text.Show()

    kullanici_adi_text.Show()
    kullanici_adi_input.Show()

    password_text.Show()
    password_input.Show()

    submit_button.Show()

    status_text.Show()

    pygame.display.update()