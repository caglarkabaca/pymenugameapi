import pygame
pygame.init()

SIZE = (640, 640)

# RENKLER

SIYAH = (0, 0, 0)
BEYAZ = (255, 255, 255)
YESIL = (0, 255, 0)
KIRMIZI = (255, 0, 0)
MAVI = (0, 0, 255)

CURRENT_COLOR = BEYAZ
TITLE = "test pythonu"

screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption(TITLE)


from cacapi.modules import Button

b_Test = Button(320, 320, color = YESIL, size= (125, 125), screen=screen)

b_Test.set_Text('aaaaaaaaaaaaaaaaa', 24)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Exiting.. ')
            exit()
            break

        if event.type == pygame.MOUSEBUTTONDOWN:

            m_pos = pygame.mouse.get_pos()

            # print(f'Mouse pos ==> { m_pos } ')
            
            if b_Test.isClicked(m_pos):
                
                pass

    screen.fill(CURRENT_COLOR)

    b_Test.Show()
    
    pygame.display.update() # Ekranı yeniliyor