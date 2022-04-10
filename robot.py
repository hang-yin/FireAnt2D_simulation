import pygame
import math
import numpy as np

bar_length = 1.5

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
		self.rotation_direction_sphere1 = 0 # 0: clockwise, 1: counter-clockwise
		self.rotation_direction_sphere2 = 0 # 0: clockwise, 1: counter-clockwise
		self.sphere1_status = 0 # 0: moving, 1: rotating
		self.sphere2_status = 0 # 0: moving, 1: rotating
		self.v_sphere1 = 0.5
		self.v_sphere2 = 0.5

	def set_status(self, status):
		self.status = status

	def rotate(self, sphere_id, v):
		# update sphere1_pos and sphere2_pos
		if sphere_id == 1:
			self.v_sphere1 = v
		else:
			self.v_sphere2 = v

	def update_position(self, dt):
		if self.sphere1_status == 1:
			# rotate sphere1
			if self.rotation_direction_sphere1 == 0:
				self.orientation += self.v_sphere1 * dt / 1000
			else:
				self.orientation -= self.v_sphere1 * dt / 1000
			if self.orientation > math.pi:
				self.orientation -= 2 * math.pi
			elif self.orientation < -math.pi:
				self.orientation += 2 * math.pi
			# update sphere1_pos
			self.sphere1_pos[0] = self.sphere2_pos[0] + math.cos(self.orientation) * bar_length
			self.sphere1_pos[1] = self.sphere2_pos[1] + math.sin(self.orientation) * bar_length
		if self.sphere2_status == 1:
			# rotate sphere2
			if self.rotation_direction_sphere2 == 0:
				self.orientation += self.v_sphere2 * dt / 1000
			else:
				self.orientation -= self.v_sphere2 * dt / 1000
			if self.orientation > math.pi:
				self.orientation -= 2 * math.pi
			elif self.orientation < -math.pi:
				self.orientation += 2 * math.pi
			# update sphere2_pos
			self.sphere2_pos[0] = self.sphere1_pos[0] + math.cos(self.orientation) * bar_length
			self.sphere2_pos[1] = self.sphere1_pos[1] + math.sin(self.orientation) * bar_length

		'''
		# update sphere1_pos and sphere2_pos
		self.sphere1_pos[0] += self.v_sphere1 * math.cos(self.orientation) * dt
		self.sphere1_pos[1] += self.v_sphere1 * math.sin(self.orientation) * dt
		self.sphere2_pos[0] += self.v_sphere2 * math.cos(self.orientation) * dt
		self.sphere2_pos[1] += self.v_sphere2 * math.sin(self.orientation) * dt
		'''
