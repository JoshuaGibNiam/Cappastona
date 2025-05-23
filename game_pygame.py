import pygame
from pygame import key
from player import Player
from walls import Wall
from enemies import *
from game_manager import GameManager
from constants import Constants
import pygame
from pygame import key

class CappastonaGame:
    def __init__(self):
        self.C = Constants()
        self.C.set_level(1)

        # Initialize sprites
        self.player = Player(self.C.PLAYER["spawn point"])  # top left corner

        self.walls = {}  # dict of wall sprites
        for index, wall in enumerate(self.C.WALLS.values()):
            self.walls[index] = eval(wall)

        self.enemy1 = enemy_1(self.C.ENEMIES["enemy1"]["spawn point"], self.C.ENEMIES["enemy1"]["angle"])  # bottom left corner
        self.enemies = [self.enemy1]

        self.game_manager = GameManager()

        self.sprites = [self.player] + list(self.walls.values()) + [self.enemy1]
        self.wall_list = list(self.walls.values())

        # settings
        pygame.init()
        self.window = pygame.display.set_mode((self.C.WINDOW_HEIGHT, self.C.WINDOW_WIDTH))
        pygame.display.set_caption(self.C.WINDOW_CAPTION)

        self.clock = pygame.time.Clock()
        self.run = True

    def run_game(self):
        while self.run:
            keys = key.get_pressed()
            self.clock.tick(self.C.FPS)  # 60 fps
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            self.player.update(keys, self.wall_list)
            self.enemy1.update(self.C.ENEMIES["enemy1"]["path"])

            # Clearing
            self.window.fill((255, 255, 255))

            self.game_manager.update(self.player, self.enemies, keys, self.window)

            for sprite in self.sprites:
                self.window.blit(sprite.image, sprite.rect)
                if isinstance(sprite, enemy_1):
                    self.window.blit(sprite.fov.image, sprite.fov.rect)
            pygame.display.update()

        pygame.quit()