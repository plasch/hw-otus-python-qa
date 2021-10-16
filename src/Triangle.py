from src.Figure import Figure


class Triangle(Figure):
    # Если метод возвращает None, то __init__() не вызывается.
    def __new__(cls, *args):
        a, b, c = args
        if not (a + b > c and a + c > b and b + c > a):
            return None
        instance = super().__new__(cls)
        return instance

    def __init__(self, a, b, c, name='Triangle'):
        super().__init__(a, name)
        self.a = a
        self.b = b
        self.c = c

    @property
    def perimeter(self) -> int:
        return self.a + self.b + self.c

    @property
    def area(self) -> int:
        return self.area_formula(self.perimeter, self.a, self.b, self.c)

    @staticmethod
    def area_formula(p, a, b, c):
        p /= 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5
