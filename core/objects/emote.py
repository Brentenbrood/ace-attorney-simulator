import pygame
from core.objects.anim_state import AnimState
from core.utils.GIFImage import GIFImage
import os

class Emote(object):
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.cb = stop
        dir = os.path.dirname(__file__)
        self.gif = GIFImage(os.path.join(dir, image))
        self.running = False

    def start(self):
    	self.running = True

    def draw(self, screen):
    	if self.running:
			self.gif.render(screen, (self.x, self.y), callback_object=self)

	def stop(self):
		self.running = False
		






        
