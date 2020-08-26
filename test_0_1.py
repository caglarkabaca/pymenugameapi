import pygame
from cacapi.modules import Color_Pallette, Button, Text

pygame.init()

screen = pygame.display.set_mode((720, 720))

pygame.display.set_caption('0.1 böyle abim')

palet = Color_Pallette(
    {
    'acik' : (255, 87, 51),
    'orta' : (199, 0, 57),
    'koyu' : (144, 12, 63)
    }
)

b_rect = Button(200,100, color = palet.get_Color('orta'), size = (200, 50), screen = screen)
b_rect.set_Text('Kare düğme',18, (255, 255, 255))

b_circ = Button(400,100, color = palet.get_Color('orta'), size = (150, 50), screen = screen)
b_circ.set_Text('Daire düğme',18, (255, 255, 255))
b_circ.set_Type('circle')

t_text = Text('cacapi 0.1', (200, 400), color = palet.get_Color('acik'), size = 32, screen = screen)



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Exiting.. ')
            exit()
            break

        if event.type == pygame.MOUSEBUTTONDOWN:

            import random

            if b_rect.isClicked(): b_rect.set_Type(random.choice(('rectangle','circle')))

            if b_circ.isClicked(): b_circ.set_Type(random.choice(('rectangle','circle')))


    
    screen.fill(palet.get_Color('koyu'))

    b_rect.Show()
    b_circ.Show()
    t_text.Show()
    
    pygame.display.update()