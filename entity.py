import pygame


class Entity:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.isAlive = True
        self.sprite_width = 60
        self.sprite_height = 60
        self.screen = screen
        self.hitbox = pygame.rect.Rect(self.x, self.y, self.sprite_width, self.sprite_height)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getHibox(self):
        return self.hitbox
