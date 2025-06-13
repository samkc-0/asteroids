import pygame
from circle import Circle
import constants as k

class Player(Circle):
    def __init__(self, x:int, y:int):
        super().__init__(x, y, k.Player.RADIUS)
        self.rotation = 0

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

       
