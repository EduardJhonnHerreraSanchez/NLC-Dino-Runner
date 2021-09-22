import pygame.time

from nlc_dino_runner.Componentes.Obstacles.cactus import Cactus
from nlc_dino_runner.utils.constants import ALL_CACTUS


class ObstaclesManager:
    def __init__(self):
        self.obstacles_list = []

    def update(self, game):
        if len(self.obstacles_list) == 0:
            self.obstacles_list.append(Cactus(ALL_CACTUS))

        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list)
            if game.player.dino_rect.colliderect(obstacle.rect): # Se cumple, hasta que me devuelva un True
                if game.player.shield:
                    self.obstacles_list.remove(obstacle)
                else:
                    pygame.time.delay(1000)
                    game.playing = False
                    game.death_count += 1
                    break # Rompemos el ciclo

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list = []
