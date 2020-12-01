import pygame
import levelfactory
from hardblock import Hardblock
from softblock import Softblock
from protagonist import Protagonist, Directions
from enemy import Enemy
from bomb import Bomb


class Gamepanel:
    def __init__(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT, fps=30, character="Terra", world_level=(1, 1)):
        self.screen = screen
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.isRunning = True
        self.fps = fps
        self.character = character
        self.coll_rect = pygame.rect.Rect(20, 30, 780, 660)
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

        self.temp = [[levelfactory.Part["NONE"] for i in range(13)]for j in range(11)]

        self.carinit()

        #self.characterInit()
        self.maincycle()

    def maincycle(self):
        """
        Initialize the clock at fps rate
        :return: None
        """
        while self.isRunning:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False

            self.eventHandler()
            self.controlCollision()
            self.redrawGameWindow()
            pygame.display.update()

    def eventHandler(self):
        key = pygame.key.get_pressed()

        if self.player.isAlive:
            if key[pygame.K_LEFT]:
                self.player.walkCount += 1
                self.player.walking = Directions["LEFT"]
                self.player.looking = Directions["LEFT"]
                self.player.moveLeft()
            elif key[pygame.K_RIGHT]:
                self.player.walkCount += 1
                self.player.walking = Directions["RIGHT"]
                self.player.looking = Directions["RIGHT"]
                self.player.moveRight()
            elif key[pygame.K_UP]:
                self.player.walkCount += 1
                self.player.walking = Directions["UP"]
                self.player.looking = Directions["UP"]
                self.player.moveUp()
            elif key[pygame.K_DOWN]:
                self.player.walkCount += 1
                self.player.walking = Directions["DOWN"]
                self.player.looking = Directions["DOWN"]
                self.player.moveDown()
            # da modificare
            elif key[pygame.K_SPACE]:
                self.bombs.append(Bomb(self.player.x, self.player.y, self.screen))
            else:
                self.player.walkCount = 0
                self.player.walking = Directions["STAY"]

    def controlCollision(self):
        pass

    def redrawGameWindow(self):
        """
        Draw all the entities in the game
        :return: None
        """
        # pygame.draw.rect(self.screen, (0, 0, 0), pygame.rect.Rect(0, 0, 20, 720))
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.rect.Rect(0, 0, 1280, 30))

        self.backgroundInit()

        #for hb in self.hardblocks:
        #    hb.draw()

        #for sb in self.softblocks:
        #    sb.draw()

        for bomb in self.bombs:
            bomb.draw()

        #for enemy in self.enemies:
        #    enemy.draw()

        #self.player.draw()

        for i in range(11):
            for j in range(13):
                if self.temp[i][j] != levelfactory.Part["NONE"]:
                    if i == 0 and j == 0:
                        continue
                    self.temp[i][j].draw()

        self.player.draw()

    def characterInit(self):
        """
        Based on the board variable, initialize the class respect to this
        board and store in vectors
        :return: None
        """
        initx = 20
        inity = 30

        for i in range(11):
            for j in range(13):
                tmp = self.board[i][j]
                if tmp is levelfactory.Part["HARDBLOCK"]:
                    self.hardblocks.append(Hardblock(initx, inity, self.screen))
                elif tmp is levelfactory.Part["SOFTBLOCK"]:
                    self.softblocks.append(Softblock(initx, inity, self.screen))
                elif tmp is levelfactory.Part["PLAYER"]:
                    self.player = Protagonist(initx, inity, self.screen, self.coll_rect, self.board, self.bombs)
                elif tmp is levelfactory.Part["ENEMY"]:
                    self.enemies.append(Enemy(initx, inity, self.screen, self.coll_rect, self.board))
                initx += 60
            inity += 60
            initx = 20

    def carinit(self):
        initx = 20
        inity = 30

        for i in range(11):
            for j in range(13):
                tmp = self.board[i][j]
                if tmp is levelfactory.Part["HARDBLOCK"]:
                    self.temp[i][j] = Hardblock(initx, inity, self.screen)
                elif tmp is levelfactory.Part["SOFTBLOCK"]:
                    self.temp[i][j] = Softblock(initx, inity, self.screen)
                elif tmp is levelfactory.Part["PLAYER"]:
                    self.temp[i][j] = Protagonist(initx, inity, self.screen, self.coll_rect, self.board, self.bombs)
                    self.player = self.temp[i][j]
                elif tmp is levelfactory.Part["ENEMY"]:
                    self.temp[i][j] = Enemy(initx, inity, self.screen, self.coll_rect, self.board)
                initx += 60
            inity += 60
            initx = 20

        self.player.setClassBoard(self.temp)

    def levelInit(self):
        """
        simple ifs and elifs
        :return: boardgame as an 2D array of "Part" enumeration
        """
        if self.world == 1:
            if self.level == 1:
                return levelfactory.LevelFactory.world_1()
        else:
            return levelfactory.LevelFactory.world_1()

    def backgroundInit(self):
        if self.world == 1:
            self.screen.blit(pygame.image.load("res/world_1/background_1.png"), (20, 30))
