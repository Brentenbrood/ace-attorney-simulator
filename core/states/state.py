import os
import pygame

class State(object):
	def __init__(self, wm, screen, game):
		self.wm = wm;
		self.screen = screen
		self.game = game
		self.images = {}

	def update(self):
		if self.wm.state['buttons'] == 4096:
			print "Closing connection..."
			exit(self.wm)

	"""Can be accessed by State.image(name) and State.images[name]"""
	def addImage(self, name, path):
		self.images[name] = pygame.image.load(self.get_path_to_file(path))

	def image(self, name):
		return self.images[name]

	def draw(self):
		pass

	def get_path_to_file(self, f):
		dir = os.path.dirname(__file__)
		return os.path.join(dir, f)