import pygame
import math, random
from robot import Robot

background_color = (0, 0, 0)  # set background color to black
robot_color = (0, 50, 200)  # set robot color to blue
sphere_radius = 5  # model spheres as dots, set radius in number of pixels

# window origin is @ top left corner
pygame.init()  # initialize pygame
pygame.display.set_caption('2D simulation for FireAnt')
screen_size = (1200, 1000)  # width and height for pygame screen
screen = pygame.display.set_mode(screen_size)



def main():
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()

if __name__ == '__main__':
    main()