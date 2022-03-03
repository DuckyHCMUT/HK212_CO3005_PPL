import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_program_simple(self):
        input = """Class A{
            foo(){}
        }"""
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_program_superclass(self):
        input = """
        Class A{}
        Class B:A{}
        """
        expect = "Program([ClassDecl(Id(A),[]),ClassDecl(Id(B),Id(A),[])])"
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_attrdecl_simple_1(self):
        input = """
        Class A{
            Val a,c: Int;       ## Int ##
            Var $b: Float;      ## Float ##
        }
        """
        expect = "Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(c),IntType,None)),AttributeDecl(Static,VarDecl(Id($b),FloatType))])])"
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_attrdecl_simple_2(self):
        input = """
        Class A:B{
            Var c: Boolean;             ## Boolean ##
            Var d: String;              ## String ##
            Var e: A;                   ## Class Type ##
            Var f: Array[Float, 5];     ## Array Type ##
        }
        """
        expect = """Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,VarDecl(Id(c),BoolType)),AttributeDecl(Instance,VarDecl(Id(d),StringType)),AttributeDecl(Instance,VarDecl(Id(e),ClassType(Id(A)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(f),ArrayType(5,FloatType)))])])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_attrdecl_multiarray(self):
        input = """
        Class A:B{
            Val $arr: Array[Array[String, 1], 012];
        }
        """
        expect = """Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Static,ConstDecl(Id($arr),ArrayType(10,ArrayType(1,StringType)),None))])])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_attrdecl_complex_1(self):
        input = """
        Class A{
            Val a,$b: Int = 00, 03_1_4;
            Var c,$d,e,f: Int = 1_5, 0B10, 0xFF, 0X0;
        }
        """
        expect = """Program([ClassDecl(Id(A),[
            AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),
            AttributeDecl(Static,ConstDecl(Id($b),IntType,IntLit(204))),
            AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(15))),
            AttributeDecl(Static,VarDecl(Id($d),IntType,IntLit(2))),
            AttributeDecl(Instance,VarDecl(Id(e),IntType,IntLit(255))),
            AttributeDecl(Instance,VarDecl(Id(f),IntType,IntLit(0)))
            ])])
            """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_attrdecl_complex_2(self):
        input = """
        Class A{
            Var a,b,c,d: Float = 2.5e-6, .5E+7, 1_2.56, 1_2e2;
            Val e,$f: Boolean = True, False;
            Var s: String = "Hello";
            Var n: String = Null;
            Var c: A = Self;
        }
        """
        expect = """Program([ClassDecl(Id(A),[
            AttributeDecl(Instance,VarDecl(Id(a),FloatType,FloatLit(2.5e-06))),
            AttributeDecl(Instance,VarDecl(Id(b),FloatType,FloatLit(5000000.0))),
            AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(12.56))),
            AttributeDecl(Instance,VarDecl(Id(d),FloatType,FloatLit(1200.0))),
            AttributeDecl(Instance,ConstDecl(Id(e),BoolType,BooleanLit(True))),
            AttributeDecl(Static,ConstDecl(Id($f),BoolType,BooleanLit(False))),
            AttributeDecl(Instance,VarDecl(Id(s),StringType,StringLit(Hello))),
            AttributeDecl(Instance,VarDecl(Id(n),StringType,NullLiteral())),
            AttributeDecl(Instance,VarDecl(Id(c),ClassType(Id(A)),Self()))
            ])])
            """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_attrdecl_complex_3(self):
        input = """
        Class A{
            Val a: Int = 5;
            Var arr: Array[Int, 2] = Array(1,a+1);
            Var c: Float = arr[0] + 1.5;
        }
        """
        expect = """Program([ClassDecl(Id(A),[
            AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(5))),
            AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(2,IntType),[IntLit(1),BinaryOp(+,Id(a),IntLit(1))])),
            AttributeDecl(Instance,VarDecl(Id(c),FloatType,
            BinaryOp(+,ArrayCell(Id(arr),[IntLit(0)]),FloatLit(1.5))))
            ])])
            """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_method_simple(self):
        input = """
        Class A{
            foo(){}
            $sfoo(){}
        }
        """
        expect = """Program([ClassDecl(Id(A),[
                MethodDecl(Id(foo),Instance,[],Block([])),
                MethodDecl(Id($sfoo),Static,[],Block([]))
            ])])
            """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_method_param(self):
        input = """
        Class A{
            foo(a,b: Int; c:Float){}
        }
        """
        expect = """Program([ClassDecl(Id(A),[
                MethodDecl(Id(foo),Instance,[
                    param(Id(a),IntType),
                    param(Id(b),IntType),
                    param(Id(c),FloatType)
                ],Block([]))
            ])])
            """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_constructor_destructor(self):
        input = """
        Class A{
            Constructor(c:String){
                Self.a = c;
            }
            Destructor(){}
        }
        """
        expect = """Program([ClassDecl(Id(A),[
                MethodDecl(Id(Constructor),Instance,[
                    param(Id(c),StringType)
                ],Block([
                    AssignStmt(FieldAccess(Self(),Id(a)),Id(c))
                ])),
                MethodDecl(Id(Destructor),Instance,[],Block([]))
            ])])
            """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_vardecl_1(self):
        input = """
        Class A{
            foo(){
                Var a: Int;
                Val b,c: Float;
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            VarDecl(
                                Id(a),
                                IntType
                            ),
                            ConstDecl(
                                Id(b),
                                FloatType,
                                None
                            ),
                            ConstDecl(
                                Id(c),
                                FloatType,
                                None
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_vardecl_2(self):
        input = """
        Class A{
            foo(){
                Var a: Boolean = True;
                Val b: Boolean = False;
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            VarDecl(
                                Id(a),
                                BoolType,
                                BooleanLit(True)
                            ),
                            ConstDecl(
                                Id(b),
                                BoolType,
                                BooleanLit(False)
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_vardecl_3(self):
        input = """
        Class A{
            foo(){
                Var a,b: Int = 1 && 1 , "kaka" ==. "hehe";
                Val c,d: Boolean = a >= b, a || b;
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            VarDecl(
                                Id(a),
                                IntType,
                                BinaryOp(&&, IntLit(1), IntLit(1))
                            ),
                            VarDecl(
                                Id(b),
                                IntType,
                                BinaryOp(==., StringLit(kaka), StringLit(hehe))
                            ),
                            ConstDecl(
                                Id(c),
                                BoolType,
                                BinaryOp(>=, Id(a), Id(b))
                            ),
                            ConstDecl(
                                Id(d),
                                BoolType,
                                BinaryOp(||, Id(a), Id(b))
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_assignment_1(self):
        input = """
        Class A{
            foo(){
                a = 10.5;
                b = a;
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            AssignStmt(
                                Id(a),
                                FloatLit(10.5)
                            ),
                            AssignStmt(
                                Id(b),
                                Id(a)
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_assignment_2(self):
        input = """
        Class A{
            foo(){
                (a + 1)[5] = 10.5;
                a[2][3] = Self.x;
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            AssignStmt(
                                ArrayCell(
                                    BinaryOp(+,Id(a),IntLit(1)),
                                    [IntLit(5)]
                                ),
                                FloatLit(10.5)
                            ),
                            AssignStmt(
                                ArrayCell(
                                    Id(a),
                                    [IntLit(2),IntLit(3)]
                                ),
                                FieldAccess(
                                    Self(),
                                    Id(x)
                                )
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_assignment_3(self):
        input = """
        Class A{
            foo(){
                Self.b.a = 0xF;
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            AssignStmt(
                                FieldAccess(
                                    FieldAccess(
                                        Self(),
                                        Id(b)
                                    ),
                                    Id(a)
                                ),
                                IntLit(15)
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_assignment_4(self):
        input = """
        Class A{
            foo(){
                (a+b).a = 077;
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            AssignStmt(
                                FieldAccess(
                                    BinaryOp(
                                        +,
                                        Id(a),
                                        Id(b)
                                    ),
                                    Id(a)
                                ),
                                IntLit(63)
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_assignment_5(self):
        input = """
        Class A{
            foo(){
                A :: $static_var = 00;
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            AssignStmt(
                                FieldAccess(
                                    Id(A),
                                    Id($static_var)
                                ),
                                IntLit(0)
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_ifstmt_1(self):
        input = """
        Class A{
            foo(){
                If (a == 5) {
                    Return;
                }
                Elseif (a == 6) {
                    Return;
                }
                Else {
                    Return;
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(A),[
                MethodDecl(Id(foo),Instance,[],Block([
                    If(BinaryOp(==,Id(a),IntLit(5)),Block([Return()]),
                        If(BinaryOp(==,Id(a),IntLit(6)),Block([Return()]),Block([
                            Return()
                        ]))
                    )
                ]))
            ])])
            """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_ifstmt_2(self):
        input = """
        Class A{
            foo(){
                If (a[2][2] == 5) {
                    Return;
                }
                If (b != 5) {
                    If (c == 5) {
                        Return;
                    }
                }
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            If(
                                BinaryOp(
                                    ==,
                                    ArrayCell(
                                        Id(a),
                                        [
                                            IntLit(2),
                                            IntLit(2)
                                        ]
                                    ),
                                    IntLit(5)
                                ),
                                Block([
                                    Return()
                                ])
                            ),
                            If(
                                BinaryOp(
                                    !=,
                                    Id(b),
                                    IntLit(5)
                                ),
                                Block([
                                    If(
                                        BinaryOp(
                                            ==,
                                            Id(c),
                                            IntLit(5)
                                        ),
                                        Block([
                                            Return()
                                        ])
                                    )
                                ])
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_ifstmt_3(self):
        input = """
        Class A{
            foo(){
                If (a[2+1][2] == 5) {
                    Return;
                }
                Elseif(Self.value == 7) {
                    A::$sfoo();
                }
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            If(
                                BinaryOp(
                                    ==,
                                    ArrayCell(
                                        Id(a),
                                        [
                                            BinaryOp(
                                                +,
                                                IntLit(2),
                                                IntLit(1)
                                            ),
                                            IntLit(2)
                                        ]
                                    ),
                                    IntLit(5)
                                ),
                                Block([
                                    Return()
                                ]),
                                If(
                                    BinaryOp(
                                        ==,
                                        FieldAccess(
                                            Self(),
                                            Id(value)
                                        ),
                                        IntLit(7)
                                    ),
                                    Block([
                                        Call(
                                            Id(A),
                                            Id($sfoo),
                                            []
                                        )
                                    ])
                                )
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_ifstmt_4(self):
        input = """
        Class A{
            foo(){
                If(1){}
                Else{}
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            If(
                                IntLit(1),
                                Block([]),
                                Block([])
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_forstmt_1(self):
        input = """
        Class A{
            foo(){
                Foreach (i In 1 .. 100 By 2) {
                    Self.print(i);
                }
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            For(
                                Id(i),
                                IntLit(1),
                                IntLit(100),
                                IntLit(2),
                                Block([
                                    Call(
                                        Self(),
                                        Id(print),
                                        [
                                            Id(i)
                                        ]
                                    )
                                ])
                            ])
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_forstmt_2(self):
        input = """
        Class A{
            foo(){
                Foreach (i In 100 .. -(1*3)) {
                    Self.print(i);
                }
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            For(
                                Id(i),
                                IntLit(100),
                                UnaryOp(
                                    -,
                                    BinaryOp(
                                        *,
                                        IntLit(1),
                                        IntLit(3)
                                    )
                                ),
                                IntLit(1),
                                Block([
                                    Call(
                                        Self(),
                                        Id(print),
                                        [
                                            Id(i)
                                        ]
                                    )
                                ])
                            ])
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_forstmt_3(self):
        input = """
        Class A{
            foo(){
                Var arr: Array[Int,5] = Array(1,2,3,4,5);
                Foreach (i In 1 .. arr.len() By 1) {
                    If(arr[i] % 2 == 0) {
                        Self.print(arr[i]);
                    }
                }
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            VarDecl(
                                Id(arr),
                                ArrayType(5,IntType),
                                [IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]
                            ),
                            For(
                                Id(i),
                                IntLit(1),
                                CallExpr(
                                    Id(arr),
                                    Id(len),
                                    []
                                ),
                                IntLit(1),
                                Block([
                                    If(
                                        BinaryOp(
                                            ==,
                                            BinaryOp(
                                                %,
                                                ArrayCell(
                                                    Id(arr),
                                                    [Id(i)]
                                                ),
                                                IntLit(2)
                                            ),
                                            IntLit(0)
                                        ),
                                        Block([
                                            Call(
                                                Self(),
                                                Id(print),
                                                [
                                                    ArrayCell(
                                                        Id(arr),
                                                        [Id(i)]
                                                    )
                                                ]
                                            )
                                        ])
                                    )
                                ])
                            ])
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_callstmt_1(self):
        input = """
        Class A{
            foo(){
                a = New A();
                a.foo();
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            AssignStmt(
                                Id(a),
                                NewExpr(
                                    Id(A),
                                    []
                                )
                            ),
                            Call(
                                Id(a),
                                Id(foo),
                                []
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_callstmt_2(self):
        input = """
        Class A{
            copy(){
                Return Self;
            }
            foo(){
                a = New A();
                a.copy().foo();
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                [
                    MethodDecl(
                        Id(copy),
                        Instance,
                        [],
                        Block([
                            Return(
                                Self()
                            )
                        ])
                    ),
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            AssignStmt(
                                Id(a),
                                NewExpr(
                                    Id(A),
                                    []
                                )
                            ),
                            Call(
                                CallExpr(
                                    Id(a),
                                    Id(copy),
                                    []
                                ),
                                Id(foo),
                                []
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_callstmt_3(self):
        input = """
        Class A{
            $copy(){
                Return Self;
            }
            foo(){
                A::$copy().foo();
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                [
                    MethodDecl(
                        Id($copy),
                        Static,
                        [],
                        Block([
                            Return(
                                Self()
                            )
                        ])
                    ),
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            Call(
                                CallExpr(
                                    Id(A),
                                    Id($copy),
                                    []
                                ),
                                Id(foo),
                                []
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_callstmt_4(self):
        input = """
        Class A{
            $copy(){
                Return Self;
            }
            foo(){
                A::$copy(Self);
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                [
                    MethodDecl(
                        Id($copy),
                        Static,
                        [],
                        Block([
                            Return(
                                Self()
                            )
                        ])
                    ),
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            Call(
                                Id(A),
                                Id($copy),
                                [Self()]
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_callstmt_5(self):
        input = """
        Class A:B{
            Var $static_var: B;
            Var attribute: B;
            copy(){
                Return Self;
            }
            foo(){
                Self.copy().attribute.foo();
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                Id(B),
                [
                    AttributeDecl(
                        Static,
                        VarDecl(
                            Id($static_var),
                            ClassType(Id(B)),
                            NullLiteral()
                        )
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(
                            Id(attribute),
                            ClassType(Id(B)),
                            NullLiteral()
                        )
                    ),
                    MethodDecl(
                        Id(copy),
                        Instance,
                        [],
                        Block([
                            Return(
                                Self()
                            )
                        ])
                    ),
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            Call(
                                FieldAccess(
                                    CallExpr(
                                        Self(),
                                        Id(copy),
                                        []
                                    ),
                                    Id(attribute)
                                ),
                                Id(foo),
                                []
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_return_1(self):
        input = """
        Class A:B{
            foo(){
                Return;
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                Id(B),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            Return()
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_return_2(self):
        input = """
        Class A:B{
            foo(){
                Return Null;
            }
            arr(){
                Return Array(Self);
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                Id(B),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            Return(
                                NullLiteral()
                            )
                        ])
                    ),
                    MethodDecl(
                        Id(arr),
                        Instance,
                        [],
                        Block([
                            Return(
                                [Self()]
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_other_stmt(self):
        input = """
        Class A{
            foo(){
                Foreach (i In 1 .. 100) {
                    If(i == 50) {
                        Break;
                    }               
                    Continue;
                }
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            For(
                                Id(i),
                                IntLit(1),
                                IntLit(100),
                                IntLit(1),
                                Block([
                                    If(
                                        BinaryOp(==,Id(i),IntLit(50)),
                                        Block([
                                            Break
                                        ])
                                    ),
                                    Continue
                                ])
                            ])
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_block(self):
        input = """
        Class A{
            foo(){
                {{}}{}
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            Block([
                                Block([])
                            ]),
                            Block([])
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_main_1(self):
        input = """
        Class Program{
            main(){}
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(Program),
                [
                    MethodDecl(
                        Id(main),
                        Static,
                        [],
                        Block([])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_main_2(self):
        input = """
        Class Program{
            main(a:Int){}
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(Program),
                [
                    MethodDecl(
                        Id(main),
                        Instance,
                        [param(Id(a),IntType)],
                        Block([])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_main_3(self):
        input = """
        Class Not_Program{
            main(){}
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(Not_Program),
                [
                    MethodDecl(
                        Id(main),
                        Instance,
                        [],
                        Block([])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_expr_1(self):
        input = """
        Class Program {
            main() {
                t = a :: $b  + New X(); 
                x = New a() * !!-(x::$y).z(a,b).a[b][a+5] + a && z && y > b +. a >b; 
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(Program),
                [
                    MethodDecl(
                        Id(main),
                        Static,
                        [],
                        Block([
                            AssignStmt(
                                Id(t),
                                BinaryOp(
                                    +,
                                    FieldAccess(Id(a),Id($b)),
                                    NewExpr(Id(X),[])
                                )
                            ),
                            AssignStmt(
                                Id(x),
                                BinaryOp(
                                    +.,
                                    BinaryOp(
                                        >,
                                        BinaryOp(
                                            &&,
                                            BinaryOp(
                                                &&,
                                                BinaryOp(
                                                    +,
                                                    BinaryOp(
                                                        *,
                                                        NewExpr(Id(a),[]),
                                                        UnaryOp(
                                                            !,
                                                            UnaryOp(
                                                                !,
                                                                UnaryOp(
                                                                    -,
                                                                    ArrayCell(
                                                                        FieldAccess(
                                                                            CallExpr(
                                                                                FieldAccess(Id(x),Id($y)),
                                                                                Id(z),
                                                                                [Id(a),Id(b)]
                                                                            ),
                                                                            Id(a)
                                                                        ),
                                                                        [Id(b),BinaryOp(+,Id(a),IntLit(5))]
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    ),
                                                    Id(a)
                                                ),
                                                Id(z)
                                            ),
                                            Id(y)
                                        ),
                                        Id(b)
                                    ),
                                    BinaryOp(>,Id(a),Id(b))
                                )
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_expr_2(self):
        input = """
        Class Program {
            main() {
                t = New X(). y;
                z = a :: $_() . z;  
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(Program),
                [
                    MethodDecl(
                        Id(main),
                        Static,
                        [],
                        Block([
                            AssignStmt(
                                Id(t),
                                FieldAccess(
                                    NewExpr(Id(X),[]),
                                    Id(y)
                                )
                            ),
                            AssignStmt(
                                Id(z),
                                FieldAccess(
                                    CallExpr(
                                        Id(a),
                                        Id($_),
                                        []
                                    ),
                                    Id(z)
                                )
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_expr_3(self):
        input = """Class Program {
            main() {
                t = a :: $b  / New X();
            }
        }"""
        expect = """
        Program([
            ClassDecl(
                Id(Program),
                [
                    MethodDecl(
                        Id(main),
                        Static,
                        [],
                        Block([
                            AssignStmt(
                                Id(t),
                                BinaryOp(
                                    /,
                                    FieldAccess(Id(a), Id($b)),
                                    NewExpr(Id(X),[])
                                )
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_program_1(self):
        input = """
        Class MyArray{
            Var arr: Array[Int,200];
            Var size: Int;
            Constructor(n:Int){
                Self.size = n;
            }
            setValue(value:Int; pos:Int){
                If (pos < Self.size){
                    arr[pos] = value;
                }
            }
            getValue(pos:Int){
                If (pos < Self.size){
                    Return arr[pos];
                }
                Else {
                    Return -1;
                }
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(MyArray),
                [
                    AttributeDecl(
                        Instance,
                        VarDecl(
                            Id(arr),
                            ArrayType(
                                200,
                                IntType
                            )
                        )
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(
                            Id(size),
                            IntType
                        )
                    ),
                    MethodDecl(
                        Id(Constructor),
                        Instance,
                        [param(Id(n),IntType)],
                        Block([
                            AssignStmt(
                                FieldAccess(Self(), Id(size)),
                                Id(n)
                            )
                        ])
                    ),
                    MethodDecl(
                        Id(setValue),
                        Instance,
                        [
                            param(Id(value), IntType),
                            param(Id(pos), IntType)
                        ],
                        Block([
                            If(
                                BinaryOp(<, Id(pos), FieldAccess(
                                    Self(), Id(size)
                                )),
                                Block([
                                    AssignStmt(
                                        ArrayCell(Id(arr),[Id(pos)]),
                                        Id(value)
                                    )
                                ])
                            )
                        ])
                    ),
                    MethodDecl(
                        Id(getValue),
                        Instance,
                        [param(Id(pos),IntType)],
                        Block([
                            If(
                                BinaryOp(<, Id(pos), FieldAccess(
                                    Self(), Id(size)
                                )),
                                Block([
                                    Return(
                                        ArrayCell(Id(arr),[Id(pos)])
                                    )
                                ]),
                                Block([
                                    Return(UnaryOp(-, IntLit(1)))
                                ])
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_program_2(self):
        input = """
        Class MyArray{
            Var arr: Array[Int,200];
            Var size: Int;
            Constructor(n:Int){
                Self.size = n;
            }
            printArray(){
                Foreach (i In 0 .. Self.n - 1 By 1) {
                    System.print(i,"\\n");
                }
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(MyArray),
                [
                    AttributeDecl(
                        Instance,
                        VarDecl(
                            Id(arr),
                            ArrayType(
                                200,
                                IntType
                            )
                        )
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(
                            Id(size),
                            IntType
                        )
                    ),
                    MethodDecl(
                        Id(Constructor),
                        Instance,
                        [param(Id(n),IntType)],
                        Block([
                            AssignStmt(
                                FieldAccess(Self(), Id(size)),
                                Id(n)
                            )
                        ])
                    ),
                    MethodDecl(
                        Id(printArray),
                        Instance,
                        [],
                        Block([
                            For(
                                Id(i),
                                IntLit(0),
                                BinaryOp(
                                    -,
                                    FieldAccess(Self(),Id(n)),
                                    IntLit(1)
                                ),
                                IntLit(1),
                                Block([
                                    Call(
                                        Id(System),
                                        Id(print),
                                        [Id(i), StringLit(\\n)]
                                    )
                                ])
                            ])
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_program_3(self):
        input = """
        Class MyArray{
            Var arr: Array[Int,200];
            Var size: Int;
            Constructor(n:Int){
                Self.size = n;
            }
            printArray(){
                Foreach (i In 0 .. Self.n - 1 By 1) {
                    System.print(i,"\\n");
                }
            }
        }
        Class Program{
            main(){
                arr = New MyArray(5);
                arr.printArray();
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(MyArray),
                [
                    AttributeDecl(
                        Instance,
                        VarDecl(
                            Id(arr),
                            ArrayType(
                                200,
                                IntType
                            )
                        )
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(
                            Id(size),
                            IntType
                        )
                    ),
                    MethodDecl(
                        Id(Constructor),
                        Instance,
                        [param(Id(n),IntType)],
                        Block([
                            AssignStmt(
                                FieldAccess(Self(), Id(size)),
                                Id(n)
                            )
                        ])
                    ),
                    MethodDecl(
                        Id(printArray),
                        Instance,
                        [],
                        Block([
                            For(
                                Id(i),
                                IntLit(0),
                                BinaryOp(
                                    -,
                                    FieldAccess(Self(),Id(n)),
                                    IntLit(1)
                                ),
                                IntLit(1),
                                Block([
                                    Call(
                                        Id(System),
                                        Id(print),
                                        [Id(i), StringLit(\\n)]
                                    )
                                ])
                            ])
                        ])
                    )
                ]
            ),
            ClassDecl(
                Id(Program),
                [
                    MethodDecl(
                        Id(main),
                        Static,
                        [],
                        Block([
                            AssignStmt(
                                Id(arr),
                                NewExpr(Id(MyArray),[IntLit(5)])
                            ),
                            Call(
                                Id(arr),
                                Id(printArray),
                                []
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_program_4(self):
        input = """
        Class MyArray{
            Var $total_len:Int = 0;
            Var arr: Array[Int,200];
            Var size: Int;
            Constructor(n:Int){
                Self.size = n;
                MyArray::$total_len = MyArray::$total_len + n;
            }
        }
        Class Program{
            main(){
                Var arr_list: Array[Int,5];
                Foreach(i In 0 .. 4) {
                    arr_list[i] = New MyArray(System.RandInt(0,200));
                }
                System.Print(MyArray::$total_len);
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(MyArray),
                [
                    AttributeDecl(
                        Static,
                        VarDecl(
                            Id($total_len),
                            IntType,
                            IntLit(0)
                        )
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(
                            Id(arr),
                            ArrayType(
                                200,
                                IntType
                            )
                        )
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(
                            Id(size),
                            IntType
                        )
                    ),
                    MethodDecl(
                        Id(Constructor),
                        Instance,
                        [param(Id(n),IntType)],
                        Block([
                            AssignStmt(
                                FieldAccess(Self(), Id(size)),
                                Id(n)
                            ),
                            AssignStmt(
                                FieldAccess(Id(MyArray),Id($total_len)),
                                BinaryOp(
                                    +,
                                    FieldAccess(Id(MyArray),Id($total_len)),
                                    Id(n)
                                )
                            )
                        ])
                    )
                ]
            ),
            ClassDecl(
                Id(Program),
                [
                    MethodDecl(
                        Id(main),
                        Static,
                        [],
                        Block([
                            VarDecl(
                                Id(arr_list),
                                ArrayType(5, IntType)
                            ),
                            For(
                                Id(i),
                                IntLit(0),
                                IntLit(4),
                                IntLit(1),
                                Block([
                                    AssignStmt(
                                        ArrayCell(Id(arr_list),[Id(i)]),
                                        NewExpr(
                                            Id(MyArray),
                                            [CallExpr(
                                                Id(System),
                                                Id(RandInt),
                                                [IntLit(0), IntLit(200)]
                                            )]
                                        )
                                    )
                                ])
                            ]),
                            Call(
                                Id(System),
                                Id(Print),
                                [FieldAccess(
                                    Id(MyArray), Id($total_len)
                                )]
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_program_5(self):
        input = """
        Class Program{
            Val $val : Int;
            Constructor(){
                Var a,b: Int = 0B11,0b0;
                A::$val = A::$val % b + a;
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(Program),
                [
                    AttributeDecl(
                        Static,
                        ConstDecl(
                            Id($val),
                            IntType,
                            None
                        )
                    ),
                    MethodDecl(
                        Id(Constructor),
                        Instance,
                        [],
                        Block([
                            VarDecl(Id(a), IntType, IntLit(3)),
                            VarDecl(Id(b), IntType, IntLit(0)),
                            AssignStmt(
                                FieldAccess(Id(A), Id($val)),
                                BinaryOp(
                                    +,
                                    BinaryOp(
                                        %,
                                        FieldAccess(Id(A),Id($val)),
                                        Id(b)
                                    ),
                                    Id(a)
                                )
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_program_6(self):
        input = """
        Class Shape {
            foo(){
                a[b[1]][c][Self.foo()] = 1;
            }
            Var e,f : Int = 1 + 1, 1 - 2;
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(Shape),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            AssignStmt(
                                ArrayCell(
                                    Id(a),
                                    [
                                        ArrayCell(Id(b),[IntLit(1)]),
                                        Id(c),
                                        CallExpr(
                                            Self(),
                                            Id(foo),
                                            []
                                        )
                                    ]
                                ),
                                IntLit(1)
                            )
                        ])
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(e),IntType,BinaryOp(+,IntLit(1),IntLit(1)))
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(f),IntType,BinaryOp(-,IntLit(1),IntLit(2)))
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_program_7(self):
        input = """
        Class Shape {
            Var a :Array[Array[Int,2],2] = Array(Array(1,1),Array(1,1));
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(Shape),
                [
                    AttributeDecl(
                        Instance,
                        VarDecl(
                            Id(a),
                            ArrayType(
                                2,
                                ArrayType(2, IntType)
                            ),
                            [
                                [IntLit(1), IntLit(1)],
                                [IntLit(1), IntLit(1)]
                            ]
                        )
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_program_8(self):
        input = """
        Class Shape {
            Constructor(width, height : Int; name:String){
                Self.Area=Self.width*Self.height;
                Self.name="shape"+.name;
            } 
            Destructor(){} 
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(Shape),
                [
                    MethodDecl(
                        Id(Constructor),
                        Instance,
                        [
                            param(Id(width),IntType),
                            param(Id(height),IntType),
                            param(Id(name),StringType)
                        ],
                        Block([
                            AssignStmt(
                                FieldAccess(Self(),Id(Area)),
                                BinaryOp(
                                    *,
                                    FieldAccess(Self(),Id(width)),
                                    FieldAccess(Self(),Id(height))
                                )
                            ),
                            AssignStmt(
                                FieldAccess(Self(),Id(name)),
                                BinaryOp(+.,StringLit(shape),Id(name))
                            )
                        ])
                    ),
                    MethodDecl(
                        Id(Destructor),
                        Instance,
                        [],
                        Block([])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_program_9(self):
        input = """
        Class Program {
            _ab() {}
            main() {
                If (a <b ) 
                {
                    System.print("lesser");
                }
                Elseif( a == b)
                {
                    System.print("equal");
                }
                Elseif ( a > b)
                {
                    System.print("greater");
                }
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(Program),
                [
                    MethodDecl(
                        Id(_ab),
                        Instance,
                        [],
                        Block([])
                    ),
                    MethodDecl(
                        Id(main),
                        Static,
                        [],
                        Block([
                            If(
                                BinaryOp(<,Id(a),Id(b)),
                                Block([
                                    Call(Id(System),Id(print),[StringLit(lesser)])
                                ]),
                                If(
                                    BinaryOp(==,Id(a),Id(b)),
                                    Block([
                                        Call(Id(System),Id(print),[StringLit(equal)])
                                    ]),
                                    If(
                                        BinaryOp(>,Id(a),Id(b)),
                                        Block([
                                            Call(Id(System),Id(print),[StringLit(greater)])
                                        ])
                                    )
                                )
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_program_10(self):
        input = """
        Class Program {
            main() {
                Foreach (a In a + b .. (c*d+x) By 1)
                {{}{}}
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(Program),
                [
                    MethodDecl(
                        Id(main),
                        Static,
                        [],
                        Block([
                            For(
                                Id(a),
                                BinaryOp(+,Id(a),Id(b)),
                                BinaryOp(+,BinaryOp(*,Id(c),Id(d)),Id(x)),
                                IntLit(1),
                                Block([
                                    Block([]),
                                    Block([])
                                ])
                            ])
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_program_12(self):
        input = """
        Class Vehicle{}
        Class Car : Vehicle {
            _run(){}
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(Vehicle),
                []
            ),
            ClassDecl(
                Id(Car),
                Id(Vehicle),
                [
                    MethodDecl(
                        Id(_run),
                        Instance,
                        [],
                        Block([])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_program_11(self):
        input = """
        Class Visitor{
            visit(ctx:Context){
                System.print(ctx.name);
            }
        }
        Class Context {
            Var name: String;
            Constructor(name:String){
                Self.name = name;
            }
            accept(visitor: Visitor){
                visitor.visit(Self);
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(Visitor),
                [
                    MethodDecl(
                        Id(visit),
                        Instance,
                        [param(Id(ctx),ClassType(Id(Context)))],
                        Block([
                            Call(
                                Id(System),
                                Id(print),
                                [FieldAccess(Id(ctx), Id(name))]
                            )
                        ])
                    )
                ]
            ),
            ClassDecl(
                Id(Context),
                [
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(name),StringType)
                    ),
                    MethodDecl(
                        Id(Constructor),
                        Instance,
                        [param(Id(name),StringType)],
                        Block([
                            AssignStmt(
                                FieldAccess(Self(),Id(name)),
                                Id(name)
                            )
                        ])
                    ),
                    MethodDecl(
                        Id(accept),
                        Instance,
                        [param(Id(visitor),ClassType(Id(Visitor)))],
                        Block([
                            Call(Id(visitor),Id(visit),[Self()])
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_program_13(self):
        input = """
        Class Program {
            main(name:String){
                visitor = New Visitor();
                ctx = New Context(name);
                ctx.accept(visitor);
            }
        }   
        """
        expect = """
        Program([
            ClassDecl(
                Id(Program),
                [
                    MethodDecl(
                        Id(main),
                        Instance,
                        [param(Id(name),StringType)],
                        Block([
                            AssignStmt(
                                Id(visitor),
                                NewExpr(Id(Visitor),[])
                            ),
                            AssignStmt(
                                Id(ctx),
                                NewExpr(Id(Context),[Id(name)])
                            ),
                            Call(
                                Id(ctx),
                                Id(accept),
                                [Id(visitor)]
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_program_14(self):
        input = """
        Class Pro_gram {
            main(){
                a::$b.c.d()[a] = Null;
            }
        }   
        """
        expect = """
        Program([
            ClassDecl(
                Id(Pro_gram),
                [
                    MethodDecl(
                        Id(main),
                        Instance,
                        [],
                        Block([
                            AssignStmt(
                                ArrayCell(
                                    CallExpr(
                                        FieldAccess(
                                            FieldAccess(Id(a),Id($b)),
                                            Id(c)
                                        ),
                                        Id(d),
                                        []
                                    ),
                                    [Id(a)]
                                ),
                                NullLiteral()
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_program_15(self):
        input = """
        Class _6 : __ {
            $_0_(){}
        }   
        """
        expect = """
        Program([
            ClassDecl(
                Id(_6),
                Id(__),
                [
                    MethodDecl(
                        Id($_0_),
                        Static,
                        [],
                        Block([])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_program_16(self):
        input = """
        Class Program : System {
            main(){
                If(True){
                    t = ---6 + 0.7e1 +. "wow";
                }
            }
        }   
        """
        expect = """
        Program([
            ClassDecl(
                Id(Program),
                Id(System),
                [
                    MethodDecl(
                        Id(main),
                        Static,
                        [],
                        Block([
                            If(
                                BooleanLit(True),
                                Block([
                                    AssignStmt(
                                        Id(t),
                                        BinaryOp(
                                            +.,
                                            BinaryOp(
                                                +,
                                                UnaryOp(
                                                    -,
                                                    UnaryOp(
                                                        -,
                                                        UnaryOp(-,IntLit(6))
                                                    )
                                                ),
                                                FloatLit(7.0)
                                            ),
                                            StringLit(wow)
                                        )
                                    )
                                ])
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_program_17(self):
        input = """
        Class Program {
            main(){
                Return 9 + 3 || 2 && 1;
            }
        }   
        """
        expect = """
        Program([
            ClassDecl(
                Id(Program),
                [
                    MethodDecl(
                        Id(main),
                        Static,
                        [],
                        Block([
                            Return(
                                BinaryOp(
                                    &&,
                                    BinaryOp(
                                        ||,
                                        BinaryOp(+,IntLit(9),IntLit(3)),
                                        IntLit(2)
                                    ),
                                    IntLit(1)
                                )
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_program_18(self):
        input = """
        Class Program {
            main(){
                ## Return 9 + 3 || 2 && 1; ##
            }
        }   
        """
        expect = """
        Program([
            ClassDecl(
                Id(Program),
                [
                    MethodDecl(
                        Id(main),
                        Static,
                        [],
                        Block([])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_program_19(self):
        input = """
        Class Program {
            main(){
                Return a.foo(a.foo(),a::$foo(a[5]));
            }
        }   
        """
        expect = """
        Program([
            ClassDecl(
                Id(Program),
                [
                    MethodDecl(
                        Id(main),
                        Static,
                        [],
                        Block([
                            Return(
                                CallExpr(
                                    Id(a),
                                    Id(foo),
                                    [
                                        CallExpr(Id(a),Id(foo),[]),
                                        CallExpr(Id(a),Id($foo),[
                                            ArrayCell(Id(a), [IntLit(5)])
                                        ])
                                    ]
                                )
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_program_20(self):
        input = """
        Class Node {
            Var key: Int;
            Var left: Node = Null;
            Var right: Node = Null;
        }
        Class BSTree {
            Var root: Node;
            Constructor(){}
            Destructor(){}
            search(key: Int){}
            insert(key: Int){}
            getHeight(){}
            countNode(){}
            countChild(){}
        }   
        """
        expect = """
        Program([
            ClassDecl(
                Id(Node),
                [
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(key),IntType)
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(left),ClassType(Id(Node)), NullLiteral())
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(right),ClassType(Id(Node)), NullLiteral())
                    )
                ]
            ),
            ClassDecl(
                Id(BSTree),
                [
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(root),ClassType(Id(Node)),NullLiteral())
                    ),
                    MethodDecl(Id(Constructor),Instance,[],Block([])),
                    MethodDecl(Id(Destructor),Instance,[],Block([])),
                    MethodDecl(Id(search),Instance,[param(Id(key),IntType)],Block([])),
                    MethodDecl(Id(insert),Instance,[param(Id(key),IntType)],Block([])),
                    MethodDecl(Id(getHeight),Instance,[],Block([])),
                    MethodDecl(Id(countNode),Instance,[],Block([])),
                    MethodDecl(Id(countChild),Instance,[],Block([]))
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_program_21(self):
        input = """
        Class Node {
            Var key: Int;
            Var left: Node = Null;
            Var right: Node = Null;
        }
        Class BSTree {
            Var root: Node;
            Constructor(){
                Self.root = Null;
            }
            Destructor(){
                System.delete(Self.root);
            }
        }   
        """
        expect = """
        Program([
            ClassDecl(
                Id(Node),
                [
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(key),IntType)
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(left),ClassType(Id(Node)), NullLiteral())
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(right),ClassType(Id(Node)), NullLiteral())
                    )
                ]
            ),
            ClassDecl(
                Id(BSTree),
                [
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(root),ClassType(Id(Node)),NullLiteral())
                    ),
                    MethodDecl(Id(Constructor),Instance,[],Block([
                        AssignStmt(
                            FieldAccess(Self(),Id(root)),
                            NullLiteral()
                        )
                    ])),
                    MethodDecl(Id(Destructor),Instance,[],Block([
                        Call(
                            Id(System),
                            Id(delete),
                            [FieldAccess(Self(),Id(root))]
                        )
                    ]))
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_program_22(self):
        input = """
        Class Node {
            Var key: Int;
            Var left: Node = Null;
            Var right: Node = Null;
        }
        Class BSTree {
            Var root: Node;
            search(key: Int){
                If(root == Null){
                    Return "Not-found";
                }
                If(key < root.key) {
                    Return New BSTree(root.left).search(key);
                }
                Elseif(key > root.key) {
                    Return New BSTree(root.right).search(key);
                }
                Else {
                    Return "Found";
                }
            }
        } 
        """
        expect = """
        Program([
            ClassDecl(
                Id(Node),
                [
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(key),IntType)
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(left),ClassType(Id(Node)), NullLiteral())
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(right),ClassType(Id(Node)), NullLiteral())
                    )
                ]
            ),
            ClassDecl(
                Id(BSTree),
                [
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(root),ClassType(Id(Node)),NullLiteral())
                    ),
                    MethodDecl(Id(search),Instance,[param(Id(key),IntType)],Block([
                        If(
                            BinaryOp(==, Id(root),NullLiteral()),
                            Block([
                                Return(StringLit(Not-found))
                            ])
                        ),
                        If(
                            BinaryOp(<,Id(key),FieldAccess(Id(root),Id(key))),
                            Block([
                                Return(CallExpr(
                                    NewExpr(
                                        Id(BSTree),
                                        [FieldAccess(Id(root),Id(left))]
                                    ),
                                    Id(search),
                                    [Id(key)]
                                ))
                            ]),
                            If(
                                BinaryOp(>,Id(key),FieldAccess(Id(root),Id(key))),
                                Block([
                                    Return(CallExpr(
                                        NewExpr(
                                            Id(BSTree),
                                            [FieldAccess(Id(root),Id(right))]
                                        ),
                                        Id(search),
                                        [Id(key)]
                                    ))
                                ]),
                                Block([
                                    Return(StringLit(Found))
                                ])
                            )
                        )
                    ]))
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_program_23(self):
        input = """
        Class Node {
            Var key: Int;
            Var left: Node = Null;
            Var right: Node = Null;
        }
        Class BSTree {
            Var root: Node;
            insert(key: Int){
                If(root == Null){
                    root = New Node(key);
                    Return root;
                }
                If(key < root.key) {
                    root.left =  New BSTree(root.left).insert(key);
                }
                Elseif(key >= root.key) {
                    root.right = New BSTree(root.right).insert(key);
                }
                Return root;
            }
        } 
        """
        expect = """
        Program([
            ClassDecl(
                Id(Node),
                [
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(key),IntType)
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(left),ClassType(Id(Node)), NullLiteral())
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(right),ClassType(Id(Node)), NullLiteral())
                    )
                ]
            ),
            ClassDecl(
                Id(BSTree),
                [
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(root),ClassType(Id(Node)),NullLiteral())
                    ),
                    MethodDecl(Id(insert),Instance,[param(Id(key),IntType)],Block([
                        If(
                            BinaryOp(==, Id(root),NullLiteral()),
                            Block([
                                AssignStmt(
                                    Id(root),
                                    NewExpr(Id(Node),[Id(key)])
                                ),
                                Return(Id(root))
                            ])
                        ),
                        If(
                            BinaryOp(<,Id(key),FieldAccess(Id(root),Id(key))),
                            Block([
                                AssignStmt(
                                    FieldAccess(Id(root),Id(left)),
                                    CallExpr(
                                        NewExpr(
                                            Id(BSTree),
                                            [FieldAccess(Id(root),Id(left))]
                                        ),
                                        Id(insert),
                                        [Id(key)]
                                    )
                                )
                            ]),
                            If(
                                BinaryOp(>=,Id(key),FieldAccess(Id(root),Id(key))),
                                Block([
                                    AssignStmt(
                                        FieldAccess(Id(root),Id(right)),
                                        CallExpr(
                                            NewExpr(
                                                Id(BSTree),
                                                [FieldAccess(Id(root),Id(right))]
                                            ),
                                            Id(insert),
                                            [Id(key)]
                                        )
                                    )
                                ])
                            )
                        ),
                        Return(Id(root))
                    ]))
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_program_24(self):
        input = """
        Class Node {
            Var key: Int;
            Var left: Node = Null;
            Var right: Node = Null;
        }
        Class BSTree {
            Var root: Node;
            getHeight(){
                If(root == Null){
                    Return 0;
                }
                Return 1 + System.max(New BSTree(root.left).getHeight(),
                New BSTree(root.right).getHeight());
            }
        } 
        """
        expect = """
        Program([
            ClassDecl(
                Id(Node),
                [
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(key),IntType)
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(left),ClassType(Id(Node)), NullLiteral())
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(right),ClassType(Id(Node)), NullLiteral())
                    )
                ]
            ),
            ClassDecl(
                Id(BSTree),
                [
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(root),ClassType(Id(Node)),NullLiteral())
                    ),
                    MethodDecl(Id(getHeight),Instance,[],Block([
                        If(
                            BinaryOp(==, Id(root),NullLiteral()),
                            Block([Return(IntLit(0))])
                        ),
                        Return(
                            BinaryOp(+, IntLit(1),CallExpr(Id(System),Id(max),[
                                CallExpr(NewExpr(Id(BSTree),[FieldAccess(Id(root),Id(left))]),Id(getHeight),[]),
                                CallExpr(NewExpr(Id(BSTree),[FieldAccess(Id(root),Id(right))]),Id(getHeight),[])
                            ]))
                        )
                    ]))
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_program_25(self):
        input = """
        Class Node {
            Var key: Int;
            Var left: Node = Null;
            Var right: Node = Null;
        }
        Class BSTree {
            Var root: Node;
            getNodeCount(){
                If(root == Null){
                    Return 0;
                }
                Return 1 + New BSTree(root.left).getNodeCount() +
                New BSTree(root.right).getNodeCount();
            }
        } 
        """
        expect = """
        Program([
            ClassDecl(
                Id(Node),
                [
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(key),IntType)
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(left),ClassType(Id(Node)), NullLiteral())
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(right),ClassType(Id(Node)), NullLiteral())
                    )
                ]
            ),
            ClassDecl(
                Id(BSTree),
                [
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(root),ClassType(Id(Node)),NullLiteral())
                    ),
                    MethodDecl(Id(getNodeCount),Instance,[],Block([
                        If(
                            BinaryOp(==, Id(root),NullLiteral()),
                            Block([Return(IntLit(0))])
                        ),
                        Return(
                            BinaryOp(
                                +,
                                BinaryOp(
                                    +,
                                    IntLit(1),
                                    CallExpr(NewExpr(Id(BSTree),[FieldAccess(Id(root),Id(left))]),Id(getNodeCount),[])
                                ),
                                CallExpr(NewExpr(Id(BSTree),[FieldAccess(Id(root),Id(right))]),Id(getNodeCount),[])
                            )
                        )
                    ]))
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_program_26(self):
        input = """
        Class Node {
            Var key: Int;
            Var left: Node = Null;
            Var right: Node = Null;
        }
        Class BSTree {
            Var root: Node;
            getLeafCount(){
                If(root == Null){
                    Return 0;
                }
                If((root.left == Null) && (root.right == Null)){
                    Return 1;
                }
                Return New BSTree(root.left).getLeafCount() + New BSTree(root.right).getLeafCount();
            }
        } 
        """
        expect = """
        Program([
            ClassDecl(
                Id(Node),
                [
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(key),IntType)
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(left),ClassType(Id(Node)), NullLiteral())
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(right),ClassType(Id(Node)), NullLiteral())
                    )
                ]
            ),
            ClassDecl(
                Id(BSTree),
                [
                    AttributeDecl(
                        Instance,
                        VarDecl(Id(root),ClassType(Id(Node)),NullLiteral())
                    ),
                    MethodDecl(Id(getLeafCount),Instance,[],Block([
                        If(
                            BinaryOp(==, Id(root),NullLiteral()),
                            Block([Return(IntLit(0))])
                        ),
                        If(
                            BinaryOp(
                                &&,
                                BinaryOp(==,FieldAccess(Id(root),Id(left)),NullLiteral()),
                                BinaryOp(==,FieldAccess(Id(root),Id(right)),NullLiteral())
                            ),
                            Block([Return(IntLit(1))])
                        ),
                        Return(
                            BinaryOp(
                                +,
                                CallExpr(NewExpr(Id(BSTree),[FieldAccess(Id(root),Id(left))]),Id(getLeafCount),[]),
                                CallExpr(NewExpr(Id(BSTree),[FieldAccess(Id(root),Id(right))]),Id(getLeafCount),[])
                            )
                        )
                    ]))
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_program_27(self):
        input = """
        Class Shape{
            foo(){
                Foreach(i In 1 .. 100 By -2 ){}
            }
        }   
        """
        expect = """
        Program([
            ClassDecl(
                Id(Shape),
                [
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            For(Id(i),IntLit(1),IntLit(100),UnaryOp(-,IntLit(2)),Block([])])
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_program_28(self):
        input = """
        Class Shape{
            Val $a: Array[Array[Array[Float,1],1],1];
        }   
        """
        expect = """
        Program([
            ClassDecl(
                Id(Shape),
                [
                    AttributeDecl(
                        Static,
                        ConstDecl(
                            Id($a),
                            ArrayType(1,ArrayType(1,ArrayType(1,FloatType))),
                            None
                        )
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_program_29(self):
        input = '''Class d:q{}Class G{}Class _{}Class _:G{}Class _{Destructor(){} }Class N8_40IWV:B__{}'''
        expect = """
        Program([
            ClassDecl(Id(d),Id(q),[]),
            ClassDecl(Id(G),[]),
            ClassDecl(Id(_),[]),
            ClassDecl(Id(_),Id(G),[]),
            ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([]))]),
            ClassDecl(Id(N8_40IWV),Id(B__),[])
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_program_30(self):
        input = """
        Class A:B{
            Var $static_var: B;
            Var attribute: B;
            copy(){
                Return Self;
            }
            foo(){
                A::$static_var.foo();
            }
        }
        """
        expect = """
        Program([
            ClassDecl(
                Id(A),
                Id(B),
                [
                    AttributeDecl(
                        Static,
                        VarDecl(
                            Id($static_var),
                            ClassType(Id(B)),
                            NullLiteral()
                        )
                    ),
                    AttributeDecl(
                        Instance,
                        VarDecl(
                            Id(attribute),
                            ClassType(Id(B)),
                            NullLiteral()
                        )
                    ),
                    MethodDecl(
                        Id(copy),
                        Instance,
                        [],
                        Block([
                            Return(
                                Self()
                            )
                        ])
                    ),
                    MethodDecl(
                        Id(foo),
                        Instance,
                        [],
                        Block([
                            Call(
                                FieldAccess(
                                    Id(A),
                                    Id($static_var)
                                ),
                                Id(foo),
                                []
                            )
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_program_31(self):
        input = '''Class _:G{}Class _{Destructor(){} }Class N8_40IWV:B__{}'''
        expect = """
        Program([
            ClassDecl(Id(_),Id(G),[]),
            ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([]))]),
            ClassDecl(Id(N8_40IWV),Id(B__),[])
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_program_32(self):
        input = '''Class _:G{}Class _{Constructor(){} }Class N8_40IWV:B__{}'''
        expect = """
        Program([
            ClassDecl(Id(_),Id(G),[]),
            ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([]))]),
            ClassDecl(Id(N8_40IWV),Id(B__),[])
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_program_33(self):
        input = '''Class _:___{}Class _{Constructor(){} }Class N_8_40IWV:B__{}'''
        expect = """
        Program([
            ClassDecl(Id(_),Id(___),[]),
            ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([]))]),
            ClassDecl(Id(N_8_40IWV),Id(B__),[])
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_program_34(self):
        input = '''Class _:___{}Class g62_{Constructor(){} }'''
        expect = """
        Program([
            ClassDecl(Id(_),Id(___),[]),
            ClassDecl(Id(g62_),[MethodDecl(Id(Constructor),Instance,[],Block([]))])
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_program_35(self):
        input = """
        Class Program {
            main(){
                Return 9 && 2 && 1; 
            }
        }   
        """
        expect = """
        Program([
            ClassDecl(
                Id(Program),
                [
                    MethodDecl(Id(main),Static,[],Block([
                            Return(BinaryOp(
                                &&,
                                BinaryOp(&&,IntLit(9),IntLit(2)),
                                IntLit(1)
                            ))
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_program_36(self):
        input = """
        Class Program {
            main(){
                Return a || 2 && 1; 
            }
        }   
        """
        expect = """
        Program([
            ClassDecl(
                Id(Program),
                [
                    MethodDecl(Id(main),Static,[],Block([
                            Return(BinaryOp(
                                &&,
                                BinaryOp(||,Id(a),IntLit(2)),
                                IntLit(1)
                            ))
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_program_37(self):
        input = """
        Class Program {
            main(){
                Return a + b % c; 
            }
        }   
        """
        expect = """
        Program([
            ClassDecl(
                Id(Program),
                [
                    MethodDecl(Id(main),Static,[],Block([
                            Return(BinaryOp(
                                +,
                                Id(a),
                                BinaryOp(%,Id(b),Id(c))
                            ))
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_program_38(self):
        input = """
        Class Program {
            main(){
                Return (a+b)%c; 
            }
        }   
        """
        expect = """
        Program([
            ClassDecl(
                Id(Program),
                [
                    MethodDecl(Id(main),Static,[],Block([
                            Return(BinaryOp(
                                %,
                                BinaryOp(+,Id(a),Id(b)),
                                Id(c)
                            ))
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_program_39(self):
        input = """
        Class Program {
            main(){
                Return !-b;
            }
        }   
        """
        expect = """
        Program([
            ClassDecl(
                Id(Program),
                [
                    MethodDecl(Id(main),Static,[],Block([
                            Return(UnaryOp(!,UnaryOp(-,Id(b))))
                        ])
                    )
                ]
            )
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_program_40(self):
        input = """
        Class A{
            Val $a,$b: Int = 00, 03_1_4;
        }
        """
        expect = """Program([ClassDecl(Id(A),[
            AttributeDecl(Static,ConstDecl(Id($a),IntType,IntLit(0))),
            AttributeDecl(Static,ConstDecl(Id($b),IntType,IntLit(204)))
            ])])
            """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_program_41(self):
        input = """
        Class A{
            Val $a,$b: Int = 0X1_4, 03_1_4;
        }
        """
        expect = """Program([ClassDecl(Id(A),[
            AttributeDecl(Static,ConstDecl(Id($a),IntType,IntLit(20))),
            AttributeDecl(Static,ConstDecl(Id($b),IntType,IntLit(204)))
            ])])
            """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_program_42(self):
        input = """
        Class A{
            Var $a,$b: Int = 00, 0B1_0;
        }
        """
        expect = """Program([ClassDecl(Id(A),[
            AttributeDecl(Static,VarDecl(Id($a),IntType,IntLit(0))),
            AttributeDecl(Static,VarDecl(Id($b),IntType,IntLit(2)))
            ])])
            """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_program_43(self):
        input = """
        Class A{
            Var a,b: Int = 00, 03_1_4;
        }
        """
        expect = """Program([ClassDecl(Id(A),[
            AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(0))),
            AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(204)))
            ])])
            """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_program_44(self):
        input = """
        Class A{
            Val $a,$b: Float = .0e6, 2_3.5;
        }
        """
        expect = """Program([ClassDecl(Id(A),[
            AttributeDecl(Static,ConstDecl(Id($a),FloatType,FloatLit(0.0))),
            AttributeDecl(Static,ConstDecl(Id($b),FloatType,FloatLit(23.5)))
            ])])
            """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_program_45(self):
        input = """
        Class A{
            Val $a,$b: String = "lolo", "\\n\\\\";
        }
        """
        expect = """Program([ClassDecl(Id(A),[
            AttributeDecl(Static,ConstDecl(Id($a),StringType,StringLit(lolo))),
            AttributeDecl(Static,ConstDecl(Id($b),StringType,StringLit(\\n\\\\)))
            ])])
            """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_program_46(self):
        input = """
        Class A{
            Val $a,$b: Int = 00, 03_1_4;
        }
        """
        expect = """Program([ClassDecl(Id(A),[
            AttributeDecl(Static,ConstDecl(Id($a),IntType,IntLit(0))),
            AttributeDecl(Static,ConstDecl(Id($b),IntType,IntLit(204)))
            ])])
            """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_program_47(self):
        input = """
        Class A{
            Val $a,$b: Int = 00, 03_1_4;
        }
        """
        expect = """Program([ClassDecl(Id(A),[
            AttributeDecl(Static,ConstDecl(Id($a),IntType,IntLit(0))),
            AttributeDecl(Static,ConstDecl(Id($b),IntType,IntLit(204)))
            ])])
            """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_program_48(self):
        input = """
        Class A{
            Val $a,$b: Int = 00, 03_1_4;
        }
        """
        expect = """Program([ClassDecl(Id(A),[
            AttributeDecl(Static,ConstDecl(Id($a),IntType,IntLit(0))),
            AttributeDecl(Static,ConstDecl(Id($b),IntType,IntLit(204)))
            ])])
            """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_program_49(self):
        input = """
        Class A{
            Val $a,$b: Int = 00, 03_1_4;
        }
        """
        expect = """Program([ClassDecl(Id(A),[
            AttributeDecl(Static,ConstDecl(Id($a),IntType,IntLit(0))),
            AttributeDecl(Static,ConstDecl(Id($b),IntType,IntLit(204)))
            ])])
            """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_program_50(self):
        input = """
        Class A{
            main(){}
            $main(){}
            $_(){}
        }
        """
        expect = """
        Program([ClassDecl(Id(A),[
            MethodDecl(Id(main),Instance,[],Block([])),
            MethodDecl(Id($main),Static,[],Block([])), 
            MethodDecl(Id($_),Static,[],Block([]))      
        ])])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_program_51(self):
        input = """
        Class A:_{
            main(){}
            $_6(){}
            _(){}
        }
        """
        expect = """
        Program([ClassDecl(Id(A),Id(_),[
            MethodDecl(Id(main),Instance,[],Block([])),
            MethodDecl(Id($_6),Static,[],Block([])), 
            MethodDecl(Id(_),Instance,[],Block([]))    
        ])])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_program_52(self):
        input = """
        Class Program:_{
            main(){}
            $_6(){}
            _(){}
        }
        """
        expect = """
        Program([ClassDecl(Id(Program),Id(_),[
            MethodDecl(Id(main),Static,[],Block([])),
            MethodDecl(Id($_6),Static,[],Block([])), 
            MethodDecl(Id(_),Instance,[],Block([]))    
        ])])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_program_53(self):
        input = """
        Class Program:_{
            _main(){}
            $_7(){}
            _(){}
        }
        """
        expect = """
        Program([ClassDecl(Id(Program),Id(_),[
            MethodDecl(Id(_main),Instance,[],Block([])),
            MethodDecl(Id($_7),Static,[],Block([])), 
            MethodDecl(Id(_),Instance,[],Block([]))    
        ])])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_program_54(self):
        input = """
        Class Sort{
            BubbleSort(arr:Array[Int,100]; size:Int){
                Foreach (i In 0 .. size - 1){
                    Foreach(j In 0 .. size - i - 1){
                        If (arr[j] > arr[j+1]) {
                            System.swap(arr[j],arr[j+1]);
                        }
                    }
                }
            }
        }
        """
        expect = """
        Program([ClassDecl(Id(Sort),[
            MethodDecl(
                Id(BubbleSort),
                Instance,
                [param(Id(arr),ArrayType(100,IntType)),param(Id(size),IntType)],
                Block([
                    For(Id(i),IntLit(0),BinaryOp(-,Id(size),IntLit(1)),IntLit(1),Block([
                        For(Id(j),IntLit(0),BinaryOp(-,BinaryOp(-,Id(size),Id(i)),IntLit(1)),IntLit(1),Block([
                            If(
                                BinaryOp(>,ArrayCell(Id(arr),[Id(j)]),ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))])),
                                Block([
                                    Call(Id(System),Id(swap),[
                                        ArrayCell(Id(arr),[Id(j)]),
                                        ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))])
                                    ])
                                ])
                            )
                        ])])
                    ])])
                ])
            )
        ])])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_program_55(self):
        input = """
        Class Sort{
            SelectionSort(arr:Array[Int,100]; size:Int){
                Foreach (i In 0 .. size - 1){
                    min_idx = i;
                    Foreach(j In i + 1 .. size ){
                        If (arr[j] < arr[min_idx]) {
                            min_idx = j;
                        }
                    }
                    System.swap(arr[i], arr[min_idx]);
                }
            }
        }
        """
        expect = """
        Program([ClassDecl(Id(Sort),[
            MethodDecl(
                Id(SelectionSort),
                Instance,
                [param(Id(arr),ArrayType(100,IntType)),param(Id(size),IntType)],
                Block([
                    For(Id(i),IntLit(0),BinaryOp(-,Id(size),IntLit(1)),IntLit(1),Block([
                        AssignStmt(Id(min_idx),Id(i)),
                        For(Id(j),BinaryOp(+,Id(i),IntLit(1)),Id(size),IntLit(1),Block([
                            If(
                                BinaryOp(<,ArrayCell(Id(arr),[Id(j)]),ArrayCell(Id(arr),[Id(min_idx)])),
                                Block([
                                    AssignStmt(Id(min_idx),Id(j))
                                ])
                            )
                        ])]),
                        Call(Id(System),Id(swap),[
                            ArrayCell(Id(arr),[Id(i)]),
                            ArrayCell(Id(arr),[Id(min_idx)])
                        ])
                    ])])
                ])
            )
        ])])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_program_56(self):
        input = """
        Class Sort{
            InsertionSort(arr:Array[Int,100]; size:Int){
                Foreach (i In 1 .. size){
                    key = arr[i];
                    ## for is exclusive higher bound ##
                    Foreach(j In i - 1 .. -1 By -1){
                        If(arr[j] <= key){
                            Break;
                        }
                        arr[j+1] = arr[j];
                    }
                    arr[j+1] = key;
                }
            }
        }
        """
        expect = """
        Program([ClassDecl(Id(Sort),[
            MethodDecl(
                Id(InsertionSort),
                Instance,
                [param(Id(arr),ArrayType(100,IntType)),param(Id(size),IntType)],
                Block([
                    For(Id(i),IntLit(1),Id(size),IntLit(1),Block([
                        AssignStmt(Id(key),ArrayCell(Id(arr),[Id(i)])),
                        For(Id(j),BinaryOp(-,Id(i),IntLit(1)),UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(1)),Block([
                            If(
                                BinaryOp(<=,ArrayCell(Id(arr),[Id(j)]),Id(key)),
                                Block([Break])
                            ),
                            AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))]),ArrayCell(Id(arr),[Id(j)]))
                        ])]),
                        AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))]),Id(key))
                    ])])
                ])
            )
        ])])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_program_57(self):
        input = """
        Class NeuralNetwork: Model{
            ## Forward pass ##
            Constructor(n_features: Int;num_classes: Int){
                ## Code goes here ##
            }
            forward(input:Matrix){
                ## Code goes here ##
            }
        }
        Class Program{
            main(m,n,c:Int; epoch: Int){
                X = New Matrix(m,n);
                y = New Matrix(m,c);
                model = New NeuralNetwork(n,c);
                optim = New Adam(model.weights,0.01);
                criterion = New CategoricalCrossEntropy();
                Foreach (i In 0 .. epoch){
                    optim.zero_grad();
                    y_hat = model.forward(X);
                    loss = criterion.fit(y_hat, y);
                    criterion.backward();
                    optim.step();
                }
            }
        }
        """
        expect = """
        Program([
            ClassDecl(Id(NeuralNetwork),Id(Model),[
                MethodDecl(
                    Id(Constructor),
                    Instance,
                    [
                        param(Id(n_features),IntType),
                        param(Id(num_classes),IntType)
                    ],
                    Block([])
                ),
                MethodDecl(
                    Id(forward),
                    Instance,
                    [param(Id(input),ClassType(Id(Matrix)))],
                    Block([])
                )
            ]),
            ClassDecl(Id(Program),[
                MethodDecl(
                    Id(main),
                    Instance,
                    [
                        param(Id(m),IntType),
                        param(Id(n),IntType),
                        param(Id(c),IntType),
                        param(Id(epoch),IntType)
                    ],
                    Block([
                        AssignStmt(
                            Id(X),
                            NewExpr(Id(Matrix),[Id(m),Id(n)])
                        ),
                        AssignStmt(
                            Id(y),
                            NewExpr(Id(Matrix),[Id(m),Id(c)])
                        ),
                        AssignStmt(
                            Id(model),
                            NewExpr(Id(NeuralNetwork),[Id(n),Id(c)])
                        ),
                        AssignStmt(
                            Id(optim),
                            NewExpr(Id(Adam),[FieldAccess(Id(model),Id(weights)),FloatLit(0.01)])
                        ),
                        AssignStmt(
                            Id(criterion),
                            NewExpr(Id(CategoricalCrossEntropy),[])
                        ),
                        For(Id(i),IntLit(0),Id(epoch),IntLit(1),Block([
                            Call(Id(optim),Id(zero_grad),[]),
                            AssignStmt(
                                Id(y_hat),
                                CallExpr(Id(model),Id(forward),[Id(X)])
                            ),
                            AssignStmt(
                                Id(loss),
                                CallExpr(Id(criterion),Id(fit),[Id(y_hat),Id(y)])
                            ),
                            Call(Id(criterion),Id(backward),[]),
                            Call(Id(optim),Id(step),[])
                        ])])
                    ])
                )
            ])
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_program_58(self):
        input = """
        Class NeuralNetwork: Model{
            ## Forward pass ##
            Constructor(n_features: Int;num_classes: Int){
                ## Code goes here ##
            }
            forward(input:Matrix){
                ## Code goes here ##
            }
        }
        Class MSE: Loss{
            fit(){}
        }
        Class SGD: Optimizer{
            step(){}
        }
        """
        expect = """
        Program([
            ClassDecl(Id(NeuralNetwork),Id(Model),[
                MethodDecl(
                    Id(Constructor),
                    Instance,
                    [
                        param(Id(n_features),IntType),
                        param(Id(num_classes),IntType)
                    ],
                    Block([])
                ),
                MethodDecl(
                    Id(forward),
                    Instance,
                    [param(Id(input),ClassType(Id(Matrix)))],
                    Block([])
                )
            ]),
            ClassDecl(Id(MSE),Id(Loss),[
                MethodDecl(Id(fit),Instance,[],Block([]))
            ]),
            ClassDecl(Id(SGD),Id(Optimizer),[
                MethodDecl(Id(step),Instance,[],Block([]))
            ])
        ])
        """.replace('\n', '').replace(' ', '').replace('\t', '')
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_program_final(self):
        input = """
        Class GoodBye{
            $message(){
                System.print("Goodbye Assignment 2, you are so annoying!");
            }
        }
        Class Program{
            main(){
                ## loop forever ##
                Foreach (i In 0 .. 1 By 0){
                    GoodBye::$message();
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(GoodBye),[MethodDecl(Id($message),Static,[],Block([Call(Id(System),Id(print),[StringLit(Goodbye Assignment 2, you are so annoying!)])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(i),IntLit(0),IntLit(1),IntLit(0),Block([Call(Id(GoodBye),Id($message),[])])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 400))
