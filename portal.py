import pygame


class Portal(pygame.sprite.Sprite):
    def __init__(self, xy):
        super().__init__()
        self.image = pygame.image.load("Images/portal.jpg")
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.topleft = xy[0], xy[1]
