import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    AsteroidField()


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 0)
    while True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")    
        for thing in updatable:
            thing.update(dt)
            
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision_detect(asteroid):
                    shot.kill()
                    asteroid.split()
            if asteroid.collision_detect(player):
                print("Game over!")
                sys.exit()
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
