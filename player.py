from enum import Enum

from entity import Entity
from levelfactory import Part
import pygame


class Directions(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    STAY = 5


class Player(Entity):
    def __init__(self, x, y, screen, coll_rect, board):
        super(Player, self).__init__(x, y, screen)
        self.velocity = 6
        self.animationsNumber = 3
        self.walkCount = 0
        self.looking = Directions["DOWN"]
        self.walking = Directions["STAY"]
        self.coll_rect = coll_rect
        self.board = board
        self.position = [0, 0]
        self.classBoard = None

        # self.hitbox = pygame.rect.Rect(self.x+5, self.y+5, 50, 50)

    # BACATO DI MERDA (MOSTRO UCCISO)
    def controlBoard(self):
        tmpy = round(self.x / 60)
        tmpx = round(self.y / 60)

        if self.board[tmpx][tmpy] == Part["NONE"]:
            self.board[self.position[1]][self.position[0]] = Part["NONE"]
            self.board[tmpx][tmpy] = Part["PLAYER"]
            tmp = self.classBoard[self.position[1]][self.position[0]]
            self.classBoard[self.position[1]][self.position[0]] = Part["NONE"]
            self.position = [tmpy, tmpx]
            self.classBoard[self.position[1]][self.position[0]] = tmp

    def gameOver(self):
        self.isAlive = False
        self.velocity = 0

    def moveUp(self):
        if not self.controlCollision("up"):
            if self.y - self.velocity >= self.coll_rect.top:
                self.y -= self.velocity
                self.hitbox.top -= self.velocity
                self.controlBoard()
                print(self.position)

    def moveDown(self):
        if not self.controlCollision("down"):
            if self.y + self.velocity + self.sprite_height <= self.coll_rect.top + self.coll_rect.height:
                self.y += self.velocity
                self.hitbox.top += self.velocity
                self.controlBoard()
                print(self.position)

    def moveLeft(self):
        if not self.controlCollision("left"):
            if self.x - self.velocity >= self.coll_rect.left:
                self.x -= self.velocity
                self.hitbox.left -= self.velocity
                self.controlBoard()
                print(self.position)

    def moveRight(self):
        if not self.controlCollision("right"):
            if self.x + self.velocity + self.sprite_width <= self.coll_rect.right:
                self.x += self.velocity
                self.hitbox.left += self.velocity
                self.controlBoard()
                print(self.position)

    def controlCollision(self, move):
        tmp = None

        if "up" == move:
            for i in range(-1, 2):
                tmp = self.classBoard[self.position[1] - 1][self.position[0] + i]
                if tmp is not Part["NONE"]:
                    if tmp3 := self.hitbox.colliderect(tmp.getHitbox()):
                        return tmp3
                    tmp2 = pygame.rect.Rect(tmp.getHitbox())
                    tmp2.bottom += self.velocity
                    if self.hitbox.colliderect(tmp2):
                        return True
            return False
        elif "down" == move:
            for i in range(-1, 2):
                tmp = self.classBoard[self.position[1] + 1][self.position[0] + i]
                if tmp is not Part["NONE"]:
                    if tmp3 := self.hitbox.colliderect(tmp.getHitbox()):
                        return tmp3
                    tmp2 = pygame.rect.Rect(tmp.getHitbox())
                    tmp2.top -= self.velocity
                    if self.hitbox.colliderect(tmp2):
                        return True
            return False
        elif "left" == move:
            for i in range(-1, 2):
                tmp = self.classBoard[self.position[1] + i][self.position[0] - 1]
                if tmp is not Part["NONE"]:
                    if tmp3 := self.hitbox.colliderect(tmp.getHitbox()):
                        return tmp3
                    tmp2 = pygame.rect.Rect(tmp.getHitbox())
                    tmp2.right += self.velocity
                    if self.hitbox.colliderect(tmp2):
                        return True
            return False
        else:
            for i in range(-1, 2):
                tmp = self.classBoard[self.position[1] + i][self.position[0] + 1]
                if tmp is not Part["NONE"]:
                    if tmp3 := self.hitbox.colliderect(tmp.getHitbox()):
                        return tmp3
                    tmp2 = pygame.rect.Rect(tmp.getHitbox())
                    tmp2.left -= self.velocity
                    if self.hitbox.colliderect(tmp2):
                        return True
            return False

    def getPosition(self):
        return self.position

    def setClassBoard(self, classBoard):
        self.classBoard = classBoard
