import pygame
import math
import numpy as np
from helper import robot_collision

def distance(point1, point2):
	point1 = np.array(point1)
	point2 = np.array(point2)
	return np.linalg.norm(point1 - point2)

class Robot:
	def __init__(self, radius, pos, motion_direction):
		self.pos = list(pos)
		self.radius = radius
		self.motion_direction = motion_direction # 0: stationary, 1-6: neighbour directions cw
		self.velocity = 0.5


	def set_status(self, status):
		self.status = status

	def check_collision(self, robot2):
		if robot_collision(self, robot2, self.radius):
			return True
		else:
			return False

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
			self.sphere1_pos[0] = self.sphere2_pos[0] - math.cos(self.orientation) * bar_length
			self.sphere1_pos[1] = self.sphere2_pos[1] - math.sin(self.orientation) * bar_length
		elif self.sphere2_status == 1:
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

		
