import unittest
from TestUtils import TestChecker
from AST import *

from main.d96.utils.AST import ArrayCell, ArrayLiteral, Assign, AttributeDecl, BinaryOp, Block, BoolType, BooleanLiteral, Break, CallExpr, ClassDecl, ClassType, ConstDecl, Continue, FieldAccess, For, If, MethodDecl, NewExpr, NullLiteral, Return
from main.d96.utils.AST import FloatLiteral, StringLiteral, IntLiteral, SelfLiteral, StringType, UnaryOp
from main.d96.utils.AST import FloatType, Id, Instance, IntType, Program, Static, VarDecl, ArrayType, CallStmt

class CheckerSuite(unittest.TestCase):
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """
        Class Program {
            Var $x: Int;

            main(){

            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))

    # def test_undeclared_function_ast(self):
    #     """Simple program: int main() {} """
    #     input = Program([ClassDecl(Id("Rectangle"),Id("Shape"),[])])
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_diff_numofparam_stmt(self):
    #     """More complex program"""
    #     input = """Class Rectangle : Shape {}"""
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
    #     self.assertTrue(TestChecker.test(input,expect,401))
    
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """Class Rectangle {
    #         Var length: Int;
    #     }"""
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
    #     self.assertTrue(TestChecker.tesProgram([ClassDecl(Id("Rectangle"),Id("Shape"),[])])t(input,expect,402))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     input = Program([ClassDecl(Id("Rectangle"),Id("Shape"),[])])
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([ClassDecl(Id("Rectangle"),[AttributeDecl(Instance,VarDecl(Id("length"),IntType))])])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """More complex program"""
    #     input = Program([ClassDecl(Id("Rectangle"),[AttributeDecl(Static,ConstDecl(Id("$x"),IntType,IntLiteral(10)))])])
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
    #     self.assertTrue(TestChecker.test(input,expect,405))
    