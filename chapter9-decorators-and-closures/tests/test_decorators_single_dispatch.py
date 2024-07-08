from unittest import TestCase
from decorators_single_dispatch import htmlize

class SingleDispatchDecoratorTest(TestCase):
    def test_default_html_for_python_object(self):
        myset = {1, 2, 3}
        self.assertEqual('<pre>{1, 2, 3}</pre>', htmlize(myset),
                          "Set object didn't match expected output")

    def test_default_html_for_python_functions(self):
        self.assertEqual('<pre><built-in function abs></pre>', htmlize(abs),
                         "Function repr didn't match expected")

    def test_htmlize_should_replace_newlines_in_strings(self):
        mystr = "Hello world! \n I'm Andy"
        self.assertEqual("<p>Hello world! <br/> I'm Andy</p>", htmlize(mystr),
                         "String didn't match expected output")
        
