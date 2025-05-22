import pygame

pygame.init()

class GameManager:
    def __init__(self):

        self.score = 0
        self.state = "Ongoing"   # "Ongoing", "Won", "Lost"
        self.font = pygame.font.SysFont('Arial', 50)


    def update(self, player, enemies, keys, window):  # enemies in list
        self.player = player
        self.enemies = enemies
        self.keys = keys



        for enemy in self.enemies:

            # if fov touching player
            if enemy.fov.rect.colliderect(player.rect):
                self.state = "Lost"
                self.text_surface = self.font.render("You Lost! Press R to Restart", True, (0, 0, 0))
                window.blit(self.text_surface, (400, 300))
                self.player.velocity = 0
                enemy.speed = 0

            elif player.rect.colliderect(enemy.rect):
                self.state = "won"
                self.text_surface = self.font.render("You Won! Press R to Restart, or N to continue to the next level", True, (0, 0, 0))
                window.blit(self.text_surface, (400, 300))
                self.player.velocity = 0
                for x in enemies:
                    x.speed = 0   # stop all enemies

        if self.keys[pygame.K_r]:
            self.state = "Ongoing"
            self.player.rect.topleft = (750, 0)
            for enemy in enemies:
                enemy.rect.topleft = (100, 535)
                enemy.speed = 3
            self.player.velocity = 5




