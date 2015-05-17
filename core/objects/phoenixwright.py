import pygame
import os

from core.objects.anim_state import AnimState
from core.utils.GIFImage import GIFImage
from core.objects.person import Person

class Lawyer(Person):
	def __init__(self, x, y, base_sprite_path):
		super(Lawyer, self).__init__(x, y, base_sprite_path)

		self.addSound("objection", "../sound/sfx-objection.wav")
		self.addSound("deskslam", "../sound/sfx-deskslam2.wav")

		self.addState(AnimState.normal, "-normal.gif", False)
		self.addState(AnimState.deskslam, "-deskslam.gif", True)
		self.addState(AnimState.objection, "-objection.gif", True)
		self.addState(AnimState.paperslap, "-paperslap.gif", False)

		self.changeState(AnimState.normal)





		
