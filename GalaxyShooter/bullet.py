import pygame


class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, screen, man):
        #создаем пулю
        super(Bullet, self).__init__()

        self.screen = screen
        self.rect = pygame.Rect(0, 0, 4, 20)
        self.color = 'red'
        self.speed = 4
        self.rect.centerx = man.rect.centerx
        self.rect.center = man.rect.center

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        #перемещение пули вверх
        self.y -=self.speed
        self.rect.y = self.y
        # #перемещине пули вправо влево test
        # self.x += self.speed
        # self.rect.x = self.x


    def draw_bullet(self):
        #рисуем пулю
        pygame.draw.rect(self.screen, self.color, self.rect)