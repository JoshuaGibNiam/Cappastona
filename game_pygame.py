import pygame
from pygame import key
from player import Player
from walls import Wall
from enemies import *
from game_manager import GameManager
from constants import Constants
C = Constants()
C.set_level(1)

#Initialize sprites
player = Player(750, 0)  ##top left corner

wall1 = Wall(0, 0, 20, 800)
wall2 = Wall(20, 0, 600, 20)
wall3 = Wall(20, 100, 600, 20)
wall4 = Wall(20, 200, 600, 20)
wall5 = Wall(20, 300, 600, 20)
wall6 = Wall(20, 400, 600, 20)
wall7 = Wall(20, 500, 600, 20)

enemy1 = enemy_1(100, 535)  # bottom left corner
enemies = [enemy1]

game_manager = GameManager()


##list of sprites (for shortening code)
sprites = [player, wall1, wall2, wall3, wall4, wall5, wall6, wall7, enemy1]
walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7]

#settings
pygame.init()
window = pygame.display.set_mode((C.WINDOW_HEIGHT, C.WINDOW_WIDTH))
pygame.display.set_caption(C.WINDOW_CAPTION)

clock = pygame.time.Clock()
run = True



##############
while run:
    clock.tick(C.FPS)  # 60 fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = key.get_pressed()
    player.update(keys, walls)
    enemy1.update(C.ENEMIES
            )
    ## Clearing
    window.fill((255, 255, 255))


    game_manager.update(player, enemies, keys, window)


    for sprite in sprites:
        window.blit(sprite.image, sprite.rect)
        if isinstance(sprite, enemy_1):
            window.blit(sprite.fov.image, sprite.fov.rect)
    pygame.display.update()

pygame.quit()
