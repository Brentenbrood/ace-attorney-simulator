import pygame
import cwiid
from core.utils.colors import Color
from core.states import main_menu
import core.utils.wiinit as wiinit

class Game():
    def __init__(self):
        pygame.init()
        self.size = (768, 384)
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Ace Attorney Simulator")
        self.wm = wiinit.get_connection_with_drawing(self.screen)
        self.state = main_menu.Menu(self.screen, self.wm, self)
        self.running = False

    def changeState(self, state):
    	self.state = state

    def start(self):
        self.running = True
        while self.running:
        	self.screen.fill(Color.BLACK)
        	for event in pygame.event.get():
        		if event.type == pygame.QUIT:
        			self.running = False

        	self.state.update()
        	self.state.draw()
        	pygame.display.update()
        	self.clock.tick(59)

