import random

from nlc_dino_runner.Componentes.Obstacles.obstacles import Obstacles
from nlc_dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
# Clase Hija, hereda de Obstacles


class Cactus(Obstacles):

    def __init__(self, image):
        self.type = random.randint(0, 5)
        super().__init__(image, self.type)
        self.rect.y = 315
