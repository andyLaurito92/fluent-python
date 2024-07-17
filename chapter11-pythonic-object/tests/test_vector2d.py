from unittest import TestCase

from vector2d import Vector2D

class Vector2DTests(TestCase):
    def setUp(self):
        self.myvector = Vector2D(3, 4)

    def test_vector_has_attributes_x_and_y(self):
        self.assertEqual((3, 4), (self.myvector.x, self.myvector.y))

    def test_repr_returns_valid_constructor(self):
        self.assertEqual("Vector2D(3, 4)", repr(self.myvector))
