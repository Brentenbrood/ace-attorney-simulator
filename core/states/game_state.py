import pygame
import cwiid
import os
from core.utils.colors import Color
from core.states.state import State
from core.objects.phoenixwright import Lawyer
from core.objects.milesedgeworth import Prosecutor
from core.objects.judge import Judge
from core.objects.emote import Emote

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
        self.images["bench-judge"] =     pygame.image.load(os.path.join(f, '../img/bench-judge.png'))

        self.lastTime = pygame.time.get_ticks()

        self.lawyer = Lawyer(0,192,"../img/phoenix")
        self.prosecutor = Prosecutor(512,192,"../img/edgeworth")
        self.judge = Judge(256,0,"../img/judge")

        self.holdit = Emote(256, 192, "../img/emote-holdit.gif")
        self.objection = Emote(256, 192, "../img/emote-objection.gif")
        self.takethat = Emote(256, 192, "../img/emote-takethat.gif")


    def update(self):
        super(GameState, self).update()
        self.Xaxis = "X: " + str(self.wm.state['acc'][0])
        self.Yaxis = "Y: " + str(self.wm.state['acc'][1])
        self.Zaxis = "Z: " + str(self.wm.state['acc'][2])

        if (pygame.time.get_ticks() - self.lastTime) > 100:
            if self.wm.state['acc'][2] <= 40:
                print "SLAM " + self.Xaxis + " " + self.Yaxis + " " + self.Zaxis
                self.lawyer.changeState(1)
                self.lastTime = pygame.time.get_ticks()
            elif self.wm.state['acc'][1] <= 50:
                print "OBJECTION " + self.Xaxis + " " + self.Yaxis + " " + self.Zaxis
                self.lawyer.changeState(2)
                self.lastTime = pygame.time.get_ticks()
                self.objection.start()
            elif self.wm.state['acc'][0] <= 30 and self.wm.state['acc'][1] >= 120 and self.wm.state['acc'][2] <= 110:
                print "PAPERSLAP " + self.Xaxis + " " + self.Yaxis + " " + self.Zaxis
                self.lawyer.changeState(3)
                self.lastTime = pygame.time.get_ticks()
        

    def draw(self):
        super(GameState, self).draw()
        wiimotetext = self.font.render(self.Xaxis + " " + self.Yaxis + " " + self.Zaxis, 1, Color.GREEN)

        #Emotes
        self.holdit.draw(self.screen)
        self.takethat.draw(self.screen)
        self.objection.draw(self.screen)
        self.screen.blit(wiimotetext, (280,384))


        #Lawyer
        self.screen.blit(self.images["empty-left"], (0,192))
        self.lawyer.draw(self.screen)
        self.screen.blit(self.images["desk-left"], (0,192))

        #Prosecutor
        self.screen.blit(self.images["empty-right"], (512,192))
        self.prosecutor.draw(self.screen)
        self.screen.blit(self.images["desk-right"], (512,192))

        #Judge
        self.screen.blit(self.images["bench-judge"], (256,0))
        self.judge.draw(self.screen)
