import pygame
from player import Player
from playerfactory import Playerfactory


class Enemy(Player):
    def __init__(self, x, y, screen, coll_rect):
        super(Enemy, self).__init__(x, y, screen, coll_rect)
        self.sprites = Playerfactory.enemy_1()
        self.myAI = None

    def draw(self):
        if self.isAlive:
            # aggiustare lo spawnpoint del disegno spostare in alto (?)
            self.screen.blit(self.sprites["up"][0], (self.x, self.y))
