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
