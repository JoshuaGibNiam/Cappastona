import pygame

## Player Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 0))  ## Color black

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = 5

    def update(self, keys, sprites):
        ## keybind movement plus wall constraints
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocity
            #collision
            for sprite in sprites:
                if self.rect.colliderect(sprite):
                    self.rect.top = sprite.rect.bottom
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocity
            for sprite in sprites:
                if self.rect.colliderect(sprite):
                    self.rect.bottom = sprite.rect.top
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
            for sprite in sprites:
                if self.rect.colliderect(sprite):
                    self.rect.left = sprite.rect.right
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
            for sprite in sprites:
                if self.rect.colliderect(sprite):
                    self.rect.right = sprite.rect.left

        ## world border constraints
        if self.rect.x >= 800 - self.rect.width:
            self.rect.x = 800 - self.rect.width
        elif self.rect.x <= 0:
            self.rect.x = 0

        if self.rect.y >= 600 - self.rect.height:
            self.rect.y = 600 - self.rect.height
        elif self.rect.y <= 0:
            self.rect.y = 0






