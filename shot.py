import pygame
from constants import *
from circleshape import CircleShape
from pygame.sprite import Group

class Shot(CircleShape):
    containers: tuple[Group, Group, Group]
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.radius = SHOT_RADIUS
        super().__init__(self.x, self.y, self.radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt    