import pygame
import cwiid
from ..utils.colors import Color

class GameState():
    def __init__(self, screen, wm):
        self.screen = screen
        self.wm = wm
        self.font = pygame.font.SysFont("monospace", 16)
        self.Xaxis = "X: " + str(self.wm.state['acc'][0])
        self.Yaxis = "Y: " + str(self.wm.state['acc'][1])
        self.Zaxis = "Z: " + str(self.wm.state['acc'][2])


    def update(self):
        self.Xaxis = "X: " + str(self.wm.state['acc'][0])
        self.Yaxis = "Y: " + str(self.wm.state['acc'][1])
        self.Zaxis = "Z: " + str(self.wm.state['acc'][2])

    def draw(self):
        wiimotetext = self.font.render(self.Xaxis + " " + self.Yaxis + " " + self.Zaxis, 1, Color.GREEN)
        self.screen.blit(wiimotetext, (300, 5))