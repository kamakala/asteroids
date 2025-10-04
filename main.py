import pygame
#from pygame.locals import *
from constants import (SCREEN_HEIGHT,
                       SCREEN_WIDTH,  
                       ASTEROID_KINDS,
                       ASTEROID_MAX_RADIUS,
                       ASTEROID_MIN_RADIUS,
                       ASTEROID_SPAWN_RATE)



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
if __name__ == "__main__":
    main()
