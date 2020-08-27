"""
modules.py

Asıl olay burada dönüyor
Burada bütün classlar depolanıyor

"""

import pygame, time
import cacapi.conf as conf


"""
Button

Buton işte tıklanabilir kare şeklinde veya daire şeklinde olabilir
içine yazı yazılabilir

"""
class Button:

    """
    __init__

    param:
        x => kordinat x i
        y => kordinat y si
        color => tuple > rgb renk
        size => tuple > boyutlar (genişlik, yükseklik)
        screen => ZORUNLU OLMAZSA ÇALIŞMAZ > pygame.display.set_mode ile geri dönen

    return:
        Button object
    """

    def __init__(self, x, y, color = (255, 255, 255), size = (100, 100), screen = None):

        self.coordinate = (x - (size[0]/2) , y - (size[1]/2) )
        self.center = (x, y)
        self.color = color
        self.size = size

        self.rect = pygame.Rect(self.coordinate[0], self.coordinate[1],
            self.size[0], self.size[1])

        self.text = None 

        self.type = 'rectangle'

        if screen is None:

            print('Screen is not defined !')

        else:

            self.screen = screen


    """
    set_Text

    param:
        txt => değişecek yazı
        t_size => yazının boyutu
        color => tuple > rgb renk
    """
    def set_Text(self, txt, t_size, color = (0, 0, 0)):

        font = pygame.font.Font('freesansbold.ttf', t_size)
        self.text = font.render(txt, True,  color)
        self.text_len , self.text_hei = font.size(txt)

    """
    set_Type

    param:
        typ => tip
    
    desc :
        rectangle => kare
        circle => daire
        bu ikisinden biri olmalı
    """
    def set_Type(self, typ):

        possible_var = ['rectangle', 'circle']

        if typ in possible_var:

            self.type = typ
        else:

            print(f' {typ} is not correct button type ! ')

    """
    Show

    desc: ekrana çizer döngünün içinde olmalı

    """
    def Show(self):

        if self.type == 'rectangle':
            pygame.draw.rect(self.screen, self.color, self.rect, border_radius = 2)
        elif self.type == 'circle':
            pygame.draw.circle(self.screen, self.color, self.center, radius = self.size[0]/2 )


        if self.text is not None:

            self.screen.blit(self.text, (self.center[0] - self.text_len/2, self.center[1] - self.text_hei/2))


        # pygame.draw.circle(self.screen, (180, 0, 0), self.center, radius = 5) # Test için lazımdı

    """
    isClicked

    desc: tıklanıp tıklanmadıgını söyler
    return : bool

    note:

        if event.type == pygame.MOUSEBUTTONDOWN: veya MOUSEBUTTONUP

        içinde olmalı yoksa hata verebilir

    """

    def isClicked(self):

        m_pos = pygame.mouse.get_pos()

        p_list = conf.get_plist(self)

        if m_pos in p_list:
            # print('Button clicked !!') # for debug
            return True

        return False

class Text:


    def __init__(self, text, pos = (0, 0),color = (0, 0, 0), size = 18, font = 'freesansbold.ttf', screen = None):
        
        self.size = size
        self.font = font 
        self.color = color

        font = pygame.font.Font(font, size)
        self.text = font.render(text, True, color)
        self.text_len, self.text_hei = font.size(text)

        self.center = pos

        self.screen = screen

    def set_Text(self, txt):

        font = pygame.font.Font(self.font, self.size)
        self.text = font.render(txt, True, self.color)
        self.text_len, self.text_hei = font.size(txt)


    def Show(self):

        self.screen.blit(self.text, (self.center[0] - self.text_len/2, self.center[1] - self.text_hei/2))

class InputBox:

    def __init__(self, pos = (0, 0), size = (50, 25), color = (255, 255, 255),
    color_text = (0, 0, 0), screen = None):

        self.screen = screen
        self.center = pos
        self.coordinates = (pos[0] - size[0]/2 , pos[1] - size[1]/2)
        self.color = color
        self.color_text = color_text 
        self.size = size

        self.text = ""
        self.text_body = Text(self.text, pos=self.center, screen=self.screen)

        self.type = "static"

        self.rect = pygame.Rect(self.coordinates[0], self.coordinates[1],
            self.size[0], self.size[1])

        self.is_Writable = False



    def Show(self):

        #Box
        if self.type == 'static':
            pygame.draw.rect(self.screen, self.color, self.rect, border_radius = 2)

        if self.type == 'dynamic':
            size_0 = self.text_body.text_len + 10
            coordinates_0 = self.center[0] - size_0/2
            pygame.draw.rect(self.screen, self.color, (coordinates_0, self.coordinates[1],
            size_0, self.size[1]), border_radius = 2)

        # dot animation

        if self.is_Writable:

            if time.time() % 1 > 0.5:
                cursor = pygame.Rect(self.center[0] + self.text_body.text_len/2, self.center[1] - self.text_body.text_hei/2, 1, self.text_body.text_hei)
                pygame.draw.rect(self.screen, (0, 0, 0), cursor)

        #text
        self.text_body.Show()
    
    def set_Text(self, txt):

        self.text = txt
        self.text_body = Text(self.text, pos=self.center, screen=self.screen)

    def set_Type(self, tip):

        possible_var = ('dynamic','static')
        if tip in possible_var:
            self.type = tip
        else:
            print('Wrong type for input !')

    def listen_text(self, event):

        if self.is_Writable:

            if event.key == pygame.locals.K_BACKSPACE:

                if len(self.text) > 0:
                    self.set_Text(self.text[:-1])

            self.set_Text(self.text + event.unicode)

    def listen_clicks(self):

        m_pos = pygame.mouse.get_pos()
        p_list = conf.get_plist(self)

        if m_pos in p_list:
            # print('Button clicked !!') # for debug
            self.is_Writable = True
        else:
            self.is_Writable = False


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


"""
Editör mod eklemeyi çok istiyorum fakat şuan tam olarak nasıl yapmam gerektiğini bilmiyorum
Biraz araştırıp ve mantığı oturtup yapıcam
Kodun da sade olmasını istiyorum ki ileride baktığımda ben naptım demiyim
"""
class Editor_Mode:

    pass


