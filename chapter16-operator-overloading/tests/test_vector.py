import unittest
import importlib
from vectors.vector import Vector
from vectors.vector2d import Vector2D

class VectorTests(unittest.TestCase):
    def setUp(self):
        self.vector = Vector(range(1, 4))

    def test_can_negate_vector(self):
        expected = Vector([-1, -2, -3])
        self.assertEqual(-self.vector, expected)

    def test_can_call_pos_unitary_operator(self):
        self.assertEqual(self.vector, Vector(x for x in range(1, 4)))

    def test_cannot_call_invert_operator_in_vector(self):
        """ We don't want to implement the bit logican negator
        because it doesn't make sense for our vector"""
        with self.assertRaises(TypeError) as context:
            ~self.vector
            self.assertTrue("bad operand type for unary ~: 'Vector'." in context.exception)

    def test_can_add_two_vectors(self):
        self.assertEqual(Vector(range(1, 4)) + Vector(range(5, 8)), Vector([6, 8, 10]))

    def test_can_add_vectors_of_multiple_size(self):
        self.assertEqual(self.vector + Vector(range(2, 3)), Vector([3, 2, 3]))

    def test_can_add_vector_with_vector2d(self):
        vec2d = Vector2D(3, 4)
        self.assertEqual(self.vector + vec2d, Vector((4, 6, 3)))

    def test_can_reverse_add_with_vector2d(self):
        vec2d = Vector2D(3, 4)
        self.assertEqual(vec2d + self.vector, Vector((4, 6, 3)))
