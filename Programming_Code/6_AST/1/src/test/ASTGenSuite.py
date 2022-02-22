import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = "int a;"""
        expect = str(4)
        self.assertTrue(TestAST.test(input, expect, 1))

    def test_2(self):
        input = """int a,b;"""
        expect = str(5)
        self.assertTrue(TestAST.test(input, expect, 2))
    
    def test_3(self):
        input = "int a;float b;"
        expect = str(5)
        self.assertTrue(TestAST.test(input, expect, 3))

    def test_4(self):
        input = "int a,b;float c;"
        expect = str(5)
        self.assertTrue(TestAST.test(input, expect, 4))

    def test_5(self):
        input = "int a,b;float c,d,e;"
        expect = str(7)
        self.assertTrue(TestAST.test(input, expect, 5))
