import pygame
import os

from core.objects.anim_state import AnimState
from core.utils.GIFImage import GIFImage
from core.objects.person import Person

class Judge(Person):
    def __init__(self, x, y, base_sprite_path):
        super(Judge, self).__init__(x, y, base_sprite_path)
      
        self.addState(AnimState.normal, "-normal.gif", False)
        self.addState(AnimState.shocked, "-shocked.gif", False)
        self.changeState(AnimState.normal)






        
