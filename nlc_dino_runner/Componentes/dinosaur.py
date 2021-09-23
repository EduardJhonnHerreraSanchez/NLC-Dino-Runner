import pygame

from pygame.sprite import Sprite
from nlc_dino_runner.utils.text_utils import get_centered_message
from nlc_dino_runner.utils.constants import (
    RUNNING,
    DUCKING,
    JUMPING,
    RUNNING_SHIELD,
    JUMPING_SHIELD,
    DEFAULT_TYPE,
    SHIELD_TYPE,
    DUCKING_SHIELD,
    RUNNING_HAMMER,
    DUCKING_HAMMER,
    JUMPING_HAMMER,
    HAMMER_TYPE,
    HAMMER, SCREEN_WIDTH
)


class Dinosaur(Sprite):

    # Constants
    X_POS = 75
    Y_POS = 295
    Y_POS_DUCK = 335
    JUMP_VEL = 20

    def __init__(self):
        self.run_img = {
            DEFAULT_TYPE: RUNNING,
            SHIELD_TYPE: RUNNING_SHIELD,
            HAMMER_TYPE: RUNNING_HAMMER,
        }
        self.jump_img = {
            DEFAULT_TYPE: JUMPING,
            SHIELD_TYPE: JUMPING_SHIELD,
            HAMMER_TYPE: JUMPING_HAMMER,
        }
        self.duck_img = {
            DEFAULT_TYPE: DUCKING,
            SHIELD_TYPE: DUCKING_SHIELD,
            HAMMER_TYPE: DUCKING_HAMMER,
        }
        self.type = DEFAULT_TYPE
        self.image = self.run_img[self.type][0]       # before RUNNING[0]
        self.dino_rect = self.image.get_rect()        # Nos devuelve el area rectangular del objeto
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0

        # Powers
        # ==== Shield ====
        self.shield_time_up = 0                       # El tiempo limite de shield
        self.shield = False
        # ==== Hammer ====
        self.hammer_rect = HAMMER.get_rect()
        self.hammer_rect.x = self.dino_rect.x + 60
        self.hammer_rect.y = 0
        self.hammer_time_up = 0
        self.hammer = False

        # ==== Others ====
        self.show_text = False
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL

    def update(self, user_input):

        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()

        if user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False
        elif user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_duck = False
            self.dino_run = False
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

        if self.step_index >= 20:
            self.step_index = 0

    def run(self):
        self.image = self.run_img[self.type][self.step_index // 10]          # before: RUNNING[0] if self.step_index <= 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()                              # Nos devuelve el area rectangular del objeto
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1
        # print(self.type)

    def duck(self):
        self.image = self.duck_img[self.type][self.step_index // 10]
        # self.image = DUCKING[0] if self.step_index <= 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()  # Nos devuelve el area rectangular del objeto
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1
        # print(self.type)

    def jump(self):
        self.image = self.jump_img[self.type]
        self.image = JUMPING

        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel
            self.jump_vel -= 1                          # Restar la velocidad del salto

        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.jump_vel = self.JUMP_VEL
            self.dino_jump = False
        # print(self.type)

    def check_invincibility(self, screen):
        if self.shield:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks())/1000, 1) # Obtiene el tiempo actual en miliseg
            if time_to_show < 0:
                self.shield = False
                if self.type == SHIELD_TYPE:
                    self.type = DEFAULT_TYPE
            else:
                # print(self.type)
                if self.show_text:
                    text, text_rect = get_centered_message(
                        f"Shield enable: {time_to_show}",
                        width=500,
                        height=40,
                        size=20
                    )
                    screen.blit(text, text_rect)

    def check_throw_hammer(self, screen, user_input):
        if self.hammer:
            time_to_show = round((self.hammer_time_up - pygame.time.get_ticks())/1000,1)
            if time_to_show < 0:
                self.hammer = False
                if self.type == HAMMER_TYPE:
                    self.type = DEFAULT_TYPE
            else:
                self.type = DEFAULT_TYPE
                screen.blit(HAMMER, (self.dino_rect.x+60, self.dino_rect.y + 5))

                if user_input[pygame.K_SPACE]:
                    self.hammer_rect.y = self.dino_rect.y
                    self.hammer_rect.x += 10
                    screen.blit(HAMMER, self.hammer_rect)
                    if self.hammer_rect.x >= SCREEN_WIDTH:
                        self.hammer_rect.x = self.dino_rect.x + 60

            if self.show_text:
                text, text_rect = get_centered_message(
                    f"Hammer enable: {time_to_show}",
                    width=500,
                    height=40,
                    size=20
                )
                screen.blit(text, text_rect)

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

