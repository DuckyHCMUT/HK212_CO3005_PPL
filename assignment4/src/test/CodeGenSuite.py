import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_ast_1(self):
        """Simple program: int main() {} """
        input = Program([VarDecl("x",IntType()),FuncDecl("main",[],VoidType(),[Assign(Id("x"),IntLiteral(10)),CallStmt(Id("putInt"),[Id("x")])])])
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 600))

