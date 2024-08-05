from unittest import TestCase
from vector import Vector

class TestVector(TestCase):

    def setUp(self):
        self.vec = Vector([3, 2, 1])

    def test_can_retrieve_len_from_vec(self):
        self.assertEqual(len(self.vec), 3)

    def test_vector_representation(self):
        self.assertEqual(repr(self.vec), "Vector([3.0, 2.0, 1.0])")

    def test_can_use_slicing_properties_on_vector(self):
        self.assertEqual(self.vec[1], 2)

        vec_slice = self.vec[0:2] 
        self.assertEqual(vec_slice, [3, 2])
        self.assertEqual(type(vec_slice), Vector)

    def test_can_access_vector_atrributes(self):
        self.assertEqual(self.vec.x, 3.0)
