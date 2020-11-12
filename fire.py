from entity import Entity


class Fire(Entity):
    def __init__(self, x, y, screen, secondsRemaining=2):
        super(Fire, self).__init__(x, y, screen)
        self.secondsRemaining = secondsRemaining

    def draw(self):
        pass
