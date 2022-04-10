import pygame
import math, random
from robot import Robot
from helper import world_to_display, collision_detection

background_color = (0, 0, 0)  # set background color to black
robot_color = (0, 50, 200)  # set robot color to blue
connection_color = (255, 255, 255)  # set connection color to white
sphere_radius = 5  # model spheres as dots, set radius in number of pixels
bar_length = 1.5 # model connection as a bar, set bar length in number of pixels

# window origin is @ top left corner
pygame.init()  # initialize pygame
pygame.display.set_caption('2D simulation for FireAnt')
screen_size = (1200, 1000)  # width and height for pygame screen
screen = pygame.display.set_mode(screen_size)

# configuring simulation
robot_quantity = 100  # number of robots
frame_period = 100  # updating period of the simulation and graphics, in ms

# reconfigure screen into a physical world
# i.e., the origin is at bottom left corner of the screen, (0,0)
physical_world_size = (100.0, 100.0 * screen_size[1]/screen_size[0])

# coefficient for robot swarm initialization distribution
distribution_coef = 0.5



vbound_gap_ratio = 0.15  # for the virtual boundaries inside the window

# calculate the corner positions of virtual boundaries, for display
# left bottom corner
pos_lb = world_to_display([physical_world_size[0]*vbound_gap_ratio,
                              physical_world_size[1]*vbound_gap_ratio], physical_world_size, screen_size)
# right bottom corner
pos_rb = world_to_display([physical_world_size[0]*(1-vbound_gap_ratio),
                              physical_world_size[1]*vbound_gap_ratio], physical_world_size, screen_size)
# right top corner
pos_rt = world_to_display([physical_world_size[0]*(1-vbound_gap_ratio),
                              physical_world_size[1]*(1-vbound_gap_ratio)], physical_world_size, screen_size)
# left top corner
pos_lt = world_to_display([physical_world_size[0]*vbound_gap_ratio,
                              physical_world_size[1]*(1-vbound_gap_ratio)], physical_world_size, screen_size)

# instantiate robot swarm
robots = []  # contains all robots, index == robot id
for i in range(robot_quantity):
    
    '''
    row_idx = i % 20
    col_idx = i // 20
    orientation_set = 0.3 * math.pi
    sphere1_pos_set = (physical_world_size[0]/2 + row_idx*0.75, physical_world_size[1]/2 + col_idx * math.sin(orientation_set) * bar_length + col_idx*0.85)
    sphere2_pos_x = sphere1_pos_set[0] + math.cos(orientation_set) * bar_length
    sphere2_pos_y = sphere1_pos_set[1] + math.sin(orientation_set) * bar_length
    sphere2_pos_set = (sphere2_pos_x,sphere2_pos_y)
    robots.append(Robot(sphere1_pos_set, sphere2_pos_set, orientation_set, 0))

    '''
    # initialize random position that is away from window edges
    sphere1_pos_rand = (((random.random() - 0.5) * distribution_coef + 0.5) * physical_world_size[0],
                         ((random.random() - 0.5) * distribution_coef + 0.5) * physical_world_size[1])
    orientation_rand = random.random() * 2*math.pi - math.pi  # random in (-pi, pi)
    sphere2_pos_x = sphere1_pos_rand[0] + math.cos(orientation_rand) * bar_length
    sphere2_pos_y = sphere1_pos_rand[1] + math.sin(orientation_rand) * bar_length
    sphere2_pos_rand = (sphere2_pos_x,sphere2_pos_y)
    collided = False
    for j in range(len(robots)):
        if collision_detection(sphere1_pos_rand, robots[j].sphere1_pos, sphere_radius) or \
            collision_detection(sphere2_pos_rand, robots[j].sphere2_pos, sphere_radius):
            collided = True
            break
    if (not collided):
        robots.append(Robot(sphere1_pos_rand, sphere2_pos_rand, orientation_rand, 0))
    


def main():

    sim_exit = False  # simulation exit flag
    timer_last = pygame.time.get_ticks()  # return number of milliseconds after pygame.init()
    timer_now = timer_last  # initialize it with timer_last
    while not sim_exit:
        # exit the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sim_exit = True  # exit with the close window button
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_ESCAPE) or (event.key == pygame.K_q):
                    sim_exit = True  # exit with ESC key or Q key

        # update the physics, control rules and graphics at the same time
        timer_now = pygame.time.get_ticks()
        if (timer_now - timer_last) > frame_period:
            timer_last = timer_now  # reset timer

            # graphics update
            screen.fill(background_color)
            # draw the virtual boundaries
            pygame.draw.lines(screen, (255, 255, 255), True, [pos_lb, pos_rb, pos_rt, pos_lt], 1)
            # draw the robots
            for i in range(len(robots)):
                sphere1_display_pos = world_to_display(robots[i].sphere1_pos, physical_world_size, screen_size)
                sphere2_display_pos = world_to_display(robots[i].sphere2_pos, physical_world_size, screen_size)

                pygame.draw.circle(screen, robot_color, sphere1_display_pos, sphere_radius, 0)
                pygame.draw.circle(screen, robot_color, sphere2_display_pos, sphere_radius, 0)
                pygame.draw.line(screen, connection_color, sphere1_display_pos, sphere2_display_pos, width=1)
            pygame.display.update()

if __name__ == '__main__':
    main()