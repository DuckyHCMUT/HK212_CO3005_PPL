import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.test("aCBbdc", "aCBbdc,<EOF>", 102))

    def test_mixed_id(self):
        self.assertTrue(TestLexer.test("aAsVN3", "aAsVN3,<EOF>", 103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 104))

    def test_identifier_1(self):
        """test abc_123"""
        self.assertTrue(TestLexer.test("abc_123", "abc_123,<EOF>", 105))

    def test_identifier_2(self):
        """test b_1"""
        self.assertTrue(TestLexer.test("b_1", "b_1,<EOF>", 106))

    def test_identifier_3(self):
        """test a"""
        self.assertTrue(TestLexer.test("a", "a,<EOF>", 107))

    def test_identifier_4(self):
        """test b"""
        self.assertTrue(TestLexer.test("b", "b,<EOF>", 108))

    def test_identifier_5(self):
        """test A"""
        self.assertTrue(TestLexer.test("A", "A,<EOF>", 109))

    def test_identifier_6(self):
        """test B"""
        self.assertTrue(TestLexer.test("B", "B,<EOF>", 110))

    def test_identifier_7(self):
        """test BCHD"""
        self.assertTrue(TestLexer.test("BCHD", "BCHD,<EOF>", 111))

    def test_identifier_8(self):
        """test 80AB"""
        self.assertTrue(TestLexer.test("80AB", "80,AB,<EOF>", 112))

    def test_identifier_9(self):
        """test _a"""
        self.assertTrue(TestLexer.test("_a", "_a,<EOF>", 113))

    def test_identifier_10(self):
        """test ______a"""
        self.assertTrue(TestLexer.test("______a", "______a,<EOF>", 114))

    def test_identifier_11(self):
        """test a______"""
        self.assertTrue(TestLexer.test("a______", "a______,<EOF>", 115))

    def test_identifier_14(self):
        """test 0a_____"""
        self.assertTrue(TestLexer.test("0a_____", "0,a_____,<EOF>", 116))

    def test_identifier_12(self):
        """test a0_____"""
        self.assertTrue(TestLexer.test("a0_____", "a0_____,<EOF>", 117))

    def test_identifier_13(self):
        """test _a_0_a_a"""
        self.assertTrue(TestLexer.test("_a_0_a_a", "_a_0_a_a,<EOF>", 118))

    def test_static_member_1(self):
        """test $abc"""
        self.assertTrue(TestLexer.test("$abc", "$abc,<EOF>", 119))

    def test_static_member_2(self):
        """test $_____"""
        self.assertTrue(TestLexer.test("$_____", "$_____,<EOF>", 120))

    def test_wrong_static_member_3(self):
        """test $089"""
        self.assertTrue(TestLexer.test("$089", "$089,<EOF>", 121))

    def test_octal_number_1(self):
        """test 0123"""
        self.assertTrue(TestLexer.test("0123", "0123,<EOF>", 122))

    def test_octal_number_2(self):
        """test 01"""
        self.assertTrue(TestLexer.test("01", "01,<EOF>", 123))

    def test_wrong_octal_number_3(self):
        """test 0568"""
        self.assertTrue(TestLexer.test("0568", "056,8,<EOF>", 124))

    def test_octal_number_4(self):
        """test 057"""
        self.assertTrue(TestLexer.test("057", "057,<EOF>", 125))

    def test_hex_number_1(self):
        """test 0x123"""
        self.assertTrue(TestLexer.test("0x123", "0x123,<EOF>", 126))

    def test_hex_number_2(self):
        """test 0xA"""
        self.assertTrue(TestLexer.test("0xA", "0xA,<EOF>", 127))

    def test_hex_number_3(self):
        """test 0x123AE"""
        self.assertTrue(TestLexer.test("0x123AE", "0x123AE,<EOF>", 128))

    def test_wrong_hex_number_4(self):
        """test 0x12AF"""
        self.assertTrue(TestLexer.test("0x12AF", "0x12AF,<EOF>", 129))

    def test_hex_number_5(self):
        """test 0X123"""
        self.assertTrue(TestLexer.test("0X123", "0X123,<EOF>", 130))

    def test_hex_number_6(self):
        """test 0XA"""
        self.assertTrue(TestLexer.test("0XA", "0XA,<EOF>", 131))

    def test_hex_number_7(self):
        """test 0X123AE"""
        self.assertTrue(TestLexer.test("0X123AE", "0X123AE,<EOF>", 132))

    def test_correct_hex_number_8(self):
        """test 0X12AF"""
        self.assertTrue(TestLexer.test("0X12AF", "0X12AF,<EOF>", 133))

    def test_binary_number_1(self):
        """test 0b1"""
        self.assertTrue(TestLexer.test("0b1", "0b1,<EOF>", 134))

    def test_binary_number_2(self):
        """test 0b0"""
        self.assertTrue(TestLexer.test("0b0", "0b0,<EOF>", 135))

    def test_binary_number_3(self):
        """test 0b10"""
        self.assertTrue(TestLexer.test("0b10", "0b10,<EOF>", 136))

    def test_wrong_binary_number_4(self):
        """test 0b12"""
        self.assertTrue(TestLexer.test("0b12", "0b1,2,<EOF>", 137))

    def test_decimal_number_1(self):
        """test 1"""
        self.assertTrue(TestLexer.test("1", "1,<EOF>", 138))

    def test_decimal_number_2(self):
        """test 123"""
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 139))

    def test_decimal_number_3(self):
        """test 100000000000000"""
        self.assertTrue(TestLexer.test(
            "100000000000000", "100000000000000,<EOF>", 140))

    def test_decimal_number_underscore_1(self):
        """test 100_000_000_000_000"""
        self.assertTrue(TestLexer.test(
            "100_000_000_000_000", "100000000000000,<EOF>", 141))

    def test_decimal_number_underscore_2(self):
        """test 1_0_0____12334"""
        self.assertTrue(TestLexer.test(
            "1_0_0____12334", "100,____12334,<EOF>", 142))

    def test_wrong_decimal_number_1(self):
        """test 10AE79"""
        self.assertTrue(TestLexer.test(
            "10AE79", "10,AE79,<EOF>", 143))

    def test_wrong_decimal_number_2(self):
        """test _12356"""
        self.assertTrue(TestLexer.test(
            "_12356", "_12356,<EOF>", 144))

    def test_negative_number_1(self):
        """test -1"""
        self.assertTrue(TestLexer.test("-1", "-,1,<EOF>", 145))

    def test_negative_number_2(self):
        """test -0123"""
        self.assertTrue(TestLexer.test("-0123", "-,0123,<EOF>", 146))

    def test_negative_number_3(self):
        """test -0xAE16"""
        self.assertTrue(TestLexer.test("-0xAE16", "-,0xAE16,<EOF>", 147))

    def test_negative_number_4(self):
        """test -0B1011"""
        self.assertTrue(TestLexer.test("-0B1011", "-,0B1011,<EOF>", 148))

    def test_float_1(self):
        """test 1.1"""
        self.assertTrue(TestLexer.test("1.1", "1.1,<EOF>", 149))

    def test_float_2(self):
        """test 1.23"""
        self.assertTrue(TestLexer.test("1.23", "1.23,<EOF>", 150))

    def test_float_3(self):
        """test 11.23"""
        self.assertTrue(TestLexer.test("11.23", "11.23,<EOF>", 151))

    def test_float_4(self):
        """test 1e13"""
        self.assertTrue(TestLexer.test("1e13", "1e13,<EOF>", 152))

    def test_float_5(self):
        """test 1E-14"""
        self.assertTrue(TestLexer.test("1E-14", "1E-14,<EOF>", 153))

    def test_float_6(self):
        """test 1e5"""
        self.assertTrue(TestLexer.test("1e5", "1e5,<EOF>", 154))

    def test_float_7(self):
        """test 11E+4"""
        self.assertTrue(TestLexer.test("11E+4", "11E+4,<EOF>", 155))

    def test_float_8(self):
        """test 1_123.1234"""
        self.assertTrue(TestLexer.test(
            "1_123.1234", "1123.1234,<EOF>", 156))

    def test_float_9(self):
        """test 1_123."""
        self.assertTrue(TestLexer.test(
            "1_123.", "1123.,<EOF>", 157))

    def test_float_10(self):
        """test 1_1.1_123e10"""
        self.assertTrue(TestLexer.test(
            "1_1.1123e10", "11.1123e10,<EOF>", 158))

    def test_float_11(self):
        """test 50.1123E-5"""
        self.assertTrue(TestLexer.test(
            "50.1123E-5", "50.1123E-5,<EOF>", 159))

    def test_float_12(self):
        """test .5e5"""
        self.assertTrue(TestLexer.test(".5e5", ".5e5,<EOF>", 160))

    def test_float_13(self):
        """test .4e+5"""
        self.assertTrue(TestLexer.test(".4e+5", ".4e+5,<EOF>", 161))

    def test_float_14(self):
        """test .1123e-10"""
        self.assertTrue(TestLexer.test(".1123e-10", ".1123e-10,<EOF>", 162))

    def test_float_15(self):
        """test 1_123E123"""
        self.assertTrue(TestLexer.test("1_123E123", "1123E123,<EOF>", 163))

    def test_float_16(self):
        """test 1________.0"""
        self.assertTrue(TestLexer.test(
            "1________.0", "1,________,.,0,<EOF>", 164))

    def test_wrong_float_1(self):
        """test 1.....1"""
        self.assertTrue(TestLexer.test("1.....1", "1.,..,..,1,<EOF>", 165))

    def test_wrong_float_2(self):
        """test 1ee13"""
        self.assertTrue(TestLexer.test("1ee13", "1,ee13,<EOF>", 166))

    def test_wrong_float_3(self):
        """test 0x12.174"""
        self.assertTrue(TestLexer.test("0x12.174", "0x12,.,174,<EOF>", 167))

    def test_wrong_float_4(self):
        """test 124.0x126"""
        self.assertTrue(TestLexer.test("124.0x126", "124.0,x126,<EOF>", 168))

    def test_wrong_float_5(self):
        """test 123E0x123"""
        self.assertTrue(TestLexer.test("123E0x123", "123E0,x123,<EOF>", 169))

    def test_wrong_float_6(self):
        """test 0B110.110"""
        self.assertTrue(TestLexer.test("0B110.110", "0B110,.,110,<EOF>", 170))

    def test_negative_float_num_1(self):
        """test -1.127"""
        self.assertTrue(TestLexer.test("-1.127", "-,1.127,<EOF>", 171))

    def test_wrong_float_7(self):
        """test 1e"""
        self.assertTrue(TestLexer.test("1e", "1,e,<EOF>", 172))

    def test_float_17(self):
        """test .e4"""
        self.assertTrue(TestLexer.test(".e4", ".e4,<EOF>", 173))

    def test_wrong_float_8(self):
        """test 0123.516"""
        self.assertTrue(TestLexer.test("0123.516", "0123,.,516,<EOF>", 174))

    def test_wrong_float_9(self):
        """test 17,417"""
        self.assertTrue(TestLexer.test("17,417", "17,,,417,<EOF>", 175))

    def test_wrong_float_10(self):
        """test 1.4E"""
        self.assertTrue(TestLexer.test("1.4E", "1.4,E,<EOF>", 176))

    def test_wrong_float_11(self):
        """test 1E&1"""
        self.assertTrue(TestLexer.test("1E&1", "1,E,Error Token &", 177))

    def test_boolean_literal_1(self):
        """test True"""
        self.assertTrue(TestLexer.test("True", "True,<EOF>", 178))

    def test_boolean_literal_2(self):
        """test False"""
        self.assertTrue(TestLexer.test("False", "False,<EOF>", 179))

    def test_wrong_boolean_literal_1(self):
        """test true"""
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 180))

    def test_wrong_boolean_literal_2(self):
        """test false"""
        self.assertTrue(TestLexer.test("false", "false,<EOF>", 181))

    def test_wrong_boolean_literal_3(self):
        """test Trueee"""
        self.assertTrue(TestLexer.test("Trueee", "Trueee,<EOF>", 182))

    def test_wrong_boolean_literal_4(self):
        """test FalseTrue"""
        self.assertTrue(TestLexer.test("FalseTrue", "FalseTrue,<EOF>", 183))

    def test_string_1(self):
        """test \"Hello World\""""
        self.assertTrue(TestLexer.test(
            '"Hello World"', 'Hello World,<EOF>', 184))

    def test_string_2(self):
        """test \"\""""
        self.assertTrue(TestLexer.test('""', ',<EOF>', 185))

    def test_string_3(self):
        """test \"\t\""""
        self.assertTrue(TestLexer.test('"\t"', '\t,<EOF>', 186))

    def test_string_4(self):
        """test \"\nWorld\""""
        self.assertTrue(TestLexer.test('"\\nWorld"', '\\nWorld,<EOF>', 187))

    def test_string_5(self):
        """test \"World\n\t\b\f\n\t\'\""""
        self.assertTrue(TestLexer.test(
            '"World\\n\\t\\b\\f\\n\\t\'""', 'World\\n\\t\\b\\f\\n\\t\'",<EOF>', 188))

    def test_string_6(self):
        """test \"World '\"Hello'\"\""""
        self.assertTrue(TestLexer.test('"World \'"Hello\'""',
                        'World \'"Hello\'",<EOF>', 189))

    def test_string_7(self):
        """test \"World '\"Hello'\" 123 '\"123'\"\""""
        self.assertTrue(TestLexer.test(
            '"World \'"Hello\'" 123 \'"123\'""', 'World \'"Hello\'" 123 \'"123\'",<EOF>', 190))

    def test_string_8(self):
        """test \"1\""""
        self.assertTrue(TestLexer.test('"1"', '1,<EOF>', 191))

    def test_string_9(self):
        """test \"0x123\""""
        self.assertTrue(TestLexer.test('"0x123"', '0x123,<EOF>', 192))

    def test_string_10(self):
        """test \"0xFE55\""""
        self.assertTrue(TestLexer.test('"0xFE55"', '0xFE55,<EOF>', 193))

    def test_wrong_string_1(self):
        """test \"Hello \"World \"\""""
        self.assertTrue(TestLexer.test('"Hello "World ""',
                        'Hello ,World,,<EOF>', 194))

    def test_wrong_string_2(self):
        '''test "Hello '"World""'''
        self.assertTrue(TestLexer.test('"Hello \'"World""',
                        'Hello \'"World,Unclosed String: ', 195))

    def test_wrong_string_3(self):
        """test Hello World\""""
        self.assertTrue(TestLexer.test(
            'Hello World"', 'Hello,World,Unclosed String: ', 196))

    def test_wrong_string_4(self):
        '''test "Hello World'''
        self.assertTrue(TestLexer.test(
            '"Hello World', 'Unclosed String: Hello World', 197))

    def test_wrong_string_5(self):
        '''test "Hello World""'''
        self.assertTrue(TestLexer.test(
            '"Hello World""', 'Hello World,Unclosed String: ', 198))

    def test_string_11(self):
        '''"This is a string containing tab \t"'''
        self.assertTrue(TestLexer.test('"This is a string containing tab \t"',
                        'This is a string containing tab \t,<EOF>', 199))

    def test_string_12(self):
        '''"He asked me: \'"Where is John?\'""'''
        self.assertTrue(TestLexer.test('"He asked me: \'"Where is John?\'""',
                        'He asked me: \'"Where is John?\'",<EOF>', 200))

    def test_array_1(self):
        """test Array(1, 2, 3)"""
        self.assertTrue(TestLexer.test(
            "Array(1, 2, 3)", "Array,(,1,,,2,,,3,),<EOF>", 201))

    def test_array_2(self):
        """test Array(1.45, 2e10, 3.)"""
        self.assertTrue(TestLexer.test(
            "Array(1.45, 2e10, 3.)", "Array,(,1.45,,,2e10,,,3.,),<EOF>", 202))

    def test_array_3(self):
        '''test Array("Hello", "Worl\'"d\'"", "")'''
        self.assertTrue(TestLexer.test(
            'Array("Hello", "Worl\'"d\'"", "")', 'Array,(,Hello,,,Worl\'"d\'",,,,),<EOF>', 203))

    def test_array_4(self):
        """test Array(Array(1, 2), Array(3,4))"""
        self.assertTrue(TestLexer.test(
            "Array(Array(1, 2), Array(3,4))", "Array,(,Array,(,1,,,2,),,,Array,(,3,,,4,),),<EOF>", 204))

    def test_array_5(self):
        """test Array()"""
        self.assertTrue(TestLexer.test("Array()", "Array,(,),<EOF>", 205))

    def test_wrong_array_1(self):
        """test Array[]"""
        self.assertTrue(TestLexer.test("Array[]", "Array,[,],<EOF>", 206))

    def test_wrong_array_2(self):
        """test Array{}"""
        self.assertTrue(TestLexer.test("Array{}", "Array,{,},<EOF>", 207))

    def test_wrong_array_3(self):
        """test Array[}"""
        self.assertTrue(TestLexer.test("Array[}", "Array,[,},<EOF>", 208))

    def test_wrong_array_4(self):
        """test Array(]"""
        self.assertTrue(TestLexer.test("Array(]", "Array,(,],<EOF>", 209))

    def test_wrong_array_5(self):
        """test Array(1.3, )"""
        self.assertTrue(TestLexer.test(
            "Array(1.3, )", "Array,(,1.3,,,),<EOF>", 210))

    def test_wrong_array_6(self):
        """test Array(,)"""
        self.assertTrue(TestLexer.test("Array(,)", "Array,(,,,),<EOF>", 211))

    def test_wrong_array_7(self):
        """test array(1, 2, 3)"""
        self.assertTrue(TestLexer.test("array(1, 2, 3)",
                        "array,(,1,,,2,,,3,),<EOF>", 212))

    def test_bool_op_1(self):
        """test Boolean!===&&||"""
        self.assertTrue(TestLexer.test(
            "Boolean!===&&||", "Boolean,!=,==,&&,||,<EOF>", 213))

    def test_bool_op_2(self):
        """test !!=!!=!!"""
        self.assertTrue(TestLexer.test("!!=!!=!!", "!,!=,!,!=,!,!,<EOF>", 214))

    def test_not_bool_op_1(self):
        """test !&|&|=&=!&=boolean"""
        self.assertTrue(TestLexer.test(
            "!&|&|=&=!&=boolean", "!,Error Token &", 215))

    def test_not_bool_keyword_1(self):
        """test BooLean"""
        self.assertTrue(TestLexer.test("BooLean", "BooLean,<EOF>", 216))

    def test_number_op_1(self):
        """test +-*/%><=>=!==<>"""
        self.assertTrue(TestLexer.test(
            "+-*/%><=>=!==<>", "+,-,*,/,%,>,<=,>=,!=,=,<,>,<EOF>", 217))

    def test_number_op_2(self):
        """test 1 + 2e+10"""
        self.assertTrue(TestLexer.test("1 + 2e+10", "1,+,2e+10,<EOF>", 218))

    def test_number_op_3(self):
        """test 1 - -2"""
        self.assertTrue(TestLexer.test("1 - -2", "1,-,-,2,<EOF>", 219))

    def test_number_op_4(self):
        """test *p = q[12] + -24 * (10.3e5 - 32);"""
        self.assertTrue(TestLexer.test(
            "*p = q[12] + -24 * (10.3e5 - 32);", "*,p,=,q,[,12,],+,-,24,*,(,10.3e5,-,32,),;,<EOF>", 220))

    def test_number_op_5(self):
        """test Int dec = 0, i = 0, rem;
        While (n!=0) {
            rem = n % 10;
            n = n / 10;
            dec = dec + rem * pow(2, i);
            i = i + 1;
        }"""
        self.assertTrue(TestLexer.test("""Int dec = 0, i = 0, rem;
        While (n!=0) { 
            rem = n % 10;
            n = n / 10;
            dec = dec + rem * pow(2, i);
            i = i + 1;
        }""", "Int,dec,=,0,,,i,=,0,,,rem,;,While,(,n,!=,0,),{,rem,=,n,%,10,;,n,=,n,/,10,;,dec,=,dec,+,rem,*,pow,(,2,,,i,),;,i,=,i,+,1,;,},<EOF>", 221))

    def test_string_op_1(self):
        """test String a, b;a +. b;a ==. c;"""
        self.assertTrue(TestLexer.test(
            "String a, b;a +. b;a ==. c;", "String,a,,,b,;,a,+.,b,;,a,==.,c,;,<EOF>", 222))

    def test_string_op_2(self):
        """test a = b ==. c;a === b;"""
        self.assertTrue(TestLexer.test(
            "a = b ==. c;a === b;", "a,=,b,==.,c,;,a,==,=,b,;,<EOF>", 223))

    def test_string_op_3(self):
        """test a ===.=.!=.==!. b"""
        self.assertTrue(TestLexer.test("a ===.=.!=.==!. b",
                        "a,==,=,.,=,.,!=,.,==,!,.,b,<EOF>", 224))

    def test_simple_arr_type_1(self):
        """test Var a: Array[Float, 10]"""
        self.assertTrue(TestLexer.test(
            "Var a: Array[Float, 10]", "Var,a,:,Array,[,Float,,,10,],<EOF>", 225))

    def test_simple_obj_1(self):
        """test Val A = New X()"""
        self.assertTrue(TestLexer.test(
            "Val A = New X()", "Val,A,=,New,X,(,),<EOF>", 226))

    def test_simple_program_1(self):
        """test Foreach (i In 1 .. 100 By 2) { Out.printInt(i);}"""
        self.assertTrue(TestLexer.test(
            "Foreach (i In 1 .. 100 By 2) { Out.printInt(i);}", "Foreach,(,i,In,1,..,100,By,2,),{,Out,.,printInt,(,i,),;,},<EOF>", 227))

    def test_wrong_token_1(self):
        """test ab?svn"""
        self.assertTrue(TestLexer.test("ab?svn", "ab,Error Token ?", 228))

    def test_illegal_escape(self):
        '''test "abc\h"'''
        self.assertTrue(TestLexer.test(
            '"abc\h"', 'Illegal Escape In String: abc\h', 229))

    def test_wrong_token_2(self):
        """test jj@jj.com"""
        self.assertTrue(TestLexer.test("jj@jj.com", "jj,Error Token @", 230))

    def test_static_token_1(self):
        """test ab$cbd"""
        self.assertTrue(TestLexer.test("ab$cbd", "ab,$cbd,<EOF>", 231))

    def test_wrong_token_3(self):
        """test console.log(`${a}`);"""
        self.assertTrue(TestLexer.test(
            "console.log(`${a}`);", "console,.,log,(,Error Token `", 232))

    def test_wrong_token_4(self):
        """test a = ~b;"""
        self.assertTrue(TestLexer.test("a = ~b;", "a,=,Error Token ~", 233))

    def test_wrong_token_5(self):
        """test ab#cd"""
        self.assertTrue(TestLexer.test("ab#cd", "ab,Error Token #", 234))

    def test_wrong_token_inside_string(self):
        '''test "ab$cd ab#cd ?abc @somewhere"'''
        self.assertTrue(TestLexer.test(
            '"ab$cd ab#cd ?abc @somewhere"', 'ab$cd ab#cd ?abc @somewhere,<EOF>', 235))

    def test_comment_1(self):
        """test ## Hello World ##"""
        self.assertTrue(TestLexer.test("## Hello World ##", "<EOF>", 236))

    def test_comment_2(self):
        """test Val a : Int = 1; ## Hello World ## b.call();"""
        self.assertTrue(TestLexer.test("Val a : Int = 1; ## Hello World ## b.call();",
                        "Val,a,:,Int,=,1,;,b,.,call,(,),;,<EOF>", 237))

    def test_comment_3(self):
        """test Val a : Int = ## Assign value ## 3;"""
        self.assertTrue(TestLexer.test(
            "Val a : Int = ## Assign value ## 3;", "Val,a,:,Int,=,3,;,<EOF>", 238))

    def test_huge_program_1(self):
        """test program.d96"""
        self.assertTrue(TestLexer.test("""Class TestNameNodeMetrics {
  Val CONF : Int = New HdfsConfiguration();
  Var $DFS_REDUNDANCY_INTERVAL : Int = 1;
  Val $TEST_ROOT_DIR_PATH : String = New Path("/testNameNodeMetrics");
  Val NN_METRICS : String = "NameNodeActivity";
  Var BLOCK_SIZE : Float = 1024e10 * 1024.05;
  
  ##
  Number of datanodes in the cluster
  ##
  Var $DATANODE_COUNT : Int = EC_POLICY.getNumDataUnits() + EC_POLICY.getNumParityUnits() + 1;
  
  Val cluster;
  Val fs;

  Int getTestPath(fileName : String) {
    Return New Path(TEST_ROOT_DIR_PATH, fileName);
  }

  Boolean setUp(a : Int, b : Float) {
    cluster.waitActive();
    someFunc();
    fs.enableErasureCodingPolicy(EC_POLICY.getName());
    ecDir = getTestPath("/ec");
    fs.setErasureCodingPolicy(ecDir, EC_POLICY.getName());
  }
  
  Void tearDown() {
    Val source : Float = DefaultMetricsSystem.instance().getSource("UgiMetrics");
    If (source != Null) {
      ##
      Run only once since the UGI metrics is cleaned up during teardown
      ##
      assertQuantileGauges("GetGroups1s", rb);
    }
    If (hostsFileWriter != Null) {
      hostsFileWriter.cleanup();
      hostsFileWriter = Null;
    }
    If (cluster != Null) {
      cluster.shutdown();
      cluster = Null;
    }

    Val includeHosts : Array[Int, 100] = New String[dnAddresses.length - 1];
    Foreach (i in 1 .. 100 By 1) {
      includeHosts[i] = dnAddresses[i + 1];
    }
  }
}

Class Program {
  main() {
    Out.println("Hello World");
  }
}""", """Class,TestNameNodeMetrics,{,Val,CONF,:,Int,=,New,HdfsConfiguration,(,),;,Var,$DFS_REDUNDANCY_INTERVAL,:,Int,=,1,;,Val,$TEST_ROOT_DIR_PATH,:,String,=,New,Path,(,/testNameNodeMetrics,),;,Val,NN_METRICS,:,String,=,NameNodeActivity,;,Var,BLOCK_SIZE,:,Float,=,1024e10,*,1024.05,;,Var,$DATANODE_COUNT,:,Int,=,EC_POLICY,.,getNumDataUnits,(,),+,EC_POLICY,.,getNumParityUnits,(,),+,1,;,Val,cluster,;,Val,fs,;,Int,getTestPath,(,fileName,:,String,),{,Return,New,Path,(,TEST_ROOT_DIR_PATH,,,fileName,),;,},Boolean,setUp,(,a,:,Int,,,b,:,Float,),{,cluster,.,waitActive,(,),;,someFunc,(,),;,fs,.,enableErasureCodingPolicy,(,EC_POLICY,.,getName,(,),),;,ecDir,=,getTestPath,(,/ec,),;,fs,.,setErasureCodingPolicy,(,ecDir,,,EC_POLICY,.,getName,(,),),;,},Void,tearDown,(,),{,Val,source,:,Float,=,DefaultMetricsSystem,.,instance,(,),.,getSource,(,UgiMetrics,),;,If,(,source,!=,Null,),{,assertQuantileGauges,(,GetGroups1s,,,rb,),;,},If,(,hostsFileWriter,!=,Null,),{,hostsFileWriter,.,cleanup,(,),;,hostsFileWriter,=,Null,;,},If,(,cluster,!=,Null,),{,cluster,.,shutdown,(,),;,cluster,=,Null,;,},Val,includeHosts,:,Array,[,Int,,,100,],=,New,String,[,dnAddresses,.,length,-,1,],;,Foreach,(,i,in,1,..,100,By,1,),{,includeHosts,[,i,],=,dnAddresses,[,i,+,1,],;,},},},Class,Program,{,main,(,),{,Out,.,println,(,Hello World,),;,},},<EOF>""", 239))

    def test_float_18(self):
        """test 1234.05"""
        self.assertTrue(TestLexer.test("1234.05", "1234.05,<EOF>", 240))

    def test_underscore_in_octal_1(self):
        """test 012356_1671_1751"""
        self.assertTrue(TestLexer.test(
            "012356_1671_1751", "01235616711751,<EOF>", 241))

    def test_wrong_underscore_in_octal_1(self):
        """test 0123__124"""
        self.assertTrue(TestLexer.test("0123__124", "0123,__124,<EOF>", 242))

    def test_underscore_in_binary_1(self):
        """test 0b1_01_01"""
        self.assertTrue(TestLexer.test("0b1_01_01", "0b10101,<EOF>", 243))

    def test_wrong_underscore_in_binary_1(self):
        """test 0B101__0101"""
        self.assertTrue(TestLexer.test(
            "0B101__0101", "0B101,__0101,<EOF>", 244))

    def test_underscore_in_hex_1(self):
        """test 0xAE15_617A"""
        self.assertTrue(TestLexer.test("0xAE15_617A", "0xAE15617A,<EOF>", 245))

    def test_wrong_underscore_in_hex_1(self):
        """test 0X167A__EEEE"""
        self.assertTrue(TestLexer.test(
            "0X167A__EEEE", "0X167A,__EEEE,<EOF>", 246))

    def test_weird_but_correct_float_1(self):
        """test .e3"""
        self.assertTrue(TestLexer.test(".e3", ".e3,<EOF>", 247))

    def test_legal_escape(self):
        '''test "abc\\h"'''
        self.assertTrue(TestLexer.test(
            '"abc\\h"', 'Illegal Escape In String: abc\h', 248))

    def test_float_19(self):
        '''test 1.2e-023'''
        self.assertTrue(TestLexer.test("1.2e-023", "1.2e-023,<EOF>", 249))

    def test_unclosed_str_1(self):
        '''test """'''
        self.assertTrue(TestLexer.test('"""', ',Unclosed String: ', 250))

    def test_single_quote_in_str_1(self):
        '''test "doesn\'t"'''
        self.assertTrue(TestLexer.test('"doesn\'t"', 'doesn\'t,<EOF>', 251))

    def test_octal_00_1(self):
        """test 00"""
        self.assertTrue(TestLexer.test("00", "00,<EOF>", 252))

    def test_octal_00_2(self):
        """test 00012"""
        self.assertTrue(TestLexer.test("00012", "00,012,<EOF>", 253))

    def test_binary_leading0_1(self):
        """test 0B010101"""
        self.assertTrue(TestLexer.test(
            "0B01010101", "0B0,1010101,<EOF>", 254))

    def test_binary_leading0_2(self):
        """test 0b012"""
        self.assertTrue(TestLexer.test("0b012", "0b0,12,<EOF>", 255))

    def test_binary_leading0_3(self):
        """test 0b01_01_01"""
        self.assertTrue(TestLexer.test("0b01_01_01", "0b0,10101,<EOF>", 256))

    def test_octal_leading0_3(self):
        """test 0057"""
        self.assertTrue(TestLexer.test("0057", "00,57,<EOF>", 257))

    def test_binary_leading0_4(self):
        """test 0b010"""
        self.assertTrue(TestLexer.test("0b010", "0b0,10,<EOF>", 258))

    def test_hex_leading0_1(self):
        """test 0x00AF"""
        self.assertTrue(TestLexer.test("0x00AF", "0x0,0,AF,<EOF>", 259))

    def test_hex_leading0_2(self):
        """test 0x0001"""
        self.assertTrue(TestLexer.test("0x0001", "0x0,00,1,<EOF>", 260))

    # def test_illegal_escape_1(self):
    #     '''test "abc\\"'''
    #     self.assertTrue(TestLexer.test(
    #         '"abc\\"', 'Illegal Escape In String: abc\\"', 262))

    def test_octal_prior_dec(self):
        '''test 001'''
        self.assertTrue(TestLexer.test("001", "00,1,<EOF>", 263))

    def test_float_20(self):
        """test 1.20000e6"""
        self.assertTrue(TestLexer.test("1.20000e6", "1.20000e6,<EOF>", 264))

    def test_array_size_hex(self):
        """test Array[Int, 0x10]"""
        self.assertTrue(TestLexer.test(
            "Array[Int, 0x10]", "Array,[,Int,,,0x10,],<EOF>", 265))

    def test_float_zeros_1(self):
        """test 0.2000000"""
        self.assertTrue(TestLexer.test("0.2000000", "0.2000000,<EOF>", 266))

    def test_float_zeros_2(self):
        """test 3.2000e7"""
        self.assertTrue(TestLexer.test("3.2000e7", "3.2000e7,<EOF>", 267))

    def test_illegal_esc_5(self):
        self.assertTrue(TestLexer.test("\"Dumbledore : '\" Lily? After all this time? \\n \\n \\t \\2 '\" \"",
                        "Illegal Escape In String: Dumbledore : '\" Lily? After all this time? \\n \\n \\t \\2", 268))

    def test_newline_in_str_1(self):
        self.assertTrue(TestLexer.test(
            """\"abc\nabc\"""", "Unclosed String: abc", 269))

    def test_unclosed_string_super(self):
        self.assertTrue(TestLexer.test(
            "\"abc'\"", "Unclosed String: abc'\"", 270))

    def test_str_28(self):
        """New line in string"""
        input = """ "My entire life
            Your career " """
        expect = "Unclosed String: My entire life"
        self.assertTrue(TestLexer.test(input, expect, 261))

    def test_str_raw_1(self):
        input = r""" "Hello \' there" """
        expect = r"""Hello \' there,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 271))

    def test_float_21(self):
        self.assertTrue(TestLexer.test("0.00000000", "0.00000000,<EOF>", 272))

    def test_octal_underscore_1(self):
        self.assertTrue(TestLexer.test("0_4_1", "0,_4_1,<EOF>", 273))

    def test_cmt_in_str_1(self):
        self.assertTrue(TestLexer.test(
            '"Hello ##My## World"', """Hello ##My## World,<EOF>""", 274))

    def test_cmt_in_str_2(self):
        self.assertTrue(TestLexer.test(
            '"Hello World## " ##', 'Hello World## ,Error Token #', 275))

    def test_splash_space_1(self):
        self.assertTrue(TestLexer.test('"Hello\\ World"',
                        'Illegal Escape In String: Hello\\ ', 276))

    def test_array_lit_1(self):
        self.assertTrue(TestLexer.test('Array()', 'Array,(,),<EOF>', 277))

    def test_foreach_stm_1(self):
        input = """
        Foreach (i In 1 .. 100 By 1) {
            Out.println(4);
        }"""
        expect = "Foreach,(,i,In,1,..,100,By,1,),{,Out,.,println,(,4,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 278))
