import random

import pygame
from pygame.sprite import Sprite

from nlc_dino_runner.Componentes import game
# from nlc_dino_runner.Components.game import Game
from nlc_dino_runner.Componentes.dinosaur import Dinosaur
from nlc_dino_runner.utils.constants import SCREEN_WIDTH, BIRD


class Bird(Sprite):

    Y_POS = Dinosaur.Y_POS - (Dinosaur.Y_POS_DUCK - Dinosaur.Y_POS)

    def __init__(self):
        self.bird0, self.bird1 = BIRD[0], BIRD[1]
        self.bird0_rect = self.bird0.get_rect()
        self.bird0_rect.x = SCREEN_WIDTH * 3
        self.bird0_rect.y = self.Y_POS
        self.image = self.bird0
        self.index = 0
        self.bird0_rect_collide = self.bird0_rect.center

    def update(self, game):
        self.fly()
        if self.index >= 20:
            self.index = 0

        # Colisión
        if game.player.dino_rect.collidepoint(self.bird0_rect.midbottom):  # Se cumple, hasta que me devuelva un True
            if game.player.shield:
                self.bird0_rect.x = - SCREEN_WIDTH
            elif game.manager_lives.number_of_lives == 1:
                pygame.time.delay(1000)
                game.playing = False
                game.death_count += 1
            else:
                game.manager_lives.reduce_lives()

        if game.player.hammer_rect.colliderect(self.bird0_rect):
            if game.player.hammer:
                self.bird0_rect.x = -SCREEN_WIDTH
            else:
                game.player.hammer = False

    def fly(self):  #update
        self.index += 1
        self.image = self.bird0 if self.index <= 10 else self.bird1
        self.bird0_rect.x -= 17
        if self.bird0_rect.x < -(SCREEN_WIDTH * 3):
            self.bird0_rect.x = SCREEN_WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.bird0_rect)

    def reset(self):
        self.bird0_rect.x = SCREEN_WIDTH * 3

    # def remove(self):
    #     self.bird0_rect.x = -SCREEN_WIDTH