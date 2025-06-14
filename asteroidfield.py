import pygame
import random
import constants as k
from asteroid import Asteroid


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-k.Asteroid.MAX_RADIUS, y * k.Screen.HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                k.Screen.WIDTH + k.Asteroid.MAX_RADIUS, y * k.Screen.HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * k.Screen.WIDTH, -k.Asteroid.MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * k.Screen.WIDTH, k.Screen.HEIGHT + k.Asteroid.MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius: float, position: pygame.Vector2, velocity: pygame.Vector2):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def get_asteroid_params(self) -> tuple[float, pygame.Vector2, pygame.Vector2]:
        edge = random.choice(self.edges)
        speed = random.randint(40, 100)
        velocity = edge[0] * speed
        velocity = velocity.rotate(random.randint(-30, 30))
        position = edge[1](random.uniform(0, 1))
        kind = random.randint(1, k.Asteroid.KINDS)
        radius = k.Asteroid.MIN_RADIUS * kind
        return radius, position, velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > k.Asteroid.SPAWN_RATE:
            self.spawn_timer = 0
            self.spawn(*self.get_asteroid_params())
