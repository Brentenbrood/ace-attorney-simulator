import pygame
import os

from core.objects.anim_state import AnimState
from core.utils.GIFImage import GIFImage
from core.objects.persons import HealthPerson

class Prosecutor(HealthPerson):
    def __init__(self, x, y, base_sprite_path):
        super(Prosecutor, self).__init__(x, y, base_sprite_path)

        self.addState(AnimState.normal, "-normal.gif", False)
        self.addState(AnimState.paperblock, "-paperblock.gif", False)
        self.addState(AnimState.pointblock, "-pointblock.gif", True)
        self.addState(AnimState.damage, "-damage.gif", True)
        self.addState(AnimState.angry, "-angry.gif", True)

        self.changeState(AnimState.normal)
