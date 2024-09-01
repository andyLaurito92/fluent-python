import unittest
import importlib
from vectors.vector import Vector
from vectors.vector2d import Vector2D
from fractions import Fraction

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

    def test_can_multiply_a_scalar(self):
        scalar = Fraction(1, 3)

        self.assertEqual(self.vector * 3, Vector((3, 6, 9)))
        self.assertEqual(self.vector * scalar, Vector(Fraction(1, 3), Fraction(2, 3), 1))

    def test_when_try_to_multiply_notnumber_raise_exception(self):
        with self.assertRaises(Exception) as context:
            self.vector * "hey"
            self.assertTrue("could not convert" in context)
        
    def test_can_initialize_vector_by_providing_multiple_values(self):
        self.assertEqual(Vector, type(Vector(1, 2, 3)))

    def test_raise_exception_when_no_argument_is_provided_to_init(self):
        with self.assertRaises(Exception) as context:
            Vector()
            self.assertTrue("Expected either iterable or list of elements to initialize vector. None given" in context)

    def test_can_multiply_another_vector(self):
        vec2 = Vector(1, 1, 1)
        # 1 + 2 + + 3
        self.assertEqual(self.vector @ vec2, 6.0)

    def test_when_tryto_multiplyvectors_differentsize_raise_exception(self):
        vec2 = Vector(1, 2)
        with self.assertRaises(ValueError) as context:
            self.vector @ vec2
            self.assertTrue(context)
