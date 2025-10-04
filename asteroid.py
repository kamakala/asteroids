from circleshape import CircleShape
import pygame
from pygame.sprite import Group
from constants import *


class Asteroid(CircleShape):
    containers: tuple[Group, Group, Group]
    def __init__(self, x, y, radius) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(self.x, self.y, self.radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt