from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b, name='Rectangle'):
        # Через super() обращаемся к конструктору Figure.
        super().__init__(a, name)
        self.a = a
        self.b = b

    @property
    def perimeter(self) -> int:
        return 2 * (self.a + self.b)

    @property
    def area(self) -> int:
        return self.a * self.b
