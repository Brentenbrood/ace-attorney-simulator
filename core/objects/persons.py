import os
import pygame

from core.objects.anim_state import AnimState
from core.utils.GIFImage import GIFImage


class Person(object):
	"""A base class for classes representing people"""
	def __init__(self, x, y, bsp):
		self.x = x
		self.y = y
		self.bsp = bsp
		self.sprites = {}
		self.sounds = {}

		self.animation = None

		self.stop = True
		self.gif = None


	def addState(self, n, name, stop):
		dir = os.path.dirname(__file__)
		full_path = os.path.join(dir, self.bsp + name)
		self.sprites[n] = (full_path, stop)

	def addSound(self, name, path):
		dir = os.path.dirname(__file__)
		full_path = os.path.join(dir, path)
		self.sounds[name] = pygame.mixer.Sound(full_path)

	def playSound(self, name):
		if self.sounds[name]:
			self.sounds[name].play()

	def changeState(self, n):
		self.animation = n
		animation = self.sprites[n]
		if animation:
			self.gif = GIFImage(animation[0])
			self.stop = animation[1]

	def draw(self, screen):
		if self.gif:
			self.gif.render(screen, (self.x,self.y), stop=self.stop)


class HealthPerson(Person):
	
	def __init__(self, x, y, bsp, max_hp=100.0):
		super(HealthPerson, self).__init__(x, y, bsp)
		self.hp = max_hp