import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
    def test_mixed_id(self):
        self.assertTrue(TestLexer.test("aAsVN3","aAsVN,3,<EOF>",103))
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test("123a123","123,a,123,<EOF>",104))
    def test_bkel(self):
        input = """int a, b,c;
float foo(int a; float c, d) {
   int e ;
   e = a + 4 ;
   c = a * d / 2.0 ;
   return c + 1
}
float goo (float a, b) {
   return foo(1, a, b);
}"""
        expect = "nothing"
        self.assertTrue(TestLexer.test(input,expect,106))