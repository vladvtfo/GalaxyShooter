import pygame

class Background():
    def __init__(self, screen):
        #инициализация фона
        self.screen = screen
        self.image = pygame.image.load('python_game/image/background.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx

    
    def output(self):
        #рисовка фона
        self.screen.blit(self.image, self.rect)

