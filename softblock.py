import pygame
from entity import Entity
from blockfactory import Blockfactory


class Softblock(Entity):
    def __init__(self, x, y, screen):
        super(Softblock, self).__init__(x, y, screen)
        self.sprites = Blockfactory.blocks_1()["softblock"]

    def destroy(self):
        self.isAlive = False

    def draw(self):
        if self.isAlive:
            self.screen.blit(self.sprites[0], (self.x, self.y))
