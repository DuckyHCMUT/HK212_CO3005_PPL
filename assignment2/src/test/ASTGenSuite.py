import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program_401(self):
        """ Simple program with nothing
            First testcase from BKEL """
        input = """
        Class Program{

        }
        """
        expect = """Program([ClassDecl(Id(Program),[])])"""
        self.assertTrue(TestAST.test(input, expect, 401))

    def test_simple_program_402(self):
        """ Simple program with nothing
        Second testcase from BKEL """
        input = "Class Rectangle : Shape {}"
        expect = """Program([ClassDecl(Id(Rectangle),Id(Shape),[])])"""
        self.assertTrue(TestAST.test(input, expect, 402))

    def test_simple_program_403(self):
        """ Simple program with nothing
        Third testcase from BKEL """
        input = """
        Class Rectangle {
            Var length: Int;
        }"""
        expect = """Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(length),IntType))])])"""
        self.assertTrue(TestAST.test(input, expect, 403))
        
    def test_simple_program_404(self):
        """Simple program, with few class members"""
        input = """
        Class Rectangle {
            Var b, c, $d, $e, _f: Float = 10, -20.1, 30.2, 40.3, 50.4 - 1;
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(10))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,UnaryOp(-,FloatLit(20.1)))),AttributeDecl(Static,VarDecl(Id($d),FloatType,FloatLit(30.2))),AttributeDecl(Static,VarDecl(Id($e),FloatType,FloatLit(40.3))),AttributeDecl(Instance,VarDecl(Id(_f),FloatType,BinaryOp(-,FloatLit(50.4),IntLit(1))))])])"
        self.assertTrue(TestAST.test(input, expect, 404))

    def test_simple_program_405(self):
        """Simple program, with few class members"""
        input = """
        Class Program{
            Var x, $y, z: Int;
            Val t: Float = 3.108;
            Var f: Float;
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(x),IntType)),AttributeDecl(Static,VarDecl(Id($y),IntType)),AttributeDecl(Instance,VarDecl(Id(z),IntType)),AttributeDecl(Instance,ConstDecl(Id(t),FloatType,FloatLit(3.108))),AttributeDecl(Instance,VarDecl(Id(f),FloatType))])])"""
        self.assertTrue(TestAST.test(input, expect, 405))

    def test_simple_program_406(self):
        """Simple program, with nothing but inheritance and many classes"""
        input = """
        Class Program : Parent{}
        Class Subprogram{}
        """
        expect = """Program([ClassDecl(Id(Program),Id(Parent),[]),ClassDecl(Id(Subprogram),[])])"""
        self.assertTrue(TestAST.test(input, expect, 406))

    def test_simple_program_407(self):
        """Simple program, with an array attribute member"""
        input = """
        Class Program{
            Var arr: Array[Array[Float, 2], 1];
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(1,ArrayType(2,FloatType))))])])"""
        self.assertTrue(TestAST.test(input, expect, 407))

    def test_simple_program_408(self):
        """Simple program, with few assigned array attribute member"""
        input = """
        Class Program{
            Var arr, brr: Array[Int, 3] = Array(1, 2, 3), Array(5, -4, 1);
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(3,IntType),[IntLit(1),IntLit(2),IntLit(3)])),AttributeDecl(Instance,VarDecl(Id(brr),ArrayType(3,IntType),[IntLit(5),UnaryOp(-,IntLit(4)),IntLit(1)]))])])"""
        self.assertTrue(TestAST.test(input, expect, 408))

    def test_simple_program_409(self):
        """Simple program, with assigned member that are expression"""
        input = """
        Class Program{
            Val a: Int = 4 + 5;
            Var $b: Float = a + 2.3;
            Val c, d: Int = 0x413EFFAB, 0B0;
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(+,IntLit(4),IntLit(5)))),AttributeDecl(Static,VarDecl(Id($b),FloatType,BinaryOp(+,Id(a),FloatLit(2.3)))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,IntLit(1094647723))),AttributeDecl(Instance,ConstDecl(Id(d),IntType,IntLit(0)))])])"""
        self.assertTrue(TestAST.test(input, expect, 409))

    def test_simple_program_410(self):
        """Simple program, with an assigned array attribute member that is nested array (mtd_array)"""
        input = """
        Class Program{
            Val arr, $brr: Array[Array[Float, 2], 3] = Array(Array(2.1, -1.3), Array(0.1, 3.1e3), Array(-0.00001, 123.321E-123)), Array(Array(1.2, 0.132), Array(0.9931, 10.1e3), Array(0.00001111, 1111111119.332321e-2));
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(arr),ArrayType(3,ArrayType(2,FloatType)),[[FloatLit(2.1),UnaryOp(-,FloatLit(1.3))],[FloatLit(0.1),FloatLit(3100.0)],[UnaryOp(-,FloatLit(1e-05)),FloatLit(1.23321e-121)]])),AttributeDecl(Static,ConstDecl(Id($brr),ArrayType(3,ArrayType(2,FloatType)),[[FloatLit(1.2),FloatLit(0.132)],[FloatLit(0.9931),FloatLit(10100.0)],[FloatLit(1.111e-05),FloatLit(11111111.19332321)]]))])])"""
        self.assertTrue(TestAST.test(input, expect, 410))

    def test_simple_program_411(self):
        """Simple program, with an attribute and a method with variable"""
        input = """
        Class Program {
            Val $c: Int = 0x413EFFAB;
            main(){
                Var f: Int = 0x413EFFAB;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($c),IntType,IntLit(1094647723))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(f),IntType,IntLit(1094647723))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 411))

    def test_method_412(self):
        """Simple program, with a param-passed method with variable"""
        input = """
        Class Program{
            notMain(f: Boolean; arr: Array[Array[Float, 3], 4]){
                Val a, b, c: Int = 500, 600, 700;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(notMain),Instance,[param(Id(f),BoolType),param(Id(arr),ArrayType(4,ArrayType(3,FloatType)))],Block([ConstDecl(Id(a),IntType,IntLit(500)),ConstDecl(Id(b),IntType,IntLit(600)),ConstDecl(Id(c),IntType,IntLit(700))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 412))

    def test_simple_program_413(self):
        """Simple program, with a param-passed method with variable"""
        input = """
        Class Program{
            notMain(f: Boolean){
                Val a, b: Array[Int, 4] = Array(1, 0B101011, 03132, 0x123), Array(-4, 31, 0xEFFE, 5);
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(notMain),Instance,[param(Id(f),BoolType)],Block([ConstDecl(Id(a),ArrayType(4,IntType),[IntLit(1),IntLit(43),IntLit(1626),IntLit(291)]),ConstDecl(Id(b),ArrayType(4,IntType),[UnaryOp(-,IntLit(4)),IntLit(31),IntLit(61438),IntLit(5)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 413))

    def test_simple_program_414(self):
        """Simple program, to check output of other than Decimal-base Integer"""
        input = """
        Class Program{
            Val a, b, $c, $d, e, $f: Int = 037415, 1239651, 0x1239EDF, 0xABCDEF01, 0b1000101, 0B110101;
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(16141))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(1239651))),AttributeDecl(Static,ConstDecl(Id($c),IntType,IntLit(19111647))),AttributeDecl(Static,ConstDecl(Id($d),IntType,IntLit(2882400001))),AttributeDecl(Instance,ConstDecl(Id(e),IntType,IntLit(69))),AttributeDecl(Static,ConstDecl(Id($f),IntType,IntLit(53)))])])"""
        self.assertTrue(TestAST.test(input, expect, 414))

    def test_simple_program_415(self):
        """Simple program, to check output of other than Decimal-base Integer"""
        input = """
        Class Program{
            main(inp: Int){
                Var a: Float;
                a = 3.5031041095815;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(inp),IntType)],Block([VarDecl(Id(a),FloatType),AssignStmt(Id(a),FloatLit(3.5031041095815))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 415))

    def test_simple_program_416(self):
        """Simple program, to check assignment statement of array cell"""
        input = """
        Class Program{
            main(){
                Var a: Array[Boolean, 4];
                a[0] = True;
                a[1] = a[0];
                a[1 + 1] = False;
                a[0xC / 0b100] = True;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(4,BoolType)),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),ArrayCell(Id(a),[IntLit(0)])),AssignStmt(ArrayCell(Id(a),[BinaryOp(+,IntLit(1),IntLit(1))]),BooleanLit(False)),AssignStmt(ArrayCell(Id(a),[BinaryOp(/,IntLit(12),IntLit(4))]),BooleanLit(True))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 416))

    def test_simple_program_417(self):
        """Simple program, to check assignment statement of multidimensional array cell"""
        input = """
        Class Program{
            main(){
                Var a: Array[Array[Boolean, 3], 2];
                a[0][0] = True;
                a[0][1] = False;
                a[1][0] = True;
                a[1][1] = False;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(2,ArrayType(3,BoolType))),AssignStmt(ArrayCell(Id(a),[IntLit(0),IntLit(0)]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[IntLit(0),IntLit(1)]),BooleanLit(False)),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(0)]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(1)]),BooleanLit(False))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 417))

    def test_simple_program_418(self):
        """Simple program, to check assignment statement of multidimensional array cell"""
        input = """
        Class Program{
            main(){
                Var a: Array[Array[Boolean, 2], 2];
                a[0][0 * 10000000] = True;
                a[0][3 * 2 * 1 / 6] = False;
                a[0x270F / 9999][0 * 0B1011110101] = True;
                a[9999 / 0x270F][1 * 9 / 9 + 0] = Sys.sampleArray[a[0x1]];
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(2,ArrayType(2,BoolType))),AssignStmt(ArrayCell(Id(a),[IntLit(0),BinaryOp(*,IntLit(0),IntLit(10000000))]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[IntLit(0),BinaryOp(/,BinaryOp(*,BinaryOp(*,IntLit(3),IntLit(2)),IntLit(1)),IntLit(6))]),BooleanLit(False)),AssignStmt(ArrayCell(Id(a),[BinaryOp(/,IntLit(9999),IntLit(9999)),BinaryOp(*,IntLit(0),IntLit(757))]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[BinaryOp(/,IntLit(9999),IntLit(9999)),BinaryOp(+,BinaryOp(/,BinaryOp(*,IntLit(1),IntLit(9)),IntLit(9)),IntLit(0))]),ArrayCell(FieldAccess(Id(Sys),Id(sampleArray)),[ArrayCell(Id(a),[IntLit(1)])]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 418))

    def test_simple_program_419(self):
        """Simple program, with rhs (all_expr) is a mtd_array"""
        input = """
        Class Program{
            Var a: Array[Array[Boolean, 2], 1];
            main(){
                Var b: Boolean = a[0][2];
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(1,ArrayType(2,BoolType)))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(b),BoolType,ArrayCell(Id(a),[IntLit(0),IntLit(2)]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 419))

    def test_simple_program_420(self):
        """Simple program, with lhs is a nested array call"""
        input = """
        Class Program{
            Var a: Array[Array[Boolean, 2], 1];
            main(){
                a[b[1]] = 123;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(1,ArrayType(2,BoolType)))),MethodDecl(Id(main),Static,[],Block([AssignStmt(ArrayCell(Id(a),[ArrayCell(Id(b),[IntLit(1)])]),IntLit(123))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 420))

    def test_simple_program_421(self):
        """Simple program, with instance field access and call expr"""
        input = """
        Class Program{
            main(){
                a = Prog.b(e, f, g);
                b = Program.a;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),CallExpr(Id(Prog),Id(b),[Id(e),Id(f),Id(g)])),AssignStmt(Id(b),FieldAccess(Id(Program),Id(a)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 421))

    def test_simple_program_422(self):
        """Simple program, with static field access and call expr"""
        input = """
        Class Program{
            main(){
                a = Prog::$b(e, f, g);
                b = Program::$a;
                c = Self::$f;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),CallExpr(Id(Prog),Id($b),[Id(e),Id(f),Id(g)])),AssignStmt(Id(b),FieldAccess(Id(Program),Id($a))),AssignStmt(Id(c),FieldAccess(Self(),Id($f)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 422))

    def test_simple_program_423(self):
        """Simple program, spiderman pointing at each other"""
        input = """
        Class Program{
            Val $a: Int = 5;
            Constructor(){
                Program::$a = Self::$a;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($a),IntType,IntLit(5))),MethodDecl(Id("Constructor"),Instance,[],Block([AssignStmt(FieldAccess(Id(Program),Id($a)),FieldAccess(Self(),Id($a)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 423))

    def test_short_program_424(self):
        """Simple program with partial If statement"""
        input = """
        Class Program{
            main(){
                If (a > b){
                    a = 2;
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(2))]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 424))

    def test_short_program_425(self):
        """Simple program with partial If - Elseif statement"""
        input = """
        Class Program{
            main(){
                If (a > b){
                    a = 2;
                }
                Elseif (a == b){
                    a = 1;
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(2))]),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(1))])))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 425))

    def test_short_program_426(self):
        """Simple program with Complete If - Elseif - Else statement"""
        input = """
        Class Program{
            main(){
                If (a > b){
                    a = 2;
                }
                Elseif (a == b){
                    a = 1;
                }
                Else{
                    a = 0;
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(2))]),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(1))]),Block([AssignStmt(Id(a),IntLit(0))])))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 426))

    def test_short_program_427(self):
        """Simple program with partial ForEach loop statement"""
        input = """
        Class Program{
            main(){
                Foreach (a In 1 .. 100000){
                    Global::$b = a + 2;
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(a),IntLit(1),IntLit(100000),IntLit(1),Block([AssignStmt(FieldAccess(Id(Global),Id($b)),BinaryOp(+,Id(a),IntLit(2)))])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 427))

    def test_short_program_428(self):
        """Short program with complete ForEach loop statement"""
        input = """
        Class Program{
            main(){
                Foreach (a In 1 .. 100000 By 5){
                    Global::$b = a + 2;
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(a),IntLit(1),IntLit(100000),IntLit(5),Block([AssignStmt(FieldAccess(Id(Global),Id($b)),BinaryOp(+,Id(a),IntLit(2)))])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 428))

    def test_short_program_429(self):
        """Simple program with Complete If - Elseif - Else statement (2 Elseif)"""
        input = """
        Class Program : System{
            Val a: Int = 1;
            fooBar() {
                Self::$fooBar();
            }
            main() {
                If (1 >= 2) {
                    Out.fooBar(True);
                } 
                Elseif (a <= 2) {
                    Self::$fooBar();
                } 
                Elseif (a[1][2] <= a[1] * a.a + Some::$a()) {
                    Out.println(g, f, e, _);
                } 
                Else {
                    Out.println("What are you looking for?");
                }
                Return;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),Id(System),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(1))),MethodDecl(Id(fooBar),Instance,[],Block([Call(Self(),Id($fooBar),[])])),MethodDecl(Id(main),Static,[],Block([If(BinaryOp(>=,IntLit(1),IntLit(2)),Block([Call(Id(Out),Id(fooBar),[BooleanLit(True)])]),If(BinaryOp(<=,Id(a),IntLit(2)),Block([Call(Self(),Id($fooBar),[])]),If(BinaryOp(<=,ArrayCell(Id(a),[IntLit(1),IntLit(2)]),BinaryOp(+,BinaryOp(*,ArrayCell(Id(a),[IntLit(1)]),FieldAccess(Id(a),Id(a))),CallExpr(Id(Some),Id($a),[]))),Block([Call(Id(Out),Id(println),[Id(g),Id(f),Id(e),Id(_)])]),Block([Call(Id(Out),Id(println),[StringLit(What are you looking for?)])])))),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 429))

    def test_short_program_430(self):
        """Simple program with 2 methods and 1 return on main"""
        input = """
        Class Program {
            Val a: Int = 1;
            fooBar(a, b : Int; c : Float) {
                Self.fooBar1(True, False, Null);
            }
            main() {
                Self.fooBar(x, y, "ZhongGuo ren");
                Return;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(1))),MethodDecl(Id(fooBar),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],Block([Call(Self(),Id(fooBar1),[BooleanLit(True),BooleanLit(False),NullLiteral()])])),MethodDecl(Id(main),Static,[],Block([Call(Self(),Id(fooBar),[Id(x),Id(y),StringLit(ZhongGuo ren)]),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 430))

    def test_float_convert_431(self):
        """Simple program to test the conversion of invalid python float literal (.e-3)"""
        input = """
        Class Program {
            main() {
                Out.println(.e-3);
            }
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(println),[FloatLit(0.0)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 432))

    def test_foreach_loop_432(self):
        """Simple program to test missing and complete Foreach loop"""
        input = """
        Class Program {
            Val b: Float = .e-3;
            main() {
                ## Missing incremental value ##
                Foreach(a In 1 .. 0x1234ABCD){
                    b = b + a / 5;
                }
                Foreach(a In -5 .. 0b1101 By 04){
                    b = b - b / (03);
                }
                Return b;
            }
        }"""
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(b),FloatType,FloatLit(0.0))),MethodDecl(Id(main),Static,[],Block([For(Id(a),IntLit(1),IntLit(305441741),IntLit(1),Block([AssignStmt(Id(b),BinaryOp(+,Id(b),BinaryOp(/,Id(a),IntLit(5))))])]),For(Id(a),UnaryOp(-,IntLit(5)),IntLit(13),IntLit(4),Block([AssignStmt(Id(b),BinaryOp(-,Id(b),BinaryOp(/,Id(b),IntLit(3))))])]),Return(Id(b))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 432))

    def test_none_const_433(self):
        """Simple program to test None in ConstDecl"""
        input = """
        Class Program{
            Val $obj: Circle;
            Val obj2: Circle = New Circle(1, 2);
            main(){      
                Val a, b: Int;
                Val d, e: Float;
                Return (obj2.radius * 3.14) + a - b / d * e;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($obj),ClassType(Id(Circle)),None)),AttributeDecl(Instance,ConstDecl(Id(obj2),ClassType(Id(Circle)),NewExpr(Id(Circle),[IntLit(1),IntLit(2)]))),MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),IntType,None),ConstDecl(Id(b),IntType,None),ConstDecl(Id(d),FloatType,None),ConstDecl(Id(e),FloatType,None),Return(BinaryOp(-,BinaryOp(+,BinaryOp(*,FieldAccess(Id(obj2),Id(radius)),FloatLit(3.14)),Id(a)),BinaryOp(*,BinaryOp(/,Id(b),Id(d)),Id(e))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 433))

    def test_new_expr_434(self):
        """Simple program to test scalar id of Foreach (Scrapped, for assignment 3)"""
        input = """
        Class Program{
            Val $obj: Circle = New Circle();
            Val obj2: Circle = New Circle(obj2);
            main(){      
                Var circle3: Circle = New Circle(1, 2);
                Return (circle3);
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($obj),ClassType(Id(Circle)),NewExpr(Id(Circle),[]))),AttributeDecl(Instance,ConstDecl(Id(obj2),ClassType(Id(Circle)),NewExpr(Id(Circle),[Id(obj2)]))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(circle3),ClassType(Id(Circle)),NewExpr(Id(Circle),[IntLit(1),IntLit(2)])),Return(Id(circle3))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 434))

    def test_return_435(self):
        """Simple program to test Return with or without expr"""
        input = """
        Class Program{
            Var $str: String = "From Class Program: ";
            main(){      
                Var circle: Circle = New Circle(math.pi, 4);
                Return circle;
            }
            print(s: String){
                System.out.println(s + " says hello to the world!");
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,VarDecl(Id($str),StringType,StringLit(From Class Program: ))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(circle),ClassType(Id(Circle)),NewExpr(Id(Circle),[FieldAccess(Id(math),Id(pi)),IntLit(4)])),Return(Id(circle))])),MethodDecl(Id(print),Instance,[param(Id(s),StringType)],Block([Call(FieldAccess(Id(System),Id(out)),Id(println),[BinaryOp(+,Id(s),StringLit( says hello to the world!))]),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 435))

    def test_constructor_destructor_436(self):
        """Simple program to test Constructor and Destructor"""
        input = """
        Class Node{
            Var $key: Int;
            Var $value: String;
            Constructor(key: Int; value: String){
                Self::$key = key;
                Self::$value = value;
                Val pair: Pair = New Pair(Self::$key, Self::$value);
                System.print("Object " + System.toString(Self.__str__()) + " has been created !");
                System.print("Pair is: ", pair);
            }
            Destructor(){
                Self.destroy();
                System.print("Object " + System.toString(Self.__str__()) + " has been destroyed !");
            }
            destroy(){
                System.delete(Self);
            }
        }
        """
        expect = """Program([ClassDecl(Id(Node),[AttributeDecl(Static,VarDecl(Id($key),IntType)),AttributeDecl(Static,VarDecl(Id($value),StringType)),MethodDecl(Id("Constructor"),Instance,[param(Id(key),IntType),param(Id(value),StringType)],Block([AssignStmt(FieldAccess(Self(),Id($key)),Id(key)),AssignStmt(FieldAccess(Self(),Id($value)),Id(value)),ConstDecl(Id(pair),ClassType(Id(Pair)),NewExpr(Id(Pair),[FieldAccess(Self(),Id($key)),FieldAccess(Self(),Id($value))])),Call(Id(System),Id(print),[BinaryOp(+,BinaryOp(+,StringLit(Object ),CallExpr(Id(System),Id(toString),[CallExpr(Self(),Id(__str__),[])])),StringLit( has been created !))]),Call(Id(System),Id(print),[StringLit(Pair is: ),Id(pair)])])),MethodDecl(Id("Destructor"),Instance,[],Block([Call(Self(),Id(destroy),[]),Call(Id(System),Id(print),[BinaryOp(+,BinaryOp(+,StringLit(Object ),CallExpr(Id(System),Id(toString),[CallExpr(Self(),Id(__str__),[])])),StringLit( has been destroyed !))])])),MethodDecl(Id(destroy),Instance,[],Block([Call(Id(System),Id(delete),[Self()])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 436))

    def test_simple_program_437(self):
        """ Test declared and not-declared variable/attribute """
        input = """
        Class B : C{
            Val a : Int = 100;
            Val $b : Float = 123.303E3;
            Var $_: Boolean;
            Val _: Any = New Any();
            Constructor(){
                a = New C();
                Self::$b = New B();
                Return;
            }
        }
        Class Program {
            main() {
                Val a : A = New A();
                a::$b();
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(B),Id(C),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(100))),AttributeDecl(Static,ConstDecl(Id($b),FloatType,FloatLit(123303.0))),AttributeDecl(Static,VarDecl(Id($_),BoolType)),AttributeDecl(Instance,ConstDecl(Id(_),ClassType(Id(Any)),NewExpr(Id(Any),[]))),MethodDecl(Id("Constructor"),Instance,[],Block([AssignStmt(Id(a),NewExpr(Id(C),[])),AssignStmt(FieldAccess(Self(),Id($b)),NewExpr(Id(B),[])),Return()]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),ClassType(Id(A)),NewExpr(Id(A),[])),Call(Id(a),Id($b),[]),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 437))

    def test_empty_block_stmt_438(self):
        input = """
        Class Program{
            main(){
                {} {} {} {}       
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Block([]),Block([]),Block([]),Block([])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 438))
    
    def test_block_stmt_439(self):
        input = """
        Class Sys_Clone : System{
            classWorker(){
                {
                    Val a : Int = 100;
                    Var _: Any = New Any();
                    _.getVar() = 100_000_000_000;
                } 
                {
                    a = True;
                    b = False;
                    Return;
                } 
                {
                    Foreach (i In 0 .. rows1 By 1) {
                        Foreach (j In 0 .. col2 By (0 + 1) * 2 - 1) {
                            c[i][j]=0;
                            Foreach (k In 0 .. col1 By 1) {
                                c[i][j] = c[i][j] + a[i][k] * b[k][j];
                            }
                            c = a + (b > c) + d;
                            Out.print(c[i][j] +. " ");
                        }
                        Out.println();
                    }
                    Return c;
                }      
            }
        }
        """
        expect = """Program([ClassDecl(Id(Sys_Clone),Id(System),[MethodDecl(Id(classWorker),Instance,[],Block([Block([ConstDecl(Id(a),IntType,IntLit(100)),VarDecl(Id(_),ClassType(Id(Any)),NewExpr(Id(Any),[])),AssignStmt(CallExpr(Id(_),Id(getVar),[]),IntLit(100000000000))]),Block([AssignStmt(Id(a),BooleanLit(True)),AssignStmt(Id(b),BooleanLit(False)),Return()]),Block([For(Id(i),IntLit(0),Id(rows1),IntLit(1),Block([For(Id(j),IntLit(0),Id(col2),BinaryOp(-,BinaryOp(*,BinaryOp(+,IntLit(0),IntLit(1)),IntLit(2)),IntLit(1)),Block([AssignStmt(ArrayCell(Id(c),[Id(i),Id(j)]),IntLit(0)),For(Id(k),IntLit(0),Id(col1),IntLit(1),Block([AssignStmt(ArrayCell(Id(c),[Id(i),Id(j)]),BinaryOp(+,ArrayCell(Id(c),[Id(i),Id(j)]),BinaryOp(*,ArrayCell(Id(a),[Id(i),Id(k)]),ArrayCell(Id(b),[Id(k),Id(j)]))))])]),AssignStmt(Id(c),BinaryOp(+,BinaryOp(+,Id(a),BinaryOp(>,Id(b),Id(c))),Id(d))),Call(Id(Out),Id(print),[BinaryOp(+.,ArrayCell(Id(c),[Id(i),Id(j)]),StringLit( ))])])]),Call(Id(Out),Id(println),[])])]),Return(Id(c))])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 439))

    def test_fake_special_method_440(self):
        input = """
        Class Program{
            main(){    
                Return BCA.doNothing();
            }
            main(fakeParam: NullType){
                ABC.doNothing();
                Return;
            }
            Constructor(){
                System.construct(Self);
            }
            Destructor(){
                System.destroy(Self);
            }
        }
        Class FakeProgram: Program{
            main(){    
                Return BCA.doNothing();
            }
            main(fakeParam: NullType){
                ABC.doNothing();
                Return;
            }
            Constructor(){
                System.construct(Self);
            }
            Destructor(){
                System.destroy(Self);
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return(CallExpr(Id(BCA),Id(doNothing),[]))])),MethodDecl(Id(main),Instance,[param(Id(fakeParam),ClassType(Id(NullType)))],Block([Call(Id(ABC),Id(doNothing),[]),Return()])),MethodDecl(Id("Constructor"),Instance,[],Block([Call(Id(System),Id(construct),[Self()])])),MethodDecl(Id("Destructor"),Instance,[],Block([Call(Id(System),Id(destroy),[Self()])]))]),ClassDecl(Id(FakeProgram),Id(Program),[MethodDecl(Id(main),Instance,[],Block([Return(CallExpr(Id(BCA),Id(doNothing),[]))])),MethodDecl(Id(main),Instance,[param(Id(fakeParam),ClassType(Id(NullType)))],Block([Call(Id(ABC),Id(doNothing),[]),Return()])),MethodDecl(Id("Constructor"),Instance,[],Block([Call(Id(System),Id(construct),[Self()])])),MethodDecl(Id("Destructor"),Instance,[],Block([Call(Id(System),Id(destroy),[Self()])]))])])""" 
        self.assertTrue(TestAST.test(input, expect, 440))

    # This marks the end of elementary test-case

    def test_complex_program_441(self):
        """ Test matrix multiplications"""
        input = """
        Class Program {
            main() {
                If (col1 != row2) {
                    Out.println("Matrix multiplication is not possible");
                }

                Else {
                    Var a : Array[Array[Int, 100], 100];
                    Var b : Array[Array[Int, 100], 100];
                    Var c : Array[Array[Int, 100], 100];

                    Out.println("Enter values for matrix A : \\n");
                    Foreach (i In 0 .. row1 By 1) {
                        Foreach (j In 0 .. col1) {
                            a[i][j] = s.nextInt();
                        }
                    }

                    Out.println("Enter values for matrix B : \\n");
                    Foreach (i In 0 .. row2 By 1) {
                        Foreach (j In 0 .. col2) {
                            b[i][j] = s.nextInt();
                        }
                    }

                    Out.println("Matrix multiplication is : \\n");
                    Foreach (i In 0 .. rows1 By 1) {
                        Foreach (j In 0 .. col2 By (0 + 1) * 2 - 1) {
                            c[i][j]=0;
                            Foreach (k In 0 .. col1 By 1) {
                                c[i][j] = c[i][j] + a[i][k] * b[k][j];
                            }
                            c = a + b > c + d;
                            Out.print(c[i][j] +. " ");
                        }
                        Out.println();
                    }
                }
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(!=,Id(col1),Id(row2)),Block([Call(Id(Out),Id(println),[StringLit(Matrix multiplication is not possible)])]),Block([VarDecl(Id(a),ArrayType(100,ArrayType(100,IntType))),VarDecl(Id(b),ArrayType(100,ArrayType(100,IntType))),VarDecl(Id(c),ArrayType(100,ArrayType(100,IntType))),Call(Id(Out),Id(println),[StringLit(Enter values for matrix A : \\n)]),For(Id(i),IntLit(0),Id(row1),IntLit(1),Block([For(Id(j),IntLit(0),Id(col1),IntLit(1),Block([AssignStmt(ArrayCell(Id(a),[Id(i),Id(j)]),CallExpr(Id(s),Id(nextInt),[]))])])])]),Call(Id(Out),Id(println),[StringLit(Enter values for matrix B : \\n)]),For(Id(i),IntLit(0),Id(row2),IntLit(1),Block([For(Id(j),IntLit(0),Id(col2),IntLit(1),Block([AssignStmt(ArrayCell(Id(b),[Id(i),Id(j)]),CallExpr(Id(s),Id(nextInt),[]))])])])]),Call(Id(Out),Id(println),[StringLit(Matrix multiplication is : \\n)]),For(Id(i),IntLit(0),Id(rows1),IntLit(1),Block([For(Id(j),IntLit(0),Id(col2),BinaryOp(-,BinaryOp(*,BinaryOp(+,IntLit(0),IntLit(1)),IntLit(2)),IntLit(1)),Block([AssignStmt(ArrayCell(Id(c),[Id(i),Id(j)]),IntLit(0)),For(Id(k),IntLit(0),Id(col1),IntLit(1),Block([AssignStmt(ArrayCell(Id(c),[Id(i),Id(j)]),BinaryOp(+,ArrayCell(Id(c),[Id(i),Id(j)]),BinaryOp(*,ArrayCell(Id(a),[Id(i),Id(k)]),ArrayCell(Id(b),[Id(k),Id(j)]))))])]),AssignStmt(Id(c),BinaryOp(>,BinaryOp(+,Id(a),Id(b)),BinaryOp(+,Id(c),Id(d)))),Call(Id(Out),Id(print),[BinaryOp(+.,ArrayCell(Id(c),[Id(i),Id(j)]),StringLit( ))])])]),Call(Id(Out),Id(println),[])])])])),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 441))

    def test_complex_program_442(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b % c + a.foo();
                a.foo2(param1, param2);
                a1 = a.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehiclee{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){

            }
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    a.foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    a.foo2();
                }
            }
        }

        Class Motor:Vehicle{
            Var $motorList:Array[Motor, 100];
            Var $numOfMotor: Int = 0;
            Val maxSpeed: Int = 40;
            Constructor(){
                motorList[Motor::$numOfMotor] = Self;
                Motor::$numOfMotor = 1;
            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(c),IntType)),AttributeDecl(Instance,VarDecl(Id(d),IntType)),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(var1),StringType,StringLit(str1))])),MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(%,Id(b),Id(c)),CallExpr(Id(a),Id(foo),[]))),Call(Id(a),Id(foo2),[Id(param1),Id(param2)]),AssignStmt(Id(a1),CallExpr(Id(a),Id(foo3),[Id(param1),Id(param2)])),VarDecl(Id(b),BoolType,BinaryOp(>=,IntLit(1),IntLit(3))),ConstDecl(Id(val1),BoolType,BinaryOp(==,BooleanLit(True),BooleanLit(False))),AssignStmt(Id(b),UnaryOp(!,Id(val1))),Return(BooleanLit(True))]))]),ClassDecl(Id(Vehiclee),[AttributeDecl(Instance,VarDecl(Id(running),BoolType,BooleanLit(True))),AttributeDecl(Instance,VarDecl(Id(speed),IntType)),AttributeDecl(Instance,VarDecl(Id(model_name),StringType)),AttributeDecl(Static,VarDecl(Id($numOfVehicle),IntType)),MethodDecl(Id("Constructor"),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(speed)),IntLit(30))])),MethodDecl(Id("Constructor"),Instance,[param(Id(speed),IntType),param(Id(model_name),StringType)],Block([AssignStmt(FieldAccess(Self(),Id(speed)),Id(speed)),AssignStmt(FieldAccess(Self(),Id(model_name)),Id(model_name))])),MethodDecl(Id("Destructor"),Instance,[],Block([])),MethodDecl(Id(run),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(running)),BooleanLit(True))])),MethodDecl(Id(stop),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(running)),BooleanLit(False))]))]),ClassDecl(Id(Door),[AttributeDecl(Instance,ConstDecl(Id(hasSunScreen),BoolType,BooleanLit(True)))]),ClassDecl(Id(Car),Id(Vehicle),[AttributeDecl(Instance,ConstDecl(Id(sunScreen),BoolType,BooleanLit(False))),AttributeDecl(Instance,ConstDecl(Id(doors),ArrayType(4,BoolType),None)),AttributeDecl(Instance,ConstDecl(Id(backDoor),ClassType(Id(Door)),NewExpr(Id(Door),[]))),MethodDecl(Id(openCabin),Instance,[],Block([If(BinaryOp(==,Id(openedCabin),BooleanLit(False)),Block([AssignStmt(Id(openedCabin),BooleanLit(True)),Return(BooleanLit(True))]),Block([Return(BooleanLit(False))]))])),MethodDecl(Id(openAllDoor),Instance,[],Block([For(Id(i),IntLit(1),IntLit(4),IntLit(1),Block([AssignStmt(ArrayCell(Id(doors),[Id(i)]),BooleanLit(True)),Call(Id(a),Id(foo1),[])])])])),MethodDecl(Id(closeAllDoor),Instance,[],Block([For(Id(i),IntLit(4),IntLit(1),UnaryOp(-,IntLit(1)),Block([AssignStmt(ArrayCell(Id(doors),[Id(i)]),BooleanLit(False)),Call(Id(a),Id(foo2),[])])])]))]),ClassDecl(Id(Motor),Id(Vehicle),[AttributeDecl(Static,VarDecl(Id($motorList),ArrayType(100,ClassType(Id(Motor))))),AttributeDecl(Static,VarDecl(Id($numOfMotor),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(maxSpeed),IntType,IntLit(40))),MethodDecl(Id("Constructor"),Instance,[],Block([AssignStmt(ArrayCell(Id(motorList),[FieldAccess(Id(Motor),Id($numOfMotor))]),Self()),AssignStmt(FieldAccess(Id(Motor),Id($numOfMotor)),IntLit(1))])),MethodDecl(Id("Constructor"),Instance,[param(Id(maxSpeed),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(maxSpeed)),Id(maxSpeed))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 442))

    def test_complex_program_443(self):
        input = """
        Class Program{
            Var a, $b : Int;
            Val c, $d : Boolean;
            Var e, $f : Int = 023, 0x45;
            Val w, $x : Float = 0.01, .3e2;
            notMain(f: Boolean; arr: Array[Array[Float, 3], 4]){
                Var a : Int;
                Val c : Boolean;
                Var e, f : Int = 023, 0x45;
                Val w, x : Float = 0.01, .3e2;
                Return a + c + e + w;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id($b),IntType)),AttributeDecl(Instance,ConstDecl(Id(c),BoolType,None)),AttributeDecl(Static,ConstDecl(Id($d),BoolType,None)),AttributeDecl(Instance,VarDecl(Id(e),IntType,IntLit(19))),AttributeDecl(Static,VarDecl(Id($f),IntType,IntLit(69))),AttributeDecl(Instance,ConstDecl(Id(w),FloatType,FloatLit(0.01))),AttributeDecl(Static,ConstDecl(Id($x),FloatType,FloatLit(30.0))),MethodDecl(Id(notMain),Instance,[param(Id(f),BoolType),param(Id(arr),ArrayType(4,ArrayType(3,FloatType)))],Block([VarDecl(Id(a),IntType),ConstDecl(Id(c),BoolType,None),VarDecl(Id(e),IntType,IntLit(19)),VarDecl(Id(f),IntType,IntLit(69)),ConstDecl(Id(w),FloatType,FloatLit(0.01)),ConstDecl(Id(x),FloatType,FloatLit(30.0)),Return(BinaryOp(+,BinaryOp(+,BinaryOp(+,Id(a),Id(c)),Id(e)),Id(w)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 443)) 

    def test_complex_program_444(self):
        input = """
        Class Map {
            Val key: Array[String, 10];
            Val value: Array[String, 10];
            Constructor(key: Array[String, 10]; value: Array[String, 10]) {
                Self.key = key;
                Self.value = value;
                Return;
            }
            Destructor() {
                Self.clean(Self.key);
                Self.clean(Self.value);
            }
            mapWorker() {
                Out.println("Cleaning");
                Foreach (k In 0 .. Self.key.length() By 2)
                {
                    myK = Self.key[k];

                    Cleaner.free(myK);
                    Self.key = Null;
                }
                Cleaner.free(key);
                Self.key = Null;
                Foreach (v In 0 .. Self.value.length() By 1)
                {
                    el = Self.value.a[v];

                    Cleaner.free(el);
                    Self.value = Null;
                }
                Cleaner.free(value);
                Self.value = Null;
                Val a : Boolean = True;
                Val b : Int = 1;
                Return (True || False) && (a == b);
            }
        }
        Class Program {
            main() {
                Val My1stCons, My2ndCons: Int = 1 + 100, 321;
                Var x, y : Int = 0, 0;
                Val sth : Sth = New Sth();
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Map),[AttributeDecl(Instance,ConstDecl(Id(key),ArrayType(10,StringType),None)),AttributeDecl(Instance,ConstDecl(Id(value),ArrayType(10,StringType),None)),MethodDecl(Id("Constructor"),Instance,[param(Id(key),ArrayType(10,StringType)),param(Id(value),ArrayType(10,StringType))],Block([AssignStmt(FieldAccess(Self(),Id(key)),Id(key)),AssignStmt(FieldAccess(Self(),Id(value)),Id(value)),Return()])),MethodDecl(Id("Destructor"),Instance,[],Block([Call(Self(),Id(clean),[FieldAccess(Self(),Id(key))]),Call(Self(),Id(clean),[FieldAccess(Self(),Id(value))])])),MethodDecl(Id(mapWorker),Instance,[],Block([Call(Id(Out),Id(println),[StringLit(Cleaning)]),For(Id(k),IntLit(0),CallExpr(FieldAccess(Self(),Id(key)),Id(length),[]),IntLit(2),Block([AssignStmt(Id(myK),ArrayCell(FieldAccess(Self(),Id(key)),[Id(k)])),Call(Id(Cleaner),Id(free),[Id(myK)]),AssignStmt(FieldAccess(Self(),Id(key)),NullLiteral())])]),Call(Id(Cleaner),Id(free),[Id(key)]),AssignStmt(FieldAccess(Self(),Id(key)),NullLiteral()),For(Id(v),IntLit(0),CallExpr(FieldAccess(Self(),Id(value)),Id(length),[]),IntLit(1),Block([AssignStmt(Id(el),ArrayCell(FieldAccess(FieldAccess(Self(),Id(value)),Id(a)),[Id(v)])),Call(Id(Cleaner),Id(free),[Id(el)]),AssignStmt(FieldAccess(Self(),Id(value)),NullLiteral())])]),Call(Id(Cleaner),Id(free),[Id(value)]),AssignStmt(FieldAccess(Self(),Id(value)),NullLiteral()),ConstDecl(Id(a),BoolType,BooleanLit(True)),ConstDecl(Id(b),IntType,IntLit(1)),Return(BinaryOp(&&,BinaryOp(||,BooleanLit(True),BooleanLit(False)),BinaryOp(==,Id(a),Id(b))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(My1stCons),IntType,BinaryOp(+,IntLit(1),IntLit(100))),ConstDecl(Id(My2ndCons),IntType,IntLit(321)),VarDecl(Id(x),IntType,IntLit(0)),VarDecl(Id(y),IntType,IntLit(0)),ConstDecl(Id(sth),ClassType(Id(Sth)),NewExpr(Id(Sth),[])),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 444))

    def test_complex_program_445(self):
        input = """Class Program {
            main() {
                a[1].func();
                Return;
            }
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(ArrayCell(Id(a),[IntLit(1)]),Id(func),[]),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 445))

    def test_complex_program_446(self):
        input = """
        Class Program {
            main() {
                Foreach(x In 100 .. 300 By 5){
                    Out.printInt(x % 10);
                }
                Foreach(y In 300 .. -0 By -2){
                    Self::$doNothing = 1;
                    a::$doNothing();
                    Foreach(z In -1 .. 50000000){
                        Out.print("Hello world");
                    }
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(x),IntLit(100),IntLit(300),IntLit(5),Block([Call(Id(Out),Id(printInt),[BinaryOp(%,Id(x),IntLit(10))])])]),For(Id(y),IntLit(300),UnaryOp(-,IntLit(0)),UnaryOp(-,IntLit(2)),Block([AssignStmt(FieldAccess(Self(),Id($doNothing)),IntLit(1)),Call(Id(a),Id($doNothing),[]),For(Id(z),UnaryOp(-,IntLit(1)),IntLit(50000000),IntLit(1),Block([Call(Id(Out),Id(print),[StringLit(Hello world)])])])])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 446))

    def test_complex_program_447(self):
        input = """
        Class Program {
            Val c : Array[Int, 0b1101];
            main() {
                Val a : Array[Int, 0x1234ABCD];
                Var b : Array[Array[Int, 0x1234ABCD], 0x1234ABCD];
                Val c : Array[Int, 500000];
                Val c : Array[Int, 0312123];
            }
        }"""
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(c),ArrayType(13,IntType),None)),MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),ArrayType(305441741,IntType),None),VarDecl(Id(b),ArrayType(305441741,ArrayType(305441741,IntType))),ConstDecl(Id(c),ArrayType(500000,IntType),None),ConstDecl(Id(c),ArrayType(103507,IntType),None)]))])])"""
        self.assertTrue(TestAST.test(input, expect, 447))

    def test_complex_program_448(self):
        input = """Class Program {
            main() {
                a[1].func()[0].bar();
                a[1].func();
                a[1] = 1;
                Val b : String = a.func()[1];
                Out.println(a.a[1]);
                Return;
            }
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(ArrayCell(CallExpr(ArrayCell(Id(a),[IntLit(1)]),Id(func),[]),[IntLit(0)]),Id(bar),[]),Call(ArrayCell(Id(a),[IntLit(1)]),Id(func),[]),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),IntLit(1)),ConstDecl(Id(b),StringType,ArrayCell(CallExpr(Id(a),Id(func),[]),[IntLit(1)])),Call(Id(Out),Id(println),[ArrayCell(FieldAccess(Id(a),Id(a)),[IntLit(1)])]),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 448))

    def test_complex_program_449(self):
        input = """
        Class Map {
            Val key: Array[String, 10];
            Val value: Array[String, 10];
            Constructor(key: Array[String, 10]; value: Array[String, 10]) {
                Self.key = key;
                Self.value = value;
            }
            Destructor() {
                Self.clean(Self.key);
                Self.clean(Self.value);
            }
            clean() {
                Out.println("Cleaning");
                Foreach (k In 0 .. Self.key.length() By 1)
                {
                    el = Self.key[k];

                    a.free(el);
                    Self.key = Null;
                }
                a.free(key);
                Self.key = Null;
                Foreach (v In 0 .. Self.value.length() By 1)
                {
                    el = Self.value.a[v];

                    a.free(el);
                    Self.value = Null;
                }
                a.free(value);
                Self.value = Null;
                Val a : Boolean = True;
                Val b : Int = 1;
                Return (True || False) && (a == b);
            }
        }
        Class Program {
            main() {
                Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                Var x, y : Int = 0, 0;
                Val sth : Sth = New Sth();
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Map),[AttributeDecl(Instance,ConstDecl(Id(key),ArrayType(10,StringType),None)),AttributeDecl(Instance,ConstDecl(Id(value),ArrayType(10,StringType),None)),MethodDecl(Id("Constructor"),Instance,[param(Id(key),ArrayType(10,StringType)),param(Id(value),ArrayType(10,StringType))],Block([AssignStmt(FieldAccess(Self(),Id(key)),Id(key)),AssignStmt(FieldAccess(Self(),Id(value)),Id(value))])),MethodDecl(Id("Destructor"),Instance,[],Block([Call(Self(),Id(clean),[FieldAccess(Self(),Id(key))]),Call(Self(),Id(clean),[FieldAccess(Self(),Id(value))])])),MethodDecl(Id(clean),Instance,[],Block([Call(Id(Out),Id(println),[StringLit(Cleaning)]),For(Id(k),IntLit(0),CallExpr(FieldAccess(Self(),Id(key)),Id(length),[]),IntLit(1),Block([AssignStmt(Id(el),ArrayCell(FieldAccess(Self(),Id(key)),[Id(k)])),Call(Id(a),Id(free),[Id(el)]),AssignStmt(FieldAccess(Self(),Id(key)),NullLiteral())])]),Call(Id(a),Id(free),[Id(key)]),AssignStmt(FieldAccess(Self(),Id(key)),NullLiteral()),For(Id(v),IntLit(0),CallExpr(FieldAccess(Self(),Id(value)),Id(length),[]),IntLit(1),Block([AssignStmt(Id(el),ArrayCell(FieldAccess(FieldAccess(Self(),Id(value)),Id(a)),[Id(v)])),Call(Id(a),Id(free),[Id(el)]),AssignStmt(FieldAccess(Self(),Id(value)),NullLiteral())])]),Call(Id(a),Id(free),[Id(value)]),AssignStmt(FieldAccess(Self(),Id(value)),NullLiteral()),ConstDecl(Id(a),BoolType,BooleanLit(True)),ConstDecl(Id(b),IntType,IntLit(1)),Return(BinaryOp(&&,BinaryOp(||,BooleanLit(True),BooleanLit(False)),BinaryOp(==,Id(a),Id(b))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(My1stCons),IntType,BinaryOp(+,IntLit(1),IntLit(5))),ConstDecl(Id(My2ndCons),IntType,IntLit(2)),VarDecl(Id(x),IntType,IntLit(0)),VarDecl(Id(y),IntType,IntLit(0)),ConstDecl(Id(sth),ClassType(Id(Sth)),NewExpr(Id(Sth),[])),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 449))
    
    def test_chaining_450(self):
        input = """
        Class Program {
            main() {
                a = a.b.c.d().e().f() + Self::$a();
            }
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(+,CallExpr(CallExpr(CallExpr(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d),[]),Id(e),[]),Id(f),[]),CallExpr(Self(),Id($a),[])))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 450))
    
    def test_complex_program_451(self):
        input = """
        Class Program {
            main() {
                Val numbers : Array[Int, 5] = Array(9, 8, 7.5, 6.9, 3);

                Foreach (i In 0 .. 10 By 1) {
                    If ( x > 6 ) {
                        Continue;
                    }
                    Else{
                        System.out.print("Passed\\n");
                    }
                    System.out.print(x);
                    System.out.print("\\n");
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(numbers),ArrayType(5,IntType),[IntLit(9),IntLit(8),FloatLit(7.5),FloatLit(6.9),IntLit(3)]),For(Id(i),IntLit(0),IntLit(10),IntLit(1),Block([If(BinaryOp(>,Id(x),IntLit(6)),Block([Continue]),Block([Call(FieldAccess(Id(System),Id(out)),Id(print),[StringLit(Passed\\n)])])),Call(FieldAccess(Id(System),Id(out)),Id(print),[Id(x)]),Call(FieldAccess(Id(System),Id(out)),Id(print),[StringLit(\\n)])])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 451))

    def test_complex_program_452(self):
        input = """
        Class Program{
            $main(){       
                {
                    Foreach (a In 1 .. n By 1) {
                        If (node != Null) {
                            System.out.print(node.data +. " ");
                            node = node.next;
                        } 
                        Else {
                            Break;
                        }
                    }
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id($main),Static,[],Block([Block([For(Id(a),IntLit(1),Id(n),IntLit(1),Block([If(BinaryOp(!=,Id(node),NullLiteral()),Block([Call(FieldAccess(Id(System),Id(out)),Id(print),[BinaryOp(+.,FieldAccess(Id(node),Id(data)),StringLit( ))]),AssignStmt(Id(node),FieldAccess(Id(node),Id(next)))]),Block([Break]))])])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 452))

    def test_complex_program_453(self):
        input = """
        Class Node {
            Var data : Int;
            Val next : Node;

            Constructor(d : Int)
            {
                data = d;
                next = Null;
            }

            reverse(node : Node)
            {
                Var prev : Node = Null;
                Val current : Node = node;
                Val next : Node = Null;
                Foreach (i In 1 .. forever By 1) {
                    If (current == Null) {
                        Break;
                    } 
                    Else {
                        next = current.next;
                        current.next = prev;
                        prev = current;
                        current = next;
                    }
                }
                node = prev;
                Return node;
            }

            printList(node : Node)
            {
                Foreach (a In 1 .. n By 1) {
                    If (node != Null) {
                        System.out.print(node.data +. " ");
                        node = node.next;
                    } 
                    Else {
                        Break;
                    }
                }
            }
        }

        Class Program {
            main()
            {
                Val num1, num2: Int = 100, 200;
                Val list : LinkedList = New LinkedList();
                list.head = New Node(num1);
                list.head.next = New Node(num2);
                list.head.next.next = New Node(-516e21);
                list.head.next.next.next = New Node(985.414400e2);

                System.out.println("Given Linked list: \\n");
                list.printList(head);
                head = list.reverse(head);
                System.out.println("");
                System.out.println("Reversed linked list: ");
                list.printList(head);
            }
        }
        """
        expect = """Program([ClassDecl(Id(Node),[AttributeDecl(Instance,VarDecl(Id(data),IntType)),AttributeDecl(Instance,ConstDecl(Id(next),ClassType(Id(Node)),None)),MethodDecl(Id("Constructor"),Instance,[param(Id(d),IntType)],Block([AssignStmt(Id(data),Id(d)),AssignStmt(Id(next),NullLiteral())])),MethodDecl(Id(reverse),Instance,[param(Id(node),ClassType(Id(Node)))],Block([VarDecl(Id(prev),ClassType(Id(Node)),NullLiteral()),ConstDecl(Id(current),ClassType(Id(Node)),Id(node)),ConstDecl(Id(next),ClassType(Id(Node)),NullLiteral()),For(Id(i),IntLit(1),Id(forever),IntLit(1),Block([If(BinaryOp(==,Id(current),NullLiteral()),Block([Break]),Block([AssignStmt(Id(next),FieldAccess(Id(current),Id(next))),AssignStmt(FieldAccess(Id(current),Id(next)),Id(prev)),AssignStmt(Id(prev),Id(current)),AssignStmt(Id(current),Id(next))]))])]),AssignStmt(Id(node),Id(prev)),Return(Id(node))])),MethodDecl(Id(printList),Instance,[param(Id(node),ClassType(Id(Node)))],Block([For(Id(a),IntLit(1),Id(n),IntLit(1),Block([If(BinaryOp(!=,Id(node),NullLiteral()),Block([Call(FieldAccess(Id(System),Id(out)),Id(print),[BinaryOp(+.,FieldAccess(Id(node),Id(data)),StringLit( ))]),AssignStmt(Id(node),FieldAccess(Id(node),Id(next)))]),Block([Break]))])])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(num1),IntType,IntLit(100)),ConstDecl(Id(num2),IntType,IntLit(200)),ConstDecl(Id(list),ClassType(Id(LinkedList)),NewExpr(Id(LinkedList),[])),AssignStmt(FieldAccess(Id(list),Id(head)),NewExpr(Id(Node),[Id(num1)])),AssignStmt(FieldAccess(FieldAccess(Id(list),Id(head)),Id(next)),NewExpr(Id(Node),[Id(num2)])),AssignStmt(FieldAccess(FieldAccess(FieldAccess(Id(list),Id(head)),Id(next)),Id(next)),NewExpr(Id(Node),[UnaryOp(-,FloatLit(5.16e+23))])),AssignStmt(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(list),Id(head)),Id(next)),Id(next)),Id(next)),NewExpr(Id(Node),[FloatLit(98541.44)])),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Given Linked list: \\n)]),Call(Id(list),Id(printList),[Id(head)]),AssignStmt(Id(head),CallExpr(Id(list),Id(reverse),[Id(head)])),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit()]),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Reversed linked list: )]),Call(Id(list),Id(printList),[Id(head)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 453))

    def test_complex_program_454(self):
        """ Test static and instance"""
        input = """
        Class C {
            foo() {
                Return nothingToReturnHehehehe;
            }
        }
        Class B : C{
            Val a : C;
            Val $b : B;
            Constructor() {
                a = New C();
                Self::$b = New B();
                Return;
            }
        }

        Class Program {
            main() {
                Val a : A = New A();
                a::$b.a.foo();
                Return;
            }
        }"""
        expect = """Program([ClassDecl(Id(C),[MethodDecl(Id(foo),Instance,[],Block([Return(Id(nothingToReturnHehehehe))]))]),ClassDecl(Id(B),Id(C),[AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Id(C)),None)),AttributeDecl(Static,ConstDecl(Id($b),ClassType(Id(B)),None)),MethodDecl(Id("Constructor"),Instance,[],Block([AssignStmt(Id(a),NewExpr(Id(C),[])),AssignStmt(FieldAccess(Self(),Id($b)),NewExpr(Id(B),[])),Return()]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),ClassType(Id(A)),NewExpr(Id(A),[])),Call(FieldAccess(FieldAccess(Id(a),Id($b)),Id(a)),Id(foo),[]),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 454))

    def test_complex_program_455(self):
        input = """
        Class D {
            Constructor() {
                a = True;
                b = False;
                Return;
            }
        }
        Class Program {
            main() {
                Val sth : Array[Float, 3] = New Map(B);
                Return "Zhege ke bu ke ma?";
            }
        }"""
        expect = """Program([ClassDecl(Id(D),[MethodDecl(Id("Constructor"),Instance,[],Block([AssignStmt(Id(a),BooleanLit(True)),AssignStmt(Id(b),BooleanLit(False)),Return()]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(sth),ArrayType(3,FloatType),NewExpr(Id(Map),[Id(B)])),Return(StringLit(Zhege ke bu ke ma?))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 455))

    def test_complex_program_456(self):
        input = """
        Class Program {
            main() {
                a[1][2] = b[1][2][3] - c[1][2][3];
                Return;
            }
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),BinaryOp(-,ArrayCell(Id(b),[IntLit(1),IntLit(2),IntLit(3)]),ArrayCell(Id(c),[IntLit(1),IntLit(2),IntLit(3)]))),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 456))

    def test_complex_program_457(self):
        input = """
        Class Map {
            Val key: Array[String, 10];
            Val value: Array[String, 10];
            Var $myMap: Map = New Map(Self.key, Self.value);
            Constructor(key: Array[String, 10]; value: Array[String, 10]) {
                Self.key = key;
                Self.value = value;
                Return;
            }
            Destructor() {
                Self.clean(Self.key);
                Self.clean(Self.value);
                Return;
            }
        }

        Class Program {
            main() {
                Val sth : Map = New Map(arr1, arr2);
                Return Null;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Map),[AttributeDecl(Instance,ConstDecl(Id(key),ArrayType(10,StringType),None)),AttributeDecl(Instance,ConstDecl(Id(value),ArrayType(10,StringType),None)),AttributeDecl(Static,VarDecl(Id($myMap),ClassType(Id(Map)),NewExpr(Id(Map),[FieldAccess(Self(),Id(key)),FieldAccess(Self(),Id(value))]))),MethodDecl(Id("Constructor"),Instance,[param(Id(key),ArrayType(10,StringType)),param(Id(value),ArrayType(10,StringType))],Block([AssignStmt(FieldAccess(Self(),Id(key)),Id(key)),AssignStmt(FieldAccess(Self(),Id(value)),Id(value)),Return()])),MethodDecl(Id("Destructor"),Instance,[],Block([Call(Self(),Id(clean),[FieldAccess(Self(),Id(key))]),Call(Self(),Id(clean),[FieldAccess(Self(),Id(value))]),Return()]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(sth),ClassType(Id(Map)),NewExpr(Id(Map),[Id(arr1),Id(arr2)])),Return(NullLiteral())]))])])"""
        self.assertTrue(TestAST.test(input, expect, 457))

    def test_fake_special_method_458(self):
        input = """
        Class Program : System{
            $main() {
                Val sth : Map = New Map(arr1, arr2);
                Return Null;
            }
            $Constructor(key: Array[String, 10]; value: Array[String, 10]) {
                Self.key = key;
                Self.value = value;
                Return;
            }
            $Destructor() {
                Self.clean(Self.key);
                Self.clean(Self.value);
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),Id(System),[MethodDecl(Id($main),Static,[],Block([ConstDecl(Id(sth),ClassType(Id(Map)),NewExpr(Id(Map),[Id(arr1),Id(arr2)])),Return(NullLiteral())])),MethodDecl(Id($Constructor),Static,[param(Id(key),ArrayType(10,StringType)),param(Id(value),ArrayType(10,StringType))],Block([AssignStmt(FieldAccess(Self(),Id(key)),Id(key)),AssignStmt(FieldAccess(Self(),Id(value)),Id(value)),Return()])),MethodDecl(Id($Destructor),Static,[],Block([Call(Self(),Id(clean),[FieldAccess(Self(),Id(key))]),Call(Self(),Id(clean),[FieldAccess(Self(),Id(value))]),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 458))

    def test_priority_459(self):
        input = """
        Class Program {
            main() {
                Val myVarB : Int = (a[5]).func()[10];
                Return;
            }
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(myVarB),IntType,ArrayCell(CallExpr(ArrayCell(Id(a),[IntLit(5)]),Id(func),[]),[IntLit(10)])),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 459))

    def test_scalar_var_460(self):
        input = """
        Class Program {
            main() {
                Val b : Int = a::$a;
                a::$func();
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(b),IntType,FieldAccess(Id(a),Id($a))),Call(Id(a),Id($func),[]),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 460))

    def test_complex_program_461(self):
        input = """
        Class Program {
            main() {
                Val a : Int;
                Foreach (i In 1 .. 1000 By 5)
                {
                    Clip.printf("enter the number:");
                    Clip.scanf("%d", a);
                    If ( a == 0 ) {
                        Break;
                        Return 100;
                    }
                    Else {
                        Continue;
                    }
                }
                Return;
            }
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),IntType,None),For(Id(i),IntLit(1),IntLit(1000),IntLit(5),Block([Call(Id(Clip),Id(printf),[StringLit(enter the number:)]),Call(Id(Clip),Id(scanf),[StringLit(%d),Id(a)]),If(BinaryOp(==,Id(a),IntLit(0)),Block([Break,Return(IntLit(100))]),Block([Continue]))])]),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 461))

    def test_index_ops_462(self):
        input = """
        Class Program {
            main() {
                Var a : Int = (a::$a[1]).func()[0];
                Return;
            }
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,ArrayCell(CallExpr(ArrayCell(FieldAccess(Id(a),Id($a)),[IntLit(1)]),Id(func),[]),[IntLit(0)])),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 462))

    def test_complex_program_463(self):
        input = """
        Class Program {
            Val a: Int = 1;
            fooBar(a, b : Int; c : Float) {
                Program.fooBar1();
            }
            main() {
                Program.fooBar(a, b, c);
                Return;
            }
        }"""
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(1))),MethodDecl(Id(fooBar),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],Block([Call(Id(Program),Id(fooBar1),[])])),MethodDecl(Id(main),Static,[],Block([Call(Id(Program),Id(fooBar),[Id(a),Id(b),Id(c)]),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 463))

    def test_complex_program_464(self):
        input = """
        Class Simple {
            main() {
                Val numbers : Array[Int, 5] = Array(10, 20, 30, 40, 50);

                Foreach (i In 0 .. 4 By 1) {
                    If ( x - i == 30 ) {
                        Continue;
                    }
                    System.out.print( x );
                    System.out.print("\\n");
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Simple),[MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(numbers),ArrayType(5,IntType),[IntLit(10),IntLit(20),IntLit(30),IntLit(40),IntLit(50)]),For(Id(i),IntLit(0),IntLit(4),IntLit(1),Block([If(BinaryOp(==,BinaryOp(-,Id(x),Id(i)),IntLit(30)),Block([Continue])),Call(FieldAccess(Id(System),Id(out)),Id(print),[Id(x)]),Call(FieldAccess(Id(System),Id(out)),Id(print),[StringLit(\\n)])])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 464))

    # def test_complex_program_465(self):
    #     input = """
    #     Class Program{
    #         main(){       
    #         }
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 465))

    # def test_complex_program_(self):
    #     input = """
    #     Class Program{
    #         main(){       
    #         }
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, ))


    # def test_complex_program_(self):
    #     input = """
    #     Class Program{
    #         main(){       
    #         }
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, ))
