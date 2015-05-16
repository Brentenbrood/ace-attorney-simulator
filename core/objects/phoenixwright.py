import pygame
from core.objects.anim_state import AnimState
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
        self.sounds["deskslam"] = pygame.mixer.Sound(os.path.join(dir, "../sound/sfx-deskslam2.wav"))

        self.sprites = {}
        self.sprites[AnimState.normal] = (os.path.join(dir, self.bsn + "-normal.gif"), False)
        self.sprites[AnimState.deskslam] = (os.path.join(dir, self.bsn + "-deskslam.gif"), True)
        self.sprites[AnimState.objection] = (os.path.join(dir, self.bsn + "-objection.gif"), True)
        self.sprites[AnimState.paperslap] = (os.path.join(dir, self.bsn + "-paperslap.gif"), False)

        self.gif = GIFImage(self.sprites[AnimState.normal][0])
        self.stop = False

    def changeState(self, n):
        f = self.sprites[n][0]
        self.stop = self.sprites[n][1]
        self.gif = GIFImage(f)

    def draw(self, screen):
		self.gif.render(screen, (self.x, self.y), stop=self.stop)
		






        
