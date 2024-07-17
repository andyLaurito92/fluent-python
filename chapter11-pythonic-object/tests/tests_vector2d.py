from unittest import TestCase

from vector2d import Vector2D

class Vector2DTests(TestCase):
    def setUp(self):
        self.myvector: Vector2D = Vector2D(3, 4)

    def test_vector_has_attributes_x_and_y(self):
        self.assertEqual((3, 4), (self.myvector.x, self.myvector.y))

    def test_repr_returns_valid_constructor(self):
        self.assertEqual("Vector2D(3, 4)", repr(self.myvector))

    def test_str_returns_user_representation(self):
        self.assertEqual("(3, 4)", str(self.myvector))

    def test_vector_can_be_unpacked(self):
        x, y = self.myvector
        self.assertEqual(x, 3)
        self.assertEqual(y, 4)

    def test_abs_returns_absolute_value(self):
        self.assertEqual(abs(self.myvector), 5)
