import pygame
from entity import Entity


class Hardblock(Entity):
    def __init__(self, x, y):
        super(Hardblock, self).__init__(x, y)

    def draw(self):
        pass
