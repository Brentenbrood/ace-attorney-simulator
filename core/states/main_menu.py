import pygame
import cwiid
from ..utils.colors import Color

class Menu():
    def __init__(self, screen):
    	self.screen = screen
        self.myfont = pygame.font.SysFont("monospace", 16)
        self.wiimotetext = self.myfont.render("Press 1 + 2 on the Wii Remote", 1, Color.GREEN)
        self.screen.blit(self.wiimotetext, (screen.get_width()/2-130, 5))

    def updated(self):
    	pass

    def draw(self):
    	pass