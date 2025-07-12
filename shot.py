from circle import Circle
import constants as k
import pygame


class Shot(Circle):
    def __init__(self, x, y):
        super().__init__(x, y, k.Player.SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
