import unittest
from main import Rectangle


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


if __name__ == '__main__':
    unittest.main()
