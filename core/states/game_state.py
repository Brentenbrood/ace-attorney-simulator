import pygame
import cwiid
import os
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

        f = os.path.dirname(__file__)

        self.images["empty-left"] =     pygame.image.load(os.path.join(f, '../img/empty-left.png'))        
        self.images["empty-right"] =    pygame.image.load(os.path.join(f, '../img/empty-right.png'))
        self.images["desk-left"] =      pygame.image.load(os.path.join(f, '../img/bench-left.png'))
        self.images["desk-right"] =     pygame.image.load(os.path.join(f, '../img/bench-right.png'))

        self.lastTime = pygame.time.get_ticks()

        self.lawyer = Lawyer(0,0,"../img/phoenix")


    def update(self):
        super(GameState, self).update()
        self.Xaxis = "X: " + str(self.wm.state['acc'][0])
        self.Yaxis = "Y: " + str(self.wm.state['acc'][1])
        self.Zaxis = "Z: " + str(self.wm.state['acc'][2])

        if (pygame.time.get_ticks() - self.lastTime) > 1000:
            if self.wm.state['acc'][2] <= 40:
                print "SLAM " + self.Xaxis + " " + self.Yaxis + " " + self.Zaxis
                self.lawyer.changeState(1)
                self.lastTime = pygame.time.get_ticks()
            elif self.wm.state['acc'][1] <= 50:
                print "OBJECTION " + self.Xaxis + " " + self.Yaxis + " " + self.Zaxis
                self.lawyer.changeState(2)
                self.lastTime = pygame.time.get_ticks()
            elif self.wm.state['acc'][0] <= 30 and self.wm.state['acc'][1] >= 120 and self.wm.state['acc'][2] <= 110:
                print "PAPERSLAP " + self.Xaxis + " " + self.Yaxis + " " + self.Zaxis
                self.lawyer.changeState(3)
                self.lastTime = pygame.time.get_ticks()
        

    def draw(self):
        super(GameState, self).draw()
        wiimotetext = self.font.render(self.Xaxis + " " + self.Yaxis + " " + self.Zaxis, 1, Color.GREEN)

        self.screen.blit(self.images["empty-left"], (0,0))
        self.lawyer.draw(self.screen, (0,0))
        self.screen.blit(self.images["desk-left"], (0, 0))
        self.screen.blit(wiimotetext, (300, 5))