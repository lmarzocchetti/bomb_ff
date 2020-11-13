import pygame


class Blockfactory:

    @staticmethod
    def blocks_1():
        ret = {"hardblock": pygame.transform.scale(pygame.image.load("res/world_1/hardblock.png"), (60, 60)),
               "softblock": [pygame.transform.scale(pygame.image.load("res/world_1/softblock_0.png"), (60, 60)),
                             pygame.transform.scale(pygame.image.load("res/world_1/softblock_1.png"), (60, 60)),
                             pygame.transform.scale(pygame.image.load("res/world_1/softblock_2.png"), (60, 60)),
                             pygame.transform.scale(pygame.image.load("res/world_1/softblock_3.png"), (60, 60)),
                             pygame.transform.scale(pygame.image.load("res/world_1/softblock_4.png"), (60, 60)),
                             pygame.transform.scale(pygame.image.load("res/world_1/softblock_5.png"), (60, 60)),
                             pygame.transform.scale(pygame.image.load("res/world_1/softblock_6.png"), (60, 60))]}
        return ret
