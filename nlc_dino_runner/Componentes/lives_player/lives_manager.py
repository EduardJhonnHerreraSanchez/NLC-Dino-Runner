from nlc_dino_runner.Componentes import game
from nlc_dino_runner.Componentes.lives_player.live import Live
from nlc_dino_runner.utils.constants import DEFAULT_NUMBER_OF_LIFE


class LivesManager:
    def __init__(self):
        self.number_of_lives = DEFAULT_NUMBER_OF_LIFE

    def reduce_lives(self):
        self.number_of_lives -= 1

    def restart_lives(self):
        self.number_of_lives = DEFAULT_NUMBER_OF_LIFE

    def print(self, screen):
        dinamic_pos_x = 60
        for i in range(self.number_of_lives):
            live = Live(dinamic_pos_x)
            live.draw(screen)
            dinamic_pos_x += 27
