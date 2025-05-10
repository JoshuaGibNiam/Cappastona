import pygame
from pygame import key
from player import Player
from walls import Wall

#Initialize sprites
player = Player(100, 100)
wall1 = Wall(100, 100, 200, 20)
wall2 = Wall(200, 100, 20, 200)
wall3 = Wall(400, 100, 20, 200)

##list of sprites (for shortening code)
sprites = [player, wall1, wall2, wall3]
walls = [wall1, wall2, wall3]

#settings
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cappastona")

clock = pygame.time.Clock()
run = True

##############
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = key.get_pressed()
    player.update(keys, walls)




    ## Clearing
    window.fill((255, 255, 255))

    for sprite in sprites:
        window.blit(sprite.image, sprite.rect)
    pygame.display.update()

pygame.quit()
