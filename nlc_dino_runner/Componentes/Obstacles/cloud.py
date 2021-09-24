from pygame.sprite import Sprite

from nlc_dino_runner.utils.constants import CLOUD, SCREEN_WIDTH


class Cloud(Sprite):

    def __init__(self):
        self.image = CLOUD
        self.rect_cloud = self.image.get_rect()
        self.rect_cloud.x = SCREEN_WIDTH - 100
        self.rect_cloud.y = 150

    def draw(self, screen, amount = 5):
        self.update()
        for i in range(amount):
            screen.blit(self.image, self.rect_cloud)
            screen.blit(self.image, (self.rect_cloud.x + 600, self.rect_cloud.y - 200))
            screen.blit(self.image, (self.rect_cloud.x + 1200, self.rect_cloud.y - 150))
            screen.blit(self.image, (self.rect_cloud.x + 1500, self.rect_cloud.y - 250))

    def update(self):
        self.rect_cloud.x -= 10
        if self.rect_cloud.x <= -SCREEN_WIDTH:
            self.rect_cloud.x = SCREEN_WIDTH


