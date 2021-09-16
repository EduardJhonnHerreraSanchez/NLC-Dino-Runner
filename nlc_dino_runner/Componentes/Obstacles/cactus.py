import random

from nlc_dino_runner.Componentes.Obstacles.obstacles import Obstacles
from nlc_dino_runner.utils.constants import SMALL_CACTUS

# Clase hija que hereda

class Cactus(Obstacles):
    def __init__(self, image):
        self.type = random.randint(0, 5)
        super().__init__(image, self.type)
        self.rect.y = 310