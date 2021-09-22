import pygame

from nlc_dino_runner.Componentes.lives_player.lives_manager import LivesManager
from nlc_dino_runner.Componentes.dinosaur import Dinosaur
from nlc_dino_runner.Componentes.powerups.power_up_manager import PowerUpManager
from nlc_dino_runner.utils import text_utils
from nlc_dino_runner.Componentes.Obstacles.obstaclesManager import ObstaclesManager
from nlc_dino_runner.utils.constants import TITLE, SCREEN_HEIGHT, SCREEN_WIDTH, ICON, BG, FPS, ICON_MENU


class Game:
    def __init__(self):
        pygame.init()                                      # Inicializa todos los módulos importados de Pygame (Hábilita los módulos)
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.playing = False                               # Significa que no estamos jugando
        self.x_pos_bg = 0
        self.y_pos_bg = 360
        self.game_speed = 15
        self.player = Dinosaur()                           # Instanciando player
        self.obstacle_manager = ObstaclesManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.running = True
        self.death_count = 0
        self.manager_lives = LivesManager()

    def run(self):                                         # Punto de entrada del juego
        self.manager_lives.restart_lives()
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups(self.points)            # reset de power ups
        self.points = 0
        self.playing = True
        while self.playing: # 3 Segundos FPS
            self.events()
            self.update()
            self.draw()
        # pygame.quit()

    def events(self):                                        # Solo se encarga de actualizar los eventos, no la pantalla
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()                # Nos devuelve todo el teclado
        self.player.update(user_input)
        self.obstacle_manager.update(self)                   # Estamos pasando el mismo game o juego
        self.power_up_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score()
        self.power_up_manager.draw(self.screen)
        self.manager_lives.print(self.screen)

        pygame.display.update()                              # Actualiza por partes de la pantalla
        pygame.display.flip()                                # Actualizar pantalla completa

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        # text, text_rect = (score_element, score_element_rect) por el return de get_score_element()
        score_element, score_element_rect = text_utils.get_score_element(self.points)
        self.screen.blit(score_element, score_element_rect)
        self.player.check_invincibility(self.screen)

    def draw_background(self):
        image_width = BG.get_width() #2404

        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))                #pos_x se va reasignando
        self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
        self.x_pos_bg -= self.game_speed

        if self.x_pos_bg <= -image_width:
            self.x_pos_bg = 0

    def execute(self):
        while self.running:     # Saber si el juego esta ejecutandose
            if not self.playing:  # Saber si todavía se esta jugando con el dionosaurio
                self.show_menu()

    def show_menu(self):
        self.running = True

        white_color = (255, 255, 255)
        self.screen.fill(white_color)

        # Luego mostrar el menú
        self.print_menu_elements()
        pygame.display.update()
        pygame.display.flip()
        self.handle_key_events_on_menu()

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                self.run()

    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT // 2 + 60

        # text, text_rect adquieren los valores de retorno de get_centered_message()
        self.screen.blit(ICON_MENU, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 150))

        death_score, death_score_rect = text_utils.get_centered_message("Death count: " + str(self.death_count), height= half_screen_height)
        self.screen.blit(death_score, death_score_rect)

        if self.death_count == 0:
            text, text_rect = text_utils.get_centered_message("Press any key to Start Game")
            self.screen.blit(text, text_rect)
        else:
            text, text_rect = text_utils.get_centered_message("Press any key to Restart Game")
            self.screen.blit(text, text_rect)


















