"""
Butonlar falan buradan çağrılacak
"""

import pygame
import cacapi.conf as conf

class Button:

    def __init__(self, x, y, color = (255, 255, 255), size = (100, 100), screen = None):

        self.coordinate = (x - (size[0]/2) , y - (size[1]/2) )
        self.center = (x, y)
        self.color = color
        self.size = size

        self.text = None # FOR NOW

        if screen is None:

            print('Screen is not defined !')

        else:

            self.screen = screen

    def set_Text(self, txt, t_size, color = (0, 0, 0)):

        font = pygame.font.Font('freesansbold.ttf', t_size)
        self.text = font.render(txt, True,  color)
        self.text_len , self.text_hei = font.size(txt)


    def Show(self):

        pygame.draw.rect(self.screen, self.color, (self.coordinate[0], self.coordinate[1],
        self.size[0], self.size[1]))

        if self.text is not None:

            self.screen.blit(self.text, (self.center[0] - self.text_len/2, self.center[1] - self.text_hei/2))


        # pygame.draw.circle(self.screen, (180, 0, 0), self.center, radius = 5) # Test için lazımdı

    def isClicked(self, m_pos):

        p_list = conf.get_plist(self)

        if m_pos in p_list:
            # print('Button clicked !!') # for debug
            return True

        return False
        
