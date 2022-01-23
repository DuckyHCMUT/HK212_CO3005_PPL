import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    # Test for normal token
    def test_bkel_1_101(self):
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    def test_bkel_2_102(self):
        self.assertTrue(TestLexer.test("Break","Break,<EOF>",102))
    def test_bkel_3_103(self):
        self.assertTrue(TestLexer.test("ab?svn","ab,Error Token ?",103))
    def test_bkel_4_104(self):
        self.assertTrue(TestLexer.test("Return x;","Return,x,;,<EOF>",104))
    def test_105(self):
        self.assertTrue(TestLexer.test("BBBBBBBBBB","BBBBBBBBBB,<EOF>",105))
    def test_106(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",106))
    def test_107(self):
        self.assertTrue(TestLexer.test("aAsVN3","aAsVN3,<EOF>",107))
    def test_108(self):
        input = 'Var myVariable: Int;'
        expect = 'Var,myVariable,:,Int,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 108))
    def test_109(self):
        input = 'Var myVariable@ Int;'
        expect = 'Var,myVariable,Error Token @'
        self.assertTrue(TestLexer.test(input, expect, 109))
    # Test for array type
    def test_110(self):
        input = 'Var myArr: Array[Float, 10];'
        expect = 'Var,myArr,:,Array,[,Float,,,10,],;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 110))
    # Test for number literal
    def test_111(self):
        input = '01_0 - 034_031_000_1 + 00 - (-012); '
        expect = '010,-,0340310001,+,00,-,(,-,012,),;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 111))
    def test_112(self):
        """test integers"""
        input = '0x1234EBFA 0 123 0123 0101 0.123 1.2 3E-8 233_41_122'
        expect = '0x1234EBFA,0,123,0123,0101,0.123,1.2,3E-8,23341122,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 112))
    def test_113(self):
        input = '-1231131 + 1234 - (-5) + Arr[1]'
        expect = '-,1231131,+,1234,-,(,-,5,),+,Arr,[,1,],<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 113))
    def test_114(self):
        input = '------------ 12 ----- 10 + 5 * 4 / 3 + 3.2 - 1.2E-1 + 1.E2 * (0XABCDEF09 - 0b0 % (0b11111110000000000 - 0x123_0031_ABCD));'
        expect = '-,-,-,-,-,-,-,-,-,-,-,-,12,-,-,-,-,-,10,+,5,*,4,/,3,+,3.2,-,1.2E-1,+,1.E2,*,(,0XABCDEF09,-,0b0,%,(,0b11111110000000000,-,0x1230031ABCD,),),;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 114))
    def test_115(self):
        input = 'Var urgay: Float = 0 + 0x0 - 0b0 + 00 % 0.0 / 0. + .0 * 0e2 + (.0e3 + 0.e3 - .e3 + e0 - 0.e0);'
        expect = 'Var,urgay,:,Float,=,0,+,0x0,-,0b0,+,00,%,0.0,/,0.,+,.,0,*,0e2,+,(,.0e3,+,0.e3,-,.e3,+,e0,-,0.,e0,),;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 115))
    # Test for string literal
    def test_116(self):
        self.assertTrue(TestLexer.test(""" "Vietnam" """, """Vietnam,<EOF>""",116))
    def test_117(self):
        input = """ "Hello \\n world \\t" """
        expect = """Hello \\n world \\t,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 117))
    def test_118(self):
        input = """ "Hello \\n"""
        expect = """Unclosed String: Hello \\n"""
        self.assertTrue(TestLexer.test(input, expect, 118))
    def test_119(self):
        input = """ "weird escape\\b" """
        expect = """weird escape\\b,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 119))  
    # Test for expression literal
    def test_120(self):
        self.assertTrue(TestLexer.test("abc[3*(2+3)/5] = 100", "abc,[,3,*,(,2,+,3,),/,5,],=,100,<EOF>", 120))
    def test_121(self):
        input = '__hp[idxArr[(3+2)*5/-(3*1)] = otherArr[idxArr[-3]]'
        expect = '__hp,[,idxArr,[,(,3,+,2,),*,5,/,-,(,3,*,1,),],=,otherArr,[,idxArr,[,-,3,],],<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 121))
    def test_122(self):
        input = '0xFFFFFFFF + 0b110101111 - 0X1122330F / (0123321 * 0.0000000004 )+ 3.14E-10'
        expect = '0xFFFFFFFF,+,0b110101111,-,0X1122330F,/,(,0123321,*,0.0000000004,),+,3.14E-10,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 122))
    def test_123(self):
        input = 'Var a: String = b +. "Welcome to PPL course";'
        expect = 'Var,a,:,String,=,b,+.,Welcome to PPL course,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 123))
    def test_124(self):
        input = """If (length <= (15.123e3 + 0x123000000)){
            print(some_string);
        }"""
        expect= 'If,(,length,<=,(,15.123e3,+,0x123000000,),),{,print,(,some_string,),;,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 124))
    # Custom test from Justince
    def test_125(self):
        input = """## VxpT$lLYZn. <=> ::AGz569YYpd ||:: <=> <=<= ||36scLLzWju %|| ::"""
        expect = """Error Token #"""
        self.assertTrue(TestLexer.test(input, expect, 125))
    def test_126(self):
        input = """## 2rDnLulZwmForeach ==## >=<= &== ==== <=>= ##>= #### |||| 5cSkUAUw$I== :::: >=<= ==* ::= ##If :::: ==<= ==>= +"""
        expect = """>=,<=,Error Token &"""
        self.assertTrue(TestLexer.test(input, expect, 126))
    def test_127(self):
        input = """Main ::Var ||"""
        expect = """Main,::,Var,||,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 127))
    def test_128(self):
        input = """= _QQtX5FNVk! Continue|| Continue>= <=>= >=>= Main## <=<= Int|| ##|| ==<= .m0AZf7zrAW :::: ==<= >=+ >=>= Continue## >="""
        expect = """=,_QQtX5FNVk,!,Continue,||,Continue,>=,<=,>=,>=,>=,Main,||,==,<=,.,m0AZf7zrAW,::,::,==,<=,>=,+,>=,>=,Continue,Error Token #"""
        self.assertTrue(TestLexer.test(input, expect, 128))
    def test_129(self):
        input = """<= .== ##== <=<= ::- :::: ==>= Constructor:: ||:: -:: ||## >=== ==& <=== ||. >="""
        expect = """<=,.,==,>=,==,==,Error Token &"""
        self.assertTrue(TestLexer.test(input, expect, 129))
    def test_130(self):
        input = """|| >=. New< <=|| .:: ::"""
        expect = """||,>=,.,New,<,<=,||,.,::,::,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 130))
    def test_131(self):
        input = """>= ##|| ::"""
        expect = """>=,Error Token #"""
        self.assertTrue(TestLexer.test(input, expect, 131))
    def test_132(self):
        input = """Class main{}"""
        expect = """Class,main,{,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 132))
    def test_133(self):
        input = """
    Class Rectangle: Shape {
        getArea() {
            Return Self.length * Self.width;
        }
    }
        """
        expect = """Class,Rectangle,:,Shape,{,getArea,(,),{,Return,Self,.,length,*,Self,.,width,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 133))
    def test_134(self):
        input = """
        Class Rectangle: Shape{
            ## Var somewhat: Int = 2;##
            Val myArray: Array[Float, 3];
                getArray(){
                    Return myArray;
            }
        }
            """
        expect = """Class,Rectangle,:,Shape,{,Val,myArray,:,Array,[,Float,,,3,],;,getArray,(,),{,Return,myArray,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 134))
    def test_135(self):
        input = """
    Class StringWorker{
        getString(someString){
            someString: String = "hello PPL";
            Return someString;
        }
    }
        """
        expect = """Class,StringWorker,{,getString,(,someString,),{,someString,:,String,=,hello PPL,;,Return,someString,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 135))

    def test_136(self):
        input = """
        Val My1stCons, My2ndCons: Int = 1 + 5, 2;
        Var $x, $y : Int = 0, 0;
        """
        expect = """Val,My1stCons,,,My2ndCons,:,Int,=,1,+,5,,,2,;,Var,$x,,,$y,:,Int,=,0,,,0,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 136))

    # Comment only
    def test_137(self):
        input = """
        ## This is a
        multi-line
        comment.
        ##
        """
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 137))
    def test_138(self):
        input = """
        Foreach(x, y In 100 .. 300 By 5){
            doNothing();
        } 
        """
        expect = """Foreach,(,x,,,y,In,100,..,300,By,5,),{,doNothing,(,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 138))
    def test_139(self):
        input = """
        {
            Foreach(x, y In 100 .. 300 By 5){
                If (i <= 9){
                    Continue;
                }
                Else{
                print(x - y);
                }
            } 
        }
        """
        expect = """{,Foreach,(,x,,,y,In,100,..,300,By,5,),{,If,(,i,<=,9,),{,Continue,;,},Else,{,print,(,x,-,y,),;,},},},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 139))

    # Template for testcase 
    # def test_1(self):
    #     input = """ """
    #     expect = """ """
    #     self.assertTrue(TestLexer.test(input, expect, 1))
