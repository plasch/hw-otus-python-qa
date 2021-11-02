from src.Rectangle import Rectangle


class TestRectangle:

    def test_create_rectangle(self):
        rectangle = Rectangle(4, 5)
        assert isinstance(rectangle, Rectangle)
        assert rectangle.name == 'Rectangle'
        assert rectangle.a == 4
        assert rectangle.b == 5

    def test_perimeter_rectangle(self):
        rectangle = Rectangle(4, 5)
        assert rectangle.perimeter == 18

    def test_area_rectangle(self):
        rectangle = Rectangle(4, 5)
        assert rectangle.area == 20

    def test_add_area_to_rectangle(self):
        rectangle_one = Rectangle(4, 5)
        rectangle_two = Rectangle(5, 4)
        assert rectangle_one.add_area(rectangle_two) == 40
