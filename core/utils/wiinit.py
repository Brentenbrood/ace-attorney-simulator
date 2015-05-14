import cwiid
import pygame
from core.utils.colors import Color

""" A utility module to get a cwiid connection with feedback """

def get_connection():
	wm = None
	try: 
		wm=cwiid.Wiimote() 
		return wm
	except RuntimeError: 
		return None


def get_connection_with_drawing(screen, maxAttempts=10):
	wm = None
	i = 0
	font = pygame.font.SysFont("monospace", 16)

	while not wm:
		print "hi"
		screen.fill(Color.BLACK)
		print "second hi"
		screen.blit(font.render("Press 1 + 2 on the wiimote to connect", 1, Color.WHITE), (screen.get_width() / 2 - 130, 5))
		if i != 0:
			screen.blit(font.render("Attempt " + str(i), 1, Color.WHITE), (screen.get_width() / 2 - 140, 20))
		pygame.display.update()
		wm = get_connection()
		if not wm:
			i = i + 1
	return wm


      		
