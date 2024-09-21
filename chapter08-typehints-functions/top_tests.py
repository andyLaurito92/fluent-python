from unittest import TestCase

from static_protocol import top_n2, SupportsLessThan

class TestTop(TestCase):
    def test_top_works_with_numbers(self):
        data = [1, 2, 3, 4, 5]
        assert top_n2(data, 3) == [5, 4, 3]

    def test_top_works_with_strings(self):
        data = ['a', 'b', 'c', 'd', 'e']
        assert top_n2(data, 3) == ['e', 'd', 'c']

    def test_top_works_with_tuples(self):
        data = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        assert top_n2(data, 3) == [(9, 10), (7, 8), (5, 6)]

    def test_top_fails_with_unsortable_types(self):
        data = [object(), object(), object()]
        with self.assertRaises(TypeError) as e:
            top_n2(data, 3)
        assert str(e.exception) == "'<' not supported between instances of 'object' and 'object'"
