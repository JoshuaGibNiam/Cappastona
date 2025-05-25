import pygame

class GameManager:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.score = 0
        self.state = "Ongoing"   # "Ongoing", "Won", "Lost"
        self.font = pygame.font.SysFont('Roboto', 50)
        self.enemy_killed = 0

    def update(self, player, enemies, keys, window):  # enemies in list
        self.player = player
        self.enemies = enemies
        self.keys = keys
        self.enemycount = len(self.enemies)
        self.window = window


        for enemy in self.enemies:

            # if fov touching player
            if enemy.fov.rect.colliderect(player.rect):
                self.state = "Lost"
                self.text_surface = self.font.render("You Lost! Press R to Restart", True, (0, 0, 0))
                window.blit(self.text_surface, (200, 300))
                self.player.speed = 0
                for _enemy in self.enemies:
                    _enemy.speed = 0

            elif player.rect.colliderect(enemy.rect):
                enemy.rect.topleft = (-10000, -10000)

                enemy.speed = 0

                self.enemy_killed += 1
                if self.enemy_killed >= (self.enemycount):
                    self.win()

        if self.state == "Lost":
            self.text_surface = self.font.render("You Lost! Press R to Restart", True, (0, 0, 0))
            self.window.blit(self.text_surface, (200, 300))

        elif self.state == "Won":
            self.text_surface = self.font.render("You Won! Press R to Restart, or N to continue to the next level",
                                                 True, (0, 0, 0))
            self.window.blit(self.text_surface, (50, 300))





        if self.keys[pygame.K_r] and (self.state == "Won" or self.state == "Lost"):
            self.state = "Ongoing"
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




