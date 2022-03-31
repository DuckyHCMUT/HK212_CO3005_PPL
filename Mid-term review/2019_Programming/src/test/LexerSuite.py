import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_1(self):
        input = "01/11/1969"
        expect = "01/11/1969,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 101))
    def test_2(self):
        input = "31/02/2001"
        expect = "31/02/2001,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 102))
    def test_3(self):
        input = "21/12/2099"
        expect = "21/12/2099,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 103))
    def test_4(self):
        input = "32/13/2100"
        expect = "Error Token 3"
        self.assertTrue(TestLexer.test(input, expect, 104))
    def test_5(self):
        input = "31-12-2001"
        expect = "Error Token 3"
        self.assertTrue(TestLexer.test(input, expect, 105))
    def test_6(self):
        input = "1/12/1999"
        expect = "Error Token 1"
        self.assertTrue(TestLexer.test(input, expect, 106))