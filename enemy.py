import pygame
from player import Player


class Enemy(Player):
    def __init__(self, x, y, screen, coll_rect):
        super(Enemy, self).__init__(x, y, screen, coll_rect)
        self.myAI = None

    def draw(self):
        pass
