import pygame
from circle import Circle
import constants as k

class Asteroid(Circle):
    def __init__(self, x:int, y:int, radius:int):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
