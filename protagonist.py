import pygame
from player import Player
from playerfactory import Playerfactory


class Protagonist(Player):
    def __init__(self, x, y, screen, coll_rect, bomb_vec, character="Terra"):
        super(Protagonist, self).__init__(x, y, screen, coll_rect)
        self.goNextLevel = False
        self.health = 4
        self.lives = 3
        self.score = 0
        self.numberOfBombs = 1
        self.bomb_vec = bomb_vec
        self.character = character
        self.sprite_dic = Playerfactory.terra()

        self.initChar()

    def draw(self):
        if self.isAlive:
            # aggiustare lo spawn point del disegno, spostare in alto(?)
            self.screen.blit(self.sprite_dic["down"][0], (self.x, self.y))

    def initChar(self):
        if self.character is "Terra":
            self.sprite_dic = Playerfactory.terra()

    def placeBomb(self):
        pass

    def takePowerUp(self):
        pass
