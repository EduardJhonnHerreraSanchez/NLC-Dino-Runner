from nlc_dino_runner.Componentes.powerups.powerup import PowerUp
from nlc_dino_runner.utils.constants import HAMMER, HAMMER_TYPE


class HammerManager(PowerUp):

    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type)