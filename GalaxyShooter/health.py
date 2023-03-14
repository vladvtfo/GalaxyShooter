from pygame.sprite import Sprite
import pygame

class Health(Sprite):
    
    def __init__(self, screen):

        super(Health, self).__init__()
        #инициализация объекта
        self.screen = screen
        self.image = pygame.image.load('python_game/image/health.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()