"""
Butonlar falan buradan çağrılacak
"""

import pygame

class Button:

    def __init__(self, x, y, color = (255, 255, 255), size = (100, 100), screen = None):

        self.coordinate = (x - (size[0]/2) , y - (size[1]/2) )
        self.center = (x, y)
        self.color = color
        self.size = size

        if screen is None:

            print('Screen is not defined !')

        else:

            self.screen = screen


    def Show(self):

        pygame.draw.rect(self.screen, self.color, (self.coordinate[0], self.coordinate[1],
        self.size[0], self.size[1]))

        # pygame.draw.circle(self.screen, (180, 0, 0), self.center, radius = 5) # Test için lazımdı

