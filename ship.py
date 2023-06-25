import pygame

class Ship():
    """класс для настроек управления корбалем"""

    def __init__(self, ai_game) -> None:
        """инициализация корабля и задание"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # появление каждого нового корабля у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # сохранение вещественной координаты центра корабля
        self.x = float(self.rect.x)

        # флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """обновление позиции корабля с учетом флагов"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
          
        # обновление атрибута rect
        self.rect.x = self.x

    def blitme(self):
        """отрисовка корабля в текущей позиции"""
        self.screen.blit(self.image, self.rect)
        