import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_bkel_1(self):
        input = Program(
            [
                ClassDecl(
                    Id("Program"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("myVar"),
                                StringType(),
                                StringLiteral("Hello World")
                            )
                        ),
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("myVar"),
                                IntType()
                            )
                        )
                    ]
                )
            ]
        )
        expect = "Redeclared Attribute: myVar"
        self.assertTrue(TestChecker.test(input, expect, 501))

    def test_bkel_2(self):
        input = Program(
            [
                ClassDecl(
                    Id("Program"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            Block(
                                [
                                    Assign(
                                        Id("myVar"),
                                        IntLiteral(10)
                                    )
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        expect = "Undeclared Identifier: myVar"
        self.assertTrue(TestChecker.test(input, expect, 502))
    
    def test_bkel_3(self):
        input = Program(
            [
                ClassDecl(
                    Id("Program"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            Block([
                                ConstDecl(
                                    Id("myVar"),
                                    IntType(),
                                    IntLiteral(5)
                                ),
                                Assign(
                                    Id("myVar"),
                                    IntLiteral(10)
                                )]
                            )
                        )
                    ]
                )
            ]
        )
        expect = "Cannot Assign To Constant: AssignStmt(Id(myVar),IntLit(10))"
        self.assertTrue(TestChecker.test(input, expect, 503))

    def test_bkel_4(self):
        input = Program(
            [
                ClassDecl(
                    Id("Program"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            Block(
                                [
                                    Break()
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 504))

    def test_bkel_5(self):
        input = Program(
            [
                ClassDecl(
                    Id("Program"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            Block(
                                [
                                    ConstDecl(
                                        Id("myVar"),
                                        IntType(),
                                        FloatLiteral(1.2)
                                    )
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(myVar),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 505))

    def test_undeclared_id_1(self):
        input = """
        Class Program {
            Var a: Int = 10;
            Var b: Int = 20 + Self.a;
            foo(){
                Var b: Float = 0.5;
                Return b + a;
            }
            main(){}
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 506))

    def test_undeclared_id_2(self):
        input = """
        Class A {
            Var a: Int;
            Constructor(){
                a = 1;
            }
            Val b: Int = Self.a;
        }
        Class Program{
            main(){}
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 507))

    def test_main_return_1(self):
        input = """
        Class Program {
            Var str: String = "Hello PPL";
            Constructor(str: String){
                Self.str = str;
            }
            main(){
                Self.str = "Nanahira";
                Return Self.str;
            }
        }
        Class Foo {}
        """
        expect = "Type Mismatch In Statement: Return(FieldAccess(Self(),Id(str)))"
        self.assertTrue(TestChecker.test(input, expect, 508))

    def test_constructor_return_509(self):
        input = """
        Class Program {
            Var str: String = "Hello PPL";
            Constructor(str: String){
                Self.str = str;
                Return Self.str;
            }
            main(){}
        }
        """
        expect = "Type Mismatch In Statement: Return(FieldAccess(Self(),Id(str)))"
        self.assertTrue(TestChecker.test(input, expect, 509))

    def test_array_lit_1(self):
        input = """
        Class Program {
            Var a: Int = 2;
            Var arr: Array[Int, 0x3] = Array(1, Self.a);
            main(){}
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(arr),ArrayType(3,IntType),[IntLit(1),FieldAccess(Self(),Id(a))])"
        self.assertTrue(TestChecker.test(input, expect, 510))

    def test_array_lit_2(self):
        input = """
        Class Program {
            Val x: Int = 2;
            Val arr: Array[Int, 2] = Array(Self.x + 5, 2.3);
            main(){}
        }
        """
        expect = "Illegal Array Literal: [BinaryOp(+,FieldAccess(Self(),Id(x)),IntLit(5)),FloatLit(2.3)]"
        self.assertTrue(TestChecker.test(input, expect, 511))

    def test_array_lit_3(self):
        input = """
        Class Program {
            Val x: Int = 2;
            Var arr: Array[String, 2] = Array("Nanahira", "Choko");
            setVocal(s: Array[String, 3]){
                Self.arr = s;
                Return Self.arr;
            }
            main(){}
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(arr)),Id(s))"
        self.assertTrue(TestChecker.test(input, expect, 512))

    def test_for_loop_1(self):
        input = """
        Class Program {
            Var a: Int = 10;
            func(s: String; b: Int){
                Foreach(z In 1 .. 100){
                    s = s +. "a";
                    z = z + b - Self.a;
                }
                Return z;
            }
            main(){}
        }
        """
        expect = "Undeclared Identifier: z"
        self.assertTrue(TestChecker.test(input, expect, 513))

    def test_break_not_in_loop_1(self):
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

    def test_continue_not_in_loop_1(self):
        input = """
        Class Program {
            main(){}
        }

        Class Song {
            worker(s: String){
                s = "Iroha \t 7";
                Var t, z: Int = 7, 77;
                Foreach (t In 1 .. 100){
                    ## Awaiting ##
                    Continue;
                    Break;
                    Continue;
                    Break;
                    Return;
                    Foreach(z In 1 .. -1){
                        Continue;
                        Break;
                    }
                    Break;
                    Continue;
                }
                Continue;
            }
            play(t: Song){
                ## Do Nothing ##
            }
        }
        """ 
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 515))

    def test_continue_not_in_loop_2(self):
        input = """
        Class Program {
            dupper(s: String; b: Int){
                Foreach(b In 1 .. 100 By 5){
                    ## Do Nothing ##
                }
                Continue;
                Return s;
            }
            main(){}
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 516))

    def test_undeclared_method_1(self):
        input = """
        Class Program {
            main(){}
        }

        Class UI {
            Var fL: Boolean = False;
            worker(){
                Var s: Int = 5;
                s = s - 1;
                Self.fL = True;
            }
            clearer(){
                Self.fL = False;
                Return;
            }
            start(){
                Self.worker();
                Self.clearer();
                Self.printStatus();
            }
        }
        """
        expect = "Undeclared Method: printStatus"
        self.assertTrue(TestChecker.test(input, expect, 517))

    def test_illegal_access_1(self):
        input = """
        Class UI {
            Var fL: Boolean = False;
            worker(){
                Var s: Int = 5;
                s = s - 1;
                Self.fL = True;
            }
            clearer(){
                Self.fL = False;
                Return;
            }
            printStatus(){
                ## pretend this line will print something ##
            }
            $start(){
                Self.worker();
                Self.clearer();
                Self.printStatus();
            }
        }

        Class Program {
            main(){
                UI::$start();
                Var x: UI = New UI();
                x::$start();
                Return;
            }
        }
        """
        expect = "Illegal Member Access: Call(Id(x),Id($start),[])"
        self.assertTrue(TestChecker.test(input, expect, 518))

    def test_undeclared_static_method_1(self):
        input = """
        Class UI {
            Var fL: Boolean = False;
            worker(){
                Var s: Int = 5;
                s = s - 1;
                Self.fL = True;
            }
            clearer(){
                Self.fL = False;
                Return;
            }
            $start(){
                Self.worker();
                Self.clearer();
            }
        }

        Class Program {
            main(){
                UI::$clearer();
                Return;
            }
        }
        """
        expect = "Undeclared Method: $clearer"
        self.assertTrue(TestChecker.test(input, expect, 519))

    def test_undeclared_static_method_2(self):
        input = """
        Class W {
            Var fL: Boolean = False;
            Var count: Int = 1;
            $inc(){
                Self.count = Self.count + 1;
            }
            starter(){
                Self.fL = True;
                W::$inc();
                W::$dec();
            }
        }

        Class Program {
            main(){
                W::$inc();
            }
        }
        """
        expect = "Undeclared Method: $dec"
        self.assertTrue(TestChecker.test(input, expect, 520))

    def test_unequal_parameter_callstmt_521(self):
        input = """
        Class Program {
            main(){}
        }

        Class UI {
            Val int: Int = 0;
            what(str: String; size: Int){
                Var s: String = "";
                Var _: Int;
                Foreach (_ In 1 .. size By size/20){
                    s = s+. str;
                }
                Return;
            }
            doSomething(){
                Self.what("hahaha", 100, 200);
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: Call(Self(),Id(what),[StringLit(hahaha),IntLit(100),IntLit(200)])"
        self.assertTrue(TestChecker.test(input, expect, 521))

    def test_unequal_parameter_static_callstmt_522(self):
        input = """
        Class UI {
            Val int: Int = 0;
            $what(str: String; size: Int; _:Int){
                Var s: String = "";
                Foreach (_ In 1 .. size By size/20){
                    s = s+. str;
                }
            }
            doWhat(){
                UI::$what("nana", 100, -5);
            }
        }

        
        Class Program {
            main(){
                UI::$what("hira");
            }
        }
        """
        expect = "Type Mismatch In Statement: Call(Id(UI),Id($what),[StringLit(hira)])"
        self.assertTrue(TestChecker.test(input, expect, 522))

    ## http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=157975
    def test_illegal_memaccess_523(self):
        input = """
        Class E{
            Var a: Int;
        }

        Class Program{
            main(){
                Var b: Int = E.a;
            }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(E),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 523))
    
    def test_call_expr_524(self):
        input = """
        Class Circle {
            Var r: Int = 10;
            getRadius(){
                Return Self.r;
            }
            calArea(){
                Return Self.getRadius() * 3.14;
            }
        }

        Class Program {
            main(){
                Circle.calArea();
            }
        }
        """
        expect = "Illegal Member Access: Call(Id(Circle),Id(calArea),[])"
        self.assertTrue(TestChecker.test(input, expect, 524))

    # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=157987
    def test_main_return_something_525(self):
        input = """
        Class Program{
            main(){
                Return 123;
            }
        }    
        """
        expect = "Type Mismatch In Statement: Return(IntLit(123))"
        self.assertTrue(TestChecker.test(input, expect, 525))
    
    # For test 526 - 528
    # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158294
    def test_typemismatch_stmt_1_526(self):
        input = """
        Class Program{
            Var flag: Int = 2.2;
            main(){}
        }    
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(flag),IntType,FloatLit(2.2))"
        self.assertTrue(TestChecker.test(input, expect, 526))

    # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=157987
    def test_return_something_527(self):
        input = """
        Class Program{
            main(){
                Var _flag: Int = 3.16;
            }
        }    
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(_flag),IntType,FloatLit(3.16))"
        self.assertTrue(TestChecker.test(input, expect, 527))

    ## http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=157987
    def test_undeclared_object_528(self):
        input = """
        Class A {
            foo(){
                Var a: Array[Int, 5];
                a = Array(1, 2, 3, 4, 5);
            }
        }
        Class Program{
            main(){
                count.foo();
            }
        }    
        """
        expect = "Undeclared Identifier: count"
        self.assertTrue(TestChecker.test(input, expect, 528))

    def test_declared_object_529(self):
        input = """
        Class A {
            foo(x: Int){
                Var a: Float = x + 0.5;
            }
            Constructor(a: Int){}
        }
        Class Program{
            main(){
                {
                    Var count: A = New A(1);   
                    count.foo(123);
                    count = count.foo;
                }
            }
        }    
        """
        expect = "Undeclared Attribute: foo"
        self.assertTrue(TestChecker.test(input, expect, 529))

    # Cannot assign to constant cases 530 --> 532
    def test_cannot_assign_to_const_1(self):
        input = """
        Class A {
            Val x: Int = 123;
            baz(){
                Self.x = 6;
            }
        }
        Class Program{
            main(){
                Return;
            }
        }    
        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(x)),IntLit(6))"
        self.assertTrue(TestChecker.test(input, expect, 530))

    def test_cannot_assign_to_const_2(self):
        input = """
        Class Program{
            main(){
                Val t: Array[String, 2] = Array("Nihao", "Zaijian");
                t[1] = "Wei?";
                Return;
            }
        }
        """
        expect = """Cannot Assign To Constant: AssignStmt(ArrayCell(Id(t),[IntLit(1)]),StringLit(Wei?))"""
        self.assertTrue(TestChecker.test(input, expect, 531))

    def test_cannot_assign_to_const_3(self):
        input = """
        Class Animal {
            main(t: Int){
                Val z: String = "Nana";
                Foreach (t In -1000 .. 1000){
                    z = z +. "Nyan";
                    Continue;
                }
                Return z;
            }
        }

        Class Program {
            main(){}
            Constructor(){}
            __Destructor__(){}
        }
        """
        expect = """Cannot Assign To Constant: AssignStmt(Id(z),BinaryOp(+.,Id(z),StringLit(Nyan)))"""
        self.assertTrue(TestChecker.test(input, expect, 532))

    # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158311
    # Test type mismatch in array assignment: 533 --> 534
    def test_type_mismatch_array_assign_1(self):
        input = """
        Class A {
            Var s: String = "No";
            foo(){
                Var a: Array[Int, 2];
                a = Array(1, 2, 3);
            }
            Constructor(s: String){
                Self.s = s;
            }
        }
        Class Program{
            main(){
                Val obj: A = New A("Let's go");
                obj.foo();
            }
        }    
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[IntLit(1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 533))

    def test_type_mismatch_array_assign_2(self):
        input = """
        Class A {
            Var s: String = "No";
            Var arr: Array[Boolean, 2] = Array(False, True);
            foo(s: String){
                Self.arr = Array("Bana", "Nana");
            }
            Constructor(s: String){
                Self.s = s;
            }
        }

        Class B : A{}

        Class Program{
            main(){
                Val ab: A = New A("12\t3");
                ab.foo("xyz^%$");
                Return;
            }
        }    
        """
        expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(arr)),[StringLit(Bana),StringLit(Nana)])"
        self.assertTrue(TestChecker.test(input, expect, 534))

    # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158205
    def test_inner_static_access(self):
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
                Else {Return 5;}
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(5))"
        self.assertTrue(TestChecker.test(input, expect, 535))

    # Need to raise because Const b was assigned by a muttable variable
    def test_mismatch_in_const_decl(self):
        input = """
        Class Program{
            main(){
                Var a: Int = 1;
                Val b: Boolean = 1 == (1 + a);
            }
        }
        """
        expect = "Illegal Constant Expression: BinaryOp(==,IntLit(1),BinaryOp(+,IntLit(1),Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 536))

    # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158007
    def test_2_sides_undeclared(self):
        input = """
        Class Program{
            main(){
                a = b;
            }
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 537))

    def test_null_array_lit(self):
        input = """
        Class Program {
            main(){
                Val a: Array[Int, 1] = Array();
            }
        }
        """
        expect = "Illegal Array Literal: []"
        self.assertTrue(TestChecker.test(input, expect, 538))

    # Undeclared method/attribute
    # Self.a() while a is an attribute
    # Self.a while a is an method
    def test_access_method_using_fieldacess_39(self):
        input = """
        Class A {
            goo(){Return 1;}
            foo(){
                Var x : Int = Self.goo;
            }
        }
        Class Program {
            main(){
                Return;
            }
        }
        """
        expect = "Undeclared Attribute: goo"
        self.assertTrue(TestChecker.test(input, expect, 539))

    def test_access_attr_using_call_40(self):
        input = """
        Class A {
            Var goo : Int = 1;
            foo(){
                Var x : Int = Self.goo();
            }
        }
        Class Program {
            main(){
                Return;
            }
        }
        """
        expect = "Undeclared Method: goo"
        self.assertTrue(TestChecker.test(input, expect, 540))

    def test_field_access_41(self):
        input = """
        Class A{
            Var t: Boolean = True;
            Val $t: Boolean = False;
            foo(){
                Return Self.t;
            }
        }
        Class Program{
            Var a: A = New A();
            main(){
                Var a: A = New A();
                Var b: Boolean = False;
                b = a.t;
                b = Self.a.t;
                b = A::$t;
                Return A::$t;
            }    
        }
        """
        expect = "Type Mismatch In Statement: Return(FieldAccess(Id(A),Id($t)))"
        self.assertTrue(TestChecker.test(input, expect, 541))

    def test_call_stmt_error_42(self):
        input = """
        Class A{
            foo(a: Int){
                Return "Instance";
            }
            $foo(s: String){
                s = "No";
                Return "Static";
            }
            Constructor(x: Int){}
        }
        Class B : A{
            Var foo: A = New A(1);
        }
        Class Program{
            Var b: B = New B();
            main(){
                Var b: B = New B();
                Var s: String = "a";
                s = Self.b.foo.foo(1);
                s = b.foo.foo(1);
                A::$foo("2");
            }    
        }
        """
        expect = "Type Mismatch In Statement: Call(Id(A),Id($foo),[StringLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 542))

    def test_array_cell_43(self):
        input = """
        Class Program{
            Var s: Int = 100;
            main(){
                Var a: Array[Int, 3] = Array(7, 5, Self.s);
                Var _a: Array[Int, 2] = Array(4, 5);
                Val b: Int = 2;
                Var z: Int = 100;
                a[a[1]][2] = z + 5.1;
            }
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)]),IntLit(2)]),BinaryOp(+,Id(z),FloatLit(5.1)))"
        self.assertTrue(TestChecker.test(input, expect, 543))

    # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158293
    def test_param_is_var_44(self):
        input = """
        Class Program {
            main(){
                Return;
            }
            method(w: Int) {
                Val a: Int = w; 
            }
        }"""
        expect = "Illegal Constant Expression: Id(w)"
        self.assertTrue(TestChecker.test(input, expect, 544))
    
    # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158315
    def test_nested_array_45(self):
        input = """
        Class Program{
            Var $myArray: Array[Array[Array[Int,4],2],2] = Array(
                    Array(
                        Array(1,2,3,4),
                        Array(5,6,7,8)
                    ),
                    Array(
                        Array(-1,-2,-3,-4),
                        Array(-5,-6,-7, False)
                    )
                );
            main(){}
        }
        """
        expect = "Illegal Array Literal: [UnaryOp(-,IntLit(5)),UnaryOp(-,IntLit(6)),UnaryOp(-,IntLit(7)),BooleanLit(False)]"
        self.assertTrue(TestChecker.test(input, expect, 545))
    
    def test_illegal_array_46(self):
        input = """
        Class Program {
            main(){
                Val f : Array[Array[Int, 2], 2] = Array(Array(2, 3), Array());
                Return;
            }
        }
        """
        expect = "Illegal Array Literal: []"
        self.assertTrue(TestChecker.test(input, expect, 546))

    def test_array_cell_error_47(self):
        input = """
        Class Program{
            Var s: Int = 100;
            main(){
                Var arr: Array[String, 1] = Array("Nanahira");
                arr[Self.s*0.5] = True;
            }   
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(arr),[BinaryOp(*,FieldAccess(Self(),Id(s)),FloatLit(0.5))])"
        self.assertTrue(TestChecker.test(input, expect, 547))

    def test_default_constructor_error_1(self):
        input = """
        Class Shape{
            Var a: Int = 50;
            Constructor(x: Int){Self.a = x;}
        }
        Class Program{
            Var s: Int = 100;
            fuu(){
                Var shape: Shape = New Shape();
            }
            main(){}   
        }"""
        expect = "Type Mismatch In Expression: NewExpr(Id(Shape),[])"
        self.assertTrue(TestChecker.test(input, expect, 548))

    def test_default_constructor_error_2(self):
        input = """
        Class Shape{
            Var a: Int = 50;
        }
        Class Program{
            Var s: Int = 100;
            main(){Var shape: Shape = New Shape(Self.s);}   
        }"""
        expect = "Type Mismatch In Expression: NewExpr(Id(Shape),[FieldAccess(Self(),Id(s))])"
        self.assertTrue(TestChecker.test(input, expect, 549))

    def test_break_not_in_loop_50(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            something() {
                Var a : Int = 1;
                If (a == 1) {
                    Foreach (a In 1 .. 10 By -1) {
                        Val a : Float = 1.0;
                        Var c : Int = 1;
                        If (a >= c + 1) {
                            Foreach (c In 1 .. 2 By 1) {
                                Val d : Int = 1;
                                If (c + 1 == 1) {
                                    Continue;
                                }
                            }
                            Continue;
                        } Else {
                            Continue;
                        }
                    }
                    Break;
                }
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 550))

    def test_null_object_51(self):
        input = """
        Class A{}
        
        Class Program{
            main(){}
            Var a: A = Null;
            Var null: B = New B();
        }
        """
        expect = "Undeclared Class: B"
        self.assertTrue(TestChecker.test(input, expect, 551))

    def test_52(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            Var a : Int = 1;
            Var $b : Int = 1;
        }
        Class BCD {
            Val a : String = "";
            Val $b : Float = 0.5;
            something(){
                Var c : ABC;
                Var b : Int = c.a + 1;
                Val a : Int = 1;
                Var d : Float = ABC::$b + 1.0;
                Val e : String = Self.a +. "Hello";
                Var f : Int = a + 2 + c.a;
                Var g : Boolean = CDE::$b >= 2.0;
            }
        }"""
        expect = "Undeclared Class: CDE"
        self.assertTrue(TestChecker.test(input, expect, 552))

    def test_illegal_member_access_53(self):
        input = """
        Class ABC {
            Var a : Int = 1;
            Var $a : Int = 1;
            $b(){}
            b(){}
            c(){Return 1;}
            $c(){Return 1;}
        }
        Class Program {
            main(){
                Return;
            }
            method(){
                Var abc: ABC;
                Var b: Int = abc::$a;
            }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(abc),Id($a))"
        self.assertTrue(TestChecker.test(input, expect, 553))

    def test_type_coerce_in_decl_54(self):
        input = """
        Class Program {
            main(){
                Var x: Float = 0X1234ABCD;
                Val y: Float = 0123321;
                Val z: Float = x + y;
                Return;
            }
        }
        """
        expect = "Illegal Constant Expression: BinaryOp(+,Id(x),Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 554))

    # Test Undeclared class and Undeclared identifier
    # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158366
    def test_instance_invoke_undeclared_id_55(self):
        input = """
        Class Program{
            main() {
                Var b : Int = E.a;
                Return;
            }
        }
        """
        expect = "Undeclared Identifier: E"
        self.assertTrue(TestChecker.test(input, expect, 555))

    def test_static_invoke_undeclared_class_56(self):
        input = """
        Class Program{
            main() {
                Var b : Int = E::$a;
                Return;
            }
        }
        """
        expect = "Undeclared Class: E"
        self.assertTrue(TestChecker.test(input, expect, 556))

    def test_raise_vardecl_57(self):
        input = """
        Class Program{
            main() {
                Val a: Float = 9e4;
                Var b: Boolean = 1 + (0B101011 - 5) * 0.4 + a;
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b),BoolType,BinaryOp(+,BinaryOp(+,IntLit(1),BinaryOp(*,BinaryOp(-,IntLit(43),IntLit(5)),FloatLit(0.4))),Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 557))

    def test_default_constructor_error_58(self):
        input = """
        Class C {}
        Class A{
            Var c: C = New C(); 
            Var d: C = New C(1); 
        }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(C),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 558))
    
    def test_undeclared_class_in_var_59(self):
        input = """
        Class A {}
        Class Program{
            main() {
                Var a: C = New C();
                Return;
            }
        }
        """
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 559))

    def test_illegal_nested_arr(self):
        input = """
        Class Program {
            Var $myArray: Array[Array[Array[Int,4],2],2] = Array(
                    Array(
                        Array(1,2,3,4),
                        Array(5,6,7,8)
                    ),
                    Array(
                        Array(-1,-2,-3,-4),
                        Array(-5,-6,-7, False)
                    )
                );
            main(){}
        }
        """
        expect = "Illegal Array Literal: [UnaryOp(-,IntLit(5)),UnaryOp(-,IntLit(6)),UnaryOp(-,IntLit(7)),BooleanLit(False)]"
        self.assertTrue(TestChecker.test(input, expect, 560))

    def test_destructor_return_1(self):
        input = """
        Class Program{
            main(){}
            Destructor(){
                Var a: Program = New Program();
                Return;
            }
        }

        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 561))

    def test_if_else_62(self):
        input = """
        Class ABC {
            $a() {}
        }
        Class Program {
            main(){
                Var a, c : Boolean = True, False;
                Var b : Int = 1;
                If (a) {
                    ABC::$a();
                } Elseif (b) {
                    ABC::$a();
                } Elseif (c) {
                    ABC::$a();
                } Else {
                    ABC::$a();
                }
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: If(Id(a),Block([Call(Id(ABC),Id($a),[])]),If(Id(b),Block([Call(Id(ABC),Id($a),[])]),If(Id(c),Block([Call(Id(ABC),Id($a),[])]),Block([Call(Id(ABC),Id($a),[])]))))"
        self.assertTrue(TestChecker.test(input, expect, 562))


    def test_mismatch_expr_63(self):
        input = """
        Class Program {
            method(w, h: Int) {
                Return "Hi";
            }
            mainAAAA(){
                Var a : String = Self.method(1);
            }
            main(){
                Return;
            }
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Self(),Id(method),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 563))

    def test_const_assign_64(self):
        input = """
        Class ABC {
            Val x : Int = 1;
        }
        Class Program{
            main() {
                Var a : ABC = New ABC();
                a.x = 2;
                Return;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(a),Id(x)),IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 564))

    # Awaiting
    # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158550
    # def test_new_expr_64(self):
    #     input = """
    #     Class ABC{
    #         Constructor() {
    #             Return;
    #         }
    #         bbb(j, i: String; k: Boolean) {
    #             If (k) {
    #                 Return j;
    #             } Else {
    #                 Return i;
    #             }
    #         }
    #     }
    #     Class CED {
    #         Constructor(w, h: Int; a : String) {
    #             Var b : Boolean = a ==. "Hi";
    #             Var c : Float = w * h;
    #             Return;
    #         }
    #     }
    #     Class Program {
    #         a(w: Float; h: Int; a : ABC) {
    #             If ((a.bbb("Hello", "World", True) +. "Cool") ==. "Amazing") {
    #                 Return h + 1.0;
    #             } Else {
    #                 Return w;
    #             }
    #         }
    #         b() {
    #             Var a : ABC = New ABC();
    #             Val b : Float = Self.a(1.0, 1, a) + 1;
    #             Var c : CED = New CED(1, 2, "Hi");
    #             Self.a(1.0, 1, a);
    #         }
    #         main(){
    #             Return;
    #         }
    #         c(){}
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Call(Self(),Id(a),[FloatLit(1.0),IntLit(1),Id(a)])"
    #     self.assertTrue(TestChecker.test(input, expect, 565))
    
    def test_array_cell_66(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            somehing(w, i: Int; h, e: Float) {
                Val a : Array[Int, 1] = Array(2);
                Val b : Int = a[0];
                Val c : Array[Array[String, 1], 1] = Array(Array("1"));
                Val d : String = c[0][0];
                Val f : Array[String, 1] = c[0];
                Val g : Int = b[0];
            }
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),[IntLit(0)])"
        self.assertTrue(TestChecker.test(input, expect, 566))

    def test_coerce_in_param_1(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class A {
            foo(w: Float; z: Int; x: A){
                Return w + z;
            }
            notFoo(w: Float){
                w = Self.foo(1, 2, Null);
                Return w;
            }
            xD(){
                Self.notFoo();
            }
        }"""
        expect = "Type Mismatch In Statement: Call(Self(),Id(notFoo),[])"
        self.assertTrue(TestChecker.test(input, expect, 567))

    def test_assign_to_const_68(self):
        input = """
        Class A{
            Val y:Int=10;
        }
        Class B{
            Var x:A = New A();
            func (){
                Self.x.y = 1;
            }
        }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(FieldAccess(Self(),Id(x)),Id(y)),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 568))

    def test_assign_to_const_69(self):
        input = """
        Class A{
            $method() {
                Val a : Array[Int, 2] = Array(2, 2);
                a[0] = 1;
            }   
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(Id(a),[IntLit(0)]),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 569))

    def test_foreach_loop_70(self):
        input = """
        Class Program {
            Var x : Int = 1;
            main() {
                Return;
            }
            method() {
                Foreach (b In 1 .. 10 By 1) {
                    Val a : Int = 1;
                }
            }
        }"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 570))

    def test_foreach_loop_71(self):
        input = """
        Class Program {
            Var x : Int = 1;
            main() {
                Return;
            }
            method() {
                Var b : String = "Hello";
                Foreach (b In 100 .. 10000 By -1) {
                    Val a : Int = 1;
                }
            }
        }"""
        expect = "Type Mismatch In Statement: For(Id(b),IntLit(100),IntLit(10000),UnaryOp(-,IntLit(1)),Block([ConstDecl(Id(a),IntType,IntLit(1))])])"
        self.assertTrue(TestChecker.test(input, expect, 571))

    def test_cannot_assign_const_for_loop_47(self):
        input = """
        Class Program {
            Var x : Int = 1;
            main() {
                Return;
            }
            method() {
                Val b : Int = 1;
                Foreach (b In 100 .. 10000 By 1) {
                    Val a : Int = 1;
                }
            }
        }"""
        expect = "Cannot Assign To Constant: AssignStmt(Id(b),IntLit(100))"
        self.assertTrue(TestChecker.test(input, expect, 572))
