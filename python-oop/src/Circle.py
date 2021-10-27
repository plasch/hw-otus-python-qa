import math
from src.Figure import Figure


class Circle(Figure):

    def __init__(self, radius, name='Circle'):
        # Через super() обращаемся к конструктору Figure.
        super().__init__(radius, name)
        self.radius = radius

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    @property
    def area(self) -> int:
        return math.pi * self.radius ** 2
