import random
import pygame
import math
from math import pi
# import PyParticles

class Robot:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = (52, 235, 225)
        self.thickness = 1

    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius, self.thickness)


width = 1200
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('FireAnt2D Simulation')
background_colour = (0,0,0)
robot_radius = 20

# draw ground
ground_width = 200
ground_height = 400
ground_1_left = 0
ground_1_top = height - ground_height
ground_1_right = ground_width
ground_1_bottom = height

ground_2_left = width - ground_width
ground_2_top = height - ground_height
ground_2_right = width
ground_2_bottom = height



# function to determine if a robot is in contact with either of the two ground
def robot_ground_contact(robot):
    if robot.y + robot.radius >= ground_1_top and robot.x + robot.radius >= ground_1_left and robot.x - robot.radius <= ground_1_right:
        return True
    elif robot.y + robot.radius >= ground_2_top and robot.x + robot.radius >= ground_2_left and robot.x - robot.radius <= ground_2_right:
        return True
    else:
        return False

# function to determine if a robot is in contact with another robot
def robot_robot_contact(robot1, robot2):
    dx = robot1.x - robot2.x
    dy = robot1.y - robot2.y
    dist = math.hypot(dx, dy)
    if dist < robot1.radius + robot2.radius:
        return True
    else:
        return False


screen.fill(background_colour)

swarm = []

# define anchors
anchor_1_x = ground_1_right - robot_radius
anchor_1_y = ground_1_top - robot_radius
anchor_2_x = ground_2_left + robot_radius
anchor_2_y = ground_2_top - robot_radius
anchor_1 = Robot(anchor_1_x, anchor_1_y, robot_radius)
anchor_2 = Robot(anchor_2_x, anchor_2_y, robot_radius)
anchor_1.display()
anchor_2.display()
swarm.append(anchor_1)
swarm.append(anchor_2)

# define number of robots that can be contained on the bridge (horizontally)
bridge_horizontal_swarm_size = int((width - 2*ground_width) / (robot_radius * 2))
bridge_vertical_swarm_size = 5
for i in range(bridge_horizontal_swarm_size):
    for j in range(bridge_vertical_swarm_size):
        x = anchor_1_x + (i + 1) * robot_radius * 2
        y = anchor_1_y + j * robot_radius * 2
        robot = Robot(x, y, robot_radius)
        robot.display()
        swarm.append(robot)

'''
swarm_size = 10
for i in range(swarm_size):
    size = 20
    contact = True
    while contact: 
        x = random.randint(size, width-size)
        y = random.randint(size, height-size)
        new_robot = Robot(x, y, size)
        if not robot_ground_contact(new_robot):
            if len(swarm)==0:
                swarm.append(new_robot)
                contact = False
            for i in range(len(swarm)):
                if not robot_robot_contact(new_robot, swarm[i]):
                    contact = False
                    swarm.append(new_robot)
                    break
    new_robot.display()
'''

pygame.draw.rect(screen, [224, 224, 224], [ground_1_left, ground_1_top, ground_width, ground_height], False)
pygame.draw.rect(screen, [224, 224, 224], [ground_2_left, ground_2_top, ground_width, ground_height], False)
pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = (True, False)[paused]
    
    

    
    