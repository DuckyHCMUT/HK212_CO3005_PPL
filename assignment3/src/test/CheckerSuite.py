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

    # def test_binop_float_int_507(self):
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
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,BinaryOp(+,IntLit(100),Id(b)))"
    #     self.assertTrue(TestChecker.test(input, expect, 507))

    # def test_main_return_508(self):
    #     input = """
    #     Class Program {
    #         Var str: String = "Hello PPL";
    #         Constructor(str: String){
    #             Self.str = str;
    #         }
    #         main(){
    #             Self.str = "Nanahira";
    #         }
    #     }
    #     Class Foo {

    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 508))

    # def test_constructor_return_509(self):
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
    #     self.assertTrue(TestChecker.test(input, expect, 509))

    # def test_array_lit_decl_510(self):
    #     input = """
    #     Class Program {
    #         Var a: Int = 2;
    #         Var arr: Array[Int, 0x3] = Array(1, Self.a);
    #         main(){}
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(arr),ArrayType(3,IntType),[IntLit(1),FieldAccess(Self(),Id(a))])"
    #     self.assertTrue(TestChecker.test(input, expect, 510))

    # def test_wrong_array_lit_511(self):
    #     input = """
    #     Class Program {
    #         Val x: Int = 2;
    #         Val arr: Array[Int, 2] = Array(Self.x + 5, 2.3);
    #         main(){}
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: [BinaryOp(+,FieldAccess(Self(),Id(x)),IntLit(5)),FloatLit(2.3)]"
    #     self.assertTrue(TestChecker.test(input, expect, 511))

    # def test_wrong_array_lit_512(self):
    #     input = """
    #     Class Program {
    #         Val x: Int = 2; ##Unused##
    #         Val arr: Array[String, 2] = Array("Nanahira", "Choko");
    #         setVocal(s: Array[String, 3]){
    #             Self.arr = Array("Choko", "Nanahira", "nayuta");
    #             Return Self.arr;
    #         }
    #         main(){}
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(arr)),[StringLit(Choko),StringLit(Nanahira),StringLit(nayuta)])"
    #     self.assertTrue(TestChecker.test(input, expect, 512))

    # def test_for_loop_513(self):
    #     input = """
    #     Class Program {
    #         Var a: Int = 10;
    #         func(s: String; b: Int){
    #             Val z: Float = 0.5e3;
    #             Foreach(z In 1 .. 100 By 5){
    #                 s = s +. "a";
    #                 z = z + b;
    #             }
    #             Return z + b;
    #         }
    #         main(){}
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 513))

    def test_break_not_in_loop_514(self):
        input = """
        Class Program {
            dupper(s: String; b: Int){
                Foreach(b In 1 .. 100 By 5){
                    s = s +. "a";
                    Break;
                }
                Break;
                Return s;
            }
            main(){}
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 514))