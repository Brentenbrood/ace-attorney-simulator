import pygame
from game_state import GameState
from ..utils.colors import Color
import cwiid

class Menu():
    def __init__(self, game, screen, wm):
        self.game = game
    	self.screen = screen
        self.font = pygame.font.SysFont("monospace", 16)

        self.wm = wm
        self.wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
        self.wm.led = 1
        #Reset the screen
        self.screen.fill(Color.BLACK)

    def update(self):

    	while self.wm.state['buttons'] == 8:
            self.game.changeState(GameState(self.screen, self.wm))

        if wm.state['buttons'] == 4096:
            print "Closing connection..."
            exit(wm)

    def draw(self):
    	self.screen.blit(self.font.render("Press A to continue", 1, Color.GREEN), (300, 5))
        self.screen.blit(self.font.render("Press + at any time to quit", 1, Color.GREEN), (300, 30))






