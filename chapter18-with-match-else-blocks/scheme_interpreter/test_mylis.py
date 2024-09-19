from unittest import TestCase

import mylis as interpreter

class TestMyLis(TestCase):
    def test_can_tokenize_expressions(self):
        self.assertEqual(interpreter.tokenize('(+ 1 2)'), ['(','+','1', '2', ')'])

    def test_can_tokenize_symbols(self):
        self.assertEqual(interpreter.tokenize('(def x 3)'), ['(', 'def', 'x', '3', ')'])

    def test_can_tokenize_nested_expression(self):
        exp = '(def x (+ 1 (* 3 4) 2 5))'
        expected = ['(', 'def', 'x', '(', '+', '1', '(', '*', '3', '4', ')', '2', '5', ')', ')']
        self.assertEqual(interpreter.tokenize(exp), expected)

    def test_can_tokenize_invalid_expression(self):
        self.assertEqual(interpreter.tokenize('(def x'), ['(', 'def', 'x'])

    def test_can_parse_atoms(self):
        self.assertEqual(interpreter.parse_atom('3'), 3)
        self.assertEqual(interpreter.parse_atom('-2'), -2)
        self.assertEqual(interpreter.parse_atom('0.3'), 0.3)
        self.assertEqual(interpreter.parse_atom('def'), 'def')

    def test_can_read_expressions_from_tokens(self):
        self.assertEqual(interpreter.read_from_tokens(['(','+','1', '2', ')']), ['+', 1, 2])
        self.assertEqual(interpreter.read_from_tokens(['(', 'def', 'x', '3', ')']), ['def', 'x', 3])

        self.assertEqual(interpreter.read_from_tokens( 
            ['(', 'def', 'x', '(', '+', '1', '(', '*', '3', '4', ')', '2', '5', ')', ')']), 
                         ['def', 'x', ['+', 1, ['*', 3, 4], 2, 5]])

    def test_if_invalid_expression_from_tokens_error_raised(self):
        with self.assertRaises(SyntaxError) as ctxt:
            interpreter.read_from_tokens(['(', 'def', 'x'])

        self.assertEqual('Unexpected' in ctxt)
