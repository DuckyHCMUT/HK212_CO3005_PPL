import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_1(self):
        input = '""" abc " de"f ""'
        expect = '""" abc " de"f "",<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 101))
    def test_2(self):
        input = """ ""??!' abc " mdm" dfg"" """
        expect = """""??!' abc " mdm" dfg"",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 102))
    def test_3(self):
        input = ' ""abc"""" '
        expect = '""abc"",Error Token "'
        self.assertTrue(TestLexer.test(input, expect, 103))
    def test_4(self):
        input = ' ""abc""" '
        expect = '""abc"",Error Token "'
        self.assertTrue(TestLexer.test(input, expect, 104))