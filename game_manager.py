import pygame

class GameManager:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1.0)

        self.score = 0
        self.state = "Ongoing"   # "Ongoing", "Won", "Lost"
        self.font = pygame.font.SysFont('Roboto', 100)
        self.enemy_killed = 0
        self.start_time = pygame.time.get_ticks()
        self.score = None
        self.provisional_score = 0

        self.die_sound = pygame.mixer.Sound("die_sound_effect.mp3")
        self.kill_sound = pygame.mixer.Sound("kill_sound_effect.mp3")

    def update(self, player, enemies, keys, window):  # enemies in list
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
                if self.enemy_killed >= (self.enemycount):
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




