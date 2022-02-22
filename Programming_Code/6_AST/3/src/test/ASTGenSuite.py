import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = "int a;"
        expect = """Program([VarDecl(Id(a),IntType)])"""
        self.assertTrue(TestAST.test(input, expect, 1))

    def test_2(self):
        input = """int a,b;"""
        expect = """Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)])"""
        self.assertTrue(TestAST.test(input, expect, 2))

    def test_3(self):
        input = "int a;float b;"
        expect = """Program([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType)])"""
        self.assertTrue(TestAST.test(input, expect, 3))

    def test_4(self):
        input = "int a,b;float c;"
        expect = """Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),FloatType)])"""
        self.assertTrue(TestAST.test(input, expect, 4))
   
    def test_5(self):
        input = "int a,b;float c,d,e;"
        expect = """Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),FloatType),VarDecl(Id(d),FloatType),VarDecl(Id(e),FloatType)])"""
        self.assertTrue(TestAST.test(input, expect, 5))