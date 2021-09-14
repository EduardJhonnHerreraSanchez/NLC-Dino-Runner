import pygame

from nlc_dino_runner.Componentes.Obstacles.cactus import Cactus
from nlc_dino_runner.Componentes.Obstacles.obstaclesManager import ObstaclesManager
from nlc_dino_runner.Componentes.dinosaur import Dinosaur
from nlc_dino_runner.utils.constants import TITLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, BG, FPS, SMALL_CACTUS, LARGE_CACTUS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE, "Icono")
        pygame.display.set_icon(ICON)

        # Atributos
        self.screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.x_pos_bg = 0
        self.y_pos_bg = 360
        self.game_speed = 20
        self.player = Dinosaur()
        self.obstacle_manager = ObstaclesManager()
        # self.cactusSmall = Cactus(SMALL_CACTUS)
        # self.cactusLarge = Cactus(LARGE_CACTUS)

    def run(self):
        print("JUGAR")
        self.playing = True
        while self.playing:
            self.event()
            self.update()
            self.draw()
        pygame.quit()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed() #Este método nos devuelve todas las teclas
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)

        pygame.display.update()
        pygame.display.flip()  # Actualización de toda la ventana

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))

        # El fondo se va moviendo
        self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
            self.x_pos_bg = 0

        self.x_pos_bg -= self.game_speed

