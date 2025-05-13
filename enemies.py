import pygame

class enemy_1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([50, 50])
        self.image.fill((100, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.fov = enemy_1_fov(self)

        self.speed = 3
        self.target_index = 0
        self.list_direction = 1

        self.angle = 0

    def update(self, path):
        """moves in a set list of target points in path
            path is in [[(x, y), bool], ....] format, where (x, y) is target and bool
            is the direction to turn (True = move horizontally first, vice versa)"""

        tx, ty = path[self.target_index][0]  #target index
        direction = path[self.target_index][1]

        if direction:  # move horizontally first
            if self.rect.x != tx:
                if self.rect.x > tx:
                    self.rect.x -= min(self.speed, self.rect.x - tx)
                elif self.rect.x < tx:
                    self.rect.x += min(self.speed, tx - self.rect.x)
            elif self.rect.y != ty:  # only move y after x is aligned
                if self.rect.y > ty:
                    self.rect.y -= min(self.speed, self.rect.y - ty)
                elif self.rect.y < ty:
                    self.rect.y += min(self.speed, ty - self.rect.y)

        elif not direction:  # move vertically first
            if self.rect.y != ty:
                if self.rect.y > ty:
                    self.rect.y -= min(self.speed, self.rect.y - ty)
                elif self.rect.y < ty:
                    self.rect.y += min(self.speed, ty - self.rect.y)

            elif self.rect.x != tx:  # only move x after y is aligned
                if self.rect.x > tx:
                    self.rect.x -= min(self.speed, self.rect.x - tx)
                elif self.rect.x < tx:
                    self.rect.x += min(self.speed, tx - self.rect.x)

        if self.rect.y == ty and self.rect.x == tx:
            self.target_index += self.list_direction

            if self.target_index >= len(path):
                self.target_index = len(path) - 2
                self.list_direction = -1

            elif self.target_index < 0:
                self.target_index = 1
                self.list_direction = 1

        self.fov.update()

class enemy_1_fov(pygame.sprite.Sprite):
    def __init__(self, parent):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([100, 50], pygame.SRCALPHA)  # Increase width for a wider FOV
        pygame.draw.polygon(self.image, (255, 0, 0, 200), [(100, 0), (0, 25), (100, 50)])
        self.rect = self.image.get_rect()
        self.parent = parent
        self.offset = pygame.math.Vector2(50, 0)  # Offset to the right of the enemy

    def update(self):
        self.rect.topleft = self.parent.rect.topleft + self.offset






