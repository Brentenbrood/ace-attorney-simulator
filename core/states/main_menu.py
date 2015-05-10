import pygame
import cwiid
from ..utils.colors import Color

class Menu():
    def __init__(self, game, screen, wm):
    	self.screen = screen
        self.font = pygame.font.SysFont("monospace", 16)

        self.wm = wm
        self.wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
        self.wm.led = 1


        #Reset the screen
        pygame.draw.rect(self.screen, (0,0,0), (0,0,self.screen.get_width(), self.screen.get_height()))
        self.wiimotetext = self.font.render("Press A to continue", 1, Color.GREEN)
        self.screen.blit(self.wiimotetext, (300, 5))

    def update(self):
    	while wm.state['buttons'] == 8:
            self.state = game_state.GameState(self.screen, cwiid.Wiimote())

    def draw(self):
    	pass






