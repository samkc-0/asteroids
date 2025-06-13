import pygame
from circle import Circle
import constants as k

class Asteroid(Circle):
    def __init__(self, x:int, y:int, radius:int):
        super().__init__(x, y, radius)

    def draw(self, x, y):
        pass

    def update(self, dt):
        pass
