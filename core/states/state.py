class State(object):
	def __init__(self, wm, screen, game):
		self.wm = wm;
		self.screen = screen
		self.game = game
		self.images = {}

	def update(self):
		if self.wm.state['buttons'] == 4096:
			print "Closing connection..."
			exit(self.wm)

	def draw(self):
		pass