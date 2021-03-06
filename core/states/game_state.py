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
from core.objects.anim_state import AnimState

class GameState(State):

	def __init__(self, screen, wm, game):
		super(GameState, self).__init__(wm, screen, game)
		
		pygame.mixer.init()

		pygame.mixer.music.load(self.get_path_to_file( "../sound/music.wav") if random.randint(0,100)>50 else
		 self.get_path_to_file("../sound/music2.wav"))
		#pygame.mixer.music.play()

		self.font =     pygame.font.SysFont("monospace", 16)
		self.Xaxis =    self.wm.state['acc'][0]
		self.Yaxis =    self.wm.state['acc'][1]
		self.Zaxis =    self.wm.state['acc'][2]
		self.rumble = 	False

		self.addImage("empty-left",     "../img/empty-left.png")
		self.addImage("empty-right",    "../img/empty-right.png")
		self.addImage("desk-left",      "../img/bench-left.png")
		self.addImage("desk-right",     "../img/bench-right.png")
		self.addImage("bench-judge",    "../img/bench-judge.png")
		self.addImage("bg-courtroom",   "../img/bg-courtroom.jpg")
		self.addImage("healthbar",      "../img/healthbar.png")

		#Scale an image by setting it to the dict directly
		self.images["bg-courtroom"] =  pygame.transform.scale(self.image("bg-courtroom"), (768,432))

		self.lastTime			=	pygame.time.get_ticks()
		self.lastTick			=	pygame.time.get_ticks()
		self.opponentPoseTick 	= 	pygame.time.get_ticks()
		self.rumbleTick			=	pygame.time.get_ticks()

		self.flashTick			=	pygame.time.get_ticks()
		self.flashing			=	False

		self.lawyer =       Lawyer(0,192,       "../img/phoenix")
		self.prosecutor =   Prosecutor(512,192, "../img/edgeworth")
		self.judge =        Judge(256,0,        "../img/judge")

		self.holdit =       Emote(256, 192, "../img/emote-holdit.gif")
		self.objection =    Emote(256, 192, "../img/emote-objection.gif")
		self.takethat =     Emote(256, 192, "../img/emote-takethat.gif")

		self.streak = 0
		self.truestreak = 0
		self.rbreakstreak = random.randint(2,6)
		self.stunned = False
		self.stunnedTick = pygame.time.get_ticks()


	def update(self):
		super(GameState, self).update()

		nowTick = pygame.time.get_ticks()
		# Gives rumble time to rumble
		if self.rumble == True and ((nowTick - self.rumbleTick) > 400):
			self.rumbleTick = pygame.time.get_ticks()
			self.wm.rumble = False

		self.Xaxis = self.wm.state['acc'][0]
		self.Yaxis = self.wm.state['acc'][1]
		self.Zaxis = self.wm.state['acc'][2]

		# Amount of time flash
		if self.flashing:
			if (nowTick - self.flashTick) > 20:
				self.flashing = False

		if self.stunned:
			self.lawyer.changeState(AnimState.ohshit)
			if (nowTick - self.stunned) > 1000:
				print "You can attack again!"
				self.stunned = False

		if (pygame.time.get_ticks() - self.lastTime) > 100 and self.stunned != True:
			if self.Zaxis <= 40:
				#print "SLAM " + self.Xaxis + " " + self.Yaxis + " " + self.Zaxis
				self.lawyer.changeState(1)
				self.lawyer.playSound('deskslam')
				self.lastTime = pygame.time.get_ticks()
				if self.prosecutor.animation == AnimState.paperblock:
					self.flash(nowTick)
					self.prosecutor.changeState(AnimState.damage)

			elif self.Yaxis <= 50:
				#print "OBJECTION " + str(self.Xaxis) + " " + str(self.Yaxis + " " + self.Zaxis
				self.lawyer.changeState(2)
				self.lastTime = pygame.time.get_ticks()

				# Only hits when prosecutor doesn't block
				if self.prosecutor.animation != AnimState.paperblock:
					r = random.randint(0, 100)
					# On succesful hit damages the prosecutor
					self.prosecutor.hp -= 200*((nowTick - self.lastTick)/1000.0)
					self.streak += 1
					self.truestreak += 1
					if r < 50:
						self.objection.start()
						self.lawyer.playSound('objection')
						self.holdit.stop()
					else:
						self.objection.stop()
						self.holdit.start()
						self.lawyer.playSound('holdit')
				else:
					# Shit happens when you use objection!/hold it! when prosecutor blocks
					self.lawyer.hp -= 400*((nowTick - self.lastTick)/1000.0)
					self.truestreak = 0
					self.lawyer.changeState(AnimState.ohshit)
					self.rumble = True
					self.wm.rumble = True

			elif self.Xaxis <= 30 and self.Yaxis >= 120 and self.Zaxis <= 110:
				#print "PAPERSLAP " + self.Xaxis + " " + self.Yaxis + " " + self.Zaxis
				self.lawyer.changeState(3)
				self.lastTime = pygame.time.get_ticks()
		
		# Prosecutor random AI v0.1
		if ((nowTick - self.opponentPoseTick) > 2000):
			self.opponentPoseTick = pygame.time.get_ticks()
			r = random.randint(0,90)
			if r < 30:
				self.prosecutor.changeState(AnimState.paperblock)
			elif r >= 30 and r < 60:
				self.prosecutor.changeState(AnimState.pointblock)
			else:
				self.prosecutor.changeState(AnimState.handslam)
				self.lawyer.hp -= 200*((nowTick - self.lastTick)/1000.0)
				self.stun(nowTick)

		# Prosecutor blocks you on succesful streak
		elif self.streak > self.rbreakstreak:
			self.rbreakstreak = self.streak + random.randint(2,6)
			self.prosecutor.changeState(AnimState.paperblock)


		self.lastTick = pygame.time.get_ticks()


	def flash(self, nowTick):
		# Start the flash
		self.flashTick = pygame.time.get_ticks()
		self.flashing = True

	def stun(self, nowTick):
		# Start the stun
		self.stunnedTick = pygame.time.get_ticks()
		self.stunned = True

	def draw(self):
		super(GameState, self).draw()

		self.screen.blit(self.image("bg-courtroom"), (0,0))

		wiimotetext = self.font.render("X: " + str(self.Xaxis) + " " + "Y: " + 
			str(self.Yaxis) + " " + "Z: " + str(self.Zaxis), 10, Color.GREEN)

		# Flash is last: needs to overwrite previous drawings
		if self.flashing:
			s = pygame.Surface((768,384))  # the size of your rect
			s.set_alpha(128)                # alpha level
			s.fill((255,255,255))           # this fills the entire surface
			self.screen.blit(s, (0,0))    # (0,0) are the top-left coordinates
		
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
			self.screen.blit(temp_img, (768-temp_img.get_width() + (((100 - self.prosecutor.hp)/100) * temp_img.get_width()), 80), (((100 - self.prosecutor.hp)/100) * temp_img.get_width(), 0, temp_img.get_width(), temp_img.get_height()))

		#Streak
		streakstr = self.font.render("Streak: " + str(self.truestreak), 10, Color.GREEN)
		self.screen.blit(streakstr, (10,60))