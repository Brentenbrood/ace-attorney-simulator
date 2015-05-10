import pygame
import cwiid
import sys
import time

class Menu():
    def __init__(self):
        self.GREEN = (255, 255, 0)
        self.myfont = pygame.font.SysFont("monospace", 16)

        self.wiimotetext = self.myfont.render("Press 1 + 2 on the Wii Remote", 1, GREEN)
        self.screen.blit(self.wiimotetext, (300, 5))
    def updated(self):

    def draw(self):
