from entity import Entity


class Bomb(Entity):
    def __init__(self, x, y, screen, secondsToExplode=5):
        super(Bomb, self).__init__(x, y, screen)
        self.isExploded = False
        self.secondsToExplode = secondsToExplode

    def draw(self):
        pass

    def explode(self):
        pass
