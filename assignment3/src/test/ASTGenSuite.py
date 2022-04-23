import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_bkel_401(self):
        input = """
        Class Program { 
            foo(b: Int; b: Float){
                a.foo();
                a::$foo();
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[param(Id(b),IntType),param(Id(b),FloatType)],Block([Call(Id(a),Id(foo),[]),Call(Id(a),Id($foo),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 401))

    def test_bkel_401(self):
        input = """
        Class Program { 
            foo(b: Int; b: Float){
                b.c();
                a = E::$a;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[param(Id(b),IntType),param(Id(b),FloatType)],Block([Call(Id(a),Id(foo),[]),Call(Id(a),Id($foo),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 402))