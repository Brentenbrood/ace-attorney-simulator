import pygame
import cwiid
from ..utils.colors import Color

class GameState():
    def __init__(self, screen, wm):
        self.wm = wm
        font = pygame.font.SysFont("monospace", 16)
        Xaxis = "X: " + str(self.wm.state['acc'][0])
        Yaxis = "Y: " + str(self.wm.state['acc'][1])
        Zaxis = "Z: " + str(self.wm.state['acc'][2])

        wiimotetext = font.render(Xaxis + " " + Yaxis + " " + Zaxis, 1, Color.GREEN)
        screen.blit(wiimotetext, (300, 5))

    def update(self):
        pass

    def draw(self):
        pass