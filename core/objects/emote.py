import pygame
from core.objects.anim_state import AnimState
from core.utils.GIFImage import GIFImage
import os

class Emote(object):
	def __init__(self, x, y, image):
		self.x = x
		self.y = y
		dir = os.path.dirname(__file__)
		self.gif = GIFImage(os.path.join(dir, image))
		self.running = False

		self.sounds = {}

	def addSound(self, name, path):
		dir = os.path.dirname(__file__)
		full_path = os.path.join(dir, path)
		self.sounds[name] = pygame.mixer.Sound(full_path)

	def playSound(self, name):
		if self.sounds[name]:
			self.sounds[name].play()

	def start(self):
		self.gif.seek(0)
		self.running = True
		
	def draw(self, screen):
		if self.running:
			self.gif.render(screen, (self.x, self.y), callback_object=self)

	def stop(self):
		self.running = False
		






		
