from unittest import TestCase

from simplepicker import SimplePicker
from randompick import RandomPicker
from typing import TYPE_CHECKING


"""
Instead of using inheritance and enforncing subclassing,
we just use protocols to enforce the interface
"""
class TestSimplePicker(TestCase):
    def is_a_picker(self) -> None:
        self.assertTrue(issubclass(SimplePicker, RandomPicker))

    def is_instance(self) -> None:
        picker: RandomPicker = SimplePicker([1, 2, 3])
        self.assertTrue(isinstance(picker, RandomPicker))


    def test_pick(self) -> None:
        picker = SimplePicker([1, 2, 3])
        item = picker.pick()
        self.assertIn(item, [1, 2, 3])
        if TYPE_CHECKING:
            # Adding note when running mypy
            reveal_type(item)
        assert isinstance(item, int)
