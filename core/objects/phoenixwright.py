import pygame
from anim_state import AnimState
from core.utils.GIFImage import GIFImage
import os

class Lawyer(object):
    def __init__(self, x, y, base_sprite_name):
        self.x = x
        self.y = y
        self.animation = AnimState.normal
        self.bsn = base_sprite_name

        dir = os.path.dirname(__file__)

        self.sounds = {}
        self.sounds["objection"] = pygame.mixer.Sound(os.path.join(dir, "../sound/sfx-objection.wav"))
        self.sounds["deskslam"] = pygame.mixer.Sound(os.path.join(dir, "../sound/sfx-deskslam.wav"))

        self.sprites = {}
        self.sprites["normal"] = os.path.join(dir, self.bsn + "-normal.gif")
        self.sprites["deskslam"] = os.path.join(dir, self.bsn + "-deskslam.gif")
        self.sprites["objection"] = os.path.join(dir, self.bsn + "-objection.gif")
        self.sprites["paperslap"] = os.path.join(dir, self.bsn + "-paperslap.gif")

        self.gif = GIFImage(self.sprites["normal"])
    def changeState(self, n):
    	self.animation = n
        f = self.sprites["normal"]
    	if self.animation == AnimState.deskslam:
            self.sounds["deskslam"].play()
            f = self.sprites["deskslam"]
        elif self.animation == AnimState.objection:
            self.sounds["objection"].play()
            f = self.sprites["objection"]
        elif self.animation == AnimState.paperslap:
            f = self.sprites["paperslap"]
        self.gif = GIFImage(f)
    def draw(self, screen, pos):
		self.gif.render(screen, pos)
		






        