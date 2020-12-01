from enum import Enum

import pygame

from entity import Entity
from levelfactory import Part


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

    def moveDown(self):
        if not self.controlCollision("down"):
            if self.y + self.velocity + self.sprite_height <= self.coll_rect.top + self.coll_rect.height:
                self.y += self.velocity
                self.hitbox.top += self.velocity
                self.controlBoard()

    def moveLeft(self):
        if not self.controlCollision("left"):
            if self.x - self.velocity >= self.coll_rect.left:
                self.x -= self.velocity
                self.hitbox.left -= self.velocity
                self.controlBoard()

    def moveRight(self):
        if not self.controlCollision("right"):
            if self.x + self.velocity + self.sprite_width <= self.coll_rect.right:
                self.x += self.velocity
                self.hitbox.left += self.velocity
                self.controlBoard()

    def controlCollision(self, move):
        print(self.classBoard)

        tmp = None

        if "up" == move:
            tmp = self.classBoard[self.position[1] - 1][self.position[0]]
            print(tmp)
            if tmp is not Part["NONE"]:
                return tmp.getHitbox().colliderect(self.hitbox)
        elif "down" == move:
            tmp = self.classBoard[self.position[1] + 1][self.position[0]]
            print(tmp)
            if tmp is not Part["NONE"]:
                return tmp.getHitbox().colliderect(self.hitbox)
        elif "left" == move:
            tmp = self.classBoard[self.position[1]][self.position[0] - 1]
            print(tmp)
            if tmp is not Part["NONE"]:
                return tmp.getHitbox().colliderect(self.hitbox)
        else:
            tmp = self.classBoard[self.position[1]][self.position[0] + 1]
            print(tmp)
            if tmp is not Part["NONE"]:
                return tmp.getHitbox().colliderect(self.hitbox)

    def getPosition(self):
        return self.position

    def setClassBoard(self, classBoard):
        self.classBoard = classBoard
