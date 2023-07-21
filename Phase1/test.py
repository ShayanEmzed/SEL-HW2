import unittest
from main import Rectangle


class TestRectangle(unittest.TestCase):

    def test_area(self):
        rectangle = Rectangle(5, 6)
        self.assertEqual(rectangle.computeArea(), 30)


if __name__ == '__main__':
    unittest.main()
