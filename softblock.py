import pygame
from entity import Entity


class Softblock(Entity):
    def __init__(self, x, y):
        super(Softblock, self).__init__(x, y)

    def destroy(self):
        pass

    def draw(self):
        pass
