import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_param_is_var(self):
        input = """
        Class Program {
            main(){
                Return;
            }
            method(w: Int) {
                Val a : Int = w;
            }
        }"""
        expect = "Illegal Constant Expression: Id(w)"
        self.assertTrue(TestChecker.test(input, expect, 1001))

    def test_recursive_class_1(self):
        input = """
        Class A{
            Constructor(){}
            Var $a : A = New A();
            Var a : A = A::$a;
        }
        Class Program {
            main(){
                Var b : A = New A();
                Val b : Int = 1;
                Return;
            }
        }"""
        expect = "Redeclared Constant: b"
        self.assertTrue(TestChecker.test(input, expect, 1002))

    def test_order_check_assign(self):
        input = """
        Class Program {
            main(){
                a = b;
                Return;
            }
        }"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 1003))


    def test_mismatch_statment_1(self):
        input = """
        Class A{
            Var a : Int = 1.1;
        }
        Class Program {
            main(){
                Return;
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,FloatLit(1.1))"
        self.assertTrue(TestChecker.test(input, expect, 1004))

    def test_mismatch_statment_2(self):
        input = """
        Class Program {
            main(){
                Var a : Int = 1.1;
                Return;
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,FloatLit(1.1))"
        self.assertTrue(TestChecker.test(input, expect, 1005))  

    def test_mismatch_statment_3(self):
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
        self.assertTrue(TestChecker.test(input, expect, 1006))

    def test_mismatch_statment_4(self):
        input = """
        Class Program {
            method(w, h: Int) {
            }
            mainAAAA(){
                Self.method(1);
            }
            main(){
                Return;
            }
        }"""
        expect = "Type Mismatch In Statement: Call(Self(),Id(method),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 1007))

    def test_typemismatch_08(self):
        input = """
        Class ABC {
        }
        Class Program {
            main(){
                Var a : Boolean = 1 == True;
                Return;
            }
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(==,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 1008))  

    def test_random_thing_09(self):
        input = """
        Class ABC {
        }
        Class Program {
            main(){
                Var a : Int = 1 + ABC;
                Return;
            }
        }"""
        expect = "Undeclared Identifier: ABC"
        self.assertTrue(TestChecker.test(input, expect, 1009))

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
                Else {Return;}
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 1010))

    def test_array_literal_3(self):
        input = """
        Class Program {
            main(){
                Val f : Array[Array[Int, 2], 2] = Array(Array(2, 3), Array());
                Return;
            }
        }
        """
        expect = "Illegal Array Literal: []"
        self.assertTrue(TestChecker.test(input, expect, 1011))

    def test_random_thing_12(self):
        input = """
        Class Program {
            Var a: Int = 20;
            main() {
                a = 10;
            }
        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 1012))

    def test_random_thing_13(self):
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
        self.assertTrue(TestChecker.test(input, expect, 1013))

    def test_random_thing_14(self):
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
        self.assertTrue(TestChecker.test(input, expect, 1014))

    def test_random_thing_15(self):
        input = """
        Class Program{
            Var a : Int = 1;
            Var b : Int = a; 
            main() {
                Return;
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 1015))

    def test_random_thing_16(self):
        input = """
        Class Program{
            main() {
                Var a:Array[Int,2];
                a = Array(1,2,3);
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[IntLit(1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 1016))

    def test_random_thing_17(self):
        input = """
        Class Program{
            main() {
                Var a:Array[Int,2];
                a = Array("a","b");
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[StringLit(a),StringLit(b)])"
        self.assertTrue(TestChecker.test(input, expect, 1017))

    def test_random_thing_18(self):
        input = """
        Class Car {
            Var a : Int = 10;
            foo() {
                Var x : Int = a;
            }
        }
        Class Program{
            main() {
                Return;
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 1018))

    def test_default_constructor_1(self):
        input = """
        Class ABC {}
        Class Program{
            main() {
                Var a : ABC = New ABC();
                Val a : Int = 1;
                Return;
            }
        }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 1019))

    def test_default_constructor_2(self):
        input = """
        Class ABC {
            Constructor(w: Int) {}
        }
        Class Program{
            main() {
                Var a : ABC = New ABC(1);
                Var b : ABC = New ABC();
                Return;
            }
        }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(ABC),[])"
        self.assertTrue(TestChecker.test(input, expect, 1020))

    def test_random_thing_21(self):
        input = """
        Class Program{
            main() {
                Return;
            }
            main(w: Int) {}
        }
        """
        expect = "Redeclared Method: main"
        self.assertTrue(TestChecker.test(input, expect, 1021))

    def test_random_thing_22(self):
        input = """
        Class Program{
            main() {
                Return;
            }
        }
        Class Programming {
            A(){ Self.B(); }
            B(){}
        }
        """
        expect = "Undeclared Method: B"
        self.assertTrue(TestChecker.test(input, expect, 1022))

    def test_random_thing_23(self):
        input = """
        Class Program{
            main() {
                Var x : Int = 1.2;
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(x),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 1023))

    def test_random_thing_24(self):
        input = """
        Class Program {
            Var a : Int;
            a() {}
            main(){
                Return;
                Val a : Int = Self.a;
            }
        }
        """
        expect = "Illegal Constant Expression: FieldAccess(Self(),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 1024))

    def test_random_thing_25(self):
        input = """
        Class Program {
            main(){
                Var a : Int = 1;
                Foreach (x In 1 .. 10 By 2) {
                    Break;
                    Break;
                    a = "ABC";
                }
                Return;
            }
        }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 1025))

    def test_random_thing_26(self):
        input = """
        Class Program {
            Val a : Int = 1;
            mainAAA(){
                Val a : Int = Self.a;
                Val b : Int = a;
                Return;
            }
            main() {
                Return;
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 1026))

    def test_random_thing_27(self):
        input = """
        Class C {}
        Class A{
            Var c: C = New C(); 
            Var d: C = New C(1); 
        }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(C),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 1027))

    def test_random_thing_28(self):
        input = """
        Class Program{
            main() {
                Val a: Int = a;
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 1028))

    def test_random_thing_29(self):
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
        self.assertTrue(TestChecker.test(input, expect, 1029))
    
    # # Undone
    # def test_random_thing_30(self):
    #     input = """
    #     Class ABC {
    #         Var x : Int = 1;
    #     }
    #     Class Program{
    #         main() {
    #             Val a : ABC = New ABC();
    #             a.x = 2;
    #             Return;
    #         }
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 1030))

    def test_random_thing_31(self):
        input = """
        Class ABC {
            Var x : Int = 1;
        }
        Class Program{
            main() {
                Var a : Int = ABC.x;
            }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(ABC),Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 1031))

    def test_random_thing_32(self):
        input = """
        Class CED {
            Var c : Int;
        }
        Class ABC {
            Var ced : CED;
        }
        Class Program{
            main() {
                Val x : Int = ABC.ced.c;
            }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(ABC),Id(ced))"
        self.assertTrue(TestChecker.test(input, expect, 1032))

    def test_chaining_immutable(self):
        input = """
        Class A{
            Val y: Int = 10;
        }
        Class B{
            Var x: A;
            func(){
                Val z: Int = Self.x.y;
            }
        }
        Class Program{
            main(){}
        }
        """
        expect = "Illegal Constant Expression: FieldAccess(FieldAccess(Self(),Id(x)),Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 1033))

    def test_random_thing_34(self):
        input = """
        Class Program{
            main() {
                Var b : Int = E::$a;
                Return;
            }
        }
        """
        expect = "Undeclared Class: E"
        self.assertTrue(TestChecker.test(input, expect, 1034))

    def test_random_thing_35(self):
        input = """
        Class Program{
            main() {
                Var b : Int = E.a;
                Return;
            }
        }
        """
        expect = "Undeclared Identifier: E"
        self.assertTrue(TestChecker.test(input, expect, 1035))

    def test_random_thing_36(self):
        input = """
        Class Program {
            main(){
                Var a : Int = 1;
                Val b : Array[Int, 2] = Array(1, a);
                Return;
            }
        }
        """
        expect = "Illegal Constant Expression: [IntLit(1),Id(a)]"
        self.assertTrue(TestChecker.test(input, expect, 1036))

    def test_random_thing_37(self):
        input = """
        Class A{}
        Class B{}
        Class Program {
            Var x: A = New B();
            main(){
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(x),ClassType(Id(A)),NewExpr(Id(B),[]))"
        self.assertTrue(TestChecker.test(input, expect, 1037))

    def test_random_thing_38(self):
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
        self.assertTrue(TestChecker.test(input, expect, 1038))

    # # Awaiting
    # def test_random_thing_39(self):
    #     input = """
    #     Class ABC {
    #         $a() {}
    #     }
    #     Class Program {
    #         main(){
    #             Var a, c : Boolean = True, False;
    #             Var b : Int = 1;
    #             If (a) {
    #                 ABC::$a();
    #             } Elseif (b) {
    #                 ABC::$a();
    #             } Elseif (c) {
    #                 ABC::$a();
    #             } Else {
    #                 ABC::$a();
    #             }
    #             Return;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: If(Id(b),Block([Call(Id(ABC),Id($a),[])]),If(Id(c),Block([Call(Id(ABC),Id($a),[])]),Block([Call(Id(ABC),Id($a),[])])))"
    #     self.assertTrue(TestChecker.test(input, expect, 1039))

    def test_random_thing_40(self):
        input = """
        Class A{
            Val x : Int = 1;
        }
        Class B : A {
            x(w: Int) {
                Return Self.x;
            }
        }
        Class Program {
            main(){
                Var b : B;
                Var a : Int = b.x(1);
                Val a : String = "Hi";
                Return;
            }
        }"""
        expect = "Undeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 1040))

    def test_random_thing_41(self):
        input = """
        Class Program{
            main() {
                Return;
            }
        }
        Class A: B{}
        Class B{}
        """
        expect = "Undeclared Class: B"
        self.assertTrue(TestChecker.test(input, expect, 1041))

    # Awaiting no Return; or Return None;
    def test_random_thing_42(self):
        input = """
        Class P {
            Destructor() {
                Return;
            }
        }
        Class Program {
            main() {
                Var p : P;
                Val a : Int = 1.2;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 1042))

    def test_random_thing_43(self):
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
        self.assertTrue(TestChecker.test(input, expect, 1043))

    def test_random_thing_44(self):
        input = """
        Class A{
            $method() {
                Val a : Array[Int, 2] = Array(2, 2);
                a[0] = 1;
            }   
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(Id(a),[IntLit(0)]),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 1044))

    def test_foreach_loop_45(self):
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
        self.assertTrue(TestChecker.test(input, expect, 1045))

    def test_foreach_loop_46(self):
        input = """
        Class Program {
            Var x : Int = 1;
            main() {
                Return;
            }
            method() {
                Var b : String = "Hello";
                Foreach (b In 100 .. 10000 By 1) {
                    Val a : Int = 1;
                }
            }
        }"""
        expect = "Type Mismatch In Statement: For(Id(b),IntLit(100),IntLit(10000),IntLit(1),Block([ConstDecl(Id(a),IntType,IntLit(1))])])"
        self.assertTrue(TestChecker.test(input, expect, 1046))


    def test_foreach_loop_47(self):
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
        self.assertTrue(TestChecker.test(input, expect, 1047))

    def test_self_inheritance(self):
        input = """
        Class A : A{}
        Class Program{main(){}}
        """
        expect = "Undeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 1048))

    def test_constructor_1(self):
        input = """
        Class C {
            Constructor(w : Int){}
            Constructor(){}
        }
        Class A{
            Var c: C = New C(); 
            Var d: C = New C(1); 
        }
        """
        expect = "Redeclared Method: Constructor"
        self.assertTrue(TestChecker.test(input, expect, 1049))

    def test_destructor_1(self):
        input = """
        Class C {
            Destructor(){}
            Destructor(){
                Val a : Int = 1;
            }
        }
        Class A{
            Var c: C = New C(); 
            Var d: C = New C(1); 
        }
        """
        expect = "Redeclared Method: Destructor"
        self.assertTrue(TestChecker.test(input, expect, 1050))

    def test_random_thing_51(self):
        input = """
        Class A {
            Var a : Int = 1.2;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 1051))

    def test_self_inheritance(self):
        input = """
        Class A : A{}
        Class Program{main(){}}
        """
        expect = "Undeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 1052))

    def test_illegal_const_arr_1(self):
        input = """
        Class Program{
            Var a: Int = 10; 
            foo() { 
                Val a : Array[Int, 3] = Array(Self.a, 1, 2);
                Val b : Int = a[0];
            }
            main(){}
        }
        """
        expect = "Illegal Constant Expression: [FieldAccess(Self(),Id(a)),IntLit(1),IntLit(2)]"
        self.assertTrue(TestChecker.test(input, expect, 1053))

    def test_confused_array(self):
        input = """
        Class A {
            Var d, e: Int;
            Val f: Array[Array[Int,1], 2] = Array( Array(Self.d), Array(Self.e) );
        }
        Class Program{main(){}}
        """
        expect = "Illegal Constant Expression: [[FieldAccess(Self(),Id(d))],[FieldAccess(Self(),Id(e))]]"
        self.assertTrue(TestChecker.test(input, expect, 1054))
