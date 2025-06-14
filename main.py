import pygame
import constants as k
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((k.Screen.WIDTH, k.Screen.HEIGHT))

    clock = pygame.time.Clock()
    dt: float = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(k.Screen.WIDTH / 2, k.Screen.HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        screen.fill("black")
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
