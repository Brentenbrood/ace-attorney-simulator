import pygame
import os

from core.objects.anim_state import AnimState
from core.utils.GIFImage import GIFImage
from core.objects.persons import HealthPerson

class Lawyer(HealthPerson):
    def __init__(self, x, y, base_sprite_path):
        super(Lawyer, self).__init__(x, y, base_sprite_path)

		self.addSound("objection", "../sound/sfx-objection.wav")
		self.addSound("deskslam", "../sound/sfx-deskslam.wav")
		self.addSound("holdit", "../sound/sfx-holdit.wav")

		self.addState(AnimState.normal, "-normal.gif", False)
		self.addState(AnimState.deskslam, "-deskslam.gif", True)
		self.addState(AnimState.objection, "-objection.gif", True)
		self.addState(AnimState.paperslap, "-paperslap.gif", False)

		self.changeState(AnimState.normal)
		