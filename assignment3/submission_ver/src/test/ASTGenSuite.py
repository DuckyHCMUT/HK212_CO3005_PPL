import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_bkel_401(self):
        input = """
            Class Program {
                main(a: Int){
                
                }
                Var myVar: String = "Hello World";
                Var myVar: Int;
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([])),AttributeDecl(Instance,VarDecl(Id(myVar),StringType,StringLit(Hello World))),AttributeDecl(Instance,VarDecl(Id(myVar),IntType))])])"
        self.assertTrue(TestAST.test(input, expect, 401))

