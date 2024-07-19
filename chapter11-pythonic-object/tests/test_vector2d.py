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

    def test_can_convert_vector_to_bytes(self):
        self.assertEqual(b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@', bytes(self.myvector))

    def test_can_convert_vector_to_bytes_and_back(self):
        self.assertEqual(Vector2D.frombytes(bytes(self.myvector)), self.myvector)

    def test_can_specify_formatting_options(self):
        self.assertEqual(format(self.myvector, '.2f'), '(3.00, 4.00)')
        self.assertEqual(format(self.myvector, '.3e'), '(3.000e+00, 4.000e+00)')

    def test_can_specify_polar_formatting(self):
        self.assertEqual(format(self.myvector, '.2fp'), '<5.00, 0.64>')
        self.assertEqual(format(Vector2D(1, 1), 'p'), '<1.4142135623730951, 0.7853981633974483>')
