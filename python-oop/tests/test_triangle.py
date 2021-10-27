from src.Triangle import Triangle


class TestTriangle:

    def test_create_regular_triangle(self):
        triangle = Triangle(4, 5, 6)
        assert isinstance(triangle, Triangle)
        assert triangle.name == 'Triangle'
        assert triangle.a == 4
        assert triangle.b == 5
        assert triangle.c == 6

    def test_create_isosceles_triangle(self):
        triangle = Triangle(2, 1, 2)
        assert isinstance(triangle, Triangle)
        assert triangle.name == 'Triangle'
        assert triangle.a == 2
        assert triangle.b == 1
        assert triangle.c == 2

    def test_create_irregular_triangle(self):
        triangle = Triangle(4, 5, 1)
        assert triangle is None

    def test_perimeter_triangle(self):
        triangle = Triangle(4, 5, 6)
        assert triangle.perimeter == 15

    def test_area_triangle(self):
        triangle = Triangle(4, 5, 6)
        assert triangle.area == 9.921567416492215

    def test_add_area_to_triangle(self):
        triangle_one = Triangle(4, 5, 6)
        triangle_two = Triangle(8, 10, 10)
        assert triangle_one.add_area(triangle_two) == 46.582172976138935
