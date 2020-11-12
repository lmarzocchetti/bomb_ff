import pygame
from entity import Entity


class Hardblock(Entity):
    def __init__(self, x, y, screen):
        super(Hardblock, self).__init__(x, y, screen)

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox, 2)
