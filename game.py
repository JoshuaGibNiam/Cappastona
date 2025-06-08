import pygame
from pygame import key
from player import *
from walls import Wall
from enemies import *
from game_manager import GameManager
from constants import Constants
import pygame
from pygame import key
import json
import sys
from portal import *

class CappastonaGame:
    def __init__(self, user, level=1):
        self.user = user
        self.C = Constants()
        self.level = level
        self.C.set_level(self.level)

        # Initialize sprites
        self.player = Player(self.C.PLAYER["spawn point"])  # top left corner

        self.portal = Portal(self.C.PORTAL)

        self.walls = {}  # dict of wall sprites
        for index, wall in enumerate(self.C.WALLS.values()):
            self.walls[index] = eval(wall)

        self.enemies = {}
        for index, enemy in enumerate(self.C.ENEMIES.values()):
            self.enemies[index] = enemy_1(self.C.ENEMIES[f"enemy{index+1}"]["spawn point"])

        self.game_manager = GameManager()

        self.healthbar = PlayerHealthBar()
        self.health_bar_padding = Pad()

        self.sprites = [self.portal] + [self.player] + list(self.walls.values()) + list(self.enemies.values()) + [self.healthbar]
        self.wall_list = list(self.walls.values())


        # settings
        pygame.init()
        self.window = pygame.display.set_mode((self.C.WINDOW_WIDTH, self.C.WINDOW_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption(self.C.WINDOW_CAPTION)

        self.clock = pygame.time.Clock()
        self.run = True

    def run_game(self):
        while self.run:
            delta_time = self.clock.get_time() / 1000
            keys = key.get_pressed()
            self.clock.tick(self.C.FPS)  # 60 fps
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    self.hard_quit()

            self.player.update(keys, self.wall_list, delta_time)
            for index, value in self.enemies.items():
                value.update(self.C.ENEMIES[f"enemy{index+1}"]["path"])

            # Clearing
            self.window.fill((255, 255, 255))


            for sprite in self.sprites:
                self.window.blit(sprite.image, sprite.rect)
                if isinstance(sprite, enemy_1):
                    self.window.blit(sprite.fov.image, sprite.fov.rect)


            self.game_manager.update(self.player, list(self.enemies.values()),
                                     keys, self.window, self.portal, self.wall_list, self.healthbar)
            pygame.display.update()

            # check if player has won and wants to go to the next level
            if self.game_manager.state == "Won" and keys[pygame.K_n]:
                with open("jsonfiles/accounts.json", "r") as f:
                    accounts = json.load(f)
                accounts[self.user]["level"] += 1
                with open("jsonfiles/accounts.json", "w") as f:
                    json.dump(accounts, f, indent=4)

                break

        pygame.quit()
        sys.exit()

    def hard_quit(self):
        self.run = False
        pygame.quit()
        sys.exit()

    def set_fps(self, fps: int):
        self.C.FPS = fps

    def set_volume(self, volume: float):  # 1.00-0

        self.game_manager.set_volume(volume)


