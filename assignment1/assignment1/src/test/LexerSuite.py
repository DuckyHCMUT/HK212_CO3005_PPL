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

    def test_110(self):
        input = 'Var myArr: Array[Float, 10];'
        expect = 'Var,myArr,:,Array,[,Float,,,10,],;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 110))

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
        expect = 'Var,urgay,:,Float,=,0,+,0x0,-,0b0,+,00,%,0.0,/,0.,+,.,0,*,0e2,+,(,.0e3,+,0.e3,-,.e3,+,e0,-,0.e0,),;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 115))

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
            $doNothing();
        } 
        """
        expect = """Foreach,(,x,,,y,In,100,..,300,By,5,),{,$doNothing,(,),;,},<EOF>"""
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

    def test_140(self):
        self.assertTrue(TestLexer.test("80AB", "80,AB,<EOF>", 140))

    def test_141(self):
        self.assertTrue(TestLexer.test("_a", "_a,<EOF>", 141))

    def test_id_142(self):
        self.assertTrue(TestLexer.test("Var ______a, a______, 0a_____, a0_____, _a_0_a_a: String", 
        "Var,______a,,,a______,,,0,a_____,,,a0_____,,,_a_0_a_a,:,String,<EOF>", 142))

    def test_dollar_id_143(self):
        self.assertTrue(TestLexer.test("$abcd, $_____, $087", "$abcd,,,$_____,,,$087,<EOF>", 143))

    def test_144(self):
        input = """ a = 0123 + 100_000_000_010_000 - 1_0_0_12334 * 0x10AE79 """
        expect = """a,=,0123,+,100000000010000,-,10012334,*,0x10AE79,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 144))

    def test_145(self):
        self.assertTrue(TestLexer.test("_12356", "_12356,<EOF>", 145))

    def test_146(self):
        self.assertTrue(TestLexer.test("-1", "-,1,<EOF>", 146))

    def test_147(self):
        self.assertTrue(TestLexer.test("-0123", "-,0123,<EOF>", 147))

    def test_148(self):
        self.assertTrue(TestLexer.test("-0xA416", "-,0xA416,<EOF>", 148))

    def test_149(self):
        self.assertTrue(TestLexer.test("-0xHK416","-,0,xHK416,<EOF>", 149))

    def test_150(self):
        self.assertTrue(TestLexer.test("-0B101111", "-,0B101111,<EOF>", 150))

    def test_151(self):
        self.assertTrue(TestLexer.test('"abc\\"', 'Illegal Escape In String: abc\\"', 151))

    def test_152(self):
        self.assertTrue(TestLexer.test("001", "00,1,<EOF>", 152))

    def test_153(self):
        self.assertTrue(TestLexer.test("1.200e6", "1.200e6,<EOF>", 153))

    def test_154(self):
        self.assertTrue(TestLexer.test("Array[Int, 0x10]", "Array,[,Int,,,0x10,],<EOF>", 154))

    def test_155(self):
        self.assertTrue(TestLexer.test("1_123E123", "1123E123,<EOF>", 155))

    def test_156(self):
        self.assertTrue(TestLexer.test("1________.0", "1,________,.,0,<EOF>", 156))

    def test_157(self):
        self.assertTrue(TestLexer.test("1.....3", "1.,..,..,3,<EOF>", 157))

    def test_158(self):
        self.assertTrue(TestLexer.test("123E0x123", "123E0,x123,<EOF>", 158))

    def test_159(self):
        self.assertTrue(TestLexer.test("-1.127", "-,1.127,<EOF>", 159))

    def test_160(self):
        self.assertTrue(TestLexer.test("2E&1", "2,E,Error Token &", 160))

    def test_161(self):
        """test True and False"""
        self.assertTrue(TestLexer.test("True == False", "True,==,False,<EOF>", 161))

    def test_string_1_162(self):
        self.assertTrue(TestLexer.test('"Hello World"', 'Hello World,<EOF>', 162))

    def test_string_2_163(self):
        self.assertTrue(TestLexer.test('""', ',<EOF>', 163))

    def test_string_3_164(self):
        self.assertTrue(TestLexer.test('"\t"', '\t,<EOF>', 164))

    def test_string_4_165(self):
        self.assertTrue(TestLexer.test('"\\nWorld"', '\\nWorld,<EOF>', 165))

    def test_string_5_166(self):
        self.assertTrue(TestLexer.test('"World\\n\\t\\b\\f\\n\\t\'""', 'World\\n\\t\\b\\f\\n\\t\'",<EOF>', 166))

    def test_string_6_167(self):
        self.assertTrue(TestLexer.test('"World \'"Hello\'""', 'World \'"Hello\'",<EOF>', 167))

    def test_string_7_168(self):
        self.assertTrue(TestLexer.test('"World \'"Hello\'" 123 \'"123\'""', 'World \'"Hello\'" 123 \'"123\'",<EOF>', 168))

    def test_string_8_169(self):
        self.assertTrue(TestLexer.test('"1" + "0x123"', '1,+,0x123,<EOF>', 169))

    def test_string_10_170(self):
        self.assertTrue(TestLexer.test('"0xFE55"', '0xFE55,<EOF>', 170))

    def test_wrong_string_1_171(self):
        self.assertTrue(TestLexer.test('"Hello "World ""', 'Hello ,World,,<EOF>', 171))

    def test_wrong_string_2_172(self):
        self.assertTrue(TestLexer.test('"Hello \'"World""', 'Hello \'"World,Unclosed String: ', 172))

    def test_wrong_string_3_173(self):
        self.assertTrue(TestLexer.test('Hello World"', 'Hello,World,Unclosed String: ', 187))

    def test_wrong_string_4_174(self):
        self.assertTrue(TestLexer.test('"Hello World', 'Unclosed String: Hello World', 174))

    def test_wrong_string_5_175(self):
        self.assertTrue(TestLexer.test('"Hello World""', 'Hello World,Unclosed String: ', 175))

    def test_string_11_176(self):
        self.assertTrue(TestLexer.test('"This is a string containing tab \t"', 'This is a string containing tab \t,<EOF>', 176))

    def test_string_12_177(self):
        self.assertTrue(TestLexer.test('"He asked me: \'"Where is John?\'""', 'He asked me: \'"Where is John?\'",<EOF>', 177))

    def test_178(self):
        self.assertTrue(TestLexer.test('Array("Hello", "Worl\'"d\'"", "")', 'Array,(,Hello,,,Worl\'"d\'",,,,),<EOF>', 178))

    def test_179(self):
        self.assertTrue(TestLexer.test("Array(Array(1, 2), Array(3,4))", "Array,(,Array,(,1,,,2,),,,Array,(,3,,,4,),),<EOF>", 179))

    def test_180(self):
        self.assertTrue(TestLexer.test("Array()", "Array,(,),<EOF>", 180))

    def test_181(self):
        self.assertTrue(TestLexer.test("Array(1.3, )", "Array,(,1.3,,,),<EOF>", 181))

    def test_182(self):
        self.assertTrue(TestLexer.test("Array(,)", "Array,(,,,),<EOF>", 182))

    def test_183(self):
        self.assertTrue(TestLexer.test("array(1, 2, 3)", "array,(,1,,,2,,,3,),<EOF>", 183))

    def test_184(self):
        self.assertTrue(TestLexer.test("Boolean!===&&||", "Boolean,!=,==,&&,||,<EOF>", 184))

    def test_185(self):
        self.assertTrue(TestLexer.test("!!=!!=!!", "!,!=,!,!=,!,!,<EOF>", 185))

    def test_186(self):
        self.assertTrue(TestLexer.test("!&|&|=&=!&=boolean", "!,Error Token &", 186))

    def test_187(self):
        self.assertTrue(TestLexer.test("BooLean", "BooLean,<EOF>", 187))

    def test_188(self):
        self.assertTrue(TestLexer.test("+-*/%><=>=!==<>", "+,-,*,/,%,>,<=,>=,!=,=,<,>,<EOF>", 188))

    def test_189(self):
        self.assertTrue(TestLexer.test("1 + 2e+10", "1,+,2e+10,<EOF>", 189))

    def test_190(self):
        self.assertTrue(TestLexer.test("0_1_2_3", "0,_1_2_3,<EOF>", 190))

    def test_191(self):
        input = """
        Foreach (i In 1..100 By 2) {
            Out.printInt(i);
        }
        """
        expect = "Foreach,(,i,In,1.,.,100,By,2,),{,Out,.,printInt,(,i,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 191))

    def test_192(self):
        self.assertTrue(TestLexer.test('"He asked me: \'"Where is John?\'""',
        'He asked me: \'"Where is John?\'",<EOF>', 192))

    def test_193(self):
        self.assertTrue(TestLexer.test("$089", "$089,<EOF>", 193))

    def test_194(self):
        self.assertTrue(TestLexer.test('"Hello ##My## World"', """Hello ##My## World,<EOF>""", 194))

    def test_195(self):
        self.assertTrue(TestLexer.test('"Hello World## " ##', 'Hello World## ,Error Token #', 195))

    def test_196(self):
        input = """
        Class Program {
            Var a: Float = !456 >= 234 && 345 + 456 || 567 <= (678 != a);
        }
        """
        expect = "Class,Program,{,Var,a,:,Float,=,!,456,>=,234,&&,345,+,456,||,567,<=,(,678,!=,a,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 196))

    def test_197(self):
        """New line in string"""
        input = """ "My entire life
            Your career " """
        expect = "Unclosed String: My entire life\n"
        self.assertTrue(TestLexer.test(input, expect, 197))

    def test_198(self):
        self.assertTrue(TestLexer.test("1.1e00", "1.1e00,<EOF>", 198))

    def test_199(self):
        input = r""" "Hello \' Vietnam" """
        expect = r"""Hello \' Vietnam,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 199))

    def test_200(self):
        self.assertTrue(TestLexer.test("1 + --2", "1,+,-,-,2,<EOF>", 200))

    def test_201(self):
        self.assertTrue(TestLexer.test("*p = q[0x23] + -24 * (10.3e5 - 32);", "*,p,=,q,[,0x23,],+,-,24,*,(,10.3e5,-,32,),;,<EOF>", 201))

    def test_202(self):
        input = """
        Int dec = 0, i = 0, rem;
        While (n > 0) { 
            remaining = n % 10;
            n = n / 10;
            dec = dec + remaining * pow(2, i);
            i = i + 1;
        }
        """
        expect = """Int,dec,=,0,,,i,=,0,,,rem,;,While,(,n,>,0,),{,remaining,=,n,%,10,;,n,=,n,/,10,;,dec,=,dec,+,remaining,*,pow,(,2,,,i,),;,i,=,i,+,1,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 202))

    def test_203(self):
        self.assertTrue(TestLexer.test("String a, b;a +. b;a ==. c;", "String,a,,,b,;,a,+.,b,;,a,==.,c,;,<EOF>", 203))

    def test_204(self):
        self.assertTrue(TestLexer.test("a = b ==. c;a === b;", "a,=,b,==.,c,;,a,==,=,b,;,<EOF>", 204))

    def test_205(self):
        self.assertTrue(TestLexer.test("a ===.=.!=.==!. f", "a,==,=,.,=,.,!=,.,==,!,.,f,<EOF>", 205))

    def test_206(self):
        self.assertTrue(TestLexer.test("Var a: Array[Float, 0b110101]", "Var,a,:,Array,[,Float,,,0b110101,],<EOF>", 206))

    def test_207(self):
        self.assertTrue(TestLexer.test("Val A = New Object()", "Val,A,=,New,Object,(,),<EOF>", 207))

    def test_208(self):
        self.assertTrue(TestLexer.test("Foreach (i In 1 .. 1000 By 20) { Out.printInt(i);}", "Foreach,(,i,In,1,..,1000,By,20,),{,Out,.,printInt,(,i,),;,},<EOF>", 208))

    def test_209(self):
        """test ab?svn"""
        self.assertTrue(TestLexer.test("ab?svn", "ab,Error Token ?", 209))

    def test_210(self):
        self.assertTrue(TestLexer.test('"abc\h"', 'Illegal Escape In String: abc\h', 210))

    def test_211(self):
        self.assertTrue(TestLexer.test("viet.trana4@hcmut.com", "viet,.,trana4,Error Token @", 211))

    def test_212(self):
        self.assertTrue(TestLexer.test("ab$cbd", "ab,$cbd,<EOF>", 212))

    def test_213(self):
        self.assertTrue(TestLexer.test("console.log(`${a}`);", "console,.,log,(,Error Token `", 213))

    def test_214(self):
        self.assertTrue(TestLexer.test("a = ~c;", "a,=,Error Token ~", 214))

    def test_215(self):
        self.assertTrue(TestLexer.test("ab#ef", "ab,Error Token #", 215))

    def test_216(self):
        self.assertTrue(TestLexer.test('"ab$cd ab#cd ?abc @London"', 'ab$cd ab#cd ?abc @London,<EOF>', 216))

    def test_217(self):
        self.assertTrue(TestLexer.test("## Hello World ##", "<EOF>", 217))

    def test_218(self):
        self.assertTrue(TestLexer.test("Val a : Int = 1; ## Hello World ## b.call();", "Val,a,:,Int,=,1,;,b,.,call,(,),;,<EOF>", 218))

    def test_219(self):
        self.assertTrue(TestLexer.test("Val a : Int = ## Assign ## 5;", "Val,a,:,Int,=,5,;,<EOF>", 219))

    def test_220(self):
        self.assertTrue(TestLexer.test("1234.056789", "1234.056789,<EOF>", 220))

    def test_221(self):
        self.assertTrue(TestLexer.test("012356_1671_17531311", "012356167117531311,<EOF>", 221))

    def test_222(self):
        self.assertTrue(TestLexer.test("0123__124", "0123,__124,<EOF>", 222))

    def test_223(self):
        self.assertTrue(TestLexer.test("0b1_01_01", "0b10101,<EOF>", 223))

    def test_224(self):
        self.assertTrue(TestLexer.test("0B101__0101", "0B101,__0101,<EOF>", 224))

    def test_225(self):
        self.assertTrue(TestLexer.test("0xAE15_617ABCD", "0xAE15617ABCD,<EOF>", 225))

    def test_226(self):
        self.assertTrue(TestLexer.test("0X167A__EEEEFFFF", "0X167A,__EEEEFFFF,<EOF>", 226))

    def test_227(self):
        self.assertTrue(TestLexer.test(".e4", ".e4,<EOF>", 227))

    def test_228(self):
        self.assertTrue(TestLexer.test('"abc\\h"', 'Illegal Escape In String: abc\h', 228))

    def test_229(self):
        self.assertTrue(TestLexer.test("1.2e-023", "1.2e-023,<EOF>", 229))

    def test_230(self):
        self.assertTrue(TestLexer.test('"""', ',Unclosed String: ', 230))

    def test_231(self):
        self.assertTrue(TestLexer.test('"doesn\'t"', 'doesn\'t,<EOF>', 231))

    def test_232(self):
        self.assertTrue(TestLexer.test("00", "00,<EOF>", 232))

    def test_233(self):
        self.assertTrue(TestLexer.test("00012", "00,012,<EOF>", 233))

    def test_234(self):
        self.assertTrue(TestLexer.test("0B0110101", "0B0,110101,<EOF>", 234))

    def test_235(self):
        self.assertTrue(TestLexer.test("0b012", "0b0,12,<EOF>", 235))

    def test_236(self):
        self.assertTrue(TestLexer.test("0b01_01_01", "0b0,10101,<EOF>", 236))

    def test_237(self):
        self.assertTrue(TestLexer.test("0057", "00,57,<EOF>", 237))

    def test_238(self):
        self.assertTrue(TestLexer.test("0b010", "0b0,10,<EOF>", 238))

    def test_239(self):
        self.assertTrue(TestLexer.test("0x00AF", "0x0,0,AF,<EOF>", 239))

    def test_240(self):
        self.assertTrue(TestLexer.test("0x0001", "0x0,00,1,<EOF>", 240))

    def test_241(self):
        self.assertTrue(TestLexer.test("\"Dumbledore : '\" Lily? After all? \\n \\t \\n \\2 '\" \"", 
        "Illegal Escape In String: Dumbledore : '\" Lily? After all? \\n \\t \\n \\2", 241))

    def test_242(self):
        self.assertTrue(TestLexer.test("\"abc'\"", "Unclosed String: abc'\"", 242))

    def test_243(self):
        self.assertTrue(TestLexer.test("0.00000000", "0.00000000,<EOF>", 243))

    def test_244(self):
        self.assertTrue(TestLexer.test('"abc\\h"', 'Illegal Escape In String: abc\h', 244))

    def test_245(self):
        self.assertTrue(TestLexer.test("3.2000e7", "3.2000e7,<EOF>", 245))

    def test_246(self):
        self.assertTrue(TestLexer.test(""" "Thanh Nhan \\" """,'Illegal Escape In String: Thanh Nhan \\"', 246))

    def test_247(self):
        self.assertTrue(TestLexer.test(' "string" " ','string,Unclosed String:  ', 247))

    def test_248(self):
        self.assertTrue(TestLexer.test("\"String with single quote \'this is good\'\"","""Unclosed String: String with single quote 'this is good'\"""", 248))

    