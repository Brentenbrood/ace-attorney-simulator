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
        
        self.font =     pygame.font.SysFont("monospace", 16)
        self.Xaxis =    self.wm.state['acc'][0]
        self.Yaxis =    self.wm.state['acc'][1]
        self.Zaxis =    self.wm.state['acc'][2]

        self.images["empty-left"] =     pygame.image.load(self.get_path_to_file('../img/empty-left.png'))        
        self.images["empty-right"] =    pygame.image.load(self.get_path_to_file('../img/empty-right.png'))
        self.images["desk-left"] =      pygame.image.load(self.get_path_to_file('../img/bench-left.png'))
        self.images["desk-right"] =     pygame.image.load(self.get_path_to_file('../img/bench-right.png'))
        self.images["bench-judge"] =    pygame.image.load(self.get_path_to_file('../img/bench-judge.png'))
        self.images["bg-courtroom"] =   pygame.image.load(self.get_path_to_file('../img/bg-courtroom.jpg'))

        self.lastTime =     pygame.time.get_ticks()

        self.lawyer =       Lawyer(0,192,"../img/phoenix")
        self.prosecutor =   Prosecutor(512,192,"../img/edgeworth")
        self.judge =        Judge(256,0,"../img/judge")

        self.holdit =       Emote(256, 192, "../img/emote-holdit.gif")
        self.objection =    Emote(256, 192, "../img/emote-objection.gif")
        self.takethat =     Emote(256, 192, "../img/emote-takethat.gif")


    def update(self):
        super(GameState, self).update()
        self.Xaxis = self.wm.state['acc'][0]
        self.Yaxis = self.wm.state['acc'][1]
        self.Zaxis = self.wm.state['acc'][2]

        if (pygame.time.get_ticks() - self.lastTime) > 100:
            if self.Zaxis <= 40:
                #print "SLAM " + self.Xaxis + " " + self.Yaxis + " " + self.Zaxis
                self.lawyer.changeState(1)
                self.lastTime = pygame.time.get_ticks()
            elif self.Yaxis <= 50:
                #print "OBJECTION " + str(self.Xaxis) + " " + str(self.Yaxis + " " + self.Zaxis
                self.lawyer.changeState(2)
                self.lastTime = pygame.time.get_ticks()
                self.objection.start()
            elif self.Xaxis <= 30 and self.Yaxis >= 120 and self.Zaxis <= 110:
                #print "PAPERSLAP " + self.Xaxis + " " + self.Yaxis + " " + self.Zaxis
                self.lawyer.changeState(3)
                self.lastTime = pygame.time.get_ticks()
        

    def draw(self):
        super(GameState, self).draw()

        self.screen.blit(self.images["bg-courtroom"], (0,0))
        # self.screen.transform.scale(["bg-courtroom"], (768,432))

        wiimotetext = self.font.render("X: " + str(self.Xaxis) + " " + "Y: " + 
            str(self.Yaxis) + " " + "Z: " + str(self.Zaxis), 1, Color.GREEN)
        
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
