# filepath: /python-3d-space/python-3d-space/src/main.py

import pygame
from player import Player
from cube import Cube

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("3D Space")

# Create player and cube
player = Player(position=(0, 0, 0))
cube = Cube(size=1, position=(0, -1, 0))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Update player and cube
    player.move()
    cube.render(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()