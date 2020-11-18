import pygame
from player import Player, Directions
from playerfactory import Playerfactory


class Protagonist(Player):
    def __init__(self, x, y, screen, coll_rect, board, bomb_vec, character="Terra"):
        super(Protagonist, self).__init__(x, y, screen, coll_rect, board)
        self.goNextLevel = False
        self.health = 4
        self.lives = 3
        self.score = 0
        self.numberOfBombs = 1
        self.bomb_vec = bomb_vec
        self.character = character
        self.sprite_up = []
        self.sprite_down = []
        self.sprite_horiz = []
        self.sprite_dead = None
        self.sprite_bomb = {}

        self.initChar()

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox, 3)

        tempvar = (self.x + 5, self.y - 20)

        if self.isAlive:

            if self.walkCount + 1 >= self.sprite_up.__len__()*self.animationsNumber:
                self.walkCount = 0

            if self.walking is Directions["STAY"]:
                if self.looking is Directions["DOWN"]:
                    self.screen.blit(self.sprite_down[0], tempvar)
                elif self.looking is Directions["UP"]:
                    self.screen.blit(self.sprite_up[0], tempvar)
                elif self.looking is Directions["LEFT"]:
                    self.screen.blit(self.sprite_horiz[0], tempvar)
                else:
                    self.screen.blit(pygame.transform.flip(self.sprite_horiz[0], True, False), tempvar)
            else:
                # aggiustare lo spawn point del disegno, spostare in alto(?)
                if self.walking is Directions["DOWN"]:
                    self.screen.blit(self.sprite_down[self.walkCount // self.animationsNumber], tempvar)
                elif self.walking is Directions["UP"]:
                    self.screen.blit(self.sprite_up[self.walkCount // self.animationsNumber], tempvar)
                elif self.walking is Directions["LEFT"]:
                    self.screen.blit(self.sprite_horiz[self.walkCount // self.animationsNumber], tempvar)
                else:
                    self.screen.blit(pygame.transform.flip(
                        self.sprite_horiz[self.walkCount // self.animationsNumber], True, False), tempvar)

    def initChar(self):
        if self.character is "Terra":
            self.assignDict(Playerfactory.terra())

    def assignDict(self, Dict):
        self.sprite_up = Dict["up"]
        self.sprite_down = Dict["down"]
        self.sprite_horiz = Dict["horiz"]
        self.sprite_dead = Dict["dead"]
        self.sprite_bomb["up"] = Dict["up_bomb"]
        self.sprite_bomb["down"] = Dict["down_bomb"]
        self.sprite_bomb["horiz"] = Dict["horiz_bomb"]

    def placeBomb(self):
        pass

    def takePowerUp(self):
        pass
