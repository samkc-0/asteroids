import pygame
import constants as k

def main():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return

if __name__ == "__main__":
    main()
