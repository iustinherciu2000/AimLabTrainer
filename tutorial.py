import math
import random
import time
import pygame
pygame.init()

# Define width and height
WIDTH, HEIGHT = 800, 600

# Initialize a Pygame window and display it on the screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AimLab Trainer")

# Create main loop that checks for different events like pressing on the screen, quitting the window, etc.
def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
