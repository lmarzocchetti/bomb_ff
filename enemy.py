import pygame
from player import Player


class Enemy(Player):
    def __init__(self, x, y, screen, coll_rect):
        super(Enemy, self).__init__(x, y, screen, coll_rect)
        self.myAI = None

    def draw(self):
        if self.isAlive:
            pygame.draw.rect(self.screen, (205, 0, 205), self.hitbox, 2)
