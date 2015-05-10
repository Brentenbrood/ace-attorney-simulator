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
        self.screen.blit(self.myfont.render("Wii Remote connected", 1, Color.GREEN), (screen.get_width()/2-130, 5))

    def updated(self):
    	pass

    def draw(self):
    	pass