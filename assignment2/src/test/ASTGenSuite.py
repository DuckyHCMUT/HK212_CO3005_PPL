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
            Var a: Int;
            Val __f: Int = 1000;
            Var b, c, $d, $e, _f: Float = 10, -20.1, 30.2, 40.3, 50.4 - 1;
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,ConstDecl(Id(__f),IntType,IntLit(1000))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(10))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,UnaryOp(-,FloatLit(20.1)))),AttributeDecl(Static,VarDecl(Id($d),FloatType,FloatLit(30.2))),AttributeDecl(Static,VarDecl(Id($e),FloatType,FloatLit(40.3))),AttributeDecl(Instance,VarDecl(Id(_f),FloatType,BinaryOp(-,FloatLit(50.4),IntLit(1))))])])"
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
        """Simple program, with few array attribute members"""
        input = """
        Class Program{
            Var arr, $brr: Array[Array[Array[Float, 3], 2], 1];
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(IntLit(3),ArrayType(IntLit(2),ArrayType(IntLit(1),FloatType))))),AttributeDecl(Static,VarDecl(Id($brr),ArrayType(IntLit(3),ArrayType(IntLit(2),ArrayType(IntLit(1),FloatType)))))])])"""
        self.assertTrue(TestAST.test(input, expect, 407))

    # def test_simple_program_408(self):
    #     """Simple program, with few assigned array attribute member"""
    #     input = """
    #     Class Program{
    #         Var arr: Array[Array[Int, 2], 3] = Array(Array(2, 3), Array(-5, 5), Array(1.2, 4));
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 408))

    def test_simple_program_409(self):
        """Simple program, with assigned member that are expression"""
        input = """
        Class Program{
            Val a: Int = 4 + 5;
            Var $b: Float = a + 2.3;
            Val c, d: Int = 0x413EFFAB, 0B0;
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(+,IntLit(4),IntLit(5)))),AttributeDecl(Static,VarDecl(Id($b),FloatType,BinaryOp(+,Id(a),FloatLit(2.3)))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,IntLit(0x413EFFAB))),AttributeDecl(Instance,ConstDecl(Id(d),IntType,IntLit(0B0)))])])"""
        self.assertTrue(TestAST.test(input, expect, 409))

    # def test_simple_program_410(self):
    #     input = """
    #     Class Program {
    #         Val c: Int = 0x413EFFAB;
    #         main(){
    #             Val c: Int = 0x413EFFAB;
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(c),IntType,IntLit(1094647723))),MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(c),IntType,IntLit(1094647723))]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 410))

    def test_method_411(self):
        """Program with methods"""
        input = """
        Class Program{
            notMain(){
                Val a, b, c: Int;
            }
            ##Constructor(){
                
            }
            Destructor(){

            }##
        }
        """
        expect = """"""
        self.assertTrue(TestAST.test(input, expect, 411))