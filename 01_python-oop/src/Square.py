from src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, a, name='Square'):
        # Через super() обращаемся к конструктору Rectangle.
        super().__init__(a, a, name)
