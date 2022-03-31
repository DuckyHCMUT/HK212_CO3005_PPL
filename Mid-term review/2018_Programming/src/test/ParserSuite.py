import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """array [1 .. 3, -2 .. 4, 15 .. 20] of array [-13 .. 15] of int"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))