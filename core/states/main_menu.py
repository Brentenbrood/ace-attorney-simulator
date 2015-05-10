import pygame
import cwiid
from ..utils.colors import Color

class Menu():
    def __init__(self, screen, wm):
    	self.screen = screen
        self.myfont = pygame.font.SysFont("monospace", 16)

        self.wm = wm
        self.wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
        self.wm.led = 1


        #Reset the screen
        pygame.draw.rect(self.screen, (0,0,0), (0,0,self.screen.get_width(), self.screen.get_height()))

    def update(self):
    	pass

    def draw(self):
    	pass






