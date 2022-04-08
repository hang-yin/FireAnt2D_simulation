import pygame
import math
import numpy as np

def distance(point1, point2):
	point1 = np.array(point1)
	point2 = np.array(point2)
	return np.linalg.norm(point1 - point2)


class Robot:
	def __init__(self, sphere1_pos, sphere2_pos, orientation, status):
		self.sphere1_pos = list(sphere1_pos) # [x, y]
		self.sphere2_pos = list(sphere2_pos) # [x, y]
		self.orientation = orientation
		self.status = status # 0: moving, 1: structural
		self.v_sphere1 = 0
		self.v_sphere2 = 0

	def set_status(self, status):
		self.status = status

	def rotate(self, sphere_id, v):
		# update sphere1_pos and sphere2_pos
		if sphere_id == 1:
			self.v_sphere1 = v
		else:
			self.v_sphere2 = v

	def kinematics(self, dt):
		# update sphere1_pos and sphere2_pos
		self.sphere1_pos[0] += self.v_sphere1 * math.cos(self.orientation) * dt
		self.sphere1_pos[1] += self.v_sphere1 * math.sin(self.orientation) * dt
		self.sphere2_pos[0] += self.v_sphere2 * math.cos(self.orientation) * dt
		self.sphere2_pos[1] += self.v_sphere2 * math.sin(self.orientation) * dt
