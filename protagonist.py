from player import Player


class Protagonist(Player):
    def __init__(self, x, y, coll_rect):
        super(Protagonist, self).__init__(x, y, coll_rect)
        self.goNextLevel = False
        self.health = 4
        self.lives = 3
        self.score = 0
        self.numberOfBombs = 1

    def draw(self):
        pass

    def placeBomb(self):
        pass

    def takePowerUp(self):
        pass
