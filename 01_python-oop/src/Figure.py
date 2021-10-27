class Figure:

    def __init__(self, side, name=None):
        if self.__class__ == Figure:
            raise Exception('Cannot instantiate abstract base class')
        self.name = name
        self.side = side

    @property
    def perimeter(self) -> int: pass

    @property
    def area(self) -> int: pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError('Receive an incorrect class')
        return self.area + figure.area
