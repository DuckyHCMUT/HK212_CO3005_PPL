import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    # def test_simple_program_501(self):
    #     input = """
    #     Class Program {
    #         Var a: Int = 10;
    #         Var b: Int = 20 + Self.a;
    #         foo(){
    #             Var b: Float = 0.5;
    #             Return b;
    #         }
    #         main(){}
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 501))

    # def test_undeclared_id_502(self):
    #     input = """
    #     Class A {
    #         Var a: Int;
    #         Constructor(){
    #             a = 1;
    #         }
    #         Val b: Int = Self.a;
    #     }
    #     Class Program{
    #         main(){}
    #     }
    #     """
    #     expect = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(input, expect, 502))

    # def test_bkel_503_use_ast(self):
    #     input = Program(
    #     [
    #         ClassDecl(
    #             Id("Program"),
    #             [
    #                 MethodDecl(
    #                     Static(),
    #                     Id("main"),
    #                     [],
    #                     Block([])
    #                 ),
    #                 AttributeDecl(
    #                     Instance(),
    #                     VarDecl(Id("myVar"),
    #                     StringType(),
    #                     StringLiteral("Hello World"))
    #                 ),
    #                 AttributeDecl(
    #                     Instance(),
    #                     VarDecl(Id("myVar"),
    #                     IntType())
    #                 )
    #             ]
    #         )
    #     ]
    # )
    #     expect = "Redeclared Attribute: myVar"
    #     self.assertTrue(TestChecker.test(input, expect, 503))

    # def test_bkel_504(self):
    #     input = """
    #         Class Program {
    #             main(){
                
    #             }
    #             Var myVar: String = "Hello World";
    #             Var myVar: Int;
    #         }
    #     """
    #     expect = "Redeclared Attribute: myVar"
    #     self.assertTrue(TestChecker.test(input, expect, 504))
        
    # def test_bkel_505(self):
    #     input = Program(
    #         [
    #             ClassDecl(
    #                 Id("Program"),
    #                 [
    #                     MethodDecl(
    #                         Static(),
    #                         Id("main"),
    #                         [],
    #                         Block(
    #                             [
    #                                 Assign(
    #                                     Id("myVar"),
    #                                     IntLiteral(10)
    #                                 )
    #                             ]
    #                         )
    #                     )
    #                 ]
    #             )
    #         ]
    #     )
    #     expect = "Undeclared Identifier: myVar"
    #     self.assertTrue(TestChecker.test(input, expect, 505))

    # def test_bkel_506(self):
    #     input = """
    #     Class Program {
    #         main(){
    #             myVar = 10;
    #         }
    #     }
    #     """
    #     expect = "Undeclared Identifier: myVar"
    #     self.assertTrue(TestChecker.test(input, expect, 506))

    # def test_binop_float_int_506(self):
    #     input = """
    #     Class Program {
    #         Var a: Float = 50.0;
    #         foo(s: Float){
    #             {
    #                 Var s: Int;
    #                 Var a: Int = 1;
    #             }
    #             Val a: Float = 0.2;
    #             Val b: Float = a + s;
    #             Var c: Float = a - b;
    #             {
    #                 Val a: Int = 100 + b;
    #             }
    #         }
    #         main(){}
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(b),IntType,BinaryOp(+,Id(a),Id(s)))"
    #     self.assertTrue(TestChecker.test(input, expect, 506))

    def test_main_return_507(self):
        input = """
        Class Program {
            Var str: String = "Hello PPL";
            Constructor(str: String){
                Self.str = str;
            }
            main(){
                Self.str = "Nanahira";
            }
        }
        Class Foo {

        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 507))

    # def test_constructor_return_508(self):
    #     input = """
    #     Class Program {
    #         Var str: String = "Hello PPL";
    #         Constructor(str: String){
    #             Self.str = str;
    #             Return Self.str;
    #         }
    #         main(){}
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 508))
