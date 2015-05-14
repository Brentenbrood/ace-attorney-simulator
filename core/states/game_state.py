import pygame
import cwiid
from core.utils.colors import Color
from core.states.state import State
from core.objects.phoenixwright import Lawyer

class GameState(State):
    def __init__(self, screen, wm, game):
        super(GameState, self).__init__(wm, screen, game)
        
        self.font = pygame.font.SysFont("monospace", 16)
        self.Xaxis = "X: " + str(self.wm.state['acc'][0])
        self.Yaxis = "Y: " + str(self.wm.state['acc'][1])
        self.Zaxis = "Z: " + str(self.wm.state['acc'][2])

        self.lawyer = Lawyer(0,0,"../img/phoenix")


    def update(self):
        super(GameState, self).update()
        self.Xaxis = "X: " + str(self.wm.state['acc'][0])
        self.Yaxis = "Y: " + str(self.wm.state['acc'][1])
        self.Zaxis = "Z: " + str(self.wm.state['acc'][2])
        if self.wm.state['acc'][2] <= 40:
            print "SLAM " + self.Xaxis + " " + self.Yaxis + " " + self.Zaxis
            self.lawyer.changeState(1)
        elif self.wm.state['acc'][1] <= 50:
            print "OBJECTION " + self.Xaxis + " " + self.Yaxis + " " + self.Zaxis
            self.lawyer.changeState(2)
        elif self.wm.state['acc'][0] <= 50 and self.wm.state['acc'][1] >= 120 and self.wm.state['acc'][2] <= 160:
            print "PAPERSLAP " + self.Xaxis + " " + self.Yaxis + " " + self.Zaxis
            self.lawyer.changeState(3)

    def draw(self):
        super(GameState, self).draw()
        wiimotetext = self.font.render(self.Xaxis + " " + self.Yaxis + " " + self.Zaxis, 1, Color.GREEN)
        self.screen.blit(wiimotetext, (300, 5))
        self.lawyer.draw(self.screen, (0,0))