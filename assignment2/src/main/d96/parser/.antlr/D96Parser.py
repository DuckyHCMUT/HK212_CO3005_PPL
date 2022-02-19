# Generated from d:\HCMUT\Semester 212\Principles of Programming Languages\HK212_CO3005_PPL\assignment2\src\main\d96\parser\D96.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3I")
        buf.write("\u02fc\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\6\2\u0096\n")
        buf.write("\2\r\2\16\2\u0097\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u00a0\n")
        buf.write("\3\3\3\3\3\7\3\u00a4\n\3\f\3\16\3\u00a7\13\3\3\3\3\3\3")
        buf.write("\4\3\4\5\4\u00ad\n\4\3\5\3\5\3\5\3\5\5\5\u00b3\n\5\3\6")
        buf.write("\3\6\3\6\3\6\7\6\u00b9\n\6\f\6\16\6\u00bc\13\6\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\5\b\u00d2\n\b\3\t\3\t\3\t\3\t\7\t\u00d8")
        buf.write("\n\t\f\t\16\t\u00db\13\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\5\13\u00f1\n\13\3\f\3\f\3\f\3\f\5\f\u00f7\n\f\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16\5\16\u0102\n\16")
        buf.write("\3\17\3\17\3\17\5\17\u0107\n\17\3\17\3\17\3\17\5\17\u010c")
        buf.write("\n\17\3\17\3\17\3\20\3\20\3\20\5\20\u0113\n\20\3\20\3")
        buf.write("\20\3\20\5\20\u0118\n\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\5\21\u0121\n\21\3\21\3\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\5\22\u012f\n\22\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u0135\n\23\3\24\3\24\3\24\3\24\7\24\u013b")
        buf.write("\n\24\f\24\16\24\u013e\13\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\5\26\u0154\n\26\3\27\3\27\3\27\3")
        buf.write("\27\7\27\u015a\n\27\f\27\16\27\u015d\13\27\3\27\3\27\3")
        buf.write("\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0173\n\31\3")
        buf.write("\32\3\32\3\32\3\32\5\32\u0179\n\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\5\33\u0181\n\33\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\35\3\35\5\35\u018a\n\35\3\36\3\36\3\36\7\36\u018f\n\36")
        buf.write("\f\36\16\36\u0192\13\36\3\37\3\37\3\37\7\37\u0197\n\37")
        buf.write("\f\37\16\37\u019a\13\37\3\37\3\37\3\37\5\37\u019f\n\37")
        buf.write("\3 \3 \3!\3!\3!\3!\3!\3!\5!\u01a9\n!\3!\3!\3!\5!\u01ae")
        buf.write("\n!\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u01b6\n\"\3\"\3\"\3\"")
        buf.write("\5\"\u01bb\n\"\3#\3#\3#\5#\u01c0\n#\3#\3#\3$\3$\3$\3$")
        buf.write("\3$\3$\5$\u01ca\n$\3$\3$\3%\3%\3%\3%\3%\3%\3%\5%\u01d5")
        buf.write("\n%\3&\3&\3\'\3\'\3\'\3\'\5\'\u01dd\n\'\3\'\3\'\3\'\3")
        buf.write("\'\5\'\u01e3\n\'\7\'\u01e5\n\'\f\'\16\'\u01e8\13\'\3(")
        buf.write("\3(\3(\3)\3)\3)\3*\3*\5*\u01f2\n*\3*\3*\3+\3+\3+\3+\3")
        buf.write("+\3,\3,\3,\3,\3,\3-\3-\5-\u0202\n-\3-\3-\3.\6.\u0207\n")
        buf.write(".\r.\16.\u0208\3/\3/\3/\3/\3/\3/\5/\u0211\n/\3/\3/\3/")
        buf.write("\3/\5/\u0217\n/\3/\3/\7/\u021b\n/\f/\16/\u021e\13/\3\60")
        buf.write("\3\60\3\60\7\60\u0223\n\60\f\60\16\60\u0226\13\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\5\61\u022d\n\61\3\61\3\61\3\62\3")
        buf.write("\62\5\62\u0233\n\62\3\63\3\63\3\63\3\63\3\63\5\63\u023a")
        buf.write("\n\63\3\64\3\64\3\64\3\64\3\64\5\64\u0241\n\64\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\7\65\u0249\n\65\f\65\16\65\u024c")
        buf.write("\13\65\3\66\3\66\3\66\3\66\3\66\3\66\7\66\u0254\n\66\f")
        buf.write("\66\16\66\u0257\13\66\3\67\3\67\3\67\3\67\3\67\3\67\7")
        buf.write("\67\u025f\n\67\f\67\16\67\u0262\13\67\38\38\38\58\u0267")
        buf.write("\n8\39\39\39\59\u026c\n9\3:\3:\3:\3:\3:\6:\u0273\n:\r")
        buf.write(":\16:\u0274\7:\u0277\n:\f:\16:\u027a\13:\3;\3;\3;\3;\3")
        buf.write("<\3<\3<\3<\3<\3<\3<\5<\u0287\n<\7<\u0289\n<\f<\16<\u028c")
        buf.write("\13<\3=\3=\3=\3=\5=\u0292\n=\3=\5=\u0295\n=\3>\3>\3>\3")
        buf.write(">\5>\u029b\n>\3>\3>\3>\5>\u02a0\n>\3?\3?\3?\3?\3?\3?\3")
        buf.write("?\3?\3?\5?\u02ab\n?\3@\3@\3A\3A\3A\3A\3A\3A\3A\3A\3A\3")
        buf.write("A\7A\u02b9\nA\fA\16A\u02bc\13A\3B\3B\3B\3B\5B\u02c2\n")
        buf.write("B\3C\3C\3C\5C\u02c7\nC\3C\3C\3D\3D\3D\3D\5D\u02cf\nD\3")
        buf.write("D\3D\3E\3E\3E\7E\u02d6\nE\fE\16E\u02d9\13E\3F\3F\3G\3")
        buf.write("G\5G\u02df\nG\3H\3H\3H\5H\u02e4\nH\3H\3H\3I\3I\3I\3I\3")
        buf.write("I\7I\u02ed\nI\fI\16I\u02f0\13I\3I\3I\3J\3J\3J\7J\u02f7")
        buf.write("\nJ\fJ\16J\u02fa\13J\3J\2\nL\\hjlrv\u0080K\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086")
        buf.write("\u0088\u008a\u008c\u008e\u0090\u0092\2\f\3\2\r\16\3\2")
        buf.write("CD\b\2\22\22\27\27\34\34  %%CC\4\2%%CC\3\2>?\4\2\67\67")
        buf.write("9=\3\2\65\66\3\2/\60\3\2\61\63\4\2\3\5\n\13\2\u0311\2")
        buf.write("\u0095\3\2\2\2\4\u009b\3\2\2\2\6\u00ac\3\2\2\2\b\u00b2")
        buf.write("\3\2\2\2\n\u00b4\3\2\2\2\f\u00c1\3\2\2\2\16\u00d1\3\2")
        buf.write("\2\2\20\u00d3\3\2\2\2\22\u00e0\3\2\2\2\24\u00f0\3\2\2")
        buf.write("\2\26\u00f2\3\2\2\2\30\u00fc\3\2\2\2\32\u0101\3\2\2\2")
        buf.write("\34\u0103\3\2\2\2\36\u010f\3\2\2\2 \u011b\3\2\2\2\"\u012e")
        buf.write("\3\2\2\2$\u0134\3\2\2\2&\u0136\3\2\2\2(\u0143\3\2\2\2")
        buf.write("*\u0153\3\2\2\2,\u0155\3\2\2\2.\u0162\3\2\2\2\60\u0172")
        buf.write("\3\2\2\2\62\u0174\3\2\2\2\64\u0180\3\2\2\2\66\u0182\3")
        buf.write("\2\2\28\u0187\3\2\2\2:\u018b\3\2\2\2<\u0193\3\2\2\2>\u01a0")
        buf.write("\3\2\2\2@\u01a2\3\2\2\2B\u01af\3\2\2\2D\u01bc\3\2\2\2")
        buf.write("F\u01c3\3\2\2\2H\u01cd\3\2\2\2J\u01d6\3\2\2\2L\u01dc\3")
        buf.write("\2\2\2N\u01e9\3\2\2\2P\u01ec\3\2\2\2R\u01ef\3\2\2\2T\u01f5")
        buf.write("\3\2\2\2V\u01fa\3\2\2\2X\u01ff\3\2\2\2Z\u0206\3\2\2\2")
        buf.write("\\\u0210\3\2\2\2^\u0224\3\2\2\2`\u0229\3\2\2\2b\u0232")
        buf.write("\3\2\2\2d\u0239\3\2\2\2f\u0240\3\2\2\2h\u0242\3\2\2\2")
        buf.write("j\u024d\3\2\2\2l\u0258\3\2\2\2n\u0266\3\2\2\2p\u026b\3")
        buf.write("\2\2\2r\u026d\3\2\2\2t\u027b\3\2\2\2v\u027f\3\2\2\2x\u0294")
        buf.write("\3\2\2\2z\u029f\3\2\2\2|\u02aa\3\2\2\2~\u02ac\3\2\2\2")
        buf.write("\u0080\u02ae\3\2\2\2\u0082\u02bd\3\2\2\2\u0084\u02c3\3")
        buf.write("\2\2\2\u0086\u02ca\3\2\2\2\u0088\u02d2\3\2\2\2\u008a\u02da")
        buf.write("\3\2\2\2\u008c\u02de\3\2\2\2\u008e\u02e0\3\2\2\2\u0090")
        buf.write("\u02e7\3\2\2\2\u0092\u02f3\3\2\2\2\u0094\u0096\5\4\3\2")
        buf.write("\u0095\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0095\3")
        buf.write("\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a")
        buf.write("\7\2\2\3\u009a\3\3\2\2\2\u009b\u009c\7\30\2\2\u009c\u009f")
        buf.write("\7C\2\2\u009d\u009e\7B\2\2\u009e\u00a0\7C\2\2\u009f\u009d")
        buf.write("\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1")
        buf.write("\u00a5\7*\2\2\u00a2\u00a4\5\6\4\2\u00a3\u00a2\3\2\2\2")
        buf.write("\u00a4\u00a7\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3")
        buf.write("\2\2\2\u00a6\u00a8\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00a9")
        buf.write("\7+\2\2\u00a9\5\3\2\2\2\u00aa\u00ad\5\b\5\2\u00ab\u00ad")
        buf.write("\5\32\16\2\u00ac\u00aa\3\2\2\2\u00ac\u00ab\3\2\2\2\u00ad")
        buf.write("\7\3\2\2\2\u00ae\u00b3\5\n\6\2\u00af\u00b3\5\f\7\2\u00b0")
        buf.write("\u00b3\5\20\t\2\u00b1\u00b3\5\22\n\2\u00b2\u00ae\3\2\2")
        buf.write("\2\u00b2\u00af\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b1")
        buf.write("\3\2\2\2\u00b3\t\3\2\2\2\u00b4\u00b5\t\2\2\2\u00b5\u00ba")
        buf.write("\5\30\r\2\u00b6\u00b7\7-\2\2\u00b7\u00b9\5\30\r\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2")
        buf.write("\u00ba\u00bb\3\2\2\2\u00bb\u00bd\3\2\2\2\u00bc\u00ba\3")
        buf.write("\2\2\2\u00bd\u00be\7B\2\2\u00be\u00bf\5> \2\u00bf\u00c0")
        buf.write("\7,\2\2\u00c0\13\3\2\2\2\u00c1\u00c2\t\2\2\2\u00c2\u00c3")
        buf.write("\5\30\r\2\u00c3\u00c4\5\16\b\2\u00c4\u00c5\5b\62\2\u00c5")
        buf.write("\u00c6\7,\2\2\u00c6\r\3\2\2\2\u00c7\u00c8\7-\2\2\u00c8")
        buf.write("\u00c9\5\30\r\2\u00c9\u00ca\5\16\b\2\u00ca\u00cb\5b\62")
        buf.write("\2\u00cb\u00cc\7-\2\2\u00cc\u00d2\3\2\2\2\u00cd\u00ce")
        buf.write("\7B\2\2\u00ce\u00cf\5> \2\u00cf\u00d0\78\2\2\u00d0\u00d2")
        buf.write("\3\2\2\2\u00d1\u00c7\3\2\2\2\u00d1\u00cd\3\2\2\2\u00d2")
        buf.write("\17\3\2\2\2\u00d3\u00d4\t\2\2\2\u00d4\u00d9\5\30\r\2\u00d5")
        buf.write("\u00d6\7-\2\2\u00d6\u00d8\5\30\r\2\u00d7\u00d5\3\2\2\2")
        buf.write("\u00d8\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3")
        buf.write("\2\2\2\u00da\u00dc\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00dd")
        buf.write("\7B\2\2\u00dd\u00de\5\26\f\2\u00de\u00df\7,\2\2\u00df")
        buf.write("\21\3\2\2\2\u00e0\u00e1\t\2\2\2\u00e1\u00e2\5\30\r\2\u00e2")
        buf.write("\u00e3\5\24\13\2\u00e3\u00e4\5\64\33\2\u00e4\u00e5\7,")
        buf.write("\2\2\u00e5\23\3\2\2\2\u00e6\u00e7\7-\2\2\u00e7\u00e8\5")
        buf.write("\30\r\2\u00e8\u00e9\5\24\13\2\u00e9\u00ea\5\64\33\2\u00ea")
        buf.write("\u00eb\7-\2\2\u00eb\u00f1\3\2\2\2\u00ec\u00ed\7B\2\2\u00ed")
        buf.write("\u00ee\5\26\f\2\u00ee\u00ef\78\2\2\u00ef\u00f1\3\2\2\2")
        buf.write("\u00f0\u00e6\3\2\2\2\u00f0\u00ec\3\2\2\2\u00f1\25\3\2")
        buf.write("\2\2\u00f2\u00f3\7\37\2\2\u00f3\u00f6\7(\2\2\u00f4\u00f7")
        buf.write("\5> \2\u00f5\u00f7\5\26\f\2\u00f6\u00f4\3\2\2\2\u00f6")
        buf.write("\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\7-\2\2")
        buf.write("\u00f9\u00fa\7\4\2\2\u00fa\u00fb\7)\2\2\u00fb\27\3\2\2")
        buf.write("\2\u00fc\u00fd\t\3\2\2\u00fd\31\3\2\2\2\u00fe\u0102\5")
        buf.write("\34\17\2\u00ff\u0102\5\36\20\2\u0100\u0102\5 \21\2\u0101")
        buf.write("\u00fe\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0100\3\2\2\2")
        buf.write("\u0102\33\3\2\2\2\u0103\u0104\5\30\r\2\u0104\u0106\7&")
        buf.write("\2\2\u0105\u0107\5:\36\2\u0106\u0105\3\2\2\2\u0106\u0107")
        buf.write("\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0109\7\'\2\2\u0109")
        buf.write("\u010b\7*\2\2\u010a\u010c\5Z.\2\u010b\u010a\3\2\2\2\u010b")
        buf.write("\u010c\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010e\7+\2\2")
        buf.write("\u010e\35\3\2\2\2\u010f\u0110\7\24\2\2\u0110\u0112\7&")
        buf.write("\2\2\u0111\u0113\5:\36\2\u0112\u0111\3\2\2\2\u0112\u0113")
        buf.write("\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0115\7\'\2\2\u0115")
        buf.write("\u0117\7*\2\2\u0116\u0118\5Z.\2\u0117\u0116\3\2\2\2\u0117")
        buf.write("\u0118\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011a\7+\2\2")
        buf.write("\u011a\37\3\2\2\2\u011b\u011c\7\31\2\2\u011c\u011d\7&")
        buf.write("\2\2\u011d\u011e\7\'\2\2\u011e\u0120\7*\2\2\u011f\u0121")
        buf.write("\5Z.\2\u0120\u011f\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0122")
        buf.write("\3\2\2\2\u0122\u0123\7+\2\2\u0123!\3\2\2\2\u0124\u012f")
        buf.write("\5$\23\2\u0125\u012f\5\66\34\2\u0126\u012f\5@!\2\u0127")
        buf.write("\u012f\5F$\2\u0128\u012f\5N(\2\u0129\u012f\5P)\2\u012a")
        buf.write("\u012f\5R*\2\u012b\u012f\5T+\2\u012c\u012f\5V,\2\u012d")
        buf.write("\u012f\5X-\2\u012e\u0124\3\2\2\2\u012e\u0125\3\2\2\2\u012e")
        buf.write("\u0126\3\2\2\2\u012e\u0127\3\2\2\2\u012e\u0128\3\2\2\2")
        buf.write("\u012e\u0129\3\2\2\2\u012e\u012a\3\2\2\2\u012e\u012b\3")
        buf.write("\2\2\2\u012e\u012c\3\2\2\2\u012e\u012d\3\2\2\2\u012f#")
        buf.write("\3\2\2\2\u0130\u0135\5&\24\2\u0131\u0135\5(\25\2\u0132")
        buf.write("\u0135\5,\27\2\u0133\u0135\5.\30\2\u0134\u0130\3\2\2\2")
        buf.write("\u0134\u0131\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0133\3")
        buf.write("\2\2\2\u0135%\3\2\2\2\u0136\u0137\t\2\2\2\u0137\u013c")
        buf.write("\7C\2\2\u0138\u0139\7-\2\2\u0139\u013b\7C\2\2\u013a\u0138")
        buf.write("\3\2\2\2\u013b\u013e\3\2\2\2\u013c\u013a\3\2\2\2\u013c")
        buf.write("\u013d\3\2\2\2\u013d\u013f\3\2\2\2\u013e\u013c\3\2\2\2")
        buf.write("\u013f\u0140\7B\2\2\u0140\u0141\5> \2\u0141\u0142\7,\2")
        buf.write("\2\u0142\'\3\2\2\2\u0143\u0144\t\2\2\2\u0144\u0145\7C")
        buf.write("\2\2\u0145\u0146\5*\26\2\u0146\u0147\5b\62\2\u0147\u0148")
        buf.write("\7,\2\2\u0148)\3\2\2\2\u0149\u014a\7-\2\2\u014a\u014b")
        buf.write("\7C\2\2\u014b\u014c\5*\26\2\u014c\u014d\5b\62\2\u014d")
        buf.write("\u014e\7-\2\2\u014e\u0154\3\2\2\2\u014f\u0150\7B\2\2\u0150")
        buf.write("\u0151\5> \2\u0151\u0152\78\2\2\u0152\u0154\3\2\2\2\u0153")
        buf.write("\u0149\3\2\2\2\u0153\u014f\3\2\2\2\u0154+\3\2\2\2\u0155")
        buf.write("\u0156\t\2\2\2\u0156\u015b\7C\2\2\u0157\u0158\7-\2\2\u0158")
        buf.write("\u015a\7C\2\2\u0159\u0157\3\2\2\2\u015a\u015d\3\2\2\2")
        buf.write("\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015e\3")
        buf.write("\2\2\2\u015d\u015b\3\2\2\2\u015e\u015f\7B\2\2\u015f\u0160")
        buf.write("\5\62\32\2\u0160\u0161\7,\2\2\u0161-\3\2\2\2\u0162\u0163")
        buf.write("\t\2\2\2\u0163\u0164\7C\2\2\u0164\u0165\5\60\31\2\u0165")
        buf.write("\u0166\5\64\33\2\u0166\u0167\7,\2\2\u0167/\3\2\2\2\u0168")
        buf.write("\u0169\7-\2\2\u0169\u016a\7C\2\2\u016a\u016b\5\60\31\2")
        buf.write("\u016b\u016c\5\64\33\2\u016c\u016d\7-\2\2\u016d\u0173")
        buf.write("\3\2\2\2\u016e\u016f\7B\2\2\u016f\u0170\5\62\32\2\u0170")
        buf.write("\u0171\78\2\2\u0171\u0173\3\2\2\2\u0172\u0168\3\2\2\2")
        buf.write("\u0172\u016e\3\2\2\2\u0173\61\3\2\2\2\u0174\u0175\7\37")
        buf.write("\2\2\u0175\u0178\7(\2\2\u0176\u0179\5> \2\u0177\u0179")
        buf.write("\5\62\32\2\u0178\u0176\3\2\2\2\u0178\u0177\3\2\2\2\u0179")
        buf.write("\u017a\3\2\2\2\u017a\u017b\7-\2\2\u017b\u017c\7\4\2\2")
        buf.write("\u017c\u017d\7)\2\2\u017d\63\3\2\2\2\u017e\u0181\5\u008c")
        buf.write("G\2\u017f\u0181\5\u0086D\2\u0180\u017e\3\2\2\2\u0180\u017f")
        buf.write("\3\2\2\2\u0181\65\3\2\2\2\u0182\u0183\58\35\2\u0183\u0184")
        buf.write("\78\2\2\u0184\u0185\5b\62\2\u0185\u0186\7,\2\2\u0186\67")
        buf.write("\3\2\2\2\u0187\u0189\5L\'\2\u0188\u018a\5~@\2\u0189\u0188")
        buf.write("\3\2\2\2\u0189\u018a\3\2\2\2\u018a9\3\2\2\2\u018b\u0190")
        buf.write("\5<\37\2\u018c\u018d\7,\2\2\u018d\u018f\5<\37\2\u018e")
        buf.write("\u018c\3\2\2\2\u018f\u0192\3\2\2\2\u0190\u018e\3\2\2\2")
        buf.write("\u0190\u0191\3\2\2\2\u0191;\3\2\2\2\u0192\u0190\3\2\2")
        buf.write("\2\u0193\u0198\7C\2\2\u0194\u0195\7-\2\2\u0195\u0197\7")
        buf.write("C\2\2\u0196\u0194\3\2\2\2\u0197\u019a\3\2\2\2\u0198\u0196")
        buf.write("\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019b\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019b\u019e\7B\2\2\u019c\u019f\5> \2\u019d")
        buf.write("\u019f\5\62\32\2\u019e\u019c\3\2\2\2\u019e\u019d\3\2\2")
        buf.write("\2\u019f=\3\2\2\2\u01a0\u01a1\t\4\2\2\u01a1?\3\2\2\2\u01a2")
        buf.write("\u01a3\7\32\2\2\u01a3\u01a4\7&\2\2\u01a4\u01a5\5b\62\2")
        buf.write("\u01a5\u01a6\7\'\2\2\u01a6\u01a8\7*\2\2\u01a7\u01a9\5")
        buf.write("Z.\2\u01a8\u01a7\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01aa")
        buf.write("\3\2\2\2\u01aa\u01ad\7+\2\2\u01ab\u01ae\5B\"\2\u01ac\u01ae")
        buf.write("\5D#\2\u01ad\u01ab\3\2\2\2\u01ad\u01ac\3\2\2\2\u01ad\u01ae")
        buf.write("\3\2\2\2\u01aeA\3\2\2\2\u01af\u01b0\7\36\2\2\u01b0\u01b1")
        buf.write("\7&\2\2\u01b1\u01b2\5b\62\2\u01b2\u01b3\7\'\2\2\u01b3")
        buf.write("\u01b5\7*\2\2\u01b4\u01b6\5Z.\2\u01b5\u01b4\3\2\2\2\u01b5")
        buf.write("\u01b6\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01ba\7+\2\2")
        buf.write("\u01b8\u01bb\5B\"\2\u01b9\u01bb\5D#\2\u01ba\u01b8\3\2")
        buf.write("\2\2\u01ba\u01b9\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bbC\3")
        buf.write("\2\2\2\u01bc\u01bd\7\"\2\2\u01bd\u01bf\7*\2\2\u01be\u01c0")
        buf.write("\5Z.\2\u01bf\u01be\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1")
        buf.write("\3\2\2\2\u01c1\u01c2\7+\2\2\u01c2E\3\2\2\2\u01c3\u01c4")
        buf.write("\7\21\2\2\u01c4\u01c5\7&\2\2\u01c5\u01c6\5H%\2\u01c6\u01c7")
        buf.write("\7\'\2\2\u01c7\u01c9\7*\2\2\u01c8\u01ca\5Z.\2\u01c9\u01c8")
        buf.write("\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb")
        buf.write("\u01cc\7+\2\2\u01ccG\3\2\2\2\u01cd\u01ce\5L\'\2\u01ce")
        buf.write("\u01cf\7#\2\2\u01cf\u01d0\5J&\2\u01d0\u01d1\7.\2\2\u01d1")
        buf.write("\u01d4\5J&\2\u01d2\u01d3\7!\2\2\u01d3\u01d5\5J&\2\u01d4")
        buf.write("\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5I\3\2\2\2\u01d6")
        buf.write("\u01d7\5b\62\2\u01d7K\3\2\2\2\u01d8\u01d9\b\'\1\2\u01d9")
        buf.write("\u01dd\5\u0082B\2\u01da\u01dd\7%\2\2\u01db\u01dd\7C\2")
        buf.write("\2\u01dc\u01d8\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01db")
        buf.write("\3\2\2\2\u01dd\u01e6\3\2\2\2\u01de\u01df\f\6\2\2\u01df")
        buf.write("\u01e2\7@\2\2\u01e0\u01e3\7C\2\2\u01e1\u01e3\5`\61\2\u01e2")
        buf.write("\u01e0\3\2\2\2\u01e2\u01e1\3\2\2\2\u01e3\u01e5\3\2\2\2")
        buf.write("\u01e4\u01de\3\2\2\2\u01e5\u01e8\3\2\2\2\u01e6\u01e4\3")
        buf.write("\2\2\2\u01e6\u01e7\3\2\2\2\u01e7M\3\2\2\2\u01e8\u01e6")
        buf.write("\3\2\2\2\u01e9\u01ea\7\20\2\2\u01ea\u01eb\7,\2\2\u01eb")
        buf.write("O\3\2\2\2\u01ec\u01ed\7\25\2\2\u01ed\u01ee\7,\2\2\u01ee")
        buf.write("Q\3\2\2\2\u01ef\u01f1\7$\2\2\u01f0\u01f2\5b\62\2\u01f1")
        buf.write("\u01f0\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\3\2\2\2")
        buf.write("\u01f3\u01f4\7,\2\2\u01f4S\3\2\2\2\u01f5\u01f6\5\\/\2")
        buf.write("\u01f6\u01f7\7@\2\2\u01f7\u01f8\5`\61\2\u01f8\u01f9\7")
        buf.write(",\2\2\u01f9U\3\2\2\2\u01fa\u01fb\t\5\2\2\u01fb\u01fc\7")
        buf.write("A\2\2\u01fc\u01fd\5\u0084C\2\u01fd\u01fe\7,\2\2\u01fe")
        buf.write("W\3\2\2\2\u01ff\u0201\7*\2\2\u0200\u0202\5Z.\2\u0201\u0200")
        buf.write("\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0203\3\2\2\2\u0203")
        buf.write("\u0204\7+\2\2\u0204Y\3\2\2\2\u0205\u0207\5\"\22\2\u0206")
        buf.write("\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u0206\3\2\2\2")
        buf.write("\u0208\u0209\3\2\2\2\u0209[\3\2\2\2\u020a\u020b\b/\1\2")
        buf.write("\u020b\u020c\7\35\2\2\u020c\u0211\5`\61\2\u020d\u0211")
        buf.write("\5\u0082B\2\u020e\u0211\7%\2\2\u020f\u0211\7C\2\2\u0210")
        buf.write("\u020a\3\2\2\2\u0210\u020d\3\2\2\2\u0210\u020e\3\2\2\2")
        buf.write("\u0210\u020f\3\2\2\2\u0211\u021c\3\2\2\2\u0212\u0213\f")
        buf.write("\b\2\2\u0213\u0216\7@\2\2\u0214\u0217\7C\2\2\u0215\u0217")
        buf.write("\5`\61\2\u0216\u0214\3\2\2\2\u0216\u0215\3\2\2\2\u0217")
        buf.write("\u021b\3\2\2\2\u0218\u0219\f\6\2\2\u0219\u021b\5~@\2\u021a")
        buf.write("\u0212\3\2\2\2\u021a\u0218\3\2\2\2\u021b\u021e\3\2\2\2")
        buf.write("\u021c\u021a\3\2\2\2\u021c\u021d\3\2\2\2\u021d]\3\2\2")
        buf.write("\2\u021e\u021c\3\2\2\2\u021f\u0220\5b\62\2\u0220\u0221")
        buf.write("\7-\2\2\u0221\u0223\3\2\2\2\u0222\u021f\3\2\2\2\u0223")
        buf.write("\u0226\3\2\2\2\u0224\u0222\3\2\2\2\u0224\u0225\3\2\2\2")
        buf.write("\u0225\u0227\3\2\2\2\u0226\u0224\3\2\2\2\u0227\u0228\5")
        buf.write("b\62\2\u0228_\3\2\2\2\u0229\u022a\7C\2\2\u022a\u022c\7")
        buf.write("&\2\2\u022b\u022d\5\u0088E\2\u022c\u022b\3\2\2\2\u022c")
        buf.write("\u022d\3\2\2\2\u022d\u022e\3\2\2\2\u022e\u022f\7\'\2\2")
        buf.write("\u022fa\3\2\2\2\u0230\u0233\5d\63\2\u0231\u0233\5\u0086")
        buf.write("D\2\u0232\u0230\3\2\2\2\u0232\u0231\3\2\2\2\u0233c\3\2")
        buf.write("\2\2\u0234\u0235\5f\64\2\u0235\u0236\t\6\2\2\u0236\u0237")
        buf.write("\5f\64\2\u0237\u023a\3\2\2\2\u0238\u023a\5f\64\2\u0239")
        buf.write("\u0234\3\2\2\2\u0239\u0238\3\2\2\2\u023ae\3\2\2\2\u023b")
        buf.write("\u023c\5h\65\2\u023c\u023d\t\7\2\2\u023d\u023e\5h\65\2")
        buf.write("\u023e\u0241\3\2\2\2\u023f\u0241\5h\65\2\u0240\u023b\3")
        buf.write("\2\2\2\u0240\u023f\3\2\2\2\u0241g\3\2\2\2\u0242\u0243")
        buf.write("\b\65\1\2\u0243\u0244\5j\66\2\u0244\u024a\3\2\2\2\u0245")
        buf.write("\u0246\f\4\2\2\u0246\u0247\t\b\2\2\u0247\u0249\5j\66\2")
        buf.write("\u0248\u0245\3\2\2\2\u0249\u024c\3\2\2\2\u024a\u0248\3")
        buf.write("\2\2\2\u024a\u024b\3\2\2\2\u024bi\3\2\2\2\u024c\u024a")
        buf.write("\3\2\2\2\u024d\u024e\b\66\1\2\u024e\u024f\5l\67\2\u024f")
        buf.write("\u0255\3\2\2\2\u0250\u0251\f\4\2\2\u0251\u0252\t\t\2\2")
        buf.write("\u0252\u0254\5l\67\2\u0253\u0250\3\2\2\2\u0254\u0257\3")
        buf.write("\2\2\2\u0255\u0253\3\2\2\2\u0255\u0256\3\2\2\2\u0256k")
        buf.write("\3\2\2\2\u0257\u0255\3\2\2\2\u0258\u0259\b\67\1\2\u0259")
        buf.write("\u025a\5n8\2\u025a\u0260\3\2\2\2\u025b\u025c\f\4\2\2\u025c")
        buf.write("\u025d\t\n\2\2\u025d\u025f\5n8\2\u025e\u025b\3\2\2\2\u025f")
        buf.write("\u0262\3\2\2\2\u0260\u025e\3\2\2\2\u0260\u0261\3\2\2\2")
        buf.write("\u0261m\3\2\2\2\u0262\u0260\3\2\2\2\u0263\u0264\7\64\2")
        buf.write("\2\u0264\u0267\5n8\2\u0265\u0267\5p9\2\u0266\u0263\3\2")
        buf.write("\2\2\u0266\u0265\3\2\2\2\u0267o\3\2\2\2\u0268\u0269\7")
        buf.write("\60\2\2\u0269\u026c\5p9\2\u026a\u026c\5r:\2\u026b\u0268")
        buf.write("\3\2\2\2\u026b\u026a\3\2\2\2\u026cq\3\2\2\2\u026d\u026e")
        buf.write("\b:\1\2\u026e\u026f\5v<\2\u026f\u0278\3\2\2\2\u0270\u0272")
        buf.write("\f\4\2\2\u0271\u0273\5t;\2\u0272\u0271\3\2\2\2\u0273\u0274")
        buf.write("\3\2\2\2\u0274\u0272\3\2\2\2\u0274\u0275\3\2\2\2\u0275")
        buf.write("\u0277\3\2\2\2\u0276\u0270\3\2\2\2\u0277\u027a\3\2\2\2")
        buf.write("\u0278\u0276\3\2\2\2\u0278\u0279\3\2\2\2\u0279s\3\2\2")
        buf.write("\2\u027a\u0278\3\2\2\2\u027b\u027c\7(\2\2\u027c\u027d")
        buf.write("\5b\62\2\u027d\u027e\7)\2\2\u027eu\3\2\2\2\u027f\u0280")
        buf.write("\b<\1\2\u0280\u0281\5x=\2\u0281\u028a\3\2\2\2\u0282\u0283")
        buf.write("\f\4\2\2\u0283\u0286\7@\2\2\u0284\u0287\7C\2\2\u0285\u0287")
        buf.write("\5`\61\2\u0286\u0284\3\2\2\2\u0286\u0285\3\2\2\2\u0287")
        buf.write("\u0289\3\2\2\2\u0288\u0282\3\2\2\2\u0289\u028c\3\2\2\2")
        buf.write("\u028a\u0288\3\2\2\2\u028a\u028b\3\2\2\2\u028bw\3\2\2")
        buf.write("\2\u028c\u028a\3\2\2\2\u028d\u028e\t\5\2\2\u028e\u0291")
        buf.write("\7A\2\2\u028f\u0292\5\u0084C\2\u0290\u0292\7D\2\2\u0291")
        buf.write("\u028f\3\2\2\2\u0291\u0290\3\2\2\2\u0292\u0295\3\2\2\2")
        buf.write("\u0293\u0295\5z>\2\u0294\u028d\3\2\2\2\u0294\u0293\3\2")
        buf.write("\2\2\u0295y\3\2\2\2\u0296\u0297\7\35\2\2\u0297\u0298\5")
        buf.write("|?\2\u0298\u029a\7&\2\2\u0299\u029b\5\u0088E\2\u029a\u0299")
        buf.write("\3\2\2\2\u029a\u029b\3\2\2\2\u029b\u029c\3\2\2\2\u029c")
        buf.write("\u029d\7\'\2\2\u029d\u02a0\3\2\2\2\u029e\u02a0\5|?\2\u029f")
        buf.write("\u0296\3\2\2\2\u029f\u029e\3\2\2\2\u02a0{\3\2\2\2\u02a1")
        buf.write("\u02ab\5\u008aF\2\u02a2\u02ab\7%\2\2\u02a3\u02ab\7C\2")
        buf.write("\2\u02a4\u02a5\7&\2\2\u02a5\u02a6\5d\63\2\u02a6\u02a7")
        buf.write("\7\'\2\2\u02a7\u02ab\3\2\2\2\u02a8\u02ab\7\23\2\2\u02a9")
        buf.write("\u02ab\5\u008cG\2\u02aa\u02a1\3\2\2\2\u02aa\u02a2\3\2")
        buf.write("\2\2\u02aa\u02a3\3\2\2\2\u02aa\u02a4\3\2\2\2\u02aa\u02a8")
        buf.write("\3\2\2\2\u02aa\u02a9\3\2\2\2\u02ab}\3\2\2\2\u02ac\u02ad")
        buf.write("\5\u0080A\2\u02ad\177\3\2\2\2\u02ae\u02af\bA\1\2\u02af")
        buf.write("\u02b0\7(\2\2\u02b0\u02b1\5b\62\2\u02b1\u02b2\7)\2\2\u02b2")
        buf.write("\u02ba\3\2\2\2\u02b3\u02b4\f\4\2\2\u02b4\u02b5\7(\2\2")
        buf.write("\u02b5\u02b6\5b\62\2\u02b6\u02b7\7)\2\2\u02b7\u02b9\3")
        buf.write("\2\2\2\u02b8\u02b3\3\2\2\2\u02b9\u02bc\3\2\2\2\u02ba\u02b8")
        buf.write("\3\2\2\2\u02ba\u02bb\3\2\2\2\u02bb\u0081\3\2\2\2\u02bc")
        buf.write("\u02ba\3\2\2\2\u02bd\u02be\t\5\2\2\u02be\u02c1\7A\2\2")
        buf.write("\u02bf\u02c2\7D\2\2\u02c0\u02c2\5\u0084C\2\u02c1\u02bf")
        buf.write("\3\2\2\2\u02c1\u02c0\3\2\2\2\u02c2\u0083\3\2\2\2\u02c3")
        buf.write("\u02c4\7D\2\2\u02c4\u02c6\7&\2\2\u02c5\u02c7\5\u0088E")
        buf.write("\2\u02c6\u02c5\3\2\2\2\u02c6\u02c7\3\2\2\2\u02c7\u02c8")
        buf.write("\3\2\2\2\u02c8\u02c9\7\'\2\2\u02c9\u0085\3\2\2\2\u02ca")
        buf.write("\u02cb\7\35\2\2\u02cb\u02cc\7C\2\2\u02cc\u02ce\7&\2\2")
        buf.write("\u02cd\u02cf\5\u0088E\2\u02ce\u02cd\3\2\2\2\u02ce\u02cf")
        buf.write("\3\2\2\2\u02cf\u02d0\3\2\2\2\u02d0\u02d1\7\'\2\2\u02d1")
        buf.write("\u0087\3\2\2\2\u02d2\u02d7\5d\63\2\u02d3\u02d4\7-\2\2")
        buf.write("\u02d4\u02d6\5d\63\2\u02d5\u02d3\3\2\2\2\u02d6\u02d9\3")
        buf.write("\2\2\2\u02d7\u02d5\3\2\2\2\u02d7\u02d8\3\2\2\2\u02d8\u0089")
        buf.write("\3\2\2\2\u02d9\u02d7\3\2\2\2\u02da\u02db\t\13\2\2\u02db")
        buf.write("\u008b\3\2\2\2\u02dc\u02df\5\u008eH\2\u02dd\u02df\5\u0090")
        buf.write("I\2\u02de\u02dc\3\2\2\2\u02de\u02dd\3\2\2\2\u02df\u008d")
        buf.write("\3\2\2\2\u02e0\u02e1\7\37\2\2\u02e1\u02e3\7&\2\2\u02e2")
        buf.write("\u02e4\5\u0092J\2\u02e3\u02e2\3\2\2\2\u02e3\u02e4\3\2")
        buf.write("\2\2\u02e4\u02e5\3\2\2\2\u02e5\u02e6\7\'\2\2\u02e6\u008f")
        buf.write("\3\2\2\2\u02e7\u02e8\7\37\2\2\u02e8\u02e9\7&\2\2\u02e9")
        buf.write("\u02ee\5\u008eH\2\u02ea\u02eb\7-\2\2\u02eb\u02ed\5\u008e")
        buf.write("H\2\u02ec\u02ea\3\2\2\2\u02ed\u02f0\3\2\2\2\u02ee\u02ec")
        buf.write("\3\2\2\2\u02ee\u02ef\3\2\2\2\u02ef\u02f1\3\2\2\2\u02f0")
        buf.write("\u02ee\3\2\2\2\u02f1\u02f2\7\'\2\2\u02f2\u0091\3\2\2\2")
        buf.write("\u02f3\u02f8\5b\62\2\u02f4\u02f5\7-\2\2\u02f5\u02f7\5")
        buf.write("b\62\2\u02f6\u02f4\3\2\2\2\u02f7\u02fa\3\2\2\2\u02f8\u02f6")
        buf.write("\3\2\2\2\u02f8\u02f9\3\2\2\2\u02f9\u0093\3\2\2\2\u02fa")
        buf.write("\u02f8\3\2\2\2K\u0097\u009f\u00a5\u00ac\u00b2\u00ba\u00d1")
        buf.write("\u00d9\u00f0\u00f6\u0101\u0106\u010b\u0112\u0117\u0120")
        buf.write("\u012e\u0134\u013c\u0153\u015b\u0172\u0178\u0180\u0189")
        buf.write("\u0190\u0198\u019e\u01a8\u01ad\u01b5\u01ba\u01bf\u01c9")
        buf.write("\u01d4\u01dc\u01e2\u01e6\u01f1\u0201\u0208\u0210\u0216")
        buf.write("\u021a\u021c\u0224\u022c\u0232\u0239\u0240\u024a\u0255")
        buf.write("\u0260\u0266\u026b\u0274\u0278\u0286\u028a\u0291\u0294")
        buf.write("\u029a\u029f\u02aa\u02ba\u02c1\u02c6\u02ce\u02d7\u02de")
        buf.write("\u02e3\u02ee\u02f8")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'Val'", "'Var'", 
                     "'$'", "'Break'", "'Foreach'", "'Int'", "'Null'", "'Constructor'", 
                     "'Continue'", "'True'", "'Float'", "'Class'", "'Destructor'", 
                     "'If'", "'False'", "'Boolean'", "'New'", "'Elseif'", 
                     "'Array'", "'String'", "'By'", "'Else'", "'In'", "'Return'", 
                     "'Self'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "';'", "','", "'..'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'==.'", "'+.'", "'.'", "'::'", 
                     "':'" ]

    symbolicNames = [ "<INVALID>", "LITERAL_BOOLEAN", "LITERAL_INT", "LITERAL_ZERO", 
                      "LITERAL_INT_DEC", "LITERAL_INT_HEX", "LITERAL_INT_OCT", 
                      "LITERAL_INT_BIN", "LITERAL_FLOAT", "LITERAL_STRING", 
                      "DOUBLE_QUOTE", "VAL", "VAR", "STATIC", "BREAK", "FOREACH", 
                      "INT", "NULL", "CONSTRUCTOR", "CONTINUE", "TRUE", 
                      "FLOAT", "CLASS", "DESTRUCTOR", "IF", "FALSE", "BOOLEAN", 
                      "NEW", "ELSEIF", "ARRAY", "STRING", "BY", "ELSE", 
                      "IN", "RETURN", "SELF", "LB", "RB", "LS", "RS", "LP", 
                      "RP", "SEMI", "COMMA", "DOTDOT", "ADD", "SUBTRACT", 
                      "MULTIPLY", "DIVIDE", "MODULO", "NOT", "AND", "OR", 
                      "EQUAL", "ASSIGN", "NOT_EQUAL", "LESS_THAN", "LEQ", 
                      "GREATER_THAN", "GEQ", "EQUAL_STRING", "STRING_CONCAT", 
                      "DOT", "DOUBLE_COLON", "COLON", "ID", "DOLLAR_ID", 
                      "BLOCK_COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_class_body = 2
    RULE_class_attr = 3
    RULE_attr_no_value = 4
    RULE_attr_with_value = 5
    RULE_attr_pair = 6
    RULE_attr_array_no_value = 7
    RULE_attr_array_with_value = 8
    RULE_attr_array_pair = 9
    RULE_attr_array_decl_tail = 10
    RULE_any_id = 11
    RULE_class_method = 12
    RULE_normal_method = 13
    RULE_constructor = 14
    RULE_destructor = 15
    RULE_stmt = 16
    RULE_var_decl = 17
    RULE_var_no_value = 18
    RULE_var_with_value = 19
    RULE_var_pair = 20
    RULE_var_array_no_value = 21
    RULE_var_array_with_value = 22
    RULE_var_array_pair = 23
    RULE_var_array_decl_tail = 24
    RULE_array_rhs = 25
    RULE_assign_stmt = 26
    RULE_assign_lhs = 27
    RULE_params_list = 28
    RULE_params = 29
    RULE_data_type = 30
    RULE_if_stmt = 31
    RULE_else_if_body = 32
    RULE_else_body = 33
    RULE_for_in_stmt = 34
    RULE_for_in_body = 35
    RULE_for_in_expr = 36
    RULE_scalar_variable = 37
    RULE_break_stmt = 38
    RULE_continue_stmt = 39
    RULE_return_stmt = 40
    RULE_method_invoc = 41
    RULE_static_method_invoc = 42
    RULE_block_stmt_stmt = 43
    RULE_block_stmt = 44
    RULE_method_invoc_literal = 45
    RULE_expr_list = 46
    RULE_funcall = 47
    RULE_all_expr = 48
    RULE_op = 49
    RULE_op1 = 50
    RULE_op2 = 51
    RULE_op3 = 52
    RULE_op4 = 53
    RULE_op5 = 54
    RULE_op6 = 55
    RULE_op7 = 56
    RULE_postfix_array_exp = 57
    RULE_op8 = 58
    RULE_op9 = 59
    RULE_op10 = 60
    RULE_operands = 61
    RULE_element_expr = 62
    RULE_index_ops = 63
    RULE_static_member_access = 64
    RULE_static_method = 65
    RULE_object_create = 66
    RULE_list_of_expr = 67
    RULE_literal = 68
    RULE_literal_array = 69
    RULE_literal_idx_array = 70
    RULE_literal_mtd_array = 71
    RULE_array_element = 72

    ruleNames =  [ "program", "class_decl", "class_body", "class_attr", 
                   "attr_no_value", "attr_with_value", "attr_pair", "attr_array_no_value", 
                   "attr_array_with_value", "attr_array_pair", "attr_array_decl_tail", 
                   "any_id", "class_method", "normal_method", "constructor", 
                   "destructor", "stmt", "var_decl", "var_no_value", "var_with_value", 
                   "var_pair", "var_array_no_value", "var_array_with_value", 
                   "var_array_pair", "var_array_decl_tail", "array_rhs", 
                   "assign_stmt", "assign_lhs", "params_list", "params", 
                   "data_type", "if_stmt", "else_if_body", "else_body", 
                   "for_in_stmt", "for_in_body", "for_in_expr", "scalar_variable", 
                   "break_stmt", "continue_stmt", "return_stmt", "method_invoc", 
                   "static_method_invoc", "block_stmt_stmt", "block_stmt", 
                   "method_invoc_literal", "expr_list", "funcall", "all_expr", 
                   "op", "op1", "op2", "op3", "op4", "op5", "op6", "op7", 
                   "postfix_array_exp", "op8", "op9", "op10", "operands", 
                   "element_expr", "index_ops", "static_member_access", 
                   "static_method", "object_create", "list_of_expr", "literal", 
                   "literal_array", "literal_idx_array", "literal_mtd_array", 
                   "array_element" ]

    EOF = Token.EOF
    LITERAL_BOOLEAN=1
    LITERAL_INT=2
    LITERAL_ZERO=3
    LITERAL_INT_DEC=4
    LITERAL_INT_HEX=5
    LITERAL_INT_OCT=6
    LITERAL_INT_BIN=7
    LITERAL_FLOAT=8
    LITERAL_STRING=9
    DOUBLE_QUOTE=10
    VAL=11
    VAR=12
    STATIC=13
    BREAK=14
    FOREACH=15
    INT=16
    NULL=17
    CONSTRUCTOR=18
    CONTINUE=19
    TRUE=20
    FLOAT=21
    CLASS=22
    DESTRUCTOR=23
    IF=24
    FALSE=25
    BOOLEAN=26
    NEW=27
    ELSEIF=28
    ARRAY=29
    STRING=30
    BY=31
    ELSE=32
    IN=33
    RETURN=34
    SELF=35
    LB=36
    RB=37
    LS=38
    RS=39
    LP=40
    RP=41
    SEMI=42
    COMMA=43
    DOTDOT=44
    ADD=45
    SUBTRACT=46
    MULTIPLY=47
    DIVIDE=48
    MODULO=49
    NOT=50
    AND=51
    OR=52
    EQUAL=53
    ASSIGN=54
    NOT_EQUAL=55
    LESS_THAN=56
    LEQ=57
    GREATER_THAN=58
    GEQ=59
    EQUAL_STRING=60
    STRING_CONCAT=61
    DOT=62
    DOUBLE_COLON=63
    COLON=64
    ID=65
    DOLLAR_ID=66
    BLOCK_COMMENT=67
    WS=68
    UNCLOSE_STRING=69
    ILLEGAL_ESCAPE=70
    ERROR_CHAR=71

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 146
                self.class_decl()
                self.state = 149 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 151
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def class_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_bodyContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_bodyContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_class_decl




    def class_decl(self):

        localctx = D96Parser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(D96Parser.CLASS)
            self.state = 154
            self.match(D96Parser.ID)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 155
                self.match(D96Parser.COLON)
                self.state = 156
                self.match(D96Parser.ID)


            self.state = 159
            self.match(D96Parser.LP)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.CONSTRUCTOR - 11)) | (1 << (D96Parser.DESTRUCTOR - 11)) | (1 << (D96Parser.ID - 11)) | (1 << (D96Parser.DOLLAR_ID - 11)))) != 0):
                self.state = 160
                self.class_body()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 166
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_attr(self):
            return self.getTypedRuleContext(D96Parser.Class_attrContext,0)


        def class_method(self):
            return self.getTypedRuleContext(D96Parser.Class_methodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_body




    def class_body(self):

        localctx = D96Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_body)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.class_attr()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.class_method()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_attrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_no_value(self):
            return self.getTypedRuleContext(D96Parser.Attr_no_valueContext,0)


        def attr_with_value(self):
            return self.getTypedRuleContext(D96Parser.Attr_with_valueContext,0)


        def attr_array_no_value(self):
            return self.getTypedRuleContext(D96Parser.Attr_array_no_valueContext,0)


        def attr_array_with_value(self):
            return self.getTypedRuleContext(D96Parser.Attr_array_with_valueContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_attr




    def class_attr(self):

        localctx = D96Parser.Class_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_attr)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.attr_no_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.attr_with_value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                self.attr_array_no_value()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 175
                self.attr_array_with_value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_no_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def any_id(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Any_idContext)
            else:
                return self.getTypedRuleContext(D96Parser.Any_idContext,i)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_no_value




    def attr_no_value(self):

        localctx = D96Parser.Attr_no_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attr_no_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 179
            self.any_id()
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 180
                self.match(D96Parser.COMMA)
                self.state = 181
                self.any_id()
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 187
            self.match(D96Parser.COLON)
            self.state = 188
            self.data_type()
            self.state = 189
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_with_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def any_id(self):
            return self.getTypedRuleContext(D96Parser.Any_idContext,0)


        def attr_pair(self):
            return self.getTypedRuleContext(D96Parser.Attr_pairContext,0)


        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_with_value




    def attr_with_value(self):

        localctx = D96Parser.Attr_with_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attr_with_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 192
            self.any_id()
            self.state = 193
            self.attr_pair()
            self.state = 194
            self.all_expr()
            self.state = 195
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_pairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def any_id(self):
            return self.getTypedRuleContext(D96Parser.Any_idContext,0)


        def attr_pair(self):
            return self.getTypedRuleContext(D96Parser.Attr_pairContext,0)


        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_pair




    def attr_pair(self):

        localctx = D96Parser.Attr_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attr_pair)
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(D96Parser.COMMA)
                self.state = 198
                self.any_id()
                self.state = 199
                self.attr_pair()
                self.state = 200
                self.all_expr()
                self.state = 201
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.match(D96Parser.COLON)
                self.state = 204
                self.data_type()
                self.state = 205
                self.match(D96Parser.ASSIGN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_array_no_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def any_id(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Any_idContext)
            else:
                return self.getTypedRuleContext(D96Parser.Any_idContext,i)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def attr_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Attr_array_decl_tailContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_array_no_value




    def attr_array_no_value(self):

        localctx = D96Parser.Attr_array_no_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attr_array_no_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 210
            self.any_id()
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 211
                self.match(D96Parser.COMMA)
                self.state = 212
                self.any_id()
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 218
            self.match(D96Parser.COLON)
            self.state = 219
            self.attr_array_decl_tail()
            self.state = 220
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_array_with_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def any_id(self):
            return self.getTypedRuleContext(D96Parser.Any_idContext,0)


        def attr_array_pair(self):
            return self.getTypedRuleContext(D96Parser.Attr_array_pairContext,0)


        def array_rhs(self):
            return self.getTypedRuleContext(D96Parser.Array_rhsContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_array_with_value




    def attr_array_with_value(self):

        localctx = D96Parser.Attr_array_with_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attr_array_with_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 223
            self.any_id()
            self.state = 224
            self.attr_array_pair()
            self.state = 225
            self.array_rhs()
            self.state = 226
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_array_pairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def any_id(self):
            return self.getTypedRuleContext(D96Parser.Any_idContext,0)


        def attr_array_pair(self):
            return self.getTypedRuleContext(D96Parser.Attr_array_pairContext,0)


        def array_rhs(self):
            return self.getTypedRuleContext(D96Parser.Array_rhsContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def attr_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Attr_array_decl_tailContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_array_pair




    def attr_array_pair(self):

        localctx = D96Parser.Attr_array_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attr_array_pair)
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.match(D96Parser.COMMA)
                self.state = 229
                self.any_id()
                self.state = 230
                self.attr_array_pair()
                self.state = 231
                self.array_rhs()
                self.state = 232
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(D96Parser.COLON)
                self.state = 235
                self.attr_array_decl_tail()
                self.state = 236
                self.match(D96Parser.ASSIGN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_array_decl_tailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def LITERAL_INT(self):
            return self.getToken(D96Parser.LITERAL_INT, 0)

        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def attr_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Attr_array_decl_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attr_array_decl_tail




    def attr_array_decl_tail(self):

        localctx = D96Parser.Attr_array_decl_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attr_array_decl_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(D96Parser.ARRAY)
            self.state = 241
            self.match(D96Parser.LS)
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.SELF, D96Parser.ID]:
                self.state = 242
                self.data_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 243
                self.attr_array_decl_tail()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 246
            self.match(D96Parser.COMMA)
            self.state = 247
            self.match(D96Parser.LITERAL_INT)
            self.state = 248
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Any_idContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_any_id




    def any_id(self):

        localctx = D96Parser.Any_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_any_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_methodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normal_method(self):
            return self.getTypedRuleContext(D96Parser.Normal_methodContext,0)


        def constructor(self):
            return self.getTypedRuleContext(D96Parser.ConstructorContext,0)


        def destructor(self):
            return self.getTypedRuleContext(D96Parser.DestructorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_method




    def class_method(self):

        localctx = D96Parser.Class_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_class_method)
        try:
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.normal_method()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 254
                self.destructor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_methodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def any_id(self):
            return self.getTypedRuleContext(D96Parser.Any_idContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def params_list(self):
            return self.getTypedRuleContext(D96Parser.Params_listContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_normal_method




    def normal_method(self):

        localctx = D96Parser.Normal_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_normal_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.any_id()
            self.state = 258
            self.match(D96Parser.LB)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 259
                self.params_list()


            self.state = 262
            self.match(D96Parser.RB)
            self.state = 263
            self.match(D96Parser.LP)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 264
                self.block_stmt()


            self.state = 267
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def params_list(self):
            return self.getTypedRuleContext(D96Parser.Params_listContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 270
            self.match(D96Parser.LB)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 271
                self.params_list()


            self.state = 274
            self.match(D96Parser.RB)
            self.state = 275
            self.match(D96Parser.LP)
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 276
                self.block_stmt()


            self.state = 279
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_destructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(D96Parser.DESTRUCTOR)
            self.state = 282
            self.match(D96Parser.LB)
            self.state = 283
            self.match(D96Parser.RB)
            self.state = 284
            self.match(D96Parser.LP)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 285
                self.block_stmt()


            self.state = 288
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(D96Parser.Var_declContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(D96Parser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(D96Parser.If_stmtContext,0)


        def for_in_stmt(self):
            return self.getTypedRuleContext(D96Parser.For_in_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(D96Parser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(D96Parser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(D96Parser.Return_stmtContext,0)


        def method_invoc(self):
            return self.getTypedRuleContext(D96Parser.Method_invocContext,0)


        def static_method_invoc(self):
            return self.getTypedRuleContext(D96Parser.Static_method_invocContext,0)


        def block_stmt_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmt_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_stmt)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 292
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 293
                self.for_in_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 294
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 295
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 296
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 297
                self.method_invoc()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 298
                self.static_method_invoc()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 299
                self.block_stmt_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_no_value(self):
            return self.getTypedRuleContext(D96Parser.Var_no_valueContext,0)


        def var_with_value(self):
            return self.getTypedRuleContext(D96Parser.Var_with_valueContext,0)


        def var_array_no_value(self):
            return self.getTypedRuleContext(D96Parser.Var_array_no_valueContext,0)


        def var_array_with_value(self):
            return self.getTypedRuleContext(D96Parser.Var_array_with_valueContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_decl




    def var_decl(self):

        localctx = D96Parser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_var_decl)
        try:
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.var_no_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.var_with_value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 304
                self.var_array_no_value()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 305
                self.var_array_with_value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_no_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_var_no_value




    def var_no_value(self):

        localctx = D96Parser.Var_no_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_var_no_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 309
            self.match(D96Parser.ID)
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 310
                self.match(D96Parser.COMMA)
                self.state = 311
                self.match(D96Parser.ID)
                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 317
            self.match(D96Parser.COLON)
            self.state = 318
            self.data_type()
            self.state = 319
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_with_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def var_pair(self):
            return self.getTypedRuleContext(D96Parser.Var_pairContext,0)


        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_with_value




    def var_with_value(self):

        localctx = D96Parser.Var_with_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_with_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 322
            self.match(D96Parser.ID)
            self.state = 323
            self.var_pair()
            self.state = 324
            self.all_expr()
            self.state = 325
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_pairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def var_pair(self):
            return self.getTypedRuleContext(D96Parser.Var_pairContext,0)


        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_pair




    def var_pair(self):

        localctx = D96Parser.Var_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_var_pair)
        try:
            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.match(D96Parser.COMMA)
                self.state = 328
                self.match(D96Parser.ID)
                self.state = 329
                self.var_pair()
                self.state = 330
                self.all_expr()
                self.state = 331
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self.match(D96Parser.COLON)
                self.state = 334
                self.data_type()
                self.state = 335
                self.match(D96Parser.ASSIGN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_array_no_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def var_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Var_array_decl_tailContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_var_array_no_value




    def var_array_no_value(self):

        localctx = D96Parser.Var_array_no_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_var_array_no_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 340
            self.match(D96Parser.ID)
            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 341
                self.match(D96Parser.COMMA)
                self.state = 342
                self.match(D96Parser.ID)
                self.state = 347
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 348
            self.match(D96Parser.COLON)
            self.state = 349
            self.var_array_decl_tail()
            self.state = 350
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_array_with_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def var_array_pair(self):
            return self.getTypedRuleContext(D96Parser.Var_array_pairContext,0)


        def array_rhs(self):
            return self.getTypedRuleContext(D96Parser.Array_rhsContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_array_with_value




    def var_array_with_value(self):

        localctx = D96Parser.Var_array_with_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_var_array_with_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 353
            self.match(D96Parser.ID)
            self.state = 354
            self.var_array_pair()
            self.state = 355
            self.array_rhs()
            self.state = 356
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_array_pairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def var_array_pair(self):
            return self.getTypedRuleContext(D96Parser.Var_array_pairContext,0)


        def array_rhs(self):
            return self.getTypedRuleContext(D96Parser.Array_rhsContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def var_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Var_array_decl_tailContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_array_pair




    def var_array_pair(self):

        localctx = D96Parser.Var_array_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_var_array_pair)
        try:
            self.state = 368
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.match(D96Parser.COMMA)
                self.state = 359
                self.match(D96Parser.ID)
                self.state = 360
                self.var_array_pair()
                self.state = 361
                self.array_rhs()
                self.state = 362
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.match(D96Parser.COLON)
                self.state = 365
                self.var_array_decl_tail()
                self.state = 366
                self.match(D96Parser.ASSIGN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_array_decl_tailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def LITERAL_INT(self):
            return self.getToken(D96Parser.LITERAL_INT, 0)

        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def var_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Var_array_decl_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_array_decl_tail




    def var_array_decl_tail(self):

        localctx = D96Parser.Var_array_decl_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_var_array_decl_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(D96Parser.ARRAY)
            self.state = 371
            self.match(D96Parser.LS)
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.SELF, D96Parser.ID]:
                self.state = 372
                self.data_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 373
                self.var_array_decl_tail()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 376
            self.match(D96Parser.COMMA)
            self.state = 377
            self.match(D96Parser.LITERAL_INT)
            self.state = 378
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_rhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_array(self):
            return self.getTypedRuleContext(D96Parser.Literal_arrayContext,0)


        def object_create(self):
            return self.getTypedRuleContext(D96Parser.Object_createContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_rhs




    def array_rhs(self):

        localctx = D96Parser.Array_rhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_array_rhs)
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.literal_array()
                pass
            elif token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.object_create()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs(self):
            return self.getTypedRuleContext(D96Parser.Assign_lhsContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.assign_lhs()
            self.state = 385
            self.match(D96Parser.ASSIGN)
            self.state = 386
            self.all_expr()
            self.state = 387
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_lhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_variable(self):
            return self.getTypedRuleContext(D96Parser.Scalar_variableContext,0)


        def element_expr(self):
            return self.getTypedRuleContext(D96Parser.Element_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_lhs




    def assign_lhs(self):

        localctx = D96Parser.Assign_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_assign_lhs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.scalar_variable(0)
            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.LS:
                self.state = 390
                self.element_expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ParamsContext)
            else:
                return self.getTypedRuleContext(D96Parser.ParamsContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI)
            else:
                return self.getToken(D96Parser.SEMI, i)

        def getRuleIndex(self):
            return D96Parser.RULE_params_list




    def params_list(self):

        localctx = D96Parser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.params()
            self.state = 398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 394
                self.match(D96Parser.SEMI)
                self.state = 395
                self.params()
                self.state = 400
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def var_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Var_array_decl_tailContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_params




    def params(self):

        localctx = D96Parser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(D96Parser.ID)
            self.state = 406
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 402
                self.match(D96Parser.COMMA)
                self.state = 403
                self.match(D96Parser.ID)
                self.state = 408
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 409
            self.match(D96Parser.COLON)
            self.state = 412
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.SELF, D96Parser.ID]:
                self.state = 410
                self.data_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 411
                self.var_array_decl_tail()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_data_type




    def data_type(self):

        localctx = D96Parser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            _la = self._input.LA(1)
            if not(((((_la - 16)) & ~0x3f) == 0 and ((1 << (_la - 16)) & ((1 << (D96Parser.INT - 16)) | (1 << (D96Parser.FLOAT - 16)) | (1 << (D96Parser.BOOLEAN - 16)) | (1 << (D96Parser.STRING - 16)) | (1 << (D96Parser.SELF - 16)) | (1 << (D96Parser.ID - 16)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def else_if_body(self):
            return self.getTypedRuleContext(D96Parser.Else_if_bodyContext,0)


        def else_body(self):
            return self.getTypedRuleContext(D96Parser.Else_bodyContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(D96Parser.IF)
            self.state = 417
            self.match(D96Parser.LB)
            self.state = 418
            self.all_expr()
            self.state = 419
            self.match(D96Parser.RB)
            self.state = 420
            self.match(D96Parser.LP)
            self.state = 422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 421
                self.block_stmt()


            self.state = 424
            self.match(D96Parser.RP)
            self.state = 427
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.state = 425
                self.else_if_body()
                pass
            elif token in [D96Parser.ELSE]:
                self.state = 426
                self.else_body()
                pass
            elif token in [D96Parser.VAL, D96Parser.VAR, D96Parser.BREAK, D96Parser.FOREACH, D96Parser.CONTINUE, D96Parser.IF, D96Parser.NEW, D96Parser.RETURN, D96Parser.SELF, D96Parser.LP, D96Parser.RP, D96Parser.ID]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def else_if_body(self):
            return self.getTypedRuleContext(D96Parser.Else_if_bodyContext,0)


        def else_body(self):
            return self.getTypedRuleContext(D96Parser.Else_bodyContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_if_body




    def else_if_body(self):

        localctx = D96Parser.Else_if_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_else_if_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(D96Parser.ELSEIF)
            self.state = 430
            self.match(D96Parser.LB)
            self.state = 431
            self.all_expr()
            self.state = 432
            self.match(D96Parser.RB)
            self.state = 433
            self.match(D96Parser.LP)
            self.state = 435
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 434
                self.block_stmt()


            self.state = 437
            self.match(D96Parser.RP)
            self.state = 440
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.state = 438
                self.else_if_body()
                pass
            elif token in [D96Parser.ELSE]:
                self.state = 439
                self.else_body()
                pass
            elif token in [D96Parser.VAL, D96Parser.VAR, D96Parser.BREAK, D96Parser.FOREACH, D96Parser.CONTINUE, D96Parser.IF, D96Parser.NEW, D96Parser.RETURN, D96Parser.SELF, D96Parser.LP, D96Parser.RP, D96Parser.ID]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_body




    def else_body(self):

        localctx = D96Parser.Else_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_else_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(D96Parser.ELSE)
            self.state = 443
            self.match(D96Parser.LP)
            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 444
                self.block_stmt()


            self.state = 447
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_in_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def for_in_body(self):
            return self.getTypedRuleContext(D96Parser.For_in_bodyContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_for_in_stmt




    def for_in_stmt(self):

        localctx = D96Parser.For_in_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_for_in_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(D96Parser.FOREACH)
            self.state = 450
            self.match(D96Parser.LB)
            self.state = 451
            self.for_in_body()
            self.state = 452
            self.match(D96Parser.RB)
            self.state = 453
            self.match(D96Parser.LP)
            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 454
                self.block_stmt()


            self.state = 457
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_in_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_variable(self):
            return self.getTypedRuleContext(D96Parser.Scalar_variableContext,0)


        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def for_in_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.For_in_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.For_in_exprContext,i)


        def DOTDOT(self):
            return self.getToken(D96Parser.DOTDOT, 0)

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_for_in_body




    def for_in_body(self):

        localctx = D96Parser.For_in_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_for_in_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.scalar_variable(0)
            self.state = 460
            self.match(D96Parser.IN)
            self.state = 461
            self.for_in_expr()
            self.state = 462
            self.match(D96Parser.DOTDOT)
            self.state = 463
            self.for_in_expr()
            self.state = 466
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 464
                self.match(D96Parser.BY)
                self.state = 465
                self.for_in_expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_in_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_for_in_expr




    def for_in_expr(self):

        localctx = D96Parser.For_in_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_for_in_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.all_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_variableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def static_member_access(self):
            return self.getTypedRuleContext(D96Parser.Static_member_accessContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def scalar_variable(self):
            return self.getTypedRuleContext(D96Parser.Scalar_variableContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_scalar_variable



    def scalar_variable(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Scalar_variableContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_scalar_variable, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 471
                self.static_member_access()
                pass

            elif la_ == 2:
                self.state = 472
                self.match(D96Parser.SELF)
                pass

            elif la_ == 3:
                self.state = 473
                self.match(D96Parser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 484
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Scalar_variableContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_scalar_variable)
                    self.state = 476
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 477
                    self.match(D96Parser.DOT)
                    self.state = 480
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        self.state = 478
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 479
                        self.funcall()
                        pass

             
                self.state = 486
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.match(D96Parser.BREAK)
            self.state = 488
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = D96Parser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.match(D96Parser.CONTINUE)
            self.state = 491
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_stmt




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.match(D96Parser.RETURN)
            self.state = 495
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_ZERO) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.ID:
                self.state = 494
                self.all_expr()


            self.state = 497
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_invoc_literal(self):
            return self.getTypedRuleContext(D96Parser.Method_invoc_literalContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_invoc




    def method_invoc(self):

        localctx = D96Parser.Method_invocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_method_invoc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.method_invoc_literal(0)
            self.state = 500
            self.match(D96Parser.DOT)
            self.state = 501
            self.funcall()
            self.state = 502
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_method_invocContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def static_method(self):
            return self.getTypedRuleContext(D96Parser.Static_methodContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_method_invoc




    def static_method_invoc(self):

        localctx = D96Parser.Static_method_invocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_static_method_invoc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            _la = self._input.LA(1)
            if not(_la==D96Parser.SELF or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 505
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 506
            self.static_method()
            self.state = 507
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmt_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt_stmt




    def block_stmt_stmt(self):

        localctx = D96Parser.Block_stmt_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_block_stmt_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self.match(D96Parser.LP)
            self.state = 511
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 510
                self.block_stmt()


            self.state = 513
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.StmtContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 515
                self.stmt()
                self.state = 518 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invoc_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def static_member_access(self):
            return self.getTypedRuleContext(D96Parser.Static_member_accessContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def method_invoc_literal(self):
            return self.getTypedRuleContext(D96Parser.Method_invoc_literalContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def element_expr(self):
            return self.getTypedRuleContext(D96Parser.Element_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invoc_literal



    def method_invoc_literal(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Method_invoc_literalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_method_invoc_literal, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 521
                self.match(D96Parser.NEW)
                self.state = 522
                self.funcall()
                pass

            elif la_ == 2:
                self.state = 523
                self.static_member_access()
                pass

            elif la_ == 3:
                self.state = 524
                self.match(D96Parser.SELF)
                pass

            elif la_ == 4:
                self.state = 525
                self.match(D96Parser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 538
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 536
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Method_invoc_literalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_method_invoc_literal)
                        self.state = 528
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 529
                        self.match(D96Parser.DOT)
                        self.state = 532
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                        if la_ == 1:
                            self.state = 530
                            self.match(D96Parser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 531
                            self.funcall()
                            pass


                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Method_invoc_literalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_method_invoc_literal)
                        self.state = 534
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 535
                        self.element_expr()
                        pass

             
                self.state = 540
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.All_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.All_exprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_list




    def expr_list(self):

        localctx = D96Parser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 541
                    self.all_expr()
                    self.state = 542
                    self.match(D96Parser.COMMA) 
                self.state = 548
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

            self.state = 549
            self.all_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_of_expr(self):
            return self.getTypedRuleContext(D96Parser.List_of_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_funcall




    def funcall(self):

        localctx = D96Parser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            self.match(D96Parser.ID)
            self.state = 552
            self.match(D96Parser.LB)
            self.state = 554
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_ZERO) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.ID:
                self.state = 553
                self.list_of_expr()


            self.state = 556
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op(self):
            return self.getTypedRuleContext(D96Parser.OpContext,0)


        def object_create(self):
            return self.getTypedRuleContext(D96Parser.Object_createContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_all_expr




    def all_expr(self):

        localctx = D96Parser.All_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_all_expr)
        try:
            self.state = 560
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 558
                self.op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 559
                self.object_create()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Op1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Op1Context,i)


        def STRING_CONCAT(self):
            return self.getToken(D96Parser.STRING_CONCAT, 0)

        def EQUAL_STRING(self):
            return self.getToken(D96Parser.EQUAL_STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_op




    def op(self):

        localctx = D96Parser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.state = 567
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 562
                self.op1()
                self.state = 563
                _la = self._input.LA(1)
                if not(_la==D96Parser.EQUAL_STRING or _la==D96Parser.STRING_CONCAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 564
                self.op1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 566
                self.op1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Op2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Op2Context,i)


        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(D96Parser.NOT_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(D96Parser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(D96Parser.GREATER_THAN, 0)

        def LEQ(self):
            return self.getToken(D96Parser.LEQ, 0)

        def GEQ(self):
            return self.getToken(D96Parser.GEQ, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_op1




    def op1(self):

        localctx = D96Parser.Op1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_op1)
        self._la = 0 # Token type
        try:
            self.state = 574
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 569
                self.op2(0)
                self.state = 570
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.LESS_THAN) | (1 << D96Parser.LEQ) | (1 << D96Parser.GREATER_THAN) | (1 << D96Parser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 571
                self.op2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 573
                self.op2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op3(self):
            return self.getTypedRuleContext(D96Parser.Op3Context,0)


        def op2(self):
            return self.getTypedRuleContext(D96Parser.Op2Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_op2



    def op2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Op2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_op2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 577
            self.op3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 584
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op2)
                    self.state = 579
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 580
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 581
                    self.op3(0) 
                self.state = 586
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Op3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op4(self):
            return self.getTypedRuleContext(D96Parser.Op4Context,0)


        def op3(self):
            return self.getTypedRuleContext(D96Parser.Op3Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUBTRACT(self):
            return self.getToken(D96Parser.SUBTRACT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_op3



    def op3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Op3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_op3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            self.op4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 595
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op3)
                    self.state = 590
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 591
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUBTRACT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 592
                    self.op4(0) 
                self.state = 597
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Op4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op5(self):
            return self.getTypedRuleContext(D96Parser.Op5Context,0)


        def op4(self):
            return self.getTypedRuleContext(D96Parser.Op4Context,0)


        def MULTIPLY(self):
            return self.getToken(D96Parser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(D96Parser.DIVIDE, 0)

        def MODULO(self):
            return self.getToken(D96Parser.MODULO, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_op4



    def op4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Op4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_op4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599
            self.op5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 606
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op4)
                    self.state = 601
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 602
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLY) | (1 << D96Parser.DIVIDE) | (1 << D96Parser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 603
                    self.op5() 
                self.state = 608
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Op5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def op5(self):
            return self.getTypedRuleContext(D96Parser.Op5Context,0)


        def op6(self):
            return self.getTypedRuleContext(D96Parser.Op6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_op5




    def op5(self):

        localctx = D96Parser.Op5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_op5)
        try:
            self.state = 612
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 609
                self.match(D96Parser.NOT)
                self.state = 610
                self.op5()
                pass
            elif token in [D96Parser.LITERAL_BOOLEAN, D96Parser.LITERAL_INT, D96Parser.LITERAL_ZERO, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.SUBTRACT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 611
                self.op6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBTRACT(self):
            return self.getToken(D96Parser.SUBTRACT, 0)

        def op6(self):
            return self.getTypedRuleContext(D96Parser.Op6Context,0)


        def op7(self):
            return self.getTypedRuleContext(D96Parser.Op7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_op6




    def op6(self):

        localctx = D96Parser.Op6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_op6)
        try:
            self.state = 617
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUBTRACT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 614
                self.match(D96Parser.SUBTRACT)
                self.state = 615
                self.op6()
                pass
            elif token in [D96Parser.LITERAL_BOOLEAN, D96Parser.LITERAL_INT, D96Parser.LITERAL_ZERO, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 616
                self.op7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op8(self):
            return self.getTypedRuleContext(D96Parser.Op8Context,0)


        def op7(self):
            return self.getTypedRuleContext(D96Parser.Op7Context,0)


        def postfix_array_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Postfix_array_expContext)
            else:
                return self.getTypedRuleContext(D96Parser.Postfix_array_expContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_op7



    def op7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Op7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_op7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 620
            self.op8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 630
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op7)
                    self.state = 622
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 624 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 623
                            self.postfix_array_exp()

                        else:
                            raise NoViableAltException(self)
                        self.state = 626 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
             
                self.state = 632
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Postfix_array_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_postfix_array_exp




    def postfix_array_exp(self):

        localctx = D96Parser.Postfix_array_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_postfix_array_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 633
            self.match(D96Parser.LS)
            self.state = 634
            self.all_expr()
            self.state = 635
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op9(self):
            return self.getTypedRuleContext(D96Parser.Op9Context,0)


        def op8(self):
            return self.getTypedRuleContext(D96Parser.Op8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_op8



    def op8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Op8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 116
        self.enterRecursionRule(localctx, 116, self.RULE_op8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 638
            self.op9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 648
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,58,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op8)
                    self.state = 640
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 641
                    self.match(D96Parser.DOT)
                    self.state = 644
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                    if la_ == 1:
                        self.state = 642
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 643
                        self.funcall()
                        pass

             
                self.state = 650
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,58,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Op9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def static_method(self):
            return self.getTypedRuleContext(D96Parser.Static_methodContext,0)


        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def op10(self):
            return self.getTypedRuleContext(D96Parser.Op10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_op9




    def op9(self):

        localctx = D96Parser.Op9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_op9)
        self._la = 0 # Token type
        try:
            self.state = 658
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 651
                _la = self._input.LA(1)
                if not(_la==D96Parser.SELF or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 652
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 655
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                if la_ == 1:
                    self.state = 653
                    self.static_method()
                    pass

                elif la_ == 2:
                    self.state = 654
                    self.match(D96Parser.DOLLAR_ID)
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 657
                self.op10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op10Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def operands(self):
            return self.getTypedRuleContext(D96Parser.OperandsContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_of_expr(self):
            return self.getTypedRuleContext(D96Parser.List_of_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_op10




    def op10(self):

        localctx = D96Parser.Op10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_op10)
        self._la = 0 # Token type
        try:
            self.state = 669
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 660
                self.match(D96Parser.NEW)
                self.state = 661
                self.operands()
                self.state = 662
                self.match(D96Parser.LB)
                self.state = 664
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_ZERO) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.ID:
                    self.state = 663
                    self.list_of_expr()


                self.state = 666
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.LITERAL_BOOLEAN, D96Parser.LITERAL_INT, D96Parser.LITERAL_ZERO, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 668
                self.operands()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def op(self):
            return self.getTypedRuleContext(D96Parser.OpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def literal_array(self):
            return self.getTypedRuleContext(D96Parser.Literal_arrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_operands




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_operands)
        try:
            self.state = 680
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LITERAL_BOOLEAN, D96Parser.LITERAL_INT, D96Parser.LITERAL_ZERO, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 671
                self.literal()
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 672
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 673
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 674
                self.match(D96Parser.LB)
                self.state = 675
                self.op()
                self.state = 676
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 678
                self.match(D96Parser.NULL)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 679
                self.literal_array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_ops(self):
            return self.getTypedRuleContext(D96Parser.Index_opsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_element_expr




    def element_expr(self):

        localctx = D96Parser.Element_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_element_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 682
            self.index_ops(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_opsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def index_ops(self):
            return self.getTypedRuleContext(D96Parser.Index_opsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_ops



    def index_ops(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Index_opsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 126
        self.enterRecursionRule(localctx, 126, self.RULE_index_ops, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 685
            self.match(D96Parser.LS)
            self.state = 686
            self.all_expr()
            self.state = 687
            self.match(D96Parser.RS)
            self._ctx.stop = self._input.LT(-1)
            self.state = 696
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_opsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_ops)
                    self.state = 689
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 690
                    self.match(D96Parser.LS)
                    self.state = 691
                    self.all_expr()
                    self.state = 692
                    self.match(D96Parser.RS) 
                self.state = 698
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Static_member_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def static_method(self):
            return self.getTypedRuleContext(D96Parser.Static_methodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_member_access




    def static_member_access(self):

        localctx = D96Parser.Static_member_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_static_member_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 699
            _la = self._input.LA(1)
            if not(_la==D96Parser.SELF or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 700
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 703
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.state = 701
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 2:
                self.state = 702
                self.static_method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_methodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_of_expr(self):
            return self.getTypedRuleContext(D96Parser.List_of_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_method




    def static_method(self):

        localctx = D96Parser.Static_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_static_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 705
            self.match(D96Parser.DOLLAR_ID)
            self.state = 706
            self.match(D96Parser.LB)
            self.state = 708
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_ZERO) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.ID:
                self.state = 707
                self.list_of_expr()


            self.state = 710
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_createContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_of_expr(self):
            return self.getTypedRuleContext(D96Parser.List_of_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_object_create




    def object_create(self):

        localctx = D96Parser.Object_createContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_object_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 712
            self.match(D96Parser.NEW)
            self.state = 713
            self.match(D96Parser.ID)
            self.state = 714
            self.match(D96Parser.LB)
            self.state = 716
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_ZERO) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.ID:
                self.state = 715
                self.list_of_expr()


            self.state = 718
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.OpContext)
            else:
                return self.getTypedRuleContext(D96Parser.OpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_list_of_expr




    def list_of_expr(self):

        localctx = D96Parser.List_of_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_list_of_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 720
            self.op()
            self.state = 725
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 721
                self.match(D96Parser.COMMA)
                self.state = 722
                self.op()
                self.state = 727
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LITERAL_INT(self):
            return self.getToken(D96Parser.LITERAL_INT, 0)

        def LITERAL_FLOAT(self):
            return self.getToken(D96Parser.LITERAL_FLOAT, 0)

        def LITERAL_STRING(self):
            return self.getToken(D96Parser.LITERAL_STRING, 0)

        def LITERAL_BOOLEAN(self):
            return self.getToken(D96Parser.LITERAL_BOOLEAN, 0)

        def LITERAL_ZERO(self):
            return self.getToken(D96Parser.LITERAL_ZERO, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_literal




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 728
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_ZERO) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_idx_array(self):
            return self.getTypedRuleContext(D96Parser.Literal_idx_arrayContext,0)


        def literal_mtd_array(self):
            return self.getTypedRuleContext(D96Parser.Literal_mtd_arrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal_array




    def literal_array(self):

        localctx = D96Parser.Literal_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_literal_array)
        try:
            self.state = 732
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 730
                self.literal_idx_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 731
                self.literal_mtd_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_idx_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def array_element(self):
            return self.getTypedRuleContext(D96Parser.Array_elementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal_idx_array




    def literal_idx_array(self):

        localctx = D96Parser.Literal_idx_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_literal_idx_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 734
            self.match(D96Parser.ARRAY)
            self.state = 735
            self.match(D96Parser.LB)
            self.state = 737
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_ZERO) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.ID:
                self.state = 736
                self.array_element()


            self.state = 739
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_mtd_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def literal_idx_array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Literal_idx_arrayContext)
            else:
                return self.getTypedRuleContext(D96Parser.Literal_idx_arrayContext,i)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_literal_mtd_array




    def literal_mtd_array(self):

        localctx = D96Parser.Literal_mtd_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_literal_mtd_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 741
            self.match(D96Parser.ARRAY)
            self.state = 742
            self.match(D96Parser.LB)
            self.state = 743
            self.literal_idx_array()
            self.state = 748
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 744
                self.match(D96Parser.COMMA)
                self.state = 745
                self.literal_idx_array()
                self.state = 750
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 751
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.All_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.All_exprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_array_element




    def array_element(self):

        localctx = D96Parser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_array_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 753
            self.all_expr()
            self.state = 758
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 754
                self.match(D96Parser.COMMA)
                self.state = 755
                self.all_expr()
                self.state = 760
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[37] = self.scalar_variable_sempred
        self._predicates[45] = self.method_invoc_literal_sempred
        self._predicates[51] = self.op2_sempred
        self._predicates[52] = self.op3_sempred
        self._predicates[53] = self.op4_sempred
        self._predicates[56] = self.op7_sempred
        self._predicates[58] = self.op8_sempred
        self._predicates[63] = self.index_ops_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def scalar_variable_sempred(self, localctx:Scalar_variableContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

    def method_invoc_literal_sempred(self, localctx:Method_invoc_literalContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

    def op2_sempred(self, localctx:Op2Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def op3_sempred(self, localctx:Op3Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def op4_sempred(self, localctx:Op4Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def op7_sempred(self, localctx:Op7Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def op8_sempred(self, localctx:Op8Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def index_ops_sempred(self, localctx:Index_opsContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




