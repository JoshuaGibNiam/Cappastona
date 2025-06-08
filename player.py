import pygame
from constants import Constants
C = Constants()

## Player Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, xy):
        super().__init__()

        self.unscaled_image_normal = pygame.image.load("Images/player_normal.png")
        self.unscaled_image_killed = pygame.image.load("Images/player_killed.png")
        self.unscaled_image_speedup = pygame.image.load("Images/player_speedup.png")
        self.unscaled_image_invincible = pygame.image.load("Images/player_invincible.png")
        self.image_types = [pygame.transform.scale(self.unscaled_image_normal, (50, 50)), pygame.transform.scale(self.unscaled_image_killed, (50, 50)),
                            pygame.transform.scale(self.unscaled_image_speedup, (50, 50)), pygame.transform.scale(self.unscaled_image_invincible, (50, 50))]
        self.image = self.image_types[0] # normal
        self.image.fill((0, 0, 0))  ## Color black

        self.rect = self.image.get_rect()
        self.rect.topleft = (xy[0], xy[1])
        self.starting_pos = self.rect.topleft
        self.speed = 5

        self.speed_boost_end_time = 0
        self.invincible_end_time = 0
        self.invincible = False

        self.health = 100

    def update(self, keys, sprites, delta_time):
        ## keybind movement plus wall constraints
        speed = self.speed * delta_time
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
            #collision
            for sprite in sprites:
                if self.rect.colliderect(sprite):
                    self.rect.top = sprite.rect.bottom
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
            for sprite in sprites:
                if self.rect.colliderect(sprite):
                    self.rect.bottom = sprite.rect.top
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            for sprite in sprites:
                if self.rect.colliderect(sprite):
                    self.rect.left = sprite.rect.right
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
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

        self.health = 0


class PlayerHealthBar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_length = 300
        self.image = pygame.Surface((self.x_length, 40), pygame.SRCALPHA)
        self.image.fill((255, 0, 0, 100))

        self.rect = self.image.get_rect()
        self.rect.topleft = (C.WINDOW_WIDTH - 200, C.WINDOW_HEIGHT - 60)

    def update(self, player_health):
        if player_health < 0:
            self.x_length = 0
        else:
            self.x_length = player_health * 3
        self.image = pygame.Surface((self.x_length, 40), pygame.SRCALPHA)
        self.image.fill((255, 0, 0, 100))

class Pad(pygame.sprite.Sprite):  # padding for the health bar
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((300, 40), pygame.SRCALPHA)
        self.image.fill((60, 60, 60, 100))

        self.rect = self.image.get_rect()
        self.rect.topleft = (C.WINDOW_WIDTH - 200, C.WINDOW_HEIGHT - 60)





