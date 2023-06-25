class Settings():
    """класс для хранения всех настроек игры"""

    def __init__(self) -> None:
        """инициализация настроек игры"""
        # параметры экрана
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (20, 20, 20)

        # настройки корабля
        self.ship_speed = 1

        # параметры снаряда
        self.bullet_speed = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 240, 245)
        self.bullets_allowed = 6
        