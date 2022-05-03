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
    #     expect = "Illegal Array Literal: [BinaryOp(+,FieldAccess(Self(),Id(x)),IntLit(5)),FloatLit(2.3)]"
    #     self.assertTrue(TestChecker.test(input, expect, 511))

    # def test_wrong_array_lit_512(self):
    #     input = """
    #     Class Program {
    #         Val x: Int = 2;
    #         Var arr: Array[String, 2] = Array("Nanahira", "Choko");
    #         setVocal(s: Array[String, 3]){
    #             Self.arr = s;
    #             Return Self.arr;
    #         }
    #         main(){}
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(arr)),Id(s))"
    #     self.assertTrue(TestChecker.test(input, expect, 512))

    # def test_for_loop_513(self):
    #     input = """
    #     Class Program {
    #         Var a: Int = 10;
    #         func(s: String; b: Int){
    #             Foreach(z In 1 .. 100){
    #                 s = s +. "a";
    #                 z = z + b - Self.a;
    #             }
    #             Return s;
    #         }
    #         main(){}
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 513))

    # def test_break_not_in_loop_514(self):
    #     input = """
    #     Class Program {
    #         dupper(s: String; b: Int){
    #             Foreach(z In 1 .. 100 By 5){
    #                 s = s +. "a";
    #                 Break;
    #             }
    #             Break;
    #             Return s;
    #         }
    #         main(){}
    #     }
    #     """
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input, expect, 514))

    # def test_multiple_break_continue_ok_515(self):
    #     input = """
    #     Class Program {
    #         main(){}
    #     }

    #     Class Song {
    #         worker(s: String){
    #             s = "Iroha \t 7";
    #             Foreach (t In 1 .. 100){
    #                 ## Awaiting ##
    #                 Continue;
    #                 Break;
    #                 Continue;
    #                 Break;
    #                 Break;
    #             }
    #         }
    #         play(t: Song){
    #             ## Do Nothing ##
    #         }
    #     }
    #     """ 
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 515))

    # def test_continue_not_in_loop_516(self):
    #     input = """
    #     Class Program {
    #         dupper(s: String; b: Int){
    #             Foreach(z In 1 .. 100 By 5){
    #                 ## Do Nothing ##
    #             }
    #             Continue;
    #             Return s;
    #         }
    #         main(){}
    #     }
    #     """
    #     expect = "Continue Not In Loop"
    #     self.assertTrue(TestChecker.test(input, expect, 516))

    # def test_undeclared_method_517(self):
    #     input = """
    #     Class Program {
    #         main(){}
    #     }

    #     Class UI {
    #         Var fL: Boolean = False;
    #         worker(){
    #             Var s: Int = 5;
    #             s = s - 1;
    #             Self.fL = True;
    #             Return s;
    #         }
    #         clearer(){
    #             Self.fL = False;
    #             Return;
    #         }
    #         start(){
    #             Self.worker();
    #             Self.clearer();
    #             Self.printStatus();
    #         }
    #     }
    #     """
    #     expect = "Undeclared Method: printStatus"
    #     self.assertTrue(TestChecker.test(input, expect, 517))

    # def test_static_method_ok_518(self):
    #     input = """
    #     Class UI {
    #         Var fL: Boolean = False;
    #         worker(){
    #             Var s: Int = 5;
    #             s = s - 1;
    #             Self.fL = True;
    #             Return s;
    #         }
    #         clearer(){
    #             Self.fL = False;
    #             Return;
    #         }
    #         printStatus(){
    #             ## pretend this line will print something ##
    #         }
    #         $start(){
    #             Self.worker();
    #             Self.clearer();
    #             Self.printStatus();
    #         }
    #     }

    #     Class Program {
    #         main(){
    #             UI::$start();
    #             Return;
    #         }
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 518))

    # def test_undeclared_static_method_519(self):
    #     input = """
    #     Class UI {
    #         Var fL: Boolean = False;
    #         worker(){
    #             Var s: Int = 5;
    #             s = s - 1;
    #             Self.fL = True;
    #             Return s;
    #         }
    #         clearer(){
    #             Self.fL = False;
    #             Return;
    #         }
    #         $start(){
    #             Self.worker();
    #             Self.clearer();
    #         }
    #     }

    #     Class Program {
    #         main(){
    #             UI::$clearer();
    #             Return;
    #         }
    #     }
    #     """
    #     expect = "Undeclared Method: $clearer"
    #     self.assertTrue(TestChecker.test(input, expect, 519))

    # def test_self_undeclared_static_method_520(self):
    #     input = """
    #     Class W {
    #         Var fL: Boolean = False;
    #         Var count: Int = 1;
    #         $inc(){
    #             Self.count = Self.count + 1;
    #         }
    #         starter(){
    #             Self.fL = True;
    #             W::$inc();
    #             W::$dec();
    #         }
    #     }

    #     Class Program {
    #         main(){
    #             W::$inc();
    #         }
    #     }
    #     """
    #     expect = "Undeclared Method: $dec"
    #     self.assertTrue(TestChecker.test(input, expect, 520))

    # def test_unequal_parameter_callstmt_521(self):
    #     input = """
    #     Class Program {
    #         main(){}
    #     }

    #     Class UI {
    #         Val int: Int = 0;
    #         what(str: String; size: Int){
    #             Var s: String = "";
    #             Foreach (_ In 1 .. size By size/20){
    #                 s = s+. str;
    #             }
    #             Return s;
    #         }
    #         doSomething(){
    #             Self.what("hahaha", 100, 200);
    #             Return;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Call(Self(),Id(what),[StringLit(hahaha),IntLit(100),IntLit(200)])"
    #     self.assertTrue(TestChecker.test(input, expect, 521))

    # def test_unequal_parameter_static_callstmt_522(self):
    #     input = """
    #     Class UI {
    #         Val int: Int = 0;
    #         $what(str: String; size: Int){
    #             Var s: String = "";
    #             Foreach (_ In 1 .. size By size/20){
    #                 s = s+. str;
    #             }
    #             Return s;
    #         }
    #         doWhat(){
    #             UI::$what("nana", 100);
    #         }
    #     }

        
    #     Class Program {
    #         main(){
    #             UI::$what("hira");
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Call(Id(UI),Id($what),[StringLit(hira)])"
    #     self.assertTrue(TestChecker.test(input, expect, 522))

    # ## http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=157975
    # def test_illegal_memaccess_523(self):
    #     input = """
    #     Class E{
    #         Var a: Int;
    #     }

    #     Class Program{
    #         main(){
    #             Var b: Int = E.a;
    #         }
    #     }
    #     """
    #     expect = "Illegal Member Access: FieldAccess(Id(E),Id(a))"
    #     self.assertTrue(TestChecker.test(input, expect, 523))

    # def test_illegal_memaccess_524(self):
    #     input = """
    #     Class Program{
    #         main(){
    #             Var b: Int = E.a;
    #         }
    #     }
    #     """
    #     expect = "Undeclared Class: E"
    #     self.assertTrue(TestChecker.test(input, expect, 523))

    # def est_call_expr_ok_524(self):
    #     input = """
    #     Class Circle {
    #         Var r: Int = 10;
    #         getRadius(){
    #             Return Self.r;
    #         }
    #         calArea(){
    #             Return Self.getRadius() * 3.14;
    #         }
    #     }

    #     Class Program {
    #         main(){}
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 524))

    # # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=157987
    # def test_return_something_525(self):
    #     input = """
    #     Class Program{
    #         main(){
    #             Return 123;
    #         }
    #     }    
    #     """
    #     expect = "Type Mismatch In Statement: Return(IntLit(123))"
    #     self.assertTrue(TestChecker.test(input, expect, 525))
    
    # # For test 526 - 528
    # # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158294
    # def test_typemismatch_stmt_1_526(self):
    #     input = """
    #     Class Program{
    #         Var flag: Int = 2.2;
    #         main(){}
    #     }    
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(flag),IntType,FloatLit(2.2))"
    #     self.assertTrue(TestChecker.test(input, expect, 526))

    # # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=157987
    # def test_return_something_527(self):
    #     input = """
    #     Class Program{
    #         main(){
    #             Var _flag: Int = 3.16;
    #         }
    #     }    
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(_flag),IntType,FloatLit(3.16))"
    #     self.assertTrue(TestChecker.test(input, expect, 527))

    # ## http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=157987
    # def test_undeclared_object_528(self):
    #     input = """
    #     Class A {
    #         foo(){
    #             Var a: Array[Int, 5];
    #             a = Array(1, 2, 3, 4, 5);
    #         }
    #     }
    #     Class Program{
    #         main(){
    #             count.foo();
    #         }
    #     }    
    #     """
    #     expect = "Undeclared Identifier: count"
    #     self.assertTrue(TestChecker.test(input, expect, 528))

    # def test_declared_object_ok_529(self):
    #     input = """
    #     Class A {
    #         foo(x: Int){
    #             Var a: Float = x + 0.5;
    #         }
    #         Constructor(a: Int){}
    #     }
    #     Class Program{
    #         main(){
    #             {
    #                 Var count: A = New A(1);   
    #                 count.foo(123);
    #             }
    #         }
    #     }    
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 529))

    # # Cannot assign to constant cases 530 --> 532
    # def test_cannot_assign_to_const_530(self):
    #     input = """
    #     Class A {
    #         Val x: Int = 123;
    #         baz(){
    #             Self.x = 6;
    #         }
    #     }
    #     Class Program{
    #         main(){
    #             Return;
    #         }
    #     }    
    #     """
    #     expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(x)),IntLit(6))"
    #     self.assertTrue(TestChecker.test(input, expect, 530))

    # def test_cannot_assign_to_const_531(self):
    #     input = """
    #     Class Program{
    #         main(){
    #             Val t: Boolean = True;
    #             t = True;
    #             Return;
    #         }
    #     }
    #     """
    #     expect = """Cannot Assign To Constant: AssignStmt(Id(t),BooleanLit(True))"""
    #     self.assertTrue(TestChecker.test(input, expect, 531))

    # def test_cannot_assign_to_const_532(self):
    #     input = """
    #     Class Animal {
    #         main(t: Int){
    #             Val z: String = "Nana";
    #             Foreach (i In t .. 1000){
    #                 z = "Nyan";
    #                 Continue;
    #             }
    #             Return z;
    #         }
    #     }

    #     Class Program {
    #         main(){}
    #         Constructor(){}
    #         Destructor(){}
    #     }
    #     """
    #     expect = """Cannot Assign To Constant: AssignStmt(Id(z),StringLit(Nyan))"""
    #     self.assertTrue(TestChecker.test(input, expect, 532))

    # # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158311
    # # Test type mismatch in array assignment: 533 --> 534
    # def test_type_mismatch_array_assign_533(self):
    #     input = """
    #     Class A {
    #         Var s: String = "No";
    #         foo(){
    #             Var a: Array[Int, 2];
    #             a = Array(1, 2, 3);
    #         }
    #         Constructor(s: String){
    #             Self.s = s;
    #         }
    #     }
    #     Class Program{
    #         main(){
    #             Val obj: A = New A("Let's go");
    #             obj.foo();
    #         }
    #     }    
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(a),[IntLit(1),IntLit(2),IntLit(3)])"
    #     self.assertTrue(TestChecker.test(input, expect, 533))

    # def test_type_mismatch_array_assign_534(self):
    #     input = """
    #     Class A {
    #         Var s: String = "No";
    #         Var arr: Array[Boolean, 2] = Array(False, True);
    #         foo(s: String){
    #             Self.arr = Array("Bana", "Nana");
    #         }
    #         Constructor(s: String){
    #             Self.s = s;
    #         }
    #     }

    #     Class B : A{}

    #     Class Program{
    #         main(){
    #             Val ab: A = New A("12\t3");
    #             ab.foo("xyz^%$");
    #             Return;
    #         }
    #     }    
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(arr)),[StringLit(Bana),StringLit(Nana)])"
    #     self.assertTrue(TestChecker.test(input, expect, 534))

    # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158205
    def test_illegal_static_access_535(self):
        input = """
        Class Program{
            Val $someStatic: Int = 10;
            $getStatic(){
                Return Program::$someStatic;
            }
            main(){
                Var Program: Float = 1.0;
                Var x: Int = Program::$getStatic();
                Var y: Int = Program::$someStatic;
                If (x == y){}
                Else {Return;}
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 535))

    # def test_bkel_1_use_ast_596(self):
    #     input = Program(
    #     [
    #             ClassDecl(
    #                 Id("Program"),
    #                 [
    #                     MethodDecl(
    #                         Static(),
    #                         Id("main"),
    #                         [],
    #                         Block([])
    #                     ),
    #                     AttributeDecl(
    #                         Instance(),
    #                         VarDecl(
    #                             Id("myVar"),
    #                             StringType(),
    #                             StringLiteral("Hello World")
    #                         )
    #                     ),
    #                     AttributeDecl(
    #                         Instance(),
    #                         VarDecl(
    #                             Id("myVar"),
    #                             IntType()
    #                         )
    #                     )
    #                 ]
    #             )
    #         ]
    #     )
    #     expect = "Redeclared Attribute: myVar"
    #     self.assertTrue(TestChecker.test(input, expect, 596))

    # def test_bkel_2_use_ast_597(self):
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
    #     self.assertTrue(TestChecker.test(input, expect, 597))

    # def test_bkel_3_use_ast_598(self):
    #     input = Program(
    #         [
    #             ClassDecl(
    #                 Id("Program"),
    #                 [
    #                     MethodDecl(
    #                         Static(),
    #                         Id("main"),
    #                         [],
    #                         Block([
    #                             ConstDecl(
    #                                 Id("myVar"),
    #                                 IntType(),
    #                                 IntLiteral(5)
    #                             ),
    #                             Assign(
    #                                 Id("myVar"),
    #                                 IntLiteral(10)
    #                             )]
    #                         )
    #                     )
    #                 ]
    #             )
    #         ]
    #     )
    #     expect = "Cannot Assign To Constant: AssignStmt(Id(myVar),IntLit(10))"
    #     self.assertTrue(TestChecker.test(input, expect, 598))

    # def test_bkel_4_use_ast_599(self):
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
    #                                 Break()
    #                             ]
    #                         )
    #                     )
    #                 ]
    #             )
    #         ]
    #     )
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input, expect, 599))

    # def test_bkel_5_use_ast_600(self):
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
    #                                 ConstDecl(
    #                                     Id("myVar"),
    #                                     IntType(),
    #                                     FloatLiteral(1.2)
    #                                 )
    #                             ]
    #                         )
    #                     )
    #                 ]
    #             )
    #         ]
    #     )
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(myVar),IntType,FloatLit(1.2))"
    #     self.assertTrue(TestChecker.test(input, expect, 600))
