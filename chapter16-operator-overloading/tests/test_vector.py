import unittest
from vector import Vector

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
