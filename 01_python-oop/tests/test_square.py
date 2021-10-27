from src.Square import Square


class TestSquare:

    def test_create_square(self):
        square = Square(5)
        assert isinstance(square, Square)
        assert square.name == 'Square'
        assert square.a == 5
        assert square.b == 5

    def test_perimeter_square(self):
        square = Square(5)
        assert square.perimeter == 20

    def test_area_square(self):
        square = Square(5)
        assert square.area == 25

    def test_add_area_to_square(self):
        square_one = Square(5)
        square_two = Square(10)
        assert square_one.add_area(square_two) == 125
