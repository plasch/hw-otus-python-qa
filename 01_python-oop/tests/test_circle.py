from src.Circle import Circle


class TestCircle:

    def test_create_circle(self):
        circle = Circle(7)
        assert isinstance(circle, Circle)
        assert circle.name == 'Circle'
        assert circle.radius == 7

    def test_perimeter_circle(self):
        circle = Circle(7)
        assert circle.perimeter == 43.982297150257104

    def test_area_circle(self):
        circle = Circle(7)
        assert circle.area == 153.93804002589985

    def test_add_area_to_circle(self):
        circle_one = Circle(5)
        circle_two = Circle(7)
        assert circle_one.add_area(circle_two) == 232.4778563656447
