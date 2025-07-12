import sys
import time
import pygame
import constants as k
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((k.Screen.WIDTH, k.Screen.HEIGHT))
    print(f"Screen width: {screen.get_width()}")
    print(f"Screen height: {screen.get_height()}")

    clock = pygame.time.Clock()
    dt: float = 0

    pygame.display.set_caption("text demo")

    font = pygame.font.SysFont(
        None, 48
    )  # or use pygame.font.Font('path/to/font.ttf', 48)
    game_over_text = font.render("Game over!", True, (255, 255, 255))  # white text

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(k.Screen.WIDTH / 2, k.Screen.HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    Shot.containers = (updatable, drawable, shots)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collide(player):
                screen.blit(
                    game_over_text,
                    (
                        k.Screen.WIDTH / 2 - game_over_text.get_width() / 2,
                        k.Screen.HEIGHT / 2 - game_over_text.get_height() / 2,
                    ),
                )
                print("Game over!")
                sys.exit(0)
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.kill()
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        screen.fill("black")
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
