from unittest import TestCase

from simplepicker import SimplePicker
from randompick import RandomPicker


"""
Instead of using inheritance and enforncing subclassing,
we just use protocols to enforce the interface
"""
class TestSimplePicker(TestCase):
    def is_a_picker(self):
        self.assertTrue(issubclass(SimplePicker, RandomPicker))

    def test_pick(self):
        picker = SimplePicker([1, 2, 3])
        self.assertIn(picker.pick(), [1, 2, 3])
