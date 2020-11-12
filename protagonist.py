import pygame
from player import Player


class Protagonist(Player):
    def __init__(self, x, y, screen, coll_rect):
        super(Protagonist, self).__init__(x, y, screen, coll_rect)
        self.goNextLevel = False
        self.health = 4
        self.lives = 3
        self.score = 0
        self.numberOfBombs = 1

    def draw(self):
        if self.isAlive:
            pygame.draw.rect(self.screen, (0, 0, 255), self.hitbox, 2)

    def placeBomb(self):
        pass

    def takePowerUp(self):
        pass
