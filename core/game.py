import pygame
import cwiid
from states import main_menu

class Game():
	def __init__(self):
		pygame.init()
		self.size = (800, 500)
		self.screen = pygame.display.set_mode(self.size)
		self.clock = pygame.time.Clock()
		pygame.display.set_caption("Ace Attorney Simulator")
		self.font = pygame.font.SysFont("monospace", 16)
        
		self.state = main_menu.Menu(self.screen, cwiid.Wiimote())
		self.running = False

	def start(self):
		self.running = True

		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			#self.state.update()
			#self.state.draw()

			pygame.display.flip()
			self.clock.tick(60)

