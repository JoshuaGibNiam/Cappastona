import pygame
import time
from constants import *
import random
from powerups import *

class GameManager:
    def __init__(self):
        self.powerups = []

        self.constants = Constants()

        self.volume = 1.0
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.load("Music/Woody Path.mp3")
        pygame.mixer.music.play(-1)

        self.score = 0
        self.state = "Ongoing"   # "Ongoing", "Won", "Lost"
        self.font = pygame.font.SysFont('Roboto', 100)
        self.enemy_killed = 0
        self.start_time = pygame.time.get_ticks()
        self.score = None
        self.provisional_score = 0

        self.die_sound = pygame.mixer.Sound("Music/die_sound_effect.mp3")
        self.kill_sound = pygame.mixer.Sound("Music/kill_sound_effect.mp3")
        self.die_sound.set_volume(self.volume)
        self.kill_sound.set_volume(self.volume)

    def set_volume(self, volume):
        self.volume = volume
        pygame.mixer.music.set_volume(self.volume)
        self.die_sound.set_volume(self.volume)
        self.kill_sound.set_volume(self.volume)

    def update(self, player, enemies, keys, window, portal, walls):  # enemies in list

        self.portal = portal
        self.player = player
        self.enemies = enemies
        self.keys = keys
        self.enemycount = len(self.enemies)
        self.window = window

        # show score while game is running
        if self.score is None:
            self.current_time = pygame.time.get_ticks()
            self.provisional_score = int((120000 - (self.current_time - self.start_time)) / 120000 * 1000)   # map from (0, 120 000) to (0, 1000)
            if self.provisional_score <= 0:
                self.provisional_score = 0
            self.score_text = self.font.render(str(self.provisional_score), True, (0, 0, 255))
            self.window.blit(self.score_text, (0,0))

        for enemy in self.enemies:

            # if fov touching player
            if enemy.fov.rect.colliderect(player.rect):

                self.die_sound.play()
                self.player.image = self.player.image_types[1]
                self.state = "Lost"
                self.end_time = pygame.time.get_ticks()

                self.text_surface = self.font.render("You Lost! Press R to Restart", True, (100, 0, 0))
                window.blit(self.text_surface, (200, 300))
                self.player.speed = 0
                for _enemy in self.enemies:
                    _enemy.speed = 0

            elif player.rect.colliderect(enemy.rect):
                self.kill_sound.play()
                enemy.rect.topleft = (-10000, -10000)
                enemy.speed = 0

                self.enemy_killed += 1
            if self.enemy_killed >= (self.enemycount) and self.portal.rect.colliderect(self.player.rect):
                self.win()

        if self.state == "Lost":
            self.text_surface = self.font.render("You Lost! Press R to Restart", True, (100, 0, 0))
            self.window.blit(self.text_surface, (200, 300))

        elif self.state == "Won":
            if self.score is None:
                self.end_time = pygame.time.get_ticks()
                self.score = int((120000 - (self.end_time - self.start_time)) / 120000 * 1000)
                if self.score <= 0:
                    self.score = 0
            print(self.score)
            self.text_surface1 = self.font.render("You Won! Press R to Restart, "
                                                 "or N to continue.",
                                                 True, (0, 255, 0))
            self.window.blit(self.text_surface1, (50, 300))
            self.text_surface2 = self.font.render(f"to the next level. Score: {self.score}", True, (0, 255, 0))
            self.window.blit(self.text_surface2, (50, 400))





        if self.keys[pygame.K_r] and (self.state == "Won" or self.state == "Lost"):
            self.state = "Ongoing"
            self.score = None
            self.provisional_score = 0
            self.start_time = pygame.time.get_ticks()
            self.enemy_killed = 0
            self.player.reset()
            for enemy in enemies:
                enemy.reset()

        # manage powerups to make them spawn randomly at a .2%percent change every frame

        random_num = random.randint(1, 1000)
        if random_num in [1, 2]:
            self.powerups.append(SpeedUp(random.randint(0, self.constants.WINDOW_WIDTH),
                                         random.randint(0, self.constants.WINDOW_HEIGHT)))
            while True:
                powerup = self.powerups[-1]
                if not any(powerup.rect.colliderect(wall.rect) for wall in walls):
                    break
                powerup.teleport(random.randint(0, self.constants.WINDOW_WIDTH),
                                 random.randint(0, self.constants.WINDOW_HEIGHT))

        for powerup in self.powerups[:]:
            if powerup.rect.colliderect(self.player.rect) and self.player.speed_boost_end_time <= 0:
                self.player.speed += 2
                self.player.speed_boost_end_time = time.time() + 5
                self.player.image = self.player.image_types[2]  # change player image to sped up
                powerup.teleport(10000, 10000)
                self.powerups.remove(powerup)

            self.window.blit(powerup.image, powerup.rect)

        if self.player.speed_boost_end_time > 0 and time.time() > self.player.speed_boost_end_time:
            self.player.speed_boost_end_time = 0
            self.player.speed -= 2

            self.player.image = self.player.image_types[0]





    def win(self):
        self.state = "Won"
        #self.text_surface = self.font.render("You Won! Press R to Restart, or N to continue to the next level", True,
        #                                     (0, 0, 0))
        #self.text_rect = self.text_surface.get_rect()
        #self.text_image = pygame.draw.rect(self.window, (255, 255, 255), self.text_rect)
        # window.blit(self.text_image, (200, 300))
        #self.window.blit(self.text_surface, self.text_image)
        self.player.speed = 0
        for x in self.enemies:
            x.speed = 0  # stop all enemies




