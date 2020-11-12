from enum import Enum
from entity import Entity


class Directions(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    STAY = 5


class Player(Entity):
    def __init__(self, x, y, screen, coll_rect):
        super(Player, self).__init__(x, y, screen)
        self.velocity = 5
        self.animationsNumber = 3
        self.walkCount = 0
        self.looking = Directions["DOWN"]
        self.walking = Directions["STAY"]
        self.coll_rect = coll_rect

    def gameOver(self):
        self.isAlive = False
        self.velocity = 0

    def moveUp(self):
        if self.y - self.velocity > self.coll_rect.top:
            self.y -= self.velocity
            self.hitbox.top -= self.velocity

    def moveDown(self):
        if self.y + self.velocity < self.coll_rect.top + self.coll_rect.height:
            self.y += self.velocity
            self.hitbox.top += self.velocity

    def moveLeft(self):
        if self.x - self.velocity > self.coll_rect.bottom:
            self.x -= self.velocity
            self.hitbox.left -= self.velocity

    def moveRight(self):
        if self.x + self.velocity < self.coll_rect.bottom + self.coll_rect.width:
            self.x += self.velocity
            self.hitbox.left += self.velocity
