import pygame
from core.states.game_state import GameState
from core.states.state import State
from core.utils.colors import Color
import cwiid

class Menu(State):
    def __init__(self, screen, wm, game):
        super(Menu, self).__init__(wm, screen, game)

        self.font = pygame.font.SysFont("monospace", 16)

        self.wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
        self.wm.led = 1
        #Reset the screen
        self.screen.fill(Color.BLACK)

    def update(self):
        super(Menu, self).update()

    	while self.wm.state['buttons'] == 8:
            self.game.changeState(GameState(self.screen, self.wm, self.game))

    def draw(self):
        super(Menu, self).draw()
    	self.screen.blit(self.font.render("Press A to continue", 1, Color.GREEN), (300, 5))
        self.screen.blit(self.font.render("Press + at any time to quit", 1, Color.GREEN), (300, 30))






