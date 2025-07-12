import pygame
from circle import Circle
import constants as k
from shot import Shot


class Player(Circle):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, k.Player.RADIUS)
        self.rotation = 0
        self.shot_timeout = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        offset = forward * self.radius
        a = self.position + offset
        b = self.position - offset - right
        c = self.position - offset + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += k.Player.TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * k.Player.SPEED * dt

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        self.shot_timeout -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            # move forward
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_a]:
            # turn anticlockwise
            self.rotate(-dt)

        if keys[pygame.K_d]:
            # turn clockwise
            self.rotate(dt)

        if keys[pygame.K_SPACE]:
            # fire main weapon
            self.shoot()

    def shoot(self):
        if self.shot_timeout > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = forward
        shot.position.rotate(self.rotation)
        shot.velocity.rotate(self.rotation)
        shot.velocity *= k.Player.SHOT_SPEED
        self.shot_timeout = k.Player.SHOT_COOLDOWN
