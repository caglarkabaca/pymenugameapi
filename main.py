import pygame
pygame.init()

SIZE = (640, 640)

# RENKLER

SIYAH = (0, 0, 0)
BEYAZ = (255, 255, 255)
YESIL = (0, 255, 0)

screen = pygame.display.set_mode(SIZE)


from cacapi.modules import Button

b_Test = Button(320, 320, color = YESIL, size= (125, 125), screen=screen)

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
                
                #do something 
                
                pass

    screen.fill(SIYAH)

    b_Test.Show()
    
    pygame.display.flip() # Ekranı yeniliyor