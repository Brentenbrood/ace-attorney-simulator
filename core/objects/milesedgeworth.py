import pygame
from core.objects.anim_state import AnimState
from core.utils.GIFImage import GIFImage
import os

class Prosecutor(object):
    def __init__(self, x, y, base_sprite_name):
        self.x = x
        self.y = y
        self.animation = AnimState.normal
        self.bsn = base_sprite_name

        dir = os.path.dirname(__file__)

        self.sprites = {}
        self.sprites["normal"] = os.path.join(dir, self.bsn + "-normal.gif")
        self.sprites["paperblock"] = os.path.join(dir, self.bsn + "-paperblock.gif")
        self.sprites["pointblock"] = os.path.join(dir, self.bsn + "-pointblock.gif")
        self.sprites["damage"] = os.path.join(dir, self.bsn + "-damage.gif")
        self.sprites["angry"] = os.path.join(dir, self.bsn + "-angry.gif")

        self.gif = GIFImage(self.sprites["normal"])
    def changeState(self, n):
    	self.animation = n
        f = self.sprites["normal"]
    	if self.animation == AnimState.damage:
            self.sounds["damage"].play()
            f = self.sprites["damage"]
        elif self.animation == AnimState.paperblock:
            self.sounds["paperblock"].play()
            f = self.sprites["paperblock"]
        elif self.animation == AnimState.pointblock:
            f = self.sprites["pointblock"]
        elif self.animation == AnimState.angry:
            f = self.sprites["angry"]
        self.gif = GIFImage(f)
    def draw(self, screen):
		self.gif.render(screen, (self.x,self.y), stop=True)