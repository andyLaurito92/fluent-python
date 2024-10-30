from unittest import TestCase
from frozenjson import FrozenJSON

class TestFrozenJSON(TestCase):

    def test_can_access_keys_as_attributes(self):
        frozen_json = FrozenJSON({'mykey': 2, 'another_key': 3})
        
        self.assertEqual(getattr(frozen_json, 'another_key'), 3, "Got a different value for another_key attr")
        self.assertEqual(frozen_json.mykey, 2, "Got a different value when calling mykey attr")

    def test_frozenjson_is_recursive(self):
        frozen_json = FrozenJSON({'recursivekey':[{'key1': 'val1', 'key2': 'val2'}], 'key3': {'key4': 'val4', 'key5': {'key6': 3}}})

        self.assertEqual(type(frozen_json.key3), FrozenJSON, "Expected internal mappings to be converted to frozen jsons")

    def test_access_attributes_that_are_keywords_can_be_accessed(self):
        frozen_json = FrozenJSON({'class': 1988, 'student': 'Andy'})

        self.assertEqual(frozen_json.class_, 1988, "Got an error when trying to access class attribute")

    def test_cannot_convert_dictionaries_with_no_valid_strings(self):
        with self.assertRaisesRegex(KeyError, "Cannot convert 2be in a valid dictionary key."):
            fronzen_json = FrozenJSON({'2be': 'something'})
