import pygame


class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isAlive = True
        self.sprite_width = 0
        self.sprite_height = 0
        self.hitbox = pygame.rect.Rect(self.x, self.y, self.sprite_width, self.sprite_height)
