import unittest
from main import Rectangle, Square


class TestRectangle(unittest.TestCase):

    def test_area(self):
        rectangle = Rectangle(5, 6)
        self.assertEqual(rectangle.computeArea(), 30)

    def test_new_height(self):
        rectangle = Rectangle(2, 4)
        rectangle.set_height(8)
        self.assertEqual(rectangle.get_height(), 8)

    def test_new_width(self):
        rectangle = Rectangle(5, 2)
        rectangle.set_width(10)
        self.assertEqual(rectangle.get_width(), 10)

class TestSquare(unittest.TestCase):

    def test_area(self):
        square = Square(8)
        self.assertEqual(square.computeArea(), 64)

    def test_new_side(self):
        sqaure = Square(5)
        sqaure.set_side(9)
        self.assertEqual(sqaure.get_side(), 9)
        self.assertEqual(sqaure.computeArea(), 81)


if __name__ == '__main__':
    unittest.main()
