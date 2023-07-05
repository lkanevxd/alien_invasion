import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """класс для представления одного пришельца"""

    def __init__(self, ai_game) -> None:
        """инициализация пришельца и задание начальной позиции"""
        super().__init__()
        self.screen = ai_game.screen

        # загрузка изображения пришельца и назначение атрибута rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # появление нового пришельца в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение горизонтальной позиции пришельца
        self.x = float(self.rect.x)
