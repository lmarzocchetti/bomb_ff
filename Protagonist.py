from player import Player


class Protagonist(Player):
    def __init__(self, x, y, coll_rect):
        super(Protagonist, self).__init__(x, y, coll_rect)
