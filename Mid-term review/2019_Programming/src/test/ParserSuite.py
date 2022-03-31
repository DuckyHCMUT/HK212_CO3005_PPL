import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """1 @ a ^ (b[a ^ c][1 @ 2][a] ? 2)"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))