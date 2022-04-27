import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_501(self):
        input = """
        Class Program {
            Var a: Int = 10;
            Var b: Int = 20;
            foo(){
                Var b: Float = 0.5;
                Return b;
            }
            main(){}
        }
        Class SubProgram{
            func(){}
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 501))

    # def test_bkel_502_use_ast(self):
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
    #     self.assertTrue(TestChecker.test(input, expect, 502))

    # def test_bkel_503(self):
    #     input = """
    #         Class Program {
    #             main(){
                
    #             }
    #             Var myVar: String = "Hello World";
    #             Var myVar: Int;
    #         }
    #     """
    #     expect = "Redeclared Attribute: myVar"
    #     self.assertTrue(TestChecker.test(input, expect, 503))
        
    # def test_bkel_504(self):
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
    #     self.assertTrue(TestChecker.test(input, expect, 504))

    # def test_bkel_505(self):
    #     input = """
    #     Class Program {
    #         main(){
    #             myVar = 10;
    #         }
    #     }
    #     """
    #     expect = "Undeclared Identifier: myVar"
    #     self.assertTrue(TestChecker.test(input, expect, 505))

