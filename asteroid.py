import random
import pygame
from circle import Circle
import constants as k


class Asteroid(Circle):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < k.Asteroid.MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        u = self.velocity.copy().rotate(-angle)
        v = self.velocity.copy().rotate(angle)
        r = self.radius - k.Asteroid.MIN_RADIUS
        first_child = Asteroid(int(self.position.x), int(self.position.y), r)
        first_child.velocity = u * 1.2
        second_child = Asteroid(int(self.position.x), int(self.position.y), r)
        second_child.velocity = v * 1.2
