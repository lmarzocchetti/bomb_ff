import pygame


class Playerfactory:

    @staticmethod
    def terra():
        ret = {"dead": pygame.transform.scale(pygame.image.load("res/characters/terra_dead.png"), (80, 50)),
               "up": [pygame.transform.scale(pygame.image.load("res/characters/terra_up.png"), (50, 80)),
                      pygame.transform.scale(pygame.image.load("res/characters/terra_up_1.png"), (50, 80)),
                      pygame.transform.scale(pygame.image.load("res/characters/terra_up_2.png"), (50, 80))],
               "down": [pygame.transform.scale(pygame.image.load("res/characters/terra_down.png"), (50, 80)),
                        pygame.transform.scale(pygame.image.load("res/characters/terra_down_1.png"), (50, 80)),
                        pygame.transform.scale(pygame.image.load("res/characters/terra_down_2.png"), (50, 80))],
               "horiz": [pygame.transform.scale(pygame.image.load("res/characters/terra_horiz.png"), (50, 80)),
                         pygame.transform.scale(pygame.image.load("res/characters/terra_horiz_1.png"), (50, 80)),
                         pygame.transform.scale(pygame.image.load("res/characters/terra_horiz_2.png"), (50, 80))],
               "horiz_bomb": pygame.transform.scale(pygame.image.load("res/characters/terra_horiz_bomb.png"), (50, 80)),
               "down_bomb": pygame.transform.scale(pygame.image.load("res/characters/terra_down_bomb.png"), (50, 80)),
               "up_bomb": pygame.transform.scale(pygame.image.load("res/characters/terra_up_bomb.png"), (50, 80))}
        return ret

    @staticmethod
    def enemy_1():
        ret = {"dead": pygame.transform.scale(pygame.image.load("res/world_1/enemy_dead.png"), (80, 50)),
               "up": [pygame.transform.scale(pygame.image.load("res/world_1/enemy_up.png"), (50, 80)),
                      pygame.transform.scale(pygame.image.load("res/world_1/enemy_up_1.png"), (50, 80)),
                      pygame.transform.scale(pygame.image.load("res/world_1/enemy_up_2.png"), (50, 80))],
               "down": [pygame.transform.scale(pygame.image.load("res/world_1/enemy_down.png"), (50, 80)),
                        pygame.transform.scale(pygame.image.load("res/world_1/enemy_down_1.png"), (50, 80)),
                        pygame.transform.scale(pygame.image.load("res/world_1/enemy_down_2.png"), (50, 80))],
               "horiz": [pygame.transform.scale(pygame.image.load("res/world_1/enemy_horiz.png"), (50, 80)),
                         pygame.transform.scale(pygame.image.load("res/world_1/enemy_horiz_1.png"), (50, 80)),
                         pygame.transform.scale(pygame.image.load("res/world_1/enemy_horiz_2.png"), (50, 80))],
               "horiz_bomb": pygame.transform.scale(pygame.image.load("res/world_1/enemy_horiz_bomb.png"), (50, 80)),
               "down_bomb": pygame.transform.scale(pygame.image.load("res/world_1/enemy_down_bomb.png"), (50, 80)),
               "up_bomb": pygame.transform.scale(pygame.image.load("res/world_1/enemy_up_bomb.png"), (50, 80))}
        return ret
