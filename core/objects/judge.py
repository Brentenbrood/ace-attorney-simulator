import pygame
from core.objects.anim_state import AnimState
from core.utils.GIFImage import GIFImage
import os

class Judge(object):
    def __init__(self, x, y, base_sprite_name):
        self.x = x
        self.y = y
        self.animation = AnimState.normal
        self.bsn = base_sprite_name

        dir = os.path.dirname(__file__)
        self.sounds = {}
        self.sprites = {}
        self.sprites[AnimState.normal] = os.path.join(dir, self.bsn + "-normal.gif")
        self.sprites[AnimState.shocked] = os.path.join(dir, self.bsn + "-shocked.gif")
        self.changeState(AnimState.normal)

    def changeState(self, n):
        f = self.sprites[n]
        self.gif = GIFImage(f)

    def draw(self, screen):
		self.gif.render(screen, (self.x, self.y), stop=False)
		






        
