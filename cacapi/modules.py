"""
Butonlar falan buradan çağrılacak
"""

import pygame
import cacapi.conf as conf

class Button:

    """
    Button
        kare veya daire şeklinde düğmeler
        bastığında anlar
    """

    def __init__(self, x, y, color = (255, 255, 255), size = (100, 100), screen = None):

        self.coordinate = (x - (size[0]/2) , y - (size[1]/2) )
        self.center = (x, y)
        self.color = color
        self.size = size

        self.text = None 

        self.type = 'rectangle'

        if screen is None:

            print('Screen is not defined !')

        else:

            self.screen = screen

    def set_Text(self, txt, t_size, color = (0, 0, 0)):

        font = pygame.font.Font('freesansbold.ttf', t_size)
        self.text = font.render(txt, True,  color)
        self.text_len , self.text_hei = font.size(txt)

    def set_Type(self, typ):

        possible_var = ['rectangle', 'circle']

        if typ in possible_var:

            self.type = typ
        else:

            print(f' {typ} is not correct button type ! ')


    def Show(self):

        if self.type == 'rectangle':
            pygame.draw.rect(self.screen, self.color, (self.coordinate[0], self.coordinate[1],
            self.size[0], self.size[1]), border_radius = 2)
        elif self.type == 'circle':
            pygame.draw.circle(self.screen, self.color, self.center, radius = self.size[0]/2 )


        if self.text is not None:

            self.screen.blit(self.text, (self.center[0] - self.text_len/2, self.center[1] - self.text_hei/2))


        # pygame.draw.circle(self.screen, (180, 0, 0), self.center, radius = 5) # Test için lazımdı

    def isClicked(self):

        m_pos = pygame.mouse.get_pos()

        p_list = conf.get_plist(self)

        if m_pos in p_list:
            # print('Button clicked !!') # for debug
            return True

        return False

class Text:

    """
    Text
        yazı yazdırmanı sağlıyor

    """

    def __init__(self, text, pos = (0, 0),color = (0, 0, 0), size = 18, font = 'freesansbold.ttf', screen = None):
        
        font = pygame.font.Font(font, size)
        self.text = font.render(text, True, color)
        self.text_len, self.text_hei = font.size(text)

        self.center = pos

        self.screen = screen

    def Show(self):

        self.screen.blit(self.text, (self.center[0] - self.text_len/2, self.center[1] - self.text_hei/2))


class Color_Pallette:

    """
    you can use color pallette like this

    p_one = Color_Pallette({'cool color': (0, 0, 0), 'more cool color' : (255, 255, 255) })

    p_one.get_Color('cool color')

    """

    def __init__(self, colors):

        self.colors = colors

    def get_Color(self, color):

        return self.colors[color]