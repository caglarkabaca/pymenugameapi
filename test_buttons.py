import pygame
pygame.init()

SIZE = (640, 640)

# RENKLER

SIYAH = (0, 0, 0)
BEYAZ = (255, 255, 255)
YESIL = (0, 255, 0)

CURRENT_COLOR = SIYAH

screen = pygame.display.set_mode(SIZE)


from cacapi.modules import Button

b_siyah= Button(160, 480, color = YESIL, size= (125, 50), screen=screen)
b_beyaz = Button(480, 480, color = YESIL, size = (125, 50), screen= screen)

b_siyah.set_Text('Turn Black', 22, BEYAZ)
b_beyaz.set_Text('Turn White', 22, BEYAZ)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Exiting.. ')
            exit()
            break

        if event.type == pygame.MOUSEBUTTONDOWN:

            m_pos = pygame.mouse.get_pos()
            
            if b_siyah.isClicked(m_pos): CURRENT_COLOR = SIYAH

            if b_beyaz.isClicked(m_pos): CURRENT_COLOR = BEYAZ

    screen.fill(CURRENT_COLOR)

    b_siyah.Show()
    b_beyaz.Show()
    
    pygame.display.update() # Ekranı yeniliyor