class Robot:
	def __init__(self, sphere1_pos, sphere2_pos, orientation, status):
		self.sphere1_pos = list(sphere1_pos) # [x, y]
		self.sphere2_pos = list(sphere2_pos) # [x, y]
		self.orientation = orientation
		self.status = status # 0: moving, 1: structural

	def set_status(self, status):
		self.status = status

	def rotate(self, new_orientation):
		self.orientation = new_orientation
		# update sphere1_pos and sphere2_pos
