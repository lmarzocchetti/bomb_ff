import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

run = True
clock = pygame.time.Clock()
fps = 30

prova = pygame.image.load("res/characters/terra_down.png")
sas = pygame.rect.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("BombFF")

    while run:
        clock.tick(fps)
        screen.fill((255, 255 ,255), rect = sas)
        screen.blit(prova, (SCREEN_HEIGHT/2, SCREEN_WIDTH/2))

        pygame.display.update()

    pygame.quit()