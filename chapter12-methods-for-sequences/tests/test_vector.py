from unittest import TestCase
from vector import Vector

class TestVector(TestCase):

    def setUp(self):
        self.vec = Vector([3, 2, 1])

    def test_can_retrieve_len_from_vec(self):
        self.assertEqual(len(self.vec), 3)

    def test_vector_representation(self):
        self.assertEqual(repr(self.vec), "Vector([3.0, 2.0, 1.0])")
