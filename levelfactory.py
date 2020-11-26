from enum import Enum
from random import randint


class Part(Enum):
    NONE = 0
    HARDBLOCK = 1
    SOFTBLOCK = 2
    PLAYER = 3
    ENEMY = 4


class LevelFactory:
    @staticmethod
    def populate_softblock(board, number=50):
        """
        insert number of softblock in the gameboard
        :param board: he gameboard to populate with softblock
        :param number: number of softblock
        :return: the modified gameboard
        """
        i = number

        while i != 0:
            randcols = randint(0, 12)
            randraws = randint(0, 10)
            if board[randraws][randcols] != Part["NONE"] or (randraws, randcols) == (0, 1) or (randraws, randcols) == (1, 0):
                continue
            else:
                board[randraws][randcols] = Part["SOFTBLOCK"]
                i -= 1

    @staticmethod
    def spawn_enemies(board, number=3):
        """
        insert number of enemies in the gameboard
        :param board: The gameboard to populate with enemies
        :param number: number of enemies
        :return: the modified gameboard
        """
        i = number

        while i != 0:
            randcols = randint(0, 12)
            randraws = randint(0, 10)
            if board[randraws][randcols] != Part["NONE"] or randraws <= 3 or randcols <= 5:
                continue
            else:
                board[randraws][randcols] = Part["ENEMY"]
                i -= 1

    @staticmethod
    def populate_hardblock(board):
        for i in range(11):
            for j in range(13):
                if i % 2 != 0 and j % 2 != 0:
                    board[i][j] = Part['HARDBLOCK']

    @staticmethod
    def world_1():
        """
        Initialize a 2D array with hardblocks in fixed positions.
        Set the player, and call 2 function to populate this gameboard with softblocks and enemies
        :return: a 2D array which represent the new gameboard.
        """
        board = [[Part["NONE"] for x in range(13)]for y in range(11)]

        board[0][0] = Part['PLAYER']

        # initialization for the normal blocks.
        # in world 1 these blocks are in the odd position of the matrix
        LevelFactory.populate_hardblock(board)

        # initialization for the destructible blocks.
        LevelFactory.populate_softblock(board)
        LevelFactory.spawn_enemies(board)

        return board
