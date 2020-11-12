import pygame
import levelfactory
from hardblock import Hardblock
from softblock import Softblock
from protagonist import Protagonist
from enemy import Enemy
from playerfactory import Playerfactory

prova = pygame.image.load("res/characters/terra_down.png")
prova = pygame.transform.scale(prova, (prova.get_size()[0] * 2, prova.get_size()[1] * 2))
sas = pygame.rect.Rect(0, 0, 1280, 720)
prova1 = pygame.image.load("res/world_1/softblock_0.png")
# prova1 = pygame.transform.scale(prova1, (prova1.get_size()[0] + 44, prova1.get_size()[1] + 44))
prova2 = pygame.transform.scale(prova, (50, 80))


class Gamepanel:
    def __init__(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT, fps=30, character="Terra", world_level=(0, 0)):
        self.screen = screen
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.isRunning = True
        self.fps = fps
        self.character = character
        self.coll_rect = pygame.rect.Rect(0, 0, 780, 660)
        self.world, self.level = world_level[0], world_level[1]
        self.clock = pygame.time.Clock()
        self.board = self.levelInit()
        self.player = None
        self.enemies = []
        self.hardblocks = []
        self.softblocks = []
        # da usare
        self.bombs = []
        # da usare 2
        self.powerUps = []
        # da usare 3
        self.nextlevelblock = None
        # da usare 4
        self.timeToHurry = None

        Playerfactory.terra()

        self.characterInit()
        self.maincycle()

    def maincycle(self):
        """
        Initialize the clock at fps rate
        :return: None
        """
        self.clock.tick(self.fps)

        while self.isRunning:
            pygame.draw.rect(self.screen, (255, 255, 255), self.coll_rect, 2)

            self.redrawGameWindow()

            pygame.display.update()

    def redrawGameWindow(self):
        """
        Draw all the entities in the game
        :return: None
        """
        self.player.draw()

        for enemy in self.enemies:
            enemy.draw()

        for hb in self.hardblocks:
            hb.draw()

        for sb in self.softblocks:
            sb.draw()

    def characterInit(self):
        """
        Based on the board variable, initialize the class respect to this
        board and store in vectors
        :return: None
        """
        initx = 0
        inity = 0

        for i in range(11):
            for j in range(13):
                tmp = self.board[i][j]
                if tmp is levelfactory.Part["HARDBLOCK"]:
                    self.hardblocks.append(Hardblock(initx, inity, self.screen))
                elif tmp is levelfactory.Part["SOFTBLOCK"]:
                    self.softblocks.append(Softblock(initx, inity, self.screen))
                elif tmp is levelfactory.Part["PLAYER"]:
                    self.player = Protagonist(initx, inity, self.screen, self.coll_rect, self.bombs)
                elif tmp is levelfactory.Part["ENEMY"]:
                    self.enemies.append(Enemy(initx, inity, self.screen, self.coll_rect))
                initx += 60
            inity += 60
            initx = 0

    def levelInit(self):
        """
        simple ifs and elifs
        :return: boardgame as an 2D array of 0(anything), and the "Part" enumeration
        """
        if self.world == 1:
            if self.level == 1:
                return levelfactory.LevelFactory.world_1()
        else:
            return levelfactory.LevelFactory.world_1()
