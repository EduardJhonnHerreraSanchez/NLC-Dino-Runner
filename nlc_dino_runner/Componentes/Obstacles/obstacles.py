from pygame.sprite import Sprite

from nlc_dino_runner.utils.constants import SCREEN_WIDTH


class Obstacles(Sprite):

    # type hace referencia a la abstracción como small_cactus y large_cactus
    def __init__(self, image, obstacle_type):
        self.image = image
        self.obstacle_type = obstacle_type # 0,1,2,3,4,5
        self.rect = self.image[self.obstacle_type].get_rect() # returna una tupla (x,y) | [self.obs..] = [0,1,2,3,4,5]
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacle_list):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacle_list.pop()

    def draw(self, screen):
        screen.blit(self.image[self.obstacle_type], self.rect)
