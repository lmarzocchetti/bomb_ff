import pygame
from levelfactory import LevelFactory

prova = pygame.image.load("res/characters/terra_down.png")
prova = pygame.transform.scale(prova, (prova.get_size()[0] * 2, prova.get_size()[1] * 2))
sas = pygame.rect.Rect(0, 0, 1280, 720)


class Gamepanel:
    def __init__(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT, fps=30, character="Terra", world_level=(0, 0)):
        self.screen = screen
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.isRunning = True
        self.fps = fps
        self.character = character
        self.world, self.level = world_level[0], world_level[1]
        self.ret_level = {}
        self.clock = pygame.time.Clock()

        self.maincycle()

    def maincycle(self):
        self.clock.tick(self.fps)
        LevelFactory.world_1()
        while self.isRunning:
            self.screen.fill((255, 255, 255), rect=sas)
            self.screen.blit(prova, (self.SCREEN_HEIGHT / 2, self.SCREEN_WIDTH / 2))

            pygame.display.update()

    def level_init(self):
        if self.world == 1:
            pass
