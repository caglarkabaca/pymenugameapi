import pygame
pygame.init()

SIZE = (640, 640)

# RENKLER

SIYAH = (0, 0, 0)
BEYAZ = (255, 255, 255)

screen = pygame.display.set_mode(SIZE)


from cacapi.modules import Button



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Exiting.. ')
            exit()
            break

    screen.fill(SIYAH)
    
    pygame.display.flip() # Ekranı yeniliyor