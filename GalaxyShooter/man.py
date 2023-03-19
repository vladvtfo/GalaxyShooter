import pygame

class Man():
    
    def __init__(self, screen):
        #инициализация объекта
        self.screen = screen
        self.image = pygame.image.load('GalaxyShooter/GalaxyShooter/image/cosmo_ship2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # стартовая позиция объекта
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #переменные движения
        self.mright = False
        self.mLeft = False
        # self.mUp = False
        # self.mDown = False
        #переменная перемещения
        self.rightAndLeft = float(self.rect.centerx)

# Движение вверх вниз для 'man'  (расскоментировать при желании добавить)  
        # self.upAndDown = float(self.rect.centery)


    def output(self):
        # рисование объекта (человека)
        self.screen.blit(self.image, self.rect)

    def update_man(self):
        #подключили переменные с типом float под ось x,y
        self.rect.centerx = self.rightAndLeft

# Движение вверх вниз для 'man'  (расскоментировать при желании добавить)  
        # self.rect.centery = self.upAndDown
        

        #обновление позиции
        if self.mright and self.rect.right < self.screen_rect.right:
            self.rightAndLeft += 1.2

        if self.mLeft and self.rect.left > 0:
            self.rightAndLeft -= 1.2
            
# Движение вверх вниз для 'man'  (расскоментировать при желании добавить)  

        # if self.mUp and self.rect.top > self.screen_rect.top:
        #     self.upAndDown -= 1.5
            

        # if self.mDown and self.rect.bottom < self.screen_rect.bottom:
        #     self.upAndDown += 1.5

    def create_man(self):
        self.centerx = self.screen_rect.centerx

