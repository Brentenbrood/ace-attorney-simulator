from enum import Enum

class AnimState(Enum):

	#All
	normal = 0

	#Attorney
	deskslam = 1
	objection = 2
	paperslap = 3
	ohshit = 9

	#Prosecutor
	damage = 4
	paperblock = 5
	pointblock = 6
	angry = 7
	handslam = 10

	#Judge
	shocked = 8
