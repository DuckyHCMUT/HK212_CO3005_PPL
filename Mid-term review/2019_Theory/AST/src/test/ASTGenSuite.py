import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # Question A
    # def test_1(self):
    #     input = """struct{
    #         float b;
    #     }"""
    #     expect = """5"""
    #     self.assertTrue(TestAST.test(input, expect, 1))

    # def test_2(self):
    #     input = """struct{
    #         int a, c;
    #         float b;
    #     }"""
    #     expect = """9"""
    #     self.assertTrue(TestAST.test(input, expect, 2))

    # Question B
    def test_1(self):
        input = """struct{
            float b;
        }"""
        expect = """Struct([MemDecl(FloatType,b)])"""
        self.assertTrue(TestAST.test(input, expect, 1))

    def test_2(self):
        input = """struct{
            int a, c;
            float b;
        }"""
        expect = """Struct([MemDecl(IntType,a),MemDecl(IntType,c),MemDecl(FloatType,b)])"""
        self.assertTrue(TestAST.test(input, expect, 2))