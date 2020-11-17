from entity import Entity
from blockfactory import Blockfactory


class Bomb(Entity):
    def __init__(self, x, y, screen, secondsToExplode=5):
        super(Bomb, self).__init__(x, y, screen)
        self.isExploded = False
        self.secondsToExplode = secondsToExplode
        self.sprites = Blockfactory.bombs()

    def draw(self):
        self.screen.blit(self.sprites[0], (self.x, self.y))

    def explode(self):
        pass
