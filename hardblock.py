import pygame
from entity import Entity
from blockfactory import Blockfactory


class Hardblock(Entity):
    def __init__(self, x, y, screen):
        super(Hardblock, self).__init__(x, y, screen)
        self.sprite = Blockfactory.blocks_1()["hardblock"]

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))
