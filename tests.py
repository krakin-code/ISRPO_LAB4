from circle import area as area_circle, perimeter as perimeter_circle
from rectangle import area as area_rectangle, perimeter as perimeter_rectangle
from triangle import area as area_triangle, perimeter as perimeter_triangle
from square import area as area_square, perimeter as perimeter_square

import unittest


class SquareTestCase(unittest.TestCase):
    def test_area_square(self):
        res = area_square(10)
        self.assertEqual(res, 100)

    def test_perimeter_square(self):
        res = perimeter_square(10)
        self.assertEqual(res, 40)

    def test_area_square_negative(self):
        res = area_square(-10)
        self.assertEqual(res, 100)


class CircleTestCase(unittest.TestCase):
    def test_area_circle(self):
        res = area_circle(2)
        self.assertAlmostEqual(res, 12.566370614359172)

    def test_perimeter_circle(self):
        res = perimeter_circle(2)
        self.assertAlmostEqual(res, 12.566370614359172)

    def test_area_circle_negative(self):
        res = area_circle(-2)
        self.assertAlmostEqual(res, 12.566370614359172)


class RectangleTestCase(unittest.TestCase):
    def test_area_rectangle(self):
        res = area_rectangle(10, 5)
        self.assertEqual(res, 50)

    def test_perimeter_rectangle(self):
        res = perimeter_rectangle(10, 5)
        self.assertEqual(res, 30)

    def test_area_rectangle_negative(self):
        res = area_rectangle(-10, 5)
        self.assertEqual(res, -50)


class TriangleTestCase(unittest.TestCase):
    def test_area_triangle(self):
        res = area_triangle(10, 3)
        self.assertEqual(res, 15)

    def test_perimeter_triangle(self):
        res = perimeter_triangle(3, 4, 5)
        self.assertEqual(res, 12)

    def test_area_triangle_negative(self):
        res = area_triangle(-10, 3)
        self.assertEqual(res, -15)

    def test_perimeter_triangle_negative(self):
        res = perimeter_triangle(-10, 3, 10)
        self.assertEqual(res, 3)

