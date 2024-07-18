from unittest import TestCase

from vector2d import Vector2D

class Vector2DTests(TestCase):
    def setUp(self):
        self.myvector: Vector2D = Vector2D(3, 4)

    def test_vector_has_attributes_x_and_y(self):
        self.assertEqual((3.0, 4.0), (self.myvector.x, self.myvector.y))

    def test_repr_returns_valid_constructor(self):
        self.assertEqual("Vector2D(3.0, 4.0)", repr(self.myvector))

    def test_str_returns_user_representation(self):
        self.assertEqual("(3.0, 4.0)", str(self.myvector))

    def test_vector_can_be_unpacked(self):
        #This behaviour can be achieved by implementing __iter__
        x, y = self.myvector
        self.assertEqual(x, 3.0)
        self.assertEqual(y, 4.0)

    def test_abs_returns_absolute_value(self):
        self.assertEqual(abs(self.myvector), 5)

    def test_equality_works_at_coordinate_level(self):
        self.assertEqual(Vector2D(3.0, 4), self.myvector)

    def test_vector_equality_fails_with_whatever_is_not_a_vector(self):
        # For now, expected behaviour
        # This hapens bc how we built method __eq__ 
        self.assertNotEqual(self.myvector, [3, 4])

    def test_nonempty_vector_evaluates_to_true(self):
        self.assertEqual(self.myvector, True)

    def test_empty_vector_evaluates_to_false(self):
        self.assertEqual(Vector2D(0, 0), False)
