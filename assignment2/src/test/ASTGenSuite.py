import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # def test_simple_program_301(self):
    #     """ Simple program with nothing
    #         First testcase from BKEL """
    #     input = """
    #     Class Program{

    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[])])"""
    #     self.assertTrue(TestAST.test(input, expect, 301))

    # def test_simple_program_302(self):
    #     """ Simple program with nothing
    #     Second testcase from BKEL """
    #     input = "Class Rectangle : Shape {}"
    #     expect = """Program([ClassDecl(Id(Rectangle),Id(Shape),[])])"""
    #     self.assertTrue(TestAST.test(input, expect, 302))

    # def test_simple_program_303(self):
    #     """ Simple program with nothing
    #     Third testcase from BKEL """
    #     input = """
    #     Class Rectangle {
    #         Var length: Int;
    #     }"""
    #     expect = """Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(length),IntType))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 303))
        
    def test_simple_program_304(self):
        """Simple program, with few class members
        Fourth testcase from BKEL """
        input = """
        Class Rectangle {
            Val $x, y, z: Int = 10, 10 + 10, 1000;
        }"""
        expect = " "
        #expect = """Program([ClassDecl(Id(Rectangle),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(10)))]), AttributeDecl(Instance,ConstDecl(Id(y),IntType,IntLit(100)))])])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    # def test_simple_program_305(self):
    #     """Simple program, with few class members"""
    #     input = """
    #     Class Program{
    #         Val x, $y, z: Int;
    #         Var t: Float = 3.108;
    #         Val f: Float;
    #     }
    #     """
    #     expect = """ """
    #     self.assertTrue(TestAST.test(input, expect, 305))

    # def test_simple_program_306(self):
    #     """Simple program, with nothing but inheritance and many classes"""
    #     input = """
    #     Class Program : Parent{}
    #     Class Subprogram{}
    #     """
    #     expect = """Program([ClassDecl(Id(Program),Id(Parent),[]),ClassDecl(Id(Subprogram),[])])"""
    #     self.assertTrue(TestAST.test(input, expect, 306))

    

    