class LevelFactory:
    def __init__(self, world_level):
        self.retval = {}

        if world_level[0] == 0 and world_level[1] == 0:
            self.retval = self.world0_0()

    @staticmethod
    def world0_0():
        return 0
