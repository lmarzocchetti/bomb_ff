import pygame
from entity import Entity


class Softblock(Entity):
    def __init__(self, x, y, screen):
        super(Softblock, self).__init__(x, y, screen)

    def destroy(self):
        self.isAlive = False

    def draw(self):
        if self.isAlive:
            pygame.draw.rect(self.screen, (0, 255, 0), self.hitbox, 2)
