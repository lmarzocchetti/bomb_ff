from entity import Entity
from blockfactory import Blockfactory


class Softblock(Entity):
    def __init__(self, x, y, screen):
        super(Softblock, self).__init__(x, y, screen)
        self.sprites = Blockfactory.blocks_1()["softblock"]
        self.count = 1

    def destroy(self):
        self.isAlive = False

    def draw(self):
        if self.isAlive:
            self.screen.blit(self.sprites[0], (self.x, self.y))
        else:
            if self.count is not self.sprites.__len__():
                self.screen.blit(self.sprites[self.count], (self.x, self.y))
                self.count += 1
