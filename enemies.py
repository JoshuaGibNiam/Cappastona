import pygame

class enemy_1(pygame.sprite.Sprite):
    def __init__(self, xy, angle=90):
        pygame.sprite.Sprite.__init__(self)
        self.xy = xy

        self.image = pygame.Surface([50, 50], pygame.SRCALPHA)
        self.image.fill((100, 0, 0, 128))
        self.rect = self.image.get_rect()
        self.rect.topleft = (xy[0], xy[1])

        self.original_image = self.image.copy()

        self.fov = enemy_1_fov(self)

        self.speed = 3
        self.target_index = 0
        self.list_direction = 1

        self.orig_angle = angle
        self.angle = angle  #facing right at first
        self.rotation_rate = 10

        self.pos = pygame.math.Vector2(self.rect.topleft)

        self.attack_rate = 1.4

    def rotate_and_check(self, angle, tx):
        print(f"rotate_and_check function called, x = {self.rect.x}")
        check = self.rotate_toward(angle, tx)
        if check:
            print(f"reached!, angle {self.angle}")

        print(f"check = {check}, x = {self.rect.x}")
        return bool(check)

    def update(self, path):
        """moves in a set list of target points in path
                    path is in [[(x, y), bool], ....] format, where (x, y) is target and bool
                    is the direction to turn (True = move horizontally first, vice versa)"""
        print(f"Enemy at {self.rect.topleft}, target {path[self.target_index][0]}")
        self.path = path
        self.check = 0
        self.move_direction = None



        tx, ty = path[self.target_index][0]  # target index
        self.direction = path[self.target_index][1]

        if self.direction:  # move horizontally first
            if self.rect.x != tx:
                if self.rect.x > tx:
                    self.rect.x -= min(self.speed, self.rect.x - tx)
                    self.move_direction = "left"
                elif self.rect.x < tx:
                    self.rect.x += min(self.speed, tx - self.rect.x)
                    self.move_direction = "right"

            if self.rect.x == tx:
                if self.rect.y > ty:
                    self.target_angle = 180
                    self.check = self.rotate_toward(self.target_angle)
                else:
                    self.target_angle = 0
                    self.check = self.rotate_toward(self.target_angle)

            if self.rect.y != ty:  # only move y after x is aligned
                if self.check == 1:
                    if self.rect.y > ty:
                        self.rect.y -= min(self.speed, self.rect.y - ty)
                    elif self.rect.y < ty:
                        self.rect.y += min(self.speed, ty - self.rect.y)

        else:  # move vertically first
            if self.rect.y != ty:
                if self.rect.y > ty:
                    self.rect.y -= min(self.speed, self.rect.y - ty)
                    self.move_direction = "up"
                elif self.rect.y < ty:
                    self.rect.y += min(self.speed, ty - self.rect.y)
                    self.move_direction = "down"

            if self.rect.y == ty:
                if self.rect.x > tx:
                    self.target_angle = 270
                    self.check = self.rotate_toward(self.target_angle)
                else:
                    self.target_angle = 90
                    self.check = self.rotate_toward(self.target_angle)

            if self.rect.x != tx:  # only move x after y is aligned
                if self.check == 1:
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

        self.fov.update(self.angle + 90)

    def rotate_toward(self, target_angle):
        self.angle %= 360
        target_angle %= 360

        diff = (target_angle - self.angle + 540) % 360 - 180  # range: [-180, 180]

        if abs(diff) < self.rotation_rate:
            self.angle = target_angle
            aligned = True
        else:
            self.angle += self.rotation_rate * (1 if diff > 0 else -1)
            aligned = False

        self.image = pygame.transform.rotozoom(self.original_image, self.angle - self.orig_angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

        return int(aligned)

    def __repr__(self):
        return f"enemy_1({self.xy}, {self.orig_angle})"

    def __str__(self):
        return f"enemy_1 obj, {self.xy}, {self.orig_angle}"

    def getxy(self):
        return (self.rect.x, self.rect.y)

    def reset(self):
        self.rect.topleft = self.xy
        self.pos = pygame.math.Vector2(self.xy)

        self.angle = self.orig_angle
        self.image = pygame.Surface([50, 50], pygame.SRCALPHA)
        self.image.fill((100, 0, 0, 128))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.xy[0], self.xy[1])
        self.speed = 3

        self.target_index = 0
        self.list_direction = 1
        self.fov.reset()

        self.direction = self.path[self.target_index][1]
        self.check = 0
        self.move_direction = None




class enemy_1_fov(pygame.sprite.Sprite):
    def __init__(self, parent):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([100, 50], pygame.SRCALPHA)
        pygame.draw.polygon(self.image, (255, 0, 0, 200), [(0, 0), (0, 50), (100, 25)])  #0, 0    0, 50   100, 25

        self.orig_image = self.image.copy()

        self.rect = self.image.get_rect()
        self.parent = parent
        self.offset = pygame.math.Vector2(-75, 0)  # Offset to the right of the enemy
        self.pivot = self.parent.rect.center

        self.rotation_rate = 10

        self.orig_angle = 90
        self.angle = 90

    def update(self, angle):
        self.angle = angle


        self.pivot = self.parent.rect.center


        rotated_offset = self.offset.rotate(-self.angle)


        image_center = (self.pivot[0] + rotated_offset.x, self.pivot[1] + rotated_offset.y)

        # Rotate image and reposition it to match rotated offset
        self.image = pygame.transform.rotozoom(self.orig_image, self.angle, 1)
        self.rect = self.image.get_rect(center=image_center)

    def __repr__(self):
        return f"enemy_1_fov({str(self.parent)})"

    def getxy(self) -> tuple:
        return (self.rect.x, self.rect.y)

    def reset(self):
        self.angle = self.orig_angle
        self.pivot = self.parent.rect.center

        rotated_offset = self.offset.rotate(-self.angle)
        image_center = (self.pivot[0] + rotated_offset.x, self.pivot[1] + rotated_offset.y)

        self.image = pygame.transform.rotozoom(self.orig_image, self.angle, 1)
        self.rect = self.image.get_rect(center=image_center)




