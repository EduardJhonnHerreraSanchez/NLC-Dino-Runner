import random
import pygame

# from nlc_dino_runner.Components.power_ups.hammer import Hammer
from nlc_dino_runner.Componentes.powerups.shield import Shield
from nlc_dino_runner.Componentes.powerups.single_powers.hammer_manager import HammerManager
from nlc_dino_runner.utils.constants import HAMMER_TYPE, DEFAULT_TYPE, SHIELD_TYPE
from random import choice as ran


class PowerUpManager: # REVISAR
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.points = 0
        self.option_numbers = list(range(1, 10))

    def reset_power_ups(self, points):
        self.power_ups = []
        self.points = points
        self.when_appears = random.randint(200, 300) + self.points

    def generate_power_ups(self, points):
        self.points = points
        if len(self.power_ups) == 0:
            if self.when_appears == self.points:
                print("generating power up")
                self.when_appears = random.randint(self.when_appears + 200, self.when_appears + 500) # 200,500
                # self.power_ups.append(HammerManager())  # la clase Shield() con sus métodos heredados de PowerUp
                self.power_ups.append(ran(
                    (Shield(),
                     HammerManager())
                ))
        return self.power_ups

    def update(self, points, game_speed, player):
        self.generate_power_ups(points)

        for power_up in self.power_ups: # Instaciamos power_up de lo que recibe de self.power_ups
            power_up.update(game_speed, self.power_ups)  # update de la class Padre (PowerUp)
            if player.dino_rect.colliderect(power_up.rect):
                if power_up.type == SHIELD_TYPE:
                    player.shield = True
                    player.show_text = True
                    player.type = power_up.type
                    power_up.start_time = pygame.time.get_ticks()  # Tiempo de choque con escudo
                    time_random = random.randrange(5, 8)
                    player.shield_time_up = power_up.start_time + (time_random * 1000)
                    self.power_ups.remove(power_up)
                elif power_up.type == HAMMER_TYPE:
                    player.hammer = True
                    player.show_text = True
                    player.type = power_up.type
                    power_up.start_time = pygame.time.get_ticks()
                    time_random = random.randrange(5, 8)
                    player.hammer_time_up = power_up.start_time + (time_random * 1000)
                    self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

