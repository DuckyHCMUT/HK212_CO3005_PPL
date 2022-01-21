import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    # Test for normal token
    def test_lowercase_identifier(self):
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    def test_uppercase_identifier(self):
        self.assertTrue(TestLexer.test("BBBBBBBBBB","BBBBBBBBBB,<EOF>",114))
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
    def test_mixed_id(self):
        self.assertTrue(TestLexer.test("aAsVN3","aAsVN3,<EOF>",103))
    def test_keyword_1(self):
        input = 'Var myVariable: Int;'
        expect = 'Var,myVariable,:,Int,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 115))
    def test_error_token(self):
        input = 'Var myVariable@ Int;'
        expect = 'Var,myVariable,Error Token @'
        self.assertTrue(TestLexer.test(input, expect, 116))

    # Test for array type
    def test_arr_1(self):
        input = 'Var myArr: Array[Float, 10];'
        expect = 'Var,myArr,:,Array,[,Float,,,10,],;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 117))
    
    # Test for number literal
    def test_octal(self):
        input = '01_0 - 034_031_000_1 + 00 - (-012);'
        expect = '010,-,0340310001,+,00,-,(,-,012,),;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 128))

    def test_integer(self):
        """test integers"""
        input = '0x1234EBFA 0 123 0123 0101 0.123 1.2 3E-8 233_41_122'
        expect = '0x1234EBFA,0,123,0123,0101,0.123,1.2,3E-8,23341122,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 104))
    def test_neg_int(self):
        input = '-1231131 + 1234 - (-5) + Arr[1]'
        expect = '-,1231131,+,1234,-,(,-,5,),+,Arr,[,1,],<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 105))
    def test_many_negative_sign(self):
        input = '------------ 12 ----- 10 + 5 * 4 / 3 + 3.2 - 1.2E-1 + 1.E2 * (0XABCDEF09 - 0b0 % (0b11111110000000000 - 0x123_0031_ABCD));'
        expect = '-,-,-,-,-,-,-,-,-,-,-,-,12,-,-,-,-,-,10,+,5,*,4,/,3,+,3.2,-,1.2E-1,+,1.E2,*,(,0XABCDEF09,-,0b0,%,(,0b11111110000000000,-,0x1230031ABCD,),),;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 110))
    def test_zero(self):
        input = 'Var urgay: Float = 0 + 0x0 - 0b0 + 00 % 0.0 / 0. + .0 * 0e2 + (.0e3 + 0.e3 - .e3 + e0 - 0.e0);'
        expect = 'Var,urgay,:,Float,=,0,+,0x0,-,0b0,+,00,%,0.0,/,0.,+,.,0,*,0e2,+,(,.0e3,+,0.e3,-,.e3,+,e0,-,0.,e0,),;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 118))

    # Test for string literal
    def test_anything(self):
        self.assertTrue(TestLexer.test(""" "Vietnam" """, """"Vietnam",<EOF>""",106))
    def test_bkel(self):
        """ One test case on BKEL"""
        self.assertTrue(TestLexer.test(""" "abc\\h def" """, "Illegal Escape In String: abc\\h", 107))
    def test_string_1(self):
        input = """ "Hello \\n world \\t" """
        expect = """"Hello \\n world \\t",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 112))
    def test_string_err_2(self):
        input = """ "Hello \\n"""
        expect = """Unclosed String: Hello \\n"""
        self.assertTrue(TestLexer.test(input, expect, 113))
    def test_string_2(self):
        input = """ "weird escape\\b" """
        expect = """"weird escape\\b",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 119))
        
    # Test for expression literal
    def test_expr_1(self):
        self.assertTrue(TestLexer.test("abc[3*(2+3)/5] = 100", "abc,[,3,*,(,2,+,3,),/,5,],=,100,<EOF>", 108))
    def test_expr_2(self):
        input = '__hp[idxArr[(3+2)*5/-(3*1)] = otherArr[idxArr[-3]]'
        expect = '__hp,[,idxArr,[,(,3,+,2,),*,5,/,-,(,3,*,1,),],=,otherArr,[,idxArr,[,-,3,],],<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 109))
    def test_expr_3(self):
        input = '0xFFFFFFFF + 0b110101111 - 0X1122330F / (0123321 * 0.0000000004 )+ 3.14E-10'
        expect = '0xFFFFFFFF,+,0b110101111,-,0X1122330F,/,(,0123321,*,0.0000000004,),+,3.14E-10,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 111))
    def test_expr_4(self):
        input = 'Var a: String = b +. "Welcome to PPL course";'
        expect = 'Var,a,:,String,=,b,+.,"Welcome to PPL course",;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 121))
    def test_expr_5(self):
        input = """If (length <= (15.123e3 + 0x123000000)){
            print(some_string);
        }"""
        expect= 'If,(,length,<=,(,15.123e3,+,0x123000000,),),{,print,(,some_string,),;,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 122))

    # Custom test from Justince
    def test_Thinh_1(self):
      self.assertTrue(TestLexer.test("""## VxpT$lLYZn. <=> ::AGz569YYpd ||:: <=> <=<= ||36scLLzWju %|| ::""","""Error Token #""",120))
    def test_Thinh_2(self):
      self.assertTrue(TestLexer.test("""## 2rDnLulZwmForeach ==## >=<= &== ==== <=>= ##>= #### |||| 5cSkUAUw$I== :::: >=<= ==* ::= ##If :::: ==<= ==>= +""",""">=,<=,Error Token &""",123))
    def test_Thinh_3(self):
      self.assertTrue(TestLexer.test("""Main ::Var ||""","""Main,::,Var,||,<EOF>""",124))
    def test_Thinh_4(self):
      self.assertTrue(TestLexer.test("""= _QQtX5FNVk! Continue|| Continue>= <=>= >=>= Main## <=<= Int|| ##|| ==<= .m0AZf7zrAW :::: ==<= >=+ >=>= Continue## >=""","""=,_QQtX5FNVk,!,Continue,||,Continue,>=,<=,>=,>=,>=,Main,||,==,<=,.,m0AZf7zrAW,::,::,==,<=,>=,+,>=,>=,Continue,Error Token #""",125))
    def test_Thinh_5(self):
      self.assertTrue(TestLexer.test("""<= .== ##== <=<= ::- :::: ==>= Constructor:: ||:: -:: ||## >=== ==& <=== ||. >=""","""<=,.,==,>=,==,==,Error Token &""",126))
    def test_Thinh_6(self):
      self.assertTrue(TestLexer.test("""|| >=. New< <=|| .:: ::""","""||,>=,.,New,<,<=,||,.,::,::,<EOF>""",127))
    def ttest_Thinh_7(self):
      self.assertTrue(TestLexer.test(""">= ##|| ::""",""">=,Error Token #""",128))