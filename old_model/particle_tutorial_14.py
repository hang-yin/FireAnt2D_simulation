from math import pi
import random
import pygame
import PyParticles

width = 1200
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Springs')

universe = PyParticles.Environment(width, height)
universe.colour = (0,0,0)
universe.addFunctions(['move', 'bounce', 'collide', 'drag', 'accelerate'])
universe.acceleration = (pi, 0.05)
universe.mass_of_air = 0.02

for p in range(3):
    universe.addParticles(mass=100, size=16, speed=0, elasticity=1, colour=(20,40,200))
#universe.addParticles(mass=40, size=10, speed=1, elasticity=1, colour=(20,200,40))

#universe.addSpring(0, 1, length=32, strength=0.05)
#universe.addSpring(1, 2, length=32, strength=0.05)
#universe.addSpring(2, 0, length=32, strength=0.05)

selected_particle = None
paused = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = (True, False)[paused]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            selected_particle = universe.findParticle(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_particle = None

    if selected_particle:
        selected_particle.mouseMove(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    if not paused:
        universe.update()
        
    screen.fill(universe.colour)
    
    for p in universe.particles:
        pygame.draw.circle(screen, p.colour, (int(p.x), int(p.y)), p.size, 0)
        
    for s in universe.springs:
        pygame.draw.aaline(screen, (255,255,255), (int(s.p1.x), int(s.p1.y)), (int(s.p2.x), int(s.p2.y)))

    pygame.display.flip()