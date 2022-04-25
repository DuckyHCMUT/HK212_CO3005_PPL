import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_bkel_401(self):
        input = """
            Class Program {
                main(){
                
                }
                Var myVar: String = "Hello World";
                Var myVar: Int;
            }
        """
        expect = "[]"
        self.assertTrue(TestAST.test(input, expect, 401))

