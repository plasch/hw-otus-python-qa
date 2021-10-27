import pytest

from src.Figure import Figure
from src.Rectangle import Rectangle


class TestFigure:

    """Проверки на ожидаемые исключения."""
    def test_create_instance_figure(self):
        with pytest.raises(Exception):
            Figure(2)

    def test_add_area_to_not_figure(self):
        rectangle = Rectangle(4, 5)
        not_figure = 0
        with pytest.raises(ValueError):
            rectangle.add_area(not_figure)
