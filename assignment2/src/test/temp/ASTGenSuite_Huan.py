import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_300(self):
        input = "Class Program {}"
        expect = 'Program([ClassDecl(Id(Program),[])])'
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_301(self):
        input = "Class Program1 {} Class Program2 {} Class Program3 {}"
        expect = 'Program([ClassDecl(Id(Program1),[]),ClassDecl(Id(Program2),[]),ClassDecl(Id(Program3),[])])'
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_302(self):
        input = "Class Program:ParentProgram {}"
        expect = 'Program([ClassDecl(Id(Program),Id(ParentProgram),[])])'
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_303(self):
        input = """
        Class Program {
            Var a:Float;
        }
        """
        expect = 'Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),FloatType))])])'
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_304(self):
        input = """
        Class Program {
            Var a,b,c:Float;
        }
        """
        expect = 'Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),FloatType)),AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(c),FloatType))])])'
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_305(self):
        input = """
        Class Program {
            Var a:Float;
            Var b: ABC;
        }
        """
        expect = 'Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),FloatType)),AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(ABC)),NullLiteral()))])])'
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_306(self):
        input = """
        Class Program {
            Val a,b,c:Float;
        }
        """
        expect = 'Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,None)),AttributeDecl(Instance,ConstDecl(Id(b),FloatType,None)),AttributeDecl(Instance,ConstDecl(Id(c),FloatType,None))])])'
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_307(self):
        input = """
        Class Program {
            Var a:Int=1+1/1;
        }
        """
        expect = 'Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),BinaryOp(/,IntLit(1),IntLit(1)))))])])'
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_308(self):
        input = """
        Class Program {
            main () {
                a.putText(10);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(a),Id(putText),[IntLit(10)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_309(self):
        input = """
        Class Program {
            main () {
                Self.putText(10);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Self(),Id(putText),[IntLit(10)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_310(self):
        input = """
        Class Program {
            main () {
                Self.putText(10);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Self(),Id(putText),[IntLit(10)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_311(self):
        input = """
         Class SubProgram : Program {
             something() {
                 Program::$func();
             }
         }
         """
        expect = "Program([ClassDecl(Id(SubProgram),Id(Program),[MethodDecl(Id(something),Instance,[],Block([Call(Id(Program),Id($func),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_312(self):
        input = """
         Class SubProgram : Program {
             function() {
                 function::$func();
             }
         }
         """
        expect = "Program([ClassDecl(Id(SubProgram),Id(Program),[MethodDecl(Id(function),Instance,[],Block([Call(Id(function),Id($func),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_313(self):
        input = """
        Class Program {
            Var a : Int;
            Var $arr : Array[Int, 10];
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id($arr),ArrayType(10,IntType)))])])"
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_314(self):
        input = """
        Class Program {
            function(){
                Var a:Boolean = True;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(function),Instance,[],Block([VarDecl(Id(a),BoolType,BooleanLit(True))]))])])'
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_315(self):
        input = """
        Class Program {
            Var a, b : String;
            func () {
                Self.a_function();
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),StringType)),AttributeDecl(Instance,VarDecl(Id(b),StringType)),MethodDecl(Id(func),Instance,[],Block([Call(Self(),Id(a_function),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_316(self):
        input = """
        Class myclass:myclassparent {
            foo(c,d,e:Int){
                Var a:Int = 1+2*3;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(myclass),Id(myclassparent),[MethodDecl(Id(foo),Instance,[param(Id(c),IntType),param(Id(d),IntType),param(Id(e),IntType)],Block([VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_317(self):
        input = """
        Class A {
            $foo(){
                a=1;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id($foo),Static,[],Block([AssignStmt(Id(a),IntLit(1))]))])])'
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_318(self):
        input = """Class Program {
                   main() {}
            Var a : Int;
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([])),AttributeDecl(Instance,VarDecl(Id(a),IntType))])])"
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_319(self):
        input = """
        Class Program {
            func(param1:Int;param2:Float){}
        }
        """
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(func),Instance,[param(Id(param1),IntType),param(Id(param2),FloatType)],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_320(self):
        input = """
        Class a_program {
            func(){
                Var arr:Array[Array[Float,5],10];
            }
        }
        """
        expect = 'Program([ClassDecl(Id(a_program),[MethodDecl(Id(func),Instance,[],Block([VarDecl(Id(arr),ArrayType(10,ArrayType(5,FloatType)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_321(self):
        input = """
        Class Program {
            Val $a: String = "abc";
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($a),StringType,StringLit(abc)))])])"
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_322(self):
        input = """
        Class A:B{
            Val $a,b:Boolean = False, True;
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Static,ConstDecl(Id($a),BoolType,BooleanLit(False))),AttributeDecl(Instance,ConstDecl(Id(b),BoolType,BooleanLit(True)))])])'
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_323(self):
        input = """Class child : parent {
            Var $a, $b, $c : Float = 11.1, 11., 1e11;
            Val $c, $d, $e : Float = .0e5, 0.000, 0.9;
        }"""
        expect = "Program([ClassDecl(Id(child),Id(parent),[AttributeDecl(Static,VarDecl(Id($a),FloatType,FloatLit(11.1))),AttributeDecl(Static,VarDecl(Id($b),FloatType,FloatLit(11.0))),AttributeDecl(Static,VarDecl(Id($c),FloatType,FloatLit(100000000000.0))),AttributeDecl(Static,ConstDecl(Id($c),FloatType,FloatLit(0.0))),AttributeDecl(Static,ConstDecl(Id($d),FloatType,FloatLit(0.0))),AttributeDecl(Static,ConstDecl(Id($e),FloatType,FloatLit(0.9)))])])"
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_324(self):
        input = """Class child : parent {
            Val $a, $b, $c : Float = 55.55E-5, .5e5, .5e+5;
            Var c, d, e : Float = 2e-22, 2E+2, 2.22e22;
            Var x, y : Float = .1234e-56, 123E123;
        }"""
        expect = "Program([ClassDecl(Id(child),Id(parent),[AttributeDecl(Static,ConstDecl(Id($a),FloatType,FloatLit(0.0005555))),AttributeDecl(Static,ConstDecl(Id($b),FloatType,FloatLit(50000.0))),AttributeDecl(Static,ConstDecl(Id($c),FloatType,FloatLit(50000.0))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(2e-22))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,FloatLit(200.0))),AttributeDecl(Instance,VarDecl(Id(e),FloatType,FloatLit(2.22e+22))),AttributeDecl(Instance,VarDecl(Id(x),FloatType,FloatLit(1.234e-57))),AttributeDecl(Instance,VarDecl(Id(y),FloatType,FloatLit(1.23e+125)))])])"
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_325(self):
        input = """
        Class child:parent{
            Var a:Array[Int,3] = Array(3,3,3);
        }
        """
        expect = "Program([ClassDecl(Id(child),Id(parent),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(3,IntType),[IntLit(3),IntLit(3),IntLit(3)]))])])"
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_326(self):
        input = """
        Class child:parent{
            Var a:Array[Array[String,9],9] = Array(Array(9),Array(9),Array(9));
        }
        """
        expect = "Program([ClassDecl(Id(child),Id(parent),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(9,ArrayType(9,StringType)),[[IntLit(9)],[IntLit(9)],[IntLit(9)]]))])])"
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_327(self):
        input = """Class Program {
            Val a : Int = 100 + a1;
            Val b : Int = 2 * b1;
            Val c : Float = 100 / c1;
        }"""
        expect = 'Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(+,IntLit(100),Id(a1)))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,BinaryOp(*,IntLit(2),Id(b1)))),AttributeDecl(Instance,ConstDecl(Id(c),FloatType,BinaryOp(/,IntLit(100),Id(c1))))])])'
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_328(self):
        input = """Class B : A {
            Var a : Array[Array[Int, 5], 5];
            Var b : Int = c[i][j] / d[i][k] + e[k][j];
        }"""
        expect = 'Program([ClassDecl(Id(B),Id(A),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,ArrayType(5,IntType)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,BinaryOp(+,BinaryOp(/,ArrayCell(Id(c),[Id(i),Id(j)]),ArrayCell(Id(d),[Id(i),Id(k)])),ArrayCell(Id(e),[Id(k),Id(j)]))))])])'
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_329(self):
        input = """Class B : A {
            Val a : Array[Array[Int, 5], 5];
            Val d : Int = c[i][j] / d[i][k] + e[k][j];
            func(){
                        c[i][j] = c[i][j] + a[i][k] * b[k][j];
                }
        }"""
        expect = 'Program([ClassDecl(Id(B),Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(5,ArrayType(5,IntType)),None)),AttributeDecl(Instance,ConstDecl(Id(d),IntType,BinaryOp(+,BinaryOp(/,ArrayCell(Id(c),[Id(i),Id(j)]),ArrayCell(Id(d),[Id(i),Id(k)])),ArrayCell(Id(e),[Id(k),Id(j)])))),MethodDecl(Id(func),Instance,[],Block([AssignStmt(ArrayCell(Id(c),[Id(i),Id(j)]),BinaryOp(+,ArrayCell(Id(c),[Id(i),Id(j)]),BinaryOp(*,ArrayCell(Id(a),[Id(i),Id(k)]),ArrayCell(Id(b),[Id(k),Id(j)]))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_330(self):
        input = """Class Program : ParenProgram {
            ##a[i][j] = c[i][j] / d[i][k] + e[k][j];##
        }"""
        expect = 'Program([ClassDecl(Id(Program),Id(ParenProgram),[])])'
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_331(self):
        input = """Class Square {
            Var a, b, c : Int = 04, 0xAF, 0b1;
            Val $d, e, f : String = "Hello", "World", "\\n";
        }"""
        expect = 'Program([ClassDecl(Id(Square),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(4))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(175))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(1))),AttributeDecl(Static,ConstDecl(Id($d),StringType,StringLit(Hello))),AttributeDecl(Instance,ConstDecl(Id(e),StringType,StringLit(World))),AttributeDecl(Instance,ConstDecl(Id(f),StringType,StringLit(\\n)))])])'
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_333(self):
        input = """
        Class A:B{
            $foo(){
                Var e, f, g, h : Boolean = a == b, a != b, a >= b, a <= b;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id($foo),Static,[],Block([VarDecl(Id(e),BoolType,BinaryOp(==,Id(a),Id(b))),VarDecl(Id(f),BoolType,BinaryOp(!=,Id(a),Id(b))),VarDecl(Id(g),BoolType,BinaryOp(>=,Id(a),Id(b))),VarDecl(Id(h),BoolType,BinaryOp(<=,Id(a),Id(b)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_334(self):
        input = """
        Class A:B{
            $foo(){
                Var i, j, k, l : Boolean = 1 <= 2, 2 != 3, 3.0 == 4.0, 4.0 > 4.5;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id($foo),Static,[],Block([VarDecl(Id(i),BoolType,BinaryOp(<=,IntLit(1),IntLit(2))),VarDecl(Id(j),BoolType,BinaryOp(!=,IntLit(2),IntLit(3))),VarDecl(Id(k),BoolType,BinaryOp(==,FloatLit(3.0),FloatLit(4.0))),VarDecl(Id(l),BoolType,BinaryOp(>,FloatLit(4.0),FloatLit(4.5)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_335(self):
        input = """Class Program : parent {
            Var b : aclass = Null;
            Val c : anotherclass = Self;
        }"""
        expect = 'Program([ClassDecl(Id(Program),Id(parent),[AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(aclass)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(c),ClassType(Id(anotherclass)),Self()))])])'
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_336(self):
        input = """Class Program : parent {
            Var a : Boolean = (e > f) && (e == f) || True && False;
            Var b : Boolean = (True == False) && (True == True) && (False == False) ;
            Var c : Boolean = ("Hello" ==. "World") || (e == f);
        }"""
        expect = 'Program([ClassDecl(Id(Program),Id(parent),[AttributeDecl(Instance,VarDecl(Id(a),BoolType,BinaryOp(&&,BinaryOp(||,BinaryOp(&&,BinaryOp(>,Id(e),Id(f)),BinaryOp(==,Id(e),Id(f))),BooleanLit(True)),BooleanLit(False)))),AttributeDecl(Instance,VarDecl(Id(b),BoolType,BinaryOp(&&,BinaryOp(&&,BinaryOp(==,BooleanLit(True),BooleanLit(False)),BinaryOp(==,BooleanLit(True),BooleanLit(True))),BinaryOp(==,BooleanLit(False),BooleanLit(False))))),AttributeDecl(Instance,VarDecl(Id(c),BoolType,BinaryOp(||,BinaryOp(==.,StringLit(Hello),StringLit(World)),BinaryOp(==,Id(e),Id(f)))))])])'
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_337(self):
        input = """Class Program : parent {
            Val a : Int = obj.foo[10];
            Var b : ABC = (obj[10]).foo;
        }"""
        expect = 'Program([ClassDecl(Id(Program),Id(parent),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,ArrayCell(FieldAccess(Id(obj),Id(foo)),[IntLit(10)]))),AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(ABC)),FieldAccess(ArrayCell(Id(obj),[IntLit(10)]),Id(foo))))])])'
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_338(self):
        input = """Class Program : parent {
            Val a : Int = obj.foo[10];
            Var b : ABC = (obj[10]).foo;
            Var c : Int = (obj[10][15][20]).foo(10);
        }"""
        expect = 'Program([ClassDecl(Id(Program),Id(parent),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,ArrayCell(FieldAccess(Id(obj),Id(foo)),[IntLit(10)]))),AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(ABC)),FieldAccess(ArrayCell(Id(obj),[IntLit(10)]),Id(foo)))),AttributeDecl(Instance,VarDecl(Id(c),IntType,CallExpr(ArrayCell(Id(obj),[IntLit(10),IntLit(15),IntLit(20)]),Id(foo),[IntLit(10)])))])])'
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_339(self):
        input = """
        Class Program {
            Val a : Int = Car::$a;
            Val b : Int = Bike::$b();
            Val c : Int = Car::$foo(a, Car::$tires, Car::$fuel(a[1], 1 + 1, 2 * 3));
        }"""
        expect = 'Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,FieldAccess(Id(Car),Id($a)))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,CallExpr(Id(Bike),Id($b),[]))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,CallExpr(Id(Car),Id($foo),[Id(a),FieldAccess(Id(Car),Id($tires)),CallExpr(Id(Car),Id($fuel),[ArrayCell(Id(a),[IntLit(1)]),BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(*,IntLit(2),IntLit(3))])])))])])'
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_340(self):
        input = """
        Class Program {
            Val a : Int = Self.func().a1.a2;
            Val b : Int = ClassABC::$a1.a2.a3.a4;
        }"""
        expect = 'Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,FieldAccess(FieldAccess(CallExpr(Self(),Id(func),[]),Id(a1)),Id(a2)))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(ClassABC),Id($a1)),Id(a2)),Id(a3)),Id(a4))))])])'
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_341(self):
        line = """
                Class Shape{
                    foo(){
                        Foreach (x In 1 .. 10 By 2){}
                    }
                }
            """
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([For(Id(x),IntLit(1),IntLit(10),IntLit(2),Block([])])]))])])'
        self.assertTrue(TestAST.test(line, expect, 341))

    def test_342(self):
        line = """
                Class Shape{
                    foo(){
                        Foreach (x In 2 .. 100){}
                    }
                }
            """
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([For(Id(x),IntLit(2),IntLit(100),IntLit(1),Block([])])]))])])'
        self.assertTrue(TestAST.test(line, expect, 342))

    def test_343(self):
        line = """
                Class Shape{
                    foo(){
                        Foreach (x In 1+1 .. 100+100 By a.foo(1+1,b)){}
                    }
                }
            """
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([For(Id(x),BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(+,IntLit(100),IntLit(100)),CallExpr(Id(a),Id(foo),[BinaryOp(+,IntLit(1),IntLit(1)),Id(b)]),Block([])])]))])])'
        self.assertTrue(TestAST.test(line, expect, 343))

    def test_344(self):
        input = """
        Class A{
            foo(){
                If(True){}
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([If(BooleanLit(True),Block([]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_345(self):
        input = """
        Class A:B{
            Foo(){
                If(1){}
                If(2){}Else{}
                If(3){}Elseif(2){}Else{}
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([If(IntLit(1),Block([])),If(IntLit(2),Block([]),Block([])),If(IntLit(3),Block([]),If(IntLit(2),Block([]),Block([])))]))])])'
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_346(self):
        input = """Class Program {
            a() {
                If (a == b) {
                    a = 1;
                } Elseif (a > b) {
                    a = 2;
                } Else {
                    a = 3;
                }
            }    
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(1))]),If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(2))]),Block([AssignStmt(Id(a),IntLit(3))])))]))])])'
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_347(self):
        line = """
        Class Program{
            main(){}
            main(a,b,c:Int){}
        }
        Class notProgram{
            main(){}
        }
        """

        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([]))]),ClassDecl(Id(notProgram),[MethodDecl(Id(main),Instance,[],Block([]))])])'
        self.assertTrue(TestAST.test(line, expect, 347))

    def test_348(self):
        line = """
        Class Program{
            main(){}
            main(a,b,c:Int){}
        }
        Class notProgram{
            main(){}
        }
        """

        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([]))]),ClassDecl(Id(notProgram),[MethodDecl(Id(main),Instance,[],Block([]))])])'
        self.assertTrue(TestAST.test(line, expect, 348))

    def test_349(self):
        input = """
        Class House{
                Constructor(){
                    room::$member = room::$member + 1;
                }
                Destructor(){
                    room::$member = room::$member - 1;
                }
            }
        """
        expect = "Program([ClassDecl(Id(House),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(room),Id($member)),BinaryOp(+,FieldAccess(Id(room),Id($member)),IntLit(1)))])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(FieldAccess(Id(room),Id($member)),BinaryOp(-,FieldAccess(Id(room),Id($member)),IntLit(1)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_350(self):
        input = """
        Class Program {
            foo() {
                Return 1;
            }
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([Return(IntLit(1))]))])])'
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_351(self):
        input = """
        Class Program {
            foo() {
                Return obj.func();
            }
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([Return(CallExpr(Id(obj),Id(func),[]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_352(self):
        input = """
        Class Program {
            foo() {
                Return New func().obj;
            }
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([Return(FieldAccess(NewExpr(Id(func),[]),Id(obj)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_353(self):
        input = """
        Class Program {
            foo() {
                Return vehicle::$car;
            }
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([Return(FieldAccess(Id(vehicle),Id($car)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_354(self):
        input = """
        Class Program {
            foo() {
                Return vehicle::$car[1][2][3];
            }
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([Return(ArrayCell(FieldAccess(Id(vehicle),Id($car)),[IntLit(1),IntLit(2),IntLit(3)]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_355(self):
        input = """
        Class Program {
            foo() {
                Return a/b+c*d;
            }
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([Return(BinaryOp(+,BinaryOp(/,Id(a),Id(b)),BinaryOp(*,Id(c),Id(d))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_356(self):
        input = """
        Class Program {
            foo() {
                Return obj.foo(param1, param2, 2+2, 4, New obj(a, b).k);
            }
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([Return(CallExpr(Id(obj),Id(foo),[Id(param1),Id(param2),BinaryOp(+,IntLit(2),IntLit(2)),IntLit(4),FieldAccess(NewExpr(Id(obj),[Id(a),Id(b)]),Id(k))]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_357(self):
        input = """
        Class Program {
            foo() {
                Return a[1][2][3];
            }
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([Return(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_358(self):
        input = """
        Class Program {
            foo() {
                Return New X(1, 2, a, b);
            }
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([Return(NewExpr(Id(X),[IntLit(1),IntLit(2),Id(a),Id(b)]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_359(self):
        input = """
        Class Program {
            foo() {
                Return outer.inner()[1][2];
            }
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([Return(ArrayCell(CallExpr(Id(outer),Id(inner),[]),[IntLit(1),IntLit(2)]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_360(self):
        input = """
        Class Program {
            foo() {
                Return (a <= b) || (a >= b) && (a == b);
            }
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([Return(BinaryOp(&&,BinaryOp(||,BinaryOp(<=,Id(a),Id(b)),BinaryOp(>=,Id(a),Id(b))),BinaryOp(==,Id(a),Id(b))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_361(self):
        input = """
        Class Program {
            Val a : Int = 0x0 + 0X0 + 0b0 + 0B0 + 00 + 0;
        }"""
        expect = 'Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(0),IntLit(0)),IntLit(0)),IntLit(0)),IntLit(0)),IntLit(0))))])])'
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_362(self):
        input = """
        Class Program {
            Val a : Int = ClassABC::$a.b.c[1][2][(0 + 012 + 0xAB + 0XAB + 0b10 + 0B10)];
        }"""
        expect = 'Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,ArrayCell(FieldAccess(FieldAccess(FieldAccess(Id(ClassABC),Id($a)),Id(b)),Id(c)),[IntLit(1),IntLit(2),BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(0),IntLit(10)),IntLit(171)),IntLit(171)),IntLit(2)),IntLit(2))])))])])'
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_363(self):
        input = """
        Class Program{
            Var _abc, $_abc: abc_123;
            foo(){
                Var a_1,b_2: ABC;
            }
        }"""
        expect = 'Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(_abc),ClassType(Id(abc_123)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($_abc),ClassType(Id(abc_123)),NullLiteral())),MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a_1),ClassType(Id(ABC)),NullLiteral()),VarDecl(Id(b_2),ClassType(Id(ABC)),NullLiteral())]))])])'
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_364(self):
        input = """
        Class Program{
            foo(){
                Break;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([Break]))])])'
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_365(self):
        input = """
        Class Program{
            foo(){
                Continue;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([Continue]))])])'
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_366(self):
        input = """
        Class Program{
            foo(){
                Continue;
                Return;                
                Return a==.!b;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([Continue,Return(),Return(BinaryOp(==.,Id(a),UnaryOp(!,Id(b))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_367(self):
        input = """
        Class Program{
            foo(){
                Foreach (x In 1 .. 100 By 1){
                    Break;
                }               

                Foreach (x In a .. b By c){
                    Continue;
                }
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([For(Id(x),IntLit(1),IntLit(100),IntLit(1),Block([Break])]),For(Id(x),Id(a),Id(b),Id(c),Block([Continue])])]))])])'
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_368(self):
        input = """
        Class Program {
            foo(a,b,c:Int){
                Var people:Int = 0x0;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([VarDecl(Id(people),IntType,IntLit(0))]))])])'
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_369(self):
        input = """Class Program {
            foo(a,b : Int; c,d : Boolean) {
                Self.callFunc(1, a != b);
            }
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),BoolType),param(Id(d),BoolType)],Block([Call(Self(),Id(callFunc),[IntLit(1),BinaryOp(!=,Id(a),Id(b))])]))])])'
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_370(self):
        input = """Class Program {
            foo(a,b : Int; c,d : Boolean) {
                Self.callFunc(1, a != b);
            }
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),BoolType),param(Id(d),BoolType)],Block([Call(Self(),Id(callFunc),[IntLit(1),BinaryOp(!=,Id(a),Id(b))])]))])])'
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_371(self):
        input = """Class Program {
            foo(a,b : Int; c,d : Boolean) {}
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),BoolType),param(Id(d),BoolType)],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_372(self):
        input = """
        Class A {
            Var a:Int=!!a--2*----3;
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(-,UnaryOp(!,UnaryOp(!,Id(a))),BinaryOp(*,UnaryOp(-,IntLit(2)),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(3)))))))))])])'
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_373(self):
        input = """
        Class A {
            Val b:Z = New a(ABC,Null);
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(b),ClassType(Id(Z)),NewExpr(Id(a),[Id(ABC),NullLiteral()])))])])'
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_374(self):
        input = """
        Class Dog:Animal{
            Var name,$tail:String;
        }
        """
        expect = 'Program([ClassDecl(Id(Dog),Id(Animal),[AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Static,VarDecl(Id($tail),StringType))])])'
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_375(self):
        input = """Class Program {
            foo() {
                If (a == b) {
                    If (a == b) {
                        Self.print("Index out of bound");
                    } Else {
                        a[1][2] = d[(a+1)][(a*b)];
                    }
                } Elseif ( i == (j + 1)) {
                    ##pass next##
                } Else {
                    Out.println("Error hehe");
                }
            }
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([If(BinaryOp(==,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Index out of bound)])]),Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),ArrayCell(Id(d),[BinaryOp(+,Id(a),IntLit(1)),BinaryOp(*,Id(a),Id(b))]))]))]),If(BinaryOp(==,Id(i),BinaryOp(+,Id(j),IntLit(1))),Block([]),Block([Call(Id(Out),Id(println),[StringLit(Error hehe)])])))]))])])'
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_376(self):
        input = """
        Class stuff:things{
            Constructor(){
                List[stuff::$num] = d;
                stuff::$num = stuff::$num + 1;
            }
            Destructor(){
                a = b[5];
            }
        }
        """
        expect = 'Program([ClassDecl(Id(stuff),Id(things),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(ArrayCell(Id(List),[FieldAccess(Id(stuff),Id($num))]),Id(d)),AssignStmt(FieldAccess(Id(stuff),Id($num)),BinaryOp(+,FieldAccess(Id(stuff),Id($num)),IntLit(1)))])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(Id(a),ArrayCell(Id(b),[IntLit(5)]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_377(self):
        input = """
        Class Program {
            foo() {
                If (a == b) {
                    If (a == b) {
                        Self.print("Index out of bound");
                    } Else {
                        a[1][2] = d[(a+1)][(a*b)];
                    }
                } Elseif ( i == (j + 1)) {
                    ##pass next##
                } Else {
                    Foreach (i In a .. b By a[5]/2) {
                        b = b + 1;
                        Self.print(d.foo().a.bar());
                    }
                }
            }
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([If(BinaryOp(==,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Index out of bound)])]),Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),ArrayCell(Id(d),[BinaryOp(+,Id(a),IntLit(1)),BinaryOp(*,Id(a),Id(b))]))]))]),If(BinaryOp(==,Id(i),BinaryOp(+,Id(j),IntLit(1))),Block([]),Block([For(Id(i),Id(a),Id(b),BinaryOp(/,ArrayCell(Id(a),[IntLit(5)]),IntLit(2)),Block([AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1))),Call(Self(),Id(print),[CallExpr(FieldAccess(CallExpr(Id(d),Id(foo),[]),Id(a)),Id(bar),[])])])])])))]))])])'
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_378(self):
        input = """
        Class stuff:things{
            Constructor(temperature:Int){
                Self.temperature = temperature;
                List[stuff::$num] = d;
                stuff::$num = stuff::$num + 1;
            }
            Destructor(){
                a = b[5];
            }
        }
        """
        expect = 'Program([ClassDecl(Id(stuff),Id(things),[MethodDecl(Id(Constructor),Instance,[param(Id(temperature),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(temperature)),Id(temperature)),AssignStmt(ArrayCell(Id(List),[FieldAccess(Id(stuff),Id($num))]),Id(d)),AssignStmt(FieldAccess(Id(stuff),Id($num)),BinaryOp(+,FieldAccess(Id(stuff),Id($num)),IntLit(1)))])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(Id(a),ArrayCell(Id(b),[IntLit(5)]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_379(self):
        input = """
        Class stuff:things{
            Constructor(temperature:Int){
                Self.temperature = temperature;
                List[stuff::$num] = d;
                stuff::$num = stuff::$num + 1;
            }
            Destructor(){
                a = b[5];
            }

            foo(){
                a.b.c[1]=d.e.f(1,2+3);
            }
        }
        """
        expect = 'Program([ClassDecl(Id(stuff),Id(things),[MethodDecl(Id(Constructor),Instance,[param(Id(temperature),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(temperature)),Id(temperature)),AssignStmt(ArrayCell(Id(List),[FieldAccess(Id(stuff),Id($num))]),Id(d)),AssignStmt(FieldAccess(Id(stuff),Id($num)),BinaryOp(+,FieldAccess(Id(stuff),Id($num)),IntLit(1)))])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(Id(a),ArrayCell(Id(b),[IntLit(5)]))])),MethodDecl(Id(foo),Instance,[],Block([AssignStmt(ArrayCell(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),[IntLit(1)]),CallExpr(FieldAccess(Id(d),Id(e)),Id(f),[IntLit(1),BinaryOp(+,IntLit(2),IntLit(3))]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_380(self):
        input = """
        Class stuff:things{
            Constructor(temperature:Int){
                Self.temperature = temperature;
                List[stuff::$num] = d;
                stuff::$num = stuff::$num + 1;
            }
            Destructor(){
                a = b[5];
            }

            foo() {
                If (a == b) {
                    If (a == b) {
                        Self.print("Index out of bound");
                    } Else {
                        a[1][2] = d[(a+1)][(a*b)];
                    }
                } Elseif ( i == (j + 1)) {
                    ##pass next##
                } Else {
                    Foreach (i In a .. b By a[5]/2) {
                        b = b + 1;
                        Self.print(d.foo().a.bar());
                    }
                }
            }
        }
        """
        expect = 'Program([ClassDecl(Id(stuff),Id(things),[MethodDecl(Id(Constructor),Instance,[param(Id(temperature),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(temperature)),Id(temperature)),AssignStmt(ArrayCell(Id(List),[FieldAccess(Id(stuff),Id($num))]),Id(d)),AssignStmt(FieldAccess(Id(stuff),Id($num)),BinaryOp(+,FieldAccess(Id(stuff),Id($num)),IntLit(1)))])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(Id(a),ArrayCell(Id(b),[IntLit(5)]))])),MethodDecl(Id(foo),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([If(BinaryOp(==,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Index out of bound)])]),Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),ArrayCell(Id(d),[BinaryOp(+,Id(a),IntLit(1)),BinaryOp(*,Id(a),Id(b))]))]))]),If(BinaryOp(==,Id(i),BinaryOp(+,Id(j),IntLit(1))),Block([]),Block([For(Id(i),Id(a),Id(b),BinaryOp(/,ArrayCell(Id(a),[IntLit(5)]),IntLit(2)),Block([AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1))),Call(Self(),Id(print),[CallExpr(FieldAccess(CallExpr(Id(d),Id(foo),[]),Id(a)),Id(bar),[])])])])])))]))])])'
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_381(self):
        input = """
        Class notProgram {
            notfunc() {
                Val a, b : Float = 2.e20-10, 0.10e+10;
            }
        }"""
        expect = 'Program([ClassDecl(Id(notProgram),[MethodDecl(Id(notfunc),Instance,[],Block([ConstDecl(Id(a),FloatType,BinaryOp(-,FloatLit(2e+20),IntLit(10))),ConstDecl(Id(b),FloatType,FloatLit(1000000000.0))]))])])'
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_382(self):
        input = """
        Class Program {
            foo(){
                Var a:B = c.d.e(f,g) + h;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),ClassType(Id(B)),BinaryOp(+,CallExpr(FieldAccess(Id(c),Id(d)),Id(e),[Id(f),Id(g)]),Id(h)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_383(self):
        line = """
        Class Program{
            foo(){
                Foreach (x In a::$b() .. a.b.c.d By a::$foo){
                    Foreach (x In a::$b() .. a.b.c.d By a::$foo){
                    }
                }
            }
            foo1(){
                Var a:B = c.d.e(f,g) + h;
            }
            foo2() {
                If (a == b) {
                    If (a == b) {
                        Self.print("Index out of bound");
                    } Else {
                        a[1][2] = d[(a+1)][(a*b)];
                    }
                } Elseif ( i == (j + 1)) {
                    ##pass next##
                } Else {
                    Foreach (i In a .. b By a[5]/2) {
                        b = b + 1;
                        Self.print(d.foo().a.bar());
                    }
                }
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([For(Id(x),CallExpr(Id(a),Id($b),[]),FieldAccess(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d)),FieldAccess(Id(a),Id($foo)),Block([For(Id(x),CallExpr(Id(a),Id($b),[]),FieldAccess(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d)),FieldAccess(Id(a),Id($foo)),Block([])])])])])),MethodDecl(Id(foo1),Instance,[],Block([VarDecl(Id(a),ClassType(Id(B)),BinaryOp(+,CallExpr(FieldAccess(Id(c),Id(d)),Id(e),[Id(f),Id(g)]),Id(h)))])),MethodDecl(Id(foo2),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([If(BinaryOp(==,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Index out of bound)])]),Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),ArrayCell(Id(d),[BinaryOp(+,Id(a),IntLit(1)),BinaryOp(*,Id(a),Id(b))]))]))]),If(BinaryOp(==,Id(i),BinaryOp(+,Id(j),IntLit(1))),Block([]),Block([For(Id(i),Id(a),Id(b),BinaryOp(/,ArrayCell(Id(a),[IntLit(5)]),IntLit(2)),Block([AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1))),Call(Self(),Id(print),[CallExpr(FieldAccess(CallExpr(Id(d),Id(foo),[]),Id(a)),Id(bar),[])])])])])))]))])])'
        self.assertTrue(TestAST.test(line, expect, 383))

    def test_384(self):
        line = """
        Class Program{
            foo(){
                Foreach (x In a::$b() .. a.b.c.d By fee::$foo){
                    Foreach (x In a::$b() .. a.b.c.d By fee::$foo){
                    }
                }
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([For(Id(x),CallExpr(Id(a),Id($b),[]),FieldAccess(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d)),FieldAccess(Id(fee),Id($foo)),Block([For(Id(x),CallExpr(Id(a),Id($b),[]),FieldAccess(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d)),FieldAccess(Id(fee),Id($foo)),Block([])])])])]))])])'
        self.assertTrue(TestAST.test(line, expect, 384))

    def test_385(self):
        input = """
        Class Program {
            foo() {
                A.a.A.a();
                (a.a[10][9]).fee();
            }
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([Call(FieldAccess(FieldAccess(Id(A),Id(a)),Id(A)),Id(a),[]),Call(ArrayCell(FieldAccess(Id(a),Id(a)),[IntLit(10),IntLit(9)]),Id(fee),[])]))])])'
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_386(self):
        input = """
        Class Program {
            foo() {
                Motor::$Bike.foo();
                (Bike::$Motor.a[8][8]).fee();
            }
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),Instance,[],Block([Call(FieldAccess(Id(Motor),Id($Bike)),Id(foo),[]),Call(ArrayCell(FieldAccess(FieldAccess(Id(Bike),Id($Motor)),Id(a)),[IntLit(8),IntLit(8)]),Id(fee),[])]))])])'
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_387(self):
        input = """
        Class Program {
            main() {
                Var a : Int = a.b();
                Val a,b: Int = a[5], b[10][11];
                Val sth : Sth = New Sth();
                Return;
            }
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,CallExpr(Id(a),Id(b),[])),ConstDecl(Id(a),IntType,ArrayCell(Id(a),[IntLit(5)])),ConstDecl(Id(b),IntType,ArrayCell(Id(b),[IntLit(10),IntLit(11)])),ConstDecl(Id(sth),ClassType(Id(Sth)),NewExpr(Id(Sth),[])),Return()]))])])'
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_388(self):
        input = """
        Class a_program {
            func(){
                a.printf("enter");
                a1.scanf("%b", c);
            }
        }
        """
        expect = 'Program([ClassDecl(Id(a_program),[MethodDecl(Id(func),Instance,[],Block([Call(Id(a),Id(printf),[StringLit(enter)]),Call(Id(a1),Id(scanf),[StringLit(%b),Id(c)])]))])])'
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_389(self):
        input = """
        Class a_program {
            func(){
                a.printf("enter");
                a1.scanf("%b", c);
            }
        }

        Class Program2 {
            main() {
                Var a : Int = a.b();
                Val a,b: Int = a[5], b[10][11];
                Val sth : Sth = New Sth();
                Return;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(a_program),[MethodDecl(Id(func),Instance,[],Block([Call(Id(a),Id(printf),[StringLit(enter)]),Call(Id(a1),Id(scanf),[StringLit(%b),Id(c)])]))]),ClassDecl(Id(Program2),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(a),IntType,CallExpr(Id(a),Id(b),[])),ConstDecl(Id(a),IntType,ArrayCell(Id(a),[IntLit(5)])),ConstDecl(Id(b),IntType,ArrayCell(Id(b),[IntLit(10),IntLit(11)])),ConstDecl(Id(sth),ClassType(Id(Sth)),NewExpr(Id(Sth),[])),Return()]))])])'
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_390(self):
        input = """
        Class a_program {
            func(){
                a.printf("enter");
                a1.scanf("%b", c);
            }
        }

        Class Program2 {
            main() {
                y[x][a::$b().c[d::$e().f[g::$h().i]]] = 1000;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(a_program),[MethodDecl(Id(func),Instance,[],Block([Call(Id(a),Id(printf),[StringLit(enter)]),Call(Id(a1),Id(scanf),[StringLit(%b),Id(c)])]))]),ClassDecl(Id(Program2),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(Id(y),[Id(x),ArrayCell(FieldAccess(CallExpr(Id(a),Id($b),[]),Id(c)),[ArrayCell(FieldAccess(CallExpr(Id(d),Id($e),[]),Id(f)),[FieldAccess(CallExpr(Id(g),Id($h),[]),Id(i))])])]),IntLit(1000))]))])])'
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_391(self):
        input = """
        Class Program2 {
            main() {
                y[x][a::$b().c[d::$e().f[g::$h().i]]] = 1000;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Program2),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(Id(y),[Id(x),ArrayCell(FieldAccess(CallExpr(Id(a),Id($b),[]),Id(c)),[ArrayCell(FieldAccess(CallExpr(Id(d),Id($e),[]),Id(f)),[FieldAccess(CallExpr(Id(g),Id($h),[]),Id(i))])])]),IntLit(1000))]))])])'
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_392(self):
        input = """
        Class Program {
            Constructor(a : customclass; d : Int) {}
            Constructor(a, b : customclass; d, e : Int) {}
            Constructor(a, b : customclass; d, e : Array[Array[Int, 100], 100]) {}
        }"""
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[param(Id(a),ClassType(Id(customclass))),param(Id(d),IntType)],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(a),ClassType(Id(customclass))),param(Id(b),ClassType(Id(customclass))),param(Id(d),IntType),param(Id(e),IntType)],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(a),ClassType(Id(customclass))),param(Id(b),ClassType(Id(customclass))),param(Id(d),ArrayType(100,ArrayType(100,IntType))),param(Id(e),ArrayType(100,ArrayType(100,IntType)))],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_393(self):
        input = """
        Class Program1 {
            Destructor() {}
        }
        Class Program2 : Program3 {
            Destructor() {}
            Destructor() {}
        }"""
        expect = 'Program([ClassDecl(Id(Program1),[MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program2),Id(Program3),[MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_394(self):
        input = """
        Class Program1 {
            Var b : Array[String, 10] = Array("This is a string", "Another string", "A", "B\\n");
            Var a:Int=\"abc\"+.1+2;
            Destructor() {}
        }
        Class Program2 : Program3 {
            Destructor() {}
            Destructor() {}
        }"""
        expect = 'Program([ClassDecl(Id(Program1),[AttributeDecl(Instance,VarDecl(Id(b),ArrayType(10,StringType),[StringLit(This is a string),StringLit(Another string),StringLit(A),StringLit(B\\n)])),AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+.,StringLit(abc),BinaryOp(+,IntLit(1),IntLit(2))))),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program2),Id(Program3),[MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_395(self):
        input = """
        Class Program1 {
            Var b : aclass = Null;
            Val c : anotherclass = Self;
            Destructor() {}
            Val a : Int = obj.foo[10];
            Var b : ABC = (obj[10]).foo;
        }

        Class Program100 {
            Var b : aclass = Null;
            Val c : anotherclass = Self;
            Destructor() {}
            Val a : Int = obj.foo[10];
            Var b : ABC = (obj[10]).foo;
        }
        Class Program2 : Program3 {
            Destructor() {}
            Destructor() {}
            foo() {
                Return a[1][2][3];
            }
        }
        Class Program2 : Program3 {
            Destructor() {}
            Destructor() {}
        }"""
        expect = 'Program([ClassDecl(Id(Program1),[AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(aclass)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(c),ClassType(Id(anotherclass)),Self())),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,ConstDecl(Id(a),IntType,ArrayCell(FieldAccess(Id(obj),Id(foo)),[IntLit(10)]))),AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(ABC)),FieldAccess(ArrayCell(Id(obj),[IntLit(10)]),Id(foo))))]),ClassDecl(Id(Program100),[AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(aclass)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(c),ClassType(Id(anotherclass)),Self())),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,ConstDecl(Id(a),IntType,ArrayCell(FieldAccess(Id(obj),Id(foo)),[IntLit(10)]))),AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(ABC)),FieldAccess(ArrayCell(Id(obj),[IntLit(10)]),Id(foo))))]),ClassDecl(Id(Program2),Id(Program3),[MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(foo),Instance,[],Block([Return(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]))]))]),ClassDecl(Id(Program2),Id(Program3),[MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_396(self):
        input = """
        Class Program100 {
            Var b : aclass = Null;
            Val c : anotherclass = Self;
            Destructor() {}
            Val a : Int = obj.foo[10];
            Var b : ABC = (obj[10]).foo;
        }
        Class Program2 : Program3 {
            Destructor() {}
            Destructor() {}
            foo() {
                Return a[1][2][3];
            }
        }
        Class Program2 : Program3 {
            Destructor() {}
            Destructor() {}
        }"""
        expect = 'Program([ClassDecl(Id(Program100),[AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(aclass)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(c),ClassType(Id(anotherclass)),Self())),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,ConstDecl(Id(a),IntType,ArrayCell(FieldAccess(Id(obj),Id(foo)),[IntLit(10)]))),AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(ABC)),FieldAccess(ArrayCell(Id(obj),[IntLit(10)]),Id(foo))))]),ClassDecl(Id(Program2),Id(Program3),[MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(foo),Instance,[],Block([Return(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]))]))]),ClassDecl(Id(Program2),Id(Program3),[MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_397(self):
        input = """
        Class Program1 {
            Var b : aclass = Null;
            Val c : anotherclass = Self;
            Destructor() {}
            Val a : Int = obj.foo[10];
            Var b : ABC = (obj[10]).foo;
        }
        Class Program2 : Program3 {
            Destructor() {}
            Destructor() {}
            foo() {
                Return a[1][2][3];
            }
        }
        Class Program {
            Var a : Int;
            Var $arr : Array[Int, 10];
        }
        """
        expect = 'Program([ClassDecl(Id(Program1),[AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(aclass)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(c),ClassType(Id(anotherclass)),Self())),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,ConstDecl(Id(a),IntType,ArrayCell(FieldAccess(Id(obj),Id(foo)),[IntLit(10)]))),AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(ABC)),FieldAccess(ArrayCell(Id(obj),[IntLit(10)]),Id(foo))))]),ClassDecl(Id(Program2),Id(Program3),[MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(foo),Instance,[],Block([Return(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]))]))]),ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id($arr),ArrayType(10,IntType)))])])'
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_398(self):
        input = """
        Class Program1 {
            Var b : aclass = Null;
            Val c : anotherclass = Self;
            Destructor() {}
            Val a : Int = obj.foo[10];
            Var b : ABC = (obj[10]).foo;
        }
        Class Program2 : Program3 {
            Destructor() {}
            Destructor() {}
            foo() {
                Return a[1][2][3];
            }
            foo1(a,b : Int; c,d : Boolean) {
                Self.callFunc(1, a != b);
            }
        }"""
        expect = 'Program([ClassDecl(Id(Program1),[AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(aclass)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(c),ClassType(Id(anotherclass)),Self())),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,ConstDecl(Id(a),IntType,ArrayCell(FieldAccess(Id(obj),Id(foo)),[IntLit(10)]))),AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(ABC)),FieldAccess(ArrayCell(Id(obj),[IntLit(10)]),Id(foo))))]),ClassDecl(Id(Program2),Id(Program3),[MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(foo),Instance,[],Block([Return(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]))])),MethodDecl(Id(foo1),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),BoolType),param(Id(d),BoolType)],Block([Call(Self(),Id(callFunc),[IntLit(1),BinaryOp(!=,Id(a),Id(b))])]))])])'
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_399(self):
        input = """
        Class Program1 {
            Var b : aclass = Null;
            Val c : anotherclass = Self;
            Destructor() {}
            Val a : Int = obj.foo[10];
            Var b : ABC = (obj[10]).foo;
        }
        Class Program2 : Program3 {
            Destructor() {}
            Destructor() {}

            Var a : Int;
            Var $arr : Array[Int, 10];

            foo() {
                Return a[1][2][3];
            }
            foo1(a,b : Int; c,d : Boolean) {
                Self.callFunc(1, a != b);
            }

            a() {
                If (a == b) {
                    a = 1;
                } Elseif (a > b) {
                    a = 2;
                } Else {
                    a = 3;
                }
            }    
        }"""
        expect = 'Program([ClassDecl(Id(Program1),[AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(aclass)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(c),ClassType(Id(anotherclass)),Self())),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,ConstDecl(Id(a),IntType,ArrayCell(FieldAccess(Id(obj),Id(foo)),[IntLit(10)]))),AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(ABC)),FieldAccess(ArrayCell(Id(obj),[IntLit(10)]),Id(foo))))]),ClassDecl(Id(Program2),Id(Program3),[MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id($arr),ArrayType(10,IntType))),MethodDecl(Id(foo),Instance,[],Block([Return(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]))])),MethodDecl(Id(foo1),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),BoolType),param(Id(d),BoolType)],Block([Call(Self(),Id(callFunc),[IntLit(1),BinaryOp(!=,Id(a),Id(b))])])),MethodDecl(Id(a),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(1))]),If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(2))]),Block([AssignStmt(Id(a),IntLit(3))])))]))])])'
        self.assertTrue(TestAST.test(input, expect, 399))
