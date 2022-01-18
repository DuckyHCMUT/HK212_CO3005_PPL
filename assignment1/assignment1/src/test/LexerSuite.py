import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
    def test_mixed_id(self):
        self.assertTrue(TestLexer.test("aAsVN3","aAsVN3,<EOF>",103))
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test("123a123","123,a,123,<EOF>",104))
    def test_anything(self):
        self.assertTrue(TestLexer.test("Vietnam no 1", "Vietnam,no,1,<EOF>",105))
    def test_bkel(self):
        self.assertTrue(TestLexer.test(""" "abc\\h def" """, "Illegal Escape In String: abc\\h", 106))
    def test_expr_1(self):
        self.assertTrue(TestLexer.test("abc[3*(2+3)/5] = 100", "abc,[,3,*,(,2,+,3,),/,5,],=,100,<EOF>", 107))