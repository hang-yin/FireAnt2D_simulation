import math

# convert positions in physics coordinates to display coordinates
def world_to_display(input_pos, world_size, display_size):
    pos_display = [0, 0]
    pos_display[0] = int(input_pos[0]/world_size[0] * display_size[0])
    pos_display[1] = int((1-input_pos[1]/world_size[1]) * display_size[1])
    return pos_display

# detect collision between two spheres
def collision_detection(sphere1_pos, sphere2_pos, sphere_radius):
    distance = math.sqrt((sphere1_pos[0] - sphere2_pos[0])**2 + (sphere1_pos[1] - sphere2_pos[1])**2)
    if distance < sphere_radius:
        return True
    else:
        return False