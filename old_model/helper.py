import math

screen_size = (1200, 1000)
physical_world_size = (100.0, 100.0 * screen_size[1]/screen_size[0])

# convert positions in physics coordinates to display coordinates
def world_to_display(input_pos, world_size, display_size):
    pos_display = [0, 0]
    pos_display[0] = int(input_pos[0]/world_size[0] * display_size[0])
    pos_display[1] = int((1-input_pos[1]/world_size[1]) * display_size[1])
    return pos_display

# detect collision between two spheres/robots
def robot_collision(robot1, robot2, sphere_radius):
    sphere1_pos = robot1.pos
    sphere2_pos = robot2.pos
    # physical_sphere1_pos = world_to_display(sphere1_pos, physical_world_size, screen_size)
    # physical_sphere2_pos = world_to_display(sphere2_pos, physical_world_size, screen_size)
    distance = math.sqrt((sphere1_pos[0] - sphere2_pos[0])**2 + (sphere1_pos[1] - sphere2_pos[1])**2)
    if distance < sphere_radius * 2:
        return True
    else:
        return False

'''
# detect collision between two robots
def robot_collision(robot1, robot2, sphere_radius):
    if sphere_collision(robot1.sphere1_pos, robot2.sphere1_pos, sphere_radius) or \
        sphere_collision(robot1.sphere2_pos, robot2.sphere2_pos, sphere_radius) or \
        sphere_collision(robot1.sphere1_pos, robot2.sphere2_pos, sphere_radius) or \
        sphere_collision(robot1.sphere2_pos, robot2.sphere1_pos, sphere_radius):
        return True
    else:
        return False
'''