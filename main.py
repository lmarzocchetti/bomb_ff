import pygame
from gamepanel import Gamepanel

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("BombFF")

    gamepanel = Gamepanel(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

    pygame.quit()
