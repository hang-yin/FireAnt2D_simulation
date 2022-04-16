import pygame
import math, random
from robot import Robot
from helper import world_to_display, robot_collision

background_color = (0, 0, 0)  # set background color to black
robot_color = (0, 50, 200)  # set robot color to blue
connection_color = (255, 255, 255)  # set connection color to white
sphere_radius = 20  # model spheres as dots, set radius in number of pixels

# window origin is @ top left corner
pygame.init()  # initialize pygame
pygame.display.set_caption('2D simulation for FireAnt')
screen_size = (1200, 1000)  # width and height for pygame screen
screen = pygame.display.set_mode(screen_size)

# configuring simulation
robot_quantity = 10  # number of robots
frame_period = 100  # updating period of the simulation and graphics, in ms

# reconfigure screen into a physical world
# i.e., the origin is at bottom left corner of the screen, (0,0)
# physical_world_size = (100.0, 100.0 * screen_size[1]/screen_size[0])

# coefficient for robot swarm initialization distribution
distribution_coef = 0.5

vbound_gap_ratio = 0.15  # for the virtual boundaries inside the window

'''
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
'''


# initialize the robot swarm
def initialize_swarm(swarmsize): 
    # instantiate robot swarm
    robots = []  # contains all robots, index == robot id
    for i in range(swarmsize):
        
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
        pos = (((random.random() - 0.5) * distribution_coef + 0.5) * screen_size[0],
                            ((random.random() - 0.5) * distribution_coef + 0.5) * screen_size[1])
        # define random motion direction beteween 1 and 6
        motion_direction = random.randint(1, 6)
        # motion_direction = 0
        collided = False
        new_robot = Robot(sphere_radius, pos, motion_direction)
        for j in range(len(robots)):
            if robot_collision(new_robot, robots[j], sphere_radius):
                collided = True
                break
        if (not collided):
            robots.append(new_robot)
    print(len(robots))
    return robots



def main():
    robots = initialize_swarm(robot_quantity)
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
        
        '''
        for i in range(len(robots)):
            robots[i].update()
            robots[i].draw(screen, robot_color, connection_color, sphere_radius, bar_length)
        '''

        # update the physics, control rules and graphics at the same time
        timer_now = pygame.time.get_ticks()
        dt = (timer_now - timer_last)  # time interval in milliseconds
        if (dt) > frame_period:
            timer_last = timer_now  # reset timer

            # update robot kinamatics
            for i in range(len(robots)):
                robots[i].update_position(dt)
                for j in range(len(robots)):
                    if i != j:
                        if robot_collision(robots[i], robots[j], sphere_radius):
                            robots[i].motion_direction = 0
                            robots[j].motion_direction = 0
                            break

            # graphics update
            screen.fill(background_color)
            # draw the virtual boundaries
            # pygame.draw.lines(screen, (255, 255, 255), True, [pos_lb, pos_rb, pos_rt, pos_lt], 1)
            # draw the robots
            for i in range(len(robots)):
                # robot_display_pos = world_to_display(robots[i].pos, physical_world_size, screen_size)

                pygame.draw.circle(screen, robot_color, robots[i].pos, sphere_radius, 0)
            pygame.display.update()

if __name__ == '__main__':
    main()