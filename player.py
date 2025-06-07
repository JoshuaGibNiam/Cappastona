import pygame
from constants import Constants
C = Constants()

## Player Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, xy):
        super().__init__()

        self.unscaled_image_normal = pygame.image.load("player_normal.png")
        self.unscaled_image_killed = pygame.image.load("player_killed.png")
        self.image_types = [pygame.transform.scale(self.unscaled_image_normal, (50, 50)), pygame.transform.scale(self.unscaled_image_killed, (50, 50))]
        self.image = self.image_types[0] # normal
        self.image.fill((0, 0, 0))  ## Color black

        self.rect = self.image.get_rect()
        self.rect.topleft = (xy[0], xy[1])
        self.starting_pos = self.rect.topleft

        self.speed = 5

    def update(self, keys, sprites, delta_time):
        ## keybind movement plus wall constraints
        speed = self.speed * delta_time
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            #collision
            for sprite in sprites:
                if self.rect.colliderect(sprite):
                    self.rect.top = sprite.rect.bottom
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            for sprite in sprites:
                if self.rect.colliderect(sprite):
                    self.rect.bottom = sprite.rect.top
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            for sprite in sprites:
                if self.rect.colliderect(sprite):
                    self.rect.left = sprite.rect.right
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            for sprite in sprites:
                if self.rect.colliderect(sprite):
                    self.rect.right = sprite.rect.left

        ## world border constraints
        if self.rect.x >= C.WINDOW_WIDTH - self.rect.width:
            self.rect.x = C.WINDOW_WIDTH - self.rect.width
        elif self.rect.x <= 0:
            self.rect.x = 0

        if self.rect.y >= C.WINDOW_HEIGHT - self.rect.height:
            self.rect.y = C.WINDOW_HEIGHT - self.rect.height
        elif self.rect.y <= 0:
            self.rect.y = 0

    def reset(self):
        self.rect.topleft = (self.starting_pos[0], self.starting_pos[1])
        self.speed = 5

        self.image = self.image_types[0]






