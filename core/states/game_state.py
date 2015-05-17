import pygame
import cwiid
import os
import random
import math

from core.utils.colors import Color
from core.states.state import State
from core.objects.phoenixwright import Lawyer
from core.objects.milesedgeworth import Prosecutor
from core.objects.judge import Judge
from core.objects.emote import Emote

class GameState(State):
    def __init__(self, screen, wm, game):
        super(GameState, self).__init__(wm, screen, game)
        
        pygame.mixer.init()

        self.font =     pygame.font.SysFont("monospace", 16)
        self.Xaxis =    self.wm.state['acc'][0]
        self.Yaxis =    self.wm.state['acc'][1]
        self.Zaxis =    self.wm.state['acc'][2]

        self.addImage("empty-left",     "../img/empty-left.png")
        self.addImage("empty-right",    "../img/empty-right.png")
        self.addImage("desk-left",      "../img/bench-left.png")
        self.addImage("desk-right",     "../img/bench-right.png")
        self.addImage("bench-judge",    "../img/bench-judge.png")
        self.addImage("bg-courtroom",   "../img/bg-courtroom.jpg")
        self.addImage("healthbar",      "../img/healthbar.png")

        #Scale some images
        self.image("bg-courtroom") =   pygame.transform.scale(self.image("bg-courtroom"), (768,432))

        self.lastTime =     pygame.time.get_ticks()
        self.lastTick =     pygame.time.get_ticks()

        self.lawyer =       Lawyer(0,192,       "../img/phoenix")
        self.prosecutor =   Prosecutor(512,192, "../img/edgeworth")
        self.judge =        Judge(256,0,        "../img/judge")

        self.holdit =       Emote(256, 192, "../img/emote-holdit.gif")
        self.objection =    Emote(256, 192, "../img/emote-objection.gif")
        self.takethat =     Emote(256, 192, "../img/emote-takethat.gif")


    def update(self):
        super(GameState, self).update()

        nowTick = pygame.time.get_ticks()

        self.lawyer.hp -= 0.1

        self.Xaxis = self.wm.state['acc'][0]
        self.Yaxis = self.wm.state['acc'][1]
        self.Zaxis = self.wm.state['acc'][2]

        if (pygame.time.get_ticks() - self.lastTime) > 100:
            if self.Zaxis <= 40:
                #print "SLAM " + self.Xaxis + " " + self.Yaxis + " " + self.Zaxis
                self.lawyer.changeState(1)
                self.lawyer.playSound('deskslam')
                self.lastTime = pygame.time.get_ticks()
            elif self.Yaxis <= 50:
                #print "OBJECTION " + str(self.Xaxis) + " " + str(self.Yaxis + " " + self.Zaxis
                self.lawyer.changeState(2)
                self.lastTime = pygame.time.get_ticks()

                r = random.randint(0, 100)

                if r < 50:
                    self.objection.start()
                    self.lawyer.playSound('objection')
                    self.holdit.stop()
                else:
                    self.objection.stop()
                    self.holdit.start()
                    self.lawyer.playSound('holdit')
            elif self.Xaxis <= 30 and self.Yaxis >= 120 and self.Zaxis <= 110:
                #print "PAPERSLAP " + self.Xaxis + " " + self.Yaxis + " " + self.Zaxis
                self.lawyer.changeState(3)
                self.lastTime = pygame.time.get_ticks()

        self.lastTick = pygame.time.get_ticks()


        

    def draw(self):
        super(GameState, self).draw()

        self.screen.blit(self.image("bg-courtroom"), (0,0))

        wiimotetext = self.font.render("X: " + str(self.Xaxis) + " " + "Y: " + 
            str(self.Yaxis) + " " + "Z: " + str(self.Zaxis), 1, Color.GREEN)
        
        #Emotes
        self.holdit.draw(self.screen)
        self.takethat.draw(self.screen)
        self.objection.draw(self.screen)
        self.screen.blit(wiimotetext, (280,384))

        #Lawyer
        self.screen.blit(self.image("empty-left"), (0,192))
        self.lawyer.draw(self.screen)
        self.screen.blit(self.image("desk-left"), (0,192))

        #Prosecutor
        self.screen.blit(self.image("empty-right"), (512,192))
        self.prosecutor.draw(self.screen)
        self.screen.blit(self.image("desk-right"), (512,192))

        #Judge
        self.screen.blit(self.image("bench-judge"), (256,0))
        self.judge.draw(self.screen)

        #Healthbar Lawyer
        temp_img  = self.image("healthbar")
        if self.lawyer.hp > 0:
            self.screen.blit(temp_img, (0, 81), (0, 0, self.lawyer.hp/100*temp_img.get_width(), temp_img.get_height()))

        #Prosecutor healthbar
        if self.prosecutor.hp > 0:
            self.screen.blit(temp_img, (768-temp_img.get_width(), 80), (0, 0, self.prosecutor.hp/100*temp_img.get_width(), temp_img.get_height()))

