from unittest import TestCase
from decorators_single_dispatch import htmlize
from fractions import Fraction
from decimal import Decimal


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

    def test_htmlize_should_create_an_ul_list(self):
        mylist = ['alpha', 66, {3, 2, 1}]
        self.assertEqual(("<ul><li><p>alpha</p></li><li><pre>66 (0x42)</pre></li>"
                          "<li><pre>{1, 2, 3}</pre></li></ul>"), htmlize(mylist),
                         "List didn't match expected output")

    def test_bool_should_be_treated_as_object(self):
        self.assertEqual("<pre>True</pre>", htmlize(True),
                         "ool didn't formatted correctly")

    def test_float_should_output_fraction_value(self):
        myfloat= 2/3
        self.assertEqual("<pre>0.6666666666666666 (2/3)</pre>", htmlize(myfloat),
                         "Float didn't formatted correctly")

    def test_decimal_should_output_fraction_value(self):
        mydecimal = Decimal('0.023809523809523808')
        self.assertEqual("<pre>0.023809523809523808 (1/42)</pre>",
                         htmlize(mydecimal),
                         "Decimal didn't formatted correctly")
