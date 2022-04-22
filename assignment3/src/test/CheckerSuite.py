import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """
        Class Program {
            Var $x: Int;
            Val t, f: Float = 1.2, 0.1;

            foo(t: Int; y, z:Float){
                If (k > 5){

                }
            }
            main(){

            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 501))

    # def test_redeclared_bkel_402(self):
    #     input = """
    #        Class Program {
    #         main(){ }
    #         Var myVar: String = "Hello World!";
    #         Var myVar: String;
    #     } 
    #     """
    #     expect = """Redeclared Attribute: myVar"""
    #     self.assertTrue(TestChecker.test(input, expect, 402))

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
    #     self.assertTrue(TestChecker.testProgram([ClassDecl(Id("Rectangle"),Id("Shape"),[])])t(input,expect,402))

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
    