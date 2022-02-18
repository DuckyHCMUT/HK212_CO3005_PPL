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
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(IntLit(1),ArrayType(IntLit(2),FloatType))))])])"""
        self.assertTrue(TestAST.test(input, expect, 407))

    def test_simple_program_408(self):
        """Simple program, with few assigned array attribute member"""
        input = """
        Class Program{
            Var arr, brr: Array[Int, 3] = Array(1, 2, 3), Array(5, -4, 1);
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(IntLit(3),IntType),[IntLit(1),IntLit(2),IntLit(3)])),AttributeDecl(Instance,VarDecl(Id(brr),ArrayType(IntLit(3),IntType),[IntLit(5),UnaryOp(-,IntLit(4)),IntLit(1)]))])])"""
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
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(arr),ArrayType(IntLit(3),ArrayType(IntLit(2),FloatType)),[[FloatLit(2.1),UnaryOp(-,FloatLit(1.3))],[FloatLit(0.1),FloatLit(3.1e3)],[UnaryOp(-,FloatLit(0.00001)),FloatLit(123.321E-123)]])),AttributeDecl(Static,ConstDecl(Id($brr),ArrayType(IntLit(3),ArrayType(IntLit(2),FloatType)),[[FloatLit(1.2),FloatLit(0.132)],[FloatLit(0.9931),FloatLit(10.1e3)],[FloatLit(0.00001111),FloatLit(1111111119.332321e-2)]]))])])"""
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
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($c),IntType,IntLit(1094647723))),MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(f),IntType,IntLit(1094647723))]))])])"""
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
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(notMain),Instance,[param(Id(f),BoolType),param(Id(arr),ArrayType(IntLit(4),ArrayType(IntLit(3),FloatType)))],Block([ConstDecl(Id(a),IntType,IntLit(500)),ConstDecl(Id(b),IntType,IntLit(600)),ConstDecl(Id(c),IntType,IntLit(700))]))])])"""
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
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(notMain),Instance,[param(Id(f),BoolType)],Block([ConstDecl(Id(a),ArrayType(IntLit(4),IntType),[IntLit(1),IntLit(43),IntLit(1626),IntLit(291)]),ConstDecl(Id(b),ArrayType(IntLit(4),IntType),[UnaryOp(-,IntLit(4)),IntLit(31),IntLit(61438),IntLit(5)])]))])])"""
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

    def _test_simple_program_416(self):
        """Simple program, to check assignment statement of array cell"""
        input = """
        Class Program{
            main(){
                Var a: Array[Boolean, 4];
                a[0] = True;
                a[1] = a[0];
                a[1 + 1] = False;
                a[0xC / 0b11] = True;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(4),BoolType))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),ArrayCell(Id(a),[IntLit(0)])),AssignStmt(ArrayCell(Id(a),[BinaryOp(+,IntLit(1),IntLit(1))]),BooleanLit(False)),AssignStmt(ArrayCell(Id(a),[BinaryOp(/,IntLit(12),IntLit(3))]),BooleanLit(True))]))])])"""
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
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(2),ArrayType(IntLit(3),BoolType)))),AssignStmt(ArrayCell(Id(a),[IntLit(0),IntLit(0)]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(0)]),BooleanLit(False)),AssignStmt(ArrayCell(Id(a),[IntLit(0),IntLit(1)]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(1)]),BooleanLit(False))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 417))

    def test_simple_program_418(self):
        """Simple program, to check assignment statement of multidimensional array cell"""
        input = """
        Class Program{
            main(){
                Var a: Array[Array[Boolean, 2], 2];
                a[0][0 * 10000000] = True;
                a[0][1 * 1 * 1 / 1] = False;
                a[0x270F / 9999][0 * 0B1011110101] = True;
                a[9999 / 0x270F][1 * 9 / 9 + 0] = False;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(2),ArrayType(IntLit(2),BoolType)))),AssignStmt(ArrayCell(Id(a),[BinaryOp(*,IntLit(0),IntLit(10000000)),IntLit(0)]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[BinaryOp(/,BinaryOp(*,BinaryOp(*,IntLit(1),IntLit(1)),IntLit(1)),IntLit(1)),IntLit(0)]),BooleanLit(False)),AssignStmt(ArrayCell(Id(a),[BinaryOp(*,IntLit(0),IntLit(757)),BinaryOp(/,IntLit(9999),IntLit(9999))]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[BinaryOp(+,BinaryOp(/,BinaryOp(*,IntLit(1),IntLit(9)),IntLit(9)),IntLit(0)),BinaryOp(/,IntLit(9999),IntLit(9999))]),BooleanLit(False))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 418))

    def _test_simple_program_419(self):
        """Simple program, with rhs (all_expr) is a mtd_array"""
        """ Not yet done, struggling"""
        input = """
        Class Program{
            Var a: Array[Array[Boolean, 2], 1];
            main(){
                Var b: Boolean = a[0][2];
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(1),ArrayType(IntLit(2),BoolType)))),MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(b),BoolType,ArrayCell(Id(a),[IntLit(0), IntLit(0)])))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 419))

    def _test_simple_program_420(self):
        """Simple program, with lhs is a nested array call"""
        input = """
        Class Program{
            Var a: Array[Array[Boolean, 2], 1];
            main(){
                a[b[1]] = 123;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(IntLit(1),ArrayType(IntLit(2),BoolType)))),MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[ArrayCell(Id(b),[IntLit(1)])]),IntLit(123))]))])])"""
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
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(a),CallExpr(Id(Prog),Id(b),[Id(e),Id(f),Id(g)])),AssignStmt(Id(b),FieldAccess(Id(Program),Id(a)))]))])])"""
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
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(a),CallExpr(Id(Prog),Id($b),[Id(e),Id(f),Id(g)])),AssignStmt(Id(b),FieldAccess(Id(Program),Id($a))),AssignStmt(Id(c),FieldAccess(Self(),Id($f)))]))])])"""
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
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(2))]))]))])])"""
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
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(2))]),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(1))])))]))])])"""
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
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(2))]),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(1))]),Block([AssignStmt(Id(a),IntLit(0))])))]))])])"""
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
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([For(Id(a),IntLit(1),IntLit(100000),Block([AssignStmt(FieldAccess(Id(Global),Id($b)),BinaryOp(+,Id(a),IntLit(2)))])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 427))

    def test_short_program_428(self):
        """Simple program with complete ForEach loop statement"""
        input = """
        Class Program{
            main(){
                Foreach (a In 1 .. 100000 By 5){
                    Global::$b = a + 2;
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[],Block([For(Id(a),IntLit(1),IntLit(100000),IntLit(5),Block([AssignStmt(FieldAccess(Id(Global),Id($b)),BinaryOp(+,Id(a),IntLit(2)))])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 428))

    # def test_simple_program_(self):
    #     input = """
    #     Class Program{
    #         main(){       
    #         }
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, ))