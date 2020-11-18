from enum import Enum
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

    def controlBoard(self):
        tmpy = round(self.x / 60)
        tmpx = round(self.y / 60)

        if self.board[tmpx][tmpy] == 0:
            self.board[self.position[0]][self.position[1]] = 0
            self.board[tmpx][tmpy] = Part["PLAYER"]
            self.position = [tmpx, tmpy]

    def gameOver(self):
        self.isAlive = False
        self.velocity = 0

    def moveUp(self):
        if self.y - self.velocity >= self.coll_rect.top:
            self.y -= self.velocity
            self.hitbox.top -= self.velocity
            self.controlBoard()

    def moveDown(self):
        if self.y + self.velocity + self.sprite_height <= self.coll_rect.top + self.coll_rect.height:
            self.y += self.velocity
            self.hitbox.top += self.velocity
            self.controlBoard()

    def moveLeft(self):
        if self.x - self.velocity >= self.coll_rect.left:
            self.x -= self.velocity
            self.hitbox.left -= self.velocity
            self.controlBoard()

    def moveRight(self):
        if self.x + self.velocity + self.sprite_width <= self.coll_rect.right:
            self.x += self.velocity
            self.hitbox.left += self.velocity
            self.controlBoard()
