from entity import Entity


class PowerUp(Entity):
    def __init__(self, x, y, screen):
        super(PowerUp, self).__init__(x, y, screen)

    def draw(self):
        pass

    def applyPowerUp(self):
        pass

    def takePowerUp(self):
        pass
