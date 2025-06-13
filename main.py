import pygame
import constants as k

def main():
    pygame.init()
    screen = pygame.display.set_mode((k.Screen.WIDTH, k.Screen.HEIGHT))

    clock = pygame.time.Clock()
    dt: float = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        screen.fill("black")
        clock.tick()

if __name__ == "__main__":
    main()
