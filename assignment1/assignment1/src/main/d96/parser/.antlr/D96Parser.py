# Generated from d:\HCMUT\Semester 212\Principles of Programming Languages\HK212_CO3005_PPL\assignment1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3G")
        buf.write("\u02a0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\3\2\6\2\u008e\n\2\r\2\16\2\u008f\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\5\3\u0098\n\3\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write("\7\4\u00a0\n\4\f\4\16\4\u00a3\13\4\3\5\3\5\3\6\3\6\3\6")
        buf.write("\5\6\u00aa\n\6\3\7\3\7\3\7\5\7\u00af\n\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\5\b\u00b6\n\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00be")
        buf.write("\n\t\3\t\3\t\3\t\5\t\u00c3\n\t\5\t\u00c5\n\t\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00d2\n")
        buf.write("\13\3\f\3\f\3\f\3\f\5\f\u00d8\n\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\5\r\u00e1\n\r\3\r\3\r\3\r\5\r\u00e6\n\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\5\16\u00ed\n\16\3\16\3\16\3\16\5\16")
        buf.write("\u00f2\n\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\5\17\u00fb")
        buf.write("\n\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\5\20\u0107\n\20\3\21\3\21\3\21\5\21\u010c\n\21\3\21\3")
        buf.write("\21\3\22\3\22\3\22\5\22\u0113\n\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u011b\n\23\3\23\3\23\3\23\5\23\u0120\n")
        buf.write("\23\5\23\u0122\n\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u012f\n\25\3\26\3\26\3\26\3")
        buf.write("\26\5\26\u0135\n\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u014a\n\31\3\31\5\31\u014d\n\31\3\31\3\31\3")
        buf.write("\31\3\31\5\31\u0153\n\31\3\31\5\31\u0156\n\31\7\31\u0158")
        buf.write("\n\31\f\31\16\31\u015b\13\31\3\31\3\31\5\31\u015f\n\31")
        buf.write("\3\32\3\32\3\32\7\32\u0164\n\32\f\32\16\32\u0167\13\32")
        buf.write("\3\33\3\33\3\33\7\33\u016c\n\33\f\33\16\33\u016f\13\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\5\34\u0179\n")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0181\n\35\3\35")
        buf.write("\3\35\5\35\u0185\n\35\3\36\3\36\3\36\3\36\3\36\3\36\5")
        buf.write("\36\u018d\n\36\3\36\3\36\5\36\u0191\n\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \5 \u01a2")
        buf.write("\n \3!\5!\u01a5\n!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\7")
        buf.write("$\u01b1\n$\f$\16$\u01b4\13$\3$\3$\3%\3%\3&\3&\5&\u01bc")
        buf.write("\n&\3&\3&\3\'\3\'\3\'\7\'\u01c3\n\'\f\'\16\'\u01c6\13")
        buf.write("\'\3\'\3\'\3(\6(\u01cb\n(\r(\16(\u01cc\3)\3)\3)\3)\5)")
        buf.write("\u01d3\n)\7)\u01d5\n)\f)\16)\u01d8\13)\3)\3)\3*\3*\3*")
        buf.write("\3*\5*\u01e0\n*\7*\u01e2\n*\f*\16*\u01e5\13*\3*\3*\3+")
        buf.write("\3+\5+\u01eb\n+\6+\u01ed\n+\r+\16+\u01ee\3,\3,\3,\5,\u01f4")
        buf.write("\n,\3-\3-\3-\3-\3-\5-\u01fb\n-\3.\3.\3.\3.\3.\5.\u0202")
        buf.write("\n.\3/\3/\3/\3/\3/\3/\7/\u020a\n/\f/\16/\u020d\13/\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\7\60\u0215\n\60\f\60\16\60\u0218")
        buf.write("\13\60\3\61\3\61\3\61\3\61\3\61\3\61\7\61\u0220\n\61\f")
        buf.write("\61\16\61\u0223\13\61\3\62\3\62\3\62\5\62\u0228\n\62\3")
        buf.write("\63\3\63\3\63\5\63\u022d\n\63\3\64\3\64\3\64\3\64\5\64")
        buf.write("\u0233\n\64\3\65\3\65\3\65\3\65\3\65\3\65\7\65\u023b\n")
        buf.write("\65\f\65\16\65\u023e\13\65\3\66\3\66\3\66\5\66\u0243\n")
        buf.write("\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u024d")
        buf.write("\n\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3<\3=\3=\3=\3=\5=")
        buf.write("\u025e\n=\3>\3>\3>\3>\5>\u0264\n>\3?\3?\3?\5?\u0269\n")
        buf.write("?\3?\3?\3@\3@\3@\5@\u0270\n@\3@\3@\3A\3A\3A\5A\u0277\n")
        buf.write("A\3A\3A\3B\3B\3B\5B\u027e\nB\3B\3B\3C\3C\3C\5C\u0285\n")
        buf.write("C\3C\3C\3C\5C\u028a\nC\3C\3C\3D\3D\3D\3D\5D\u0292\nD\3")
        buf.write("D\3D\3E\3E\5E\u0298\nE\6E\u029a\nE\rE\16E\u029b\3F\3F")
        buf.write("\3F\2\6\\^`hG\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 ")
        buf.write("\"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtv")
        buf.write("xz|~\u0080\u0082\u0084\u0086\u0088\u008a\2\16\3\2\13\f")
        buf.write("\3\2AB\4\2##AA\3\2<=\4\2\65\65\67;\3\2\63\64\3\2-.\3\2")
        buf.write("/\61\3\2>?\3\2-\61\4\2\62\64<<\4\2\3\3\b\t\2\u02b5\2\u008d")
        buf.write("\3\2\2\2\4\u0093\3\2\2\2\6\u00a1\3\2\2\2\b\u00a4\3\2\2")
        buf.write("\2\n\u00a9\3\2\2\2\f\u00ab\3\2\2\2\16\u00b2\3\2\2\2\20")
        buf.write("\u00c4\3\2\2\2\22\u00c6\3\2\2\2\24\u00d1\3\2\2\2\26\u00d3")
        buf.write("\3\2\2\2\30\u00dd\3\2\2\2\32\u00e9\3\2\2\2\34\u00f5\3")
        buf.write("\2\2\2\36\u0106\3\2\2\2 \u0108\3\2\2\2\"\u010f\3\2\2\2")
        buf.write("$\u0121\3\2\2\2&\u0123\3\2\2\2(\u012e\3\2\2\2*\u0130\3")
        buf.write("\2\2\2,\u013a\3\2\2\2.\u013f\3\2\2\2\60\u015e\3\2\2\2")
        buf.write("\62\u0160\3\2\2\2\64\u0168\3\2\2\2\66\u0178\3\2\2\28\u017a")
        buf.write("\3\2\2\2:\u0186\3\2\2\2<\u0192\3\2\2\2>\u019a\3\2\2\2")
        buf.write("@\u01a4\3\2\2\2B\u01a8\3\2\2\2D\u01ab\3\2\2\2F\u01ae\3")
        buf.write("\2\2\2H\u01b7\3\2\2\2J\u01bb\3\2\2\2L\u01c4\3\2\2\2N\u01ca")
        buf.write("\3\2\2\2P\u01ce\3\2\2\2R\u01db\3\2\2\2T\u01ec\3\2\2\2")
        buf.write("V\u01f3\3\2\2\2X\u01fa\3\2\2\2Z\u0201\3\2\2\2\\\u0203")
        buf.write("\3\2\2\2^\u020e\3\2\2\2`\u0219\3\2\2\2b\u0227\3\2\2\2")
        buf.write("d\u022c\3\2\2\2f\u0232\3\2\2\2h\u0234\3\2\2\2j\u0242\3")
        buf.write("\2\2\2l\u024c\3\2\2\2n\u024e\3\2\2\2p\u0250\3\2\2\2r\u0252")
        buf.write("\3\2\2\2t\u0254\3\2\2\2v\u0256\3\2\2\2x\u0259\3\2\2\2")
        buf.write("z\u0263\3\2\2\2|\u0268\3\2\2\2~\u026f\3\2\2\2\u0080\u0276")
        buf.write("\3\2\2\2\u0082\u027a\3\2\2\2\u0084\u0284\3\2\2\2\u0086")
        buf.write("\u028d\3\2\2\2\u0088\u0299\3\2\2\2\u008a\u029d\3\2\2\2")
        buf.write("\u008c\u008e\5\4\3\2\u008d\u008c\3\2\2\2\u008e\u008f\3")
        buf.write("\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0091")
        buf.write("\3\2\2\2\u0091\u0092\7\2\2\3\u0092\3\3\2\2\2\u0093\u0094")
        buf.write("\7\26\2\2\u0094\u0097\5H%\2\u0095\u0096\7@\2\2\u0096\u0098")
        buf.write("\5H%\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0099\u009a\7(\2\2\u009a\u009b\5\6\4\2\u009b")
        buf.write("\u009c\7)\2\2\u009c\5\3\2\2\2\u009d\u00a0\5\b\5\2\u009e")
        buf.write("\u00a0\5\n\6\2\u009f\u009d\3\2\2\2\u009f\u009e\3\2\2\2")
        buf.write("\u00a0\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3")
        buf.write("\2\2\2\u00a2\7\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5")
        buf.write("\5\f\7\2\u00a5\t\3\2\2\2\u00a6\u00aa\5\30\r\2\u00a7\u00aa")
        buf.write("\5\32\16\2\u00a8\u00aa\5\34\17\2\u00a9\u00a6\3\2\2\2\u00a9")
        buf.write("\u00a7\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa\13\3\2\2\2\u00ab")
        buf.write("\u00ae\t\2\2\2\u00ac\u00af\5\16\b\2\u00ad\u00af\5\22\n")
        buf.write("\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\u00b0")
        buf.write("\3\2\2\2\u00b0\u00b1\7*\2\2\u00b1\r\3\2\2\2\u00b2\u00b3")
        buf.write("\t\3\2\2\u00b3\u00b5\5\20\t\2\u00b4\u00b6\5V,\2\u00b5")
        buf.write("\u00b4\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\17\3\2\2\2\u00b7")
        buf.write("\u00b8\7+\2\2\u00b8\u00b9\t\3\2\2\u00b9\u00bd\5\20\t\2")
        buf.write("\u00ba\u00bb\5V,\2\u00bb\u00bc\7+\2\2\u00bc\u00be\3\2")
        buf.write("\2\2\u00bd\u00ba\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c5")
        buf.write("\3\2\2\2\u00bf\u00c0\7@\2\2\u00c0\u00c2\5\66\34\2\u00c1")
        buf.write("\u00c3\7\66\2\2\u00c2\u00c1\3\2\2\2\u00c2\u00c3\3\2\2")
        buf.write("\2\u00c3\u00c5\3\2\2\2\u00c4\u00b7\3\2\2\2\u00c4\u00bf")
        buf.write("\3\2\2\2\u00c5\21\3\2\2\2\u00c6\u00c7\t\3\2\2\u00c7\u00c8")
        buf.write("\5\24\13\2\u00c8\u00c9\5\26\f\2\u00c9\23\3\2\2\2\u00ca")
        buf.write("\u00cb\7+\2\2\u00cb\u00cc\t\3\2\2\u00cc\u00cd\5\24\13")
        buf.write("\2\u00cd\u00ce\5\26\f\2\u00ce\u00cf\7+\2\2\u00cf\u00d2")
        buf.write("\3\2\2\2\u00d0\u00d2\7@\2\2\u00d1\u00ca\3\2\2\2\u00d1")
        buf.write("\u00d0\3\2\2\2\u00d2\25\3\2\2\2\u00d3\u00d4\7\35\2\2\u00d4")
        buf.write("\u00d7\7&\2\2\u00d5\u00d8\5\66\34\2\u00d6\u00d8\7\35\2")
        buf.write("\2\u00d7\u00d5\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8\u00d9")
        buf.write("\3\2\2\2\u00d9\u00da\7+\2\2\u00da\u00db\7\3\2\2\u00db")
        buf.write("\u00dc\7\'\2\2\u00dc\27\3\2\2\2\u00dd\u00de\t\3\2\2\u00de")
        buf.write("\u00e0\7$\2\2\u00df\u00e1\5\62\32\2\u00e0\u00df\3\2\2")
        buf.write("\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3")
        buf.write("\7%\2\2\u00e3\u00e5\7(\2\2\u00e4\u00e6\5N(\2\u00e5\u00e4")
        buf.write("\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7")
        buf.write("\u00e8\7)\2\2\u00e8\31\3\2\2\2\u00e9\u00ea\7\22\2\2\u00ea")
        buf.write("\u00ec\7$\2\2\u00eb\u00ed\5\62\32\2\u00ec\u00eb\3\2\2")
        buf.write("\2\u00ec\u00ed\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00ef")
        buf.write("\7%\2\2\u00ef\u00f1\7(\2\2\u00f0\u00f2\5N(\2\u00f1\u00f0")
        buf.write("\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3")
        buf.write("\u00f4\7)\2\2\u00f4\33\3\2\2\2\u00f5\u00f6\7\27\2\2\u00f6")
        buf.write("\u00f7\7$\2\2\u00f7\u00f8\7%\2\2\u00f8\u00fa\7(\2\2\u00f9")
        buf.write("\u00fb\5N(\2\u00fa\u00f9\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb")
        buf.write("\u00fc\3\2\2\2\u00fc\u00fd\7)\2\2\u00fd\35\3\2\2\2\u00fe")
        buf.write("\u0107\5 \21\2\u00ff\u0107\5.\30\2\u0100\u0107\58\35\2")
        buf.write("\u0101\u0107\5<\37\2\u0102\u0107\5B\"\2\u0103\u0107\5")
        buf.write("D#\2\u0104\u0107\5F$\2\u0105\u0107\5J&\2\u0106\u00fe\3")
        buf.write("\2\2\2\u0106\u00ff\3\2\2\2\u0106\u0100\3\2\2\2\u0106\u0101")
        buf.write("\3\2\2\2\u0106\u0102\3\2\2\2\u0106\u0103\3\2\2\2\u0106")
        buf.write("\u0104\3\2\2\2\u0106\u0105\3\2\2\2\u0107\37\3\2\2\2\u0108")
        buf.write("\u010b\t\2\2\2\u0109\u010c\5\"\22\2\u010a\u010c\5&\24")
        buf.write("\2\u010b\u0109\3\2\2\2\u010b\u010a\3\2\2\2\u010c\u010d")
        buf.write("\3\2\2\2\u010d\u010e\7*\2\2\u010e!\3\2\2\2\u010f\u0110")
        buf.write("\7A\2\2\u0110\u0112\5$\23\2\u0111\u0113\5V,\2\u0112\u0111")
        buf.write("\3\2\2\2\u0112\u0113\3\2\2\2\u0113#\3\2\2\2\u0114\u0115")
        buf.write("\7+\2\2\u0115\u0116\7A\2\2\u0116\u011a\5$\23\2\u0117\u0118")
        buf.write("\5V,\2\u0118\u0119\7+\2\2\u0119\u011b\3\2\2\2\u011a\u0117")
        buf.write("\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u0122\3\2\2\2\u011c")
        buf.write("\u011d\7@\2\2\u011d\u011f\5\66\34\2\u011e\u0120\7\66\2")
        buf.write("\2\u011f\u011e\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0122")
        buf.write("\3\2\2\2\u0121\u0114\3\2\2\2\u0121\u011c\3\2\2\2\u0122")
        buf.write("%\3\2\2\2\u0123\u0124\7A\2\2\u0124\u0125\5(\25\2\u0125")
        buf.write("\u0126\5*\26\2\u0126\'\3\2\2\2\u0127\u0128\7+\2\2\u0128")
        buf.write("\u0129\7A\2\2\u0129\u012a\5(\25\2\u012a\u012b\5*\26\2")
        buf.write("\u012b\u012c\7+\2\2\u012c\u012f\3\2\2\2\u012d\u012f\7")
        buf.write("@\2\2\u012e\u0127\3\2\2\2\u012e\u012d\3\2\2\2\u012f)\3")
        buf.write("\2\2\2\u0130\u0131\7\35\2\2\u0131\u0134\7&\2\2\u0132\u0135")
        buf.write("\5\66\34\2\u0133\u0135\5*\26\2\u0134\u0132\3\2\2\2\u0134")
        buf.write("\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0137\7+\2\2")
        buf.write("\u0137\u0138\7\3\2\2\u0138\u0139\7\'\2\2\u0139+\3\2\2")
        buf.write("\2\u013a\u013b\7\33\2\2\u013b\u013c\7A\2\2\u013c\u013d")
        buf.write("\7$\2\2\u013d\u013e\7%\2\2\u013e-\3\2\2\2\u013f\u0140")
        buf.write("\5\60\31\2\u0140\u0141\7\66\2\2\u0141\u0142\5V,\2\u0142")
        buf.write("\u0143\7*\2\2\u0143/\3\2\2\2\u0144\u0159\5H%\2\u0145\u0146")
        buf.write("\7?\2\2\u0146\u014c\7B\2\2\u0147\u0149\7$\2\2\u0148\u014a")
        buf.write("\5\62\32\2\u0149\u0148\3\2\2\2\u0149\u014a\3\2\2\2\u014a")
        buf.write("\u014b\3\2\2\2\u014b\u014d\7%\2\2\u014c\u0147\3\2\2\2")
        buf.write("\u014c\u014d\3\2\2\2\u014d\u0158\3\2\2\2\u014e\u014f\7")
        buf.write(">\2\2\u014f\u0155\7A\2\2\u0150\u0152\7$\2\2\u0151\u0153")
        buf.write("\5\62\32\2\u0152\u0151\3\2\2\2\u0152\u0153\3\2\2\2\u0153")
        buf.write("\u0154\3\2\2\2\u0154\u0156\7%\2\2\u0155\u0150\3\2\2\2")
        buf.write("\u0155\u0156\3\2\2\2\u0156\u0158\3\2\2\2\u0157\u0145\3")
        buf.write("\2\2\2\u0157\u014e\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157")
        buf.write("\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015f\3\2\2\2\u015b")
        buf.write("\u0159\3\2\2\2\u015c\u015f\7A\2\2\u015d\u015f\7B\2\2\u015e")
        buf.write("\u0144\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015d\3\2\2\2")
        buf.write("\u015f\61\3\2\2\2\u0160\u0165\5\64\33\2\u0161\u0162\7")
        buf.write("*\2\2\u0162\u0164\5\64\33\2\u0163\u0161\3\2\2\2\u0164")
        buf.write("\u0167\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166\3\2\2\2")
        buf.write("\u0166\63\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u016d\7A\2")
        buf.write("\2\u0169\u016a\7+\2\2\u016a\u016c\7A\2\2\u016b\u0169\3")
        buf.write("\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e")
        buf.write("\3\2\2\2\u016e\u0170\3\2\2\2\u016f\u016d\3\2\2\2\u0170")
        buf.write("\u0171\7@\2\2\u0171\u0172\5\66\34\2\u0172\65\3\2\2\2\u0173")
        buf.write("\u0179\7\20\2\2\u0174\u0179\7\25\2\2\u0175\u0179\7\32")
        buf.write("\2\2\u0176\u0179\7\36\2\2\u0177\u0179\5H%\2\u0178\u0173")
        buf.write("\3\2\2\2\u0178\u0174\3\2\2\2\u0178\u0175\3\2\2\2\u0178")
        buf.write("\u0176\3\2\2\2\u0178\u0177\3\2\2\2\u0179\67\3\2\2\2\u017a")
        buf.write("\u017b\7\30\2\2\u017b\u017c\7$\2\2\u017c\u017d\5V,\2\u017d")
        buf.write("\u017e\7%\2\2\u017e\u0180\7(\2\2\u017f\u0181\5N(\2\u0180")
        buf.write("\u017f\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0182\3\2\2\2")
        buf.write("\u0182\u0184\7)\2\2\u0183\u0185\5:\36\2\u0184\u0183\3")
        buf.write("\2\2\2\u0184\u0185\3\2\2\2\u01859\3\2\2\2\u0186\u0187")
        buf.write("\7\34\2\2\u0187\u0188\7$\2\2\u0188\u0189\5V,\2\u0189\u018a")
        buf.write("\7%\2\2\u018a\u018c\7(\2\2\u018b\u018d\5N(\2\u018c\u018b")
        buf.write("\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018e\3\2\2\2\u018e")
        buf.write("\u0190\7)\2\2\u018f\u0191\5:\36\2\u0190\u018f\3\2\2\2")
        buf.write("\u0190\u0191\3\2\2\2\u0191;\3\2\2\2\u0192\u0193\7\17\2")
        buf.write("\2\u0193\u0194\7$\2\2\u0194\u0195\5> \2\u0195\u0196\7")
        buf.write("%\2\2\u0196\u0197\7(\2\2\u0197\u0198\5N(\2\u0198\u0199")
        buf.write("\7)\2\2\u0199=\3\2\2\2\u019a\u019b\7A\2\2\u019b\u019c")
        buf.write("\7!\2\2\u019c\u019d\5@!\2\u019d\u019e\7,\2\2\u019e\u01a1")
        buf.write("\5@!\2\u019f\u01a0\7\37\2\2\u01a0\u01a2\5@!\2\u01a1\u019f")
        buf.write("\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2?\3\2\2\2\u01a3\u01a5")
        buf.write("\7.\2\2\u01a4\u01a3\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5")
        buf.write("\u01a6\3\2\2\2\u01a6\u01a7\7\3\2\2\u01a7A\3\2\2\2\u01a8")
        buf.write("\u01a9\7\16\2\2\u01a9\u01aa\7*\2\2\u01aaC\3\2\2\2\u01ab")
        buf.write("\u01ac\7\23\2\2\u01ac\u01ad\7*\2\2\u01adE\3\2\2\2\u01ae")
        buf.write("\u01b2\7\"\2\2\u01af\u01b1\5V,\2\u01b0\u01af\3\2\2\2\u01b1")
        buf.write("\u01b4\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2")
        buf.write("\u01b3\u01b5\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5\u01b6\7")
        buf.write("*\2\2\u01b6G\3\2\2\2\u01b7\u01b8\t\4\2\2\u01b8I\3\2\2")
        buf.write("\2\u01b9\u01bc\5\u0080A\2\u01ba\u01bc\5\u0084C\2\u01bb")
        buf.write("\u01b9\3\2\2\2\u01bb\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2")
        buf.write("\u01bd\u01be\7*\2\2\u01beK\3\2\2\2\u01bf\u01c0\5V,\2\u01c0")
        buf.write("\u01c1\7+\2\2\u01c1\u01c3\3\2\2\2\u01c2\u01bf\3\2\2\2")
        buf.write("\u01c3\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3")
        buf.write("\2\2\2\u01c5\u01c7\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01c8")
        buf.write("\5V,\2\u01c8M\3\2\2\2\u01c9\u01cb\5\36\20\2\u01ca\u01c9")
        buf.write("\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc")
        buf.write("\u01cd\3\2\2\2\u01cdO\3\2\2\2\u01ce\u01cf\7\35\2\2\u01cf")
        buf.write("\u01d6\7$\2\2\u01d0\u01d2\5T+\2\u01d1\u01d3\7+\2\2\u01d2")
        buf.write("\u01d1\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d5\3\2\2\2")
        buf.write("\u01d4\u01d0\3\2\2\2\u01d5\u01d8\3\2\2\2\u01d6\u01d4\3")
        buf.write("\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d9\3\2\2\2\u01d8\u01d6")
        buf.write("\3\2\2\2\u01d9\u01da\7%\2\2\u01daQ\3\2\2\2\u01db\u01dc")
        buf.write("\7\35\2\2\u01dc\u01e3\7$\2\2\u01dd\u01df\5P)\2\u01de\u01e0")
        buf.write("\7+\2\2\u01df\u01de\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0")
        buf.write("\u01e2\3\2\2\2\u01e1\u01dd\3\2\2\2\u01e2\u01e5\3\2\2\2")
        buf.write("\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e6\3")
        buf.write("\2\2\2\u01e5\u01e3\3\2\2\2\u01e6\u01e7\7%\2\2\u01e7S\3")
        buf.write("\2\2\2\u01e8\u01ea\5\u008aF\2\u01e9\u01eb\7+\2\2\u01ea")
        buf.write("\u01e9\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ed\3\2\2\2")
        buf.write("\u01ec\u01e8\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01ec\3")
        buf.write("\2\2\2\u01ee\u01ef\3\2\2\2\u01efU\3\2\2\2\u01f0\u01f4")
        buf.write("\5X-\2\u01f1\u01f4\5z>\2\u01f2\u01f4\5\u0086D\2\u01f3")
        buf.write("\u01f0\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f3\u01f2\3\2\2\2")
        buf.write("\u01f4W\3\2\2\2\u01f5\u01f6\5Z.\2\u01f6\u01f7\t\5\2\2")
        buf.write("\u01f7\u01f8\5Z.\2\u01f8\u01fb\3\2\2\2\u01f9\u01fb\5Z")
        buf.write(".\2\u01fa\u01f5\3\2\2\2\u01fa\u01f9\3\2\2\2\u01fbY\3\2")
        buf.write("\2\2\u01fc\u01fd\5\\/\2\u01fd\u01fe\t\6\2\2\u01fe\u01ff")
        buf.write("\5\\/\2\u01ff\u0202\3\2\2\2\u0200\u0202\5\\/\2\u0201\u01fc")
        buf.write("\3\2\2\2\u0201\u0200\3\2\2\2\u0202[\3\2\2\2\u0203\u0204")
        buf.write("\b/\1\2\u0204\u0205\5^\60\2\u0205\u020b\3\2\2\2\u0206")
        buf.write("\u0207\f\4\2\2\u0207\u0208\t\7\2\2\u0208\u020a\5^\60\2")
        buf.write("\u0209\u0206\3\2\2\2\u020a\u020d\3\2\2\2\u020b\u0209\3")
        buf.write("\2\2\2\u020b\u020c\3\2\2\2\u020c]\3\2\2\2\u020d\u020b")
        buf.write("\3\2\2\2\u020e\u020f\b\60\1\2\u020f\u0210\5`\61\2\u0210")
        buf.write("\u0216\3\2\2\2\u0211\u0212\f\4\2\2\u0212\u0213\t\b\2\2")
        buf.write("\u0213\u0215\5`\61\2\u0214\u0211\3\2\2\2\u0215\u0218\3")
        buf.write("\2\2\2\u0216\u0214\3\2\2\2\u0216\u0217\3\2\2\2\u0217_")
        buf.write("\3\2\2\2\u0218\u0216\3\2\2\2\u0219\u021a\b\61\1\2\u021a")
        buf.write("\u021b\5b\62\2\u021b\u0221\3\2\2\2\u021c\u021d\f\4\2\2")
        buf.write("\u021d\u021e\t\t\2\2\u021e\u0220\5b\62\2\u021f\u021c\3")
        buf.write("\2\2\2\u0220\u0223\3\2\2\2\u0221\u021f\3\2\2\2\u0221\u0222")
        buf.write("\3\2\2\2\u0222a\3\2\2\2\u0223\u0221\3\2\2\2\u0224\u0225")
        buf.write("\7\62\2\2\u0225\u0228\5b\62\2\u0226\u0228\5d\63\2\u0227")
        buf.write("\u0224\3\2\2\2\u0227\u0226\3\2\2\2\u0228c\3\2\2\2\u0229")
        buf.write("\u022a\7.\2\2\u022a\u022d\5d\63\2\u022b\u022d\5f\64\2")
        buf.write("\u022c\u0229\3\2\2\2\u022c\u022b\3\2\2\2\u022de\3\2\2")
        buf.write("\2\u022e\u022f\5h\65\2\u022f\u0230\5x=\2\u0230\u0233\3")
        buf.write("\2\2\2\u0231\u0233\5h\65\2\u0232\u022e\3\2\2\2\u0232\u0231")
        buf.write("\3\2\2\2\u0233g\3\2\2\2\u0234\u0235\b\65\1\2\u0235\u0236")
        buf.write("\5j\66\2\u0236\u023c\3\2\2\2\u0237\u0238\f\4\2\2\u0238")
        buf.write("\u0239\t\n\2\2\u0239\u023b\5j\66\2\u023a\u0237\3\2\2\2")
        buf.write("\u023b\u023e\3\2\2\2\u023c\u023a\3\2\2\2\u023c\u023d\3")
        buf.write("\2\2\2\u023di\3\2\2\2\u023e\u023c\3\2\2\2\u023f\u0240")
        buf.write("\7\33\2\2\u0240\u0243\5j\66\2\u0241\u0243\5l\67\2\u0242")
        buf.write("\u023f\3\2\2\2\u0242\u0241\3\2\2\2\u0243k\3\2\2\2\u0244")
        buf.write("\u024d\5\u008aF\2\u0245\u024d\7A\2\2\u0246\u0247\7$\2")
        buf.write("\2\u0247\u0248\5X-\2\u0248\u0249\7%\2\2\u0249\u024d\3")
        buf.write("\2\2\2\u024a\u024d\7\21\2\2\u024b\u024d\5z>\2\u024c\u0244")
        buf.write("\3\2\2\2\u024c\u0245\3\2\2\2\u024c\u0246\3\2\2\2\u024c")
        buf.write("\u024a\3\2\2\2\u024c\u024b\3\2\2\2\u024dm\3\2\2\2\u024e")
        buf.write("\u024f\t\13\2\2\u024fo\3\2\2\2\u0250\u0251\t\f\2\2\u0251")
        buf.write("q\3\2\2\2\u0252\u0253\7=\2\2\u0253s\3\2\2\2\u0254\u0255")
        buf.write("\t\6\2\2\u0255u\3\2\2\2\u0256\u0257\5V,\2\u0257\u0258")
        buf.write("\5x=\2\u0258w\3\2\2\2\u0259\u025a\7&\2\2\u025a\u025b\5")
        buf.write("V,\2\u025b\u025d\7\'\2\2\u025c\u025e\5x=\2\u025d\u025c")
        buf.write("\3\2\2\2\u025d\u025e\3\2\2\2\u025ey\3\2\2\2\u025f\u0264")
        buf.write("\5|?\2\u0260\u0264\5~@\2\u0261\u0264\5\u0080A\2\u0262")
        buf.write("\u0264\5\u0084C\2\u0263\u025f\3\2\2\2\u0263\u0260\3\2")
        buf.write("\2\2\u0263\u0261\3\2\2\2\u0263\u0262\3\2\2\2\u0264{\3")
        buf.write("\2\2\2\u0265\u0266\5H%\2\u0266\u0267\7>\2\2\u0267\u0269")
        buf.write("\3\2\2\2\u0268\u0265\3\2\2\2\u0268\u0269\3\2\2\2\u0269")
        buf.write("\u026a\3\2\2\2\u026a\u026b\7A\2\2\u026b}\3\2\2\2\u026c")
        buf.write("\u026d\5H%\2\u026d\u026e\7?\2\2\u026e\u0270\3\2\2\2\u026f")
        buf.write("\u026c\3\2\2\2\u026f\u0270\3\2\2\2\u0270\u0271\3\2\2\2")
        buf.write("\u0271\u0272\7B\2\2\u0272\177\3\2\2\2\u0273\u0274\5H%")
        buf.write("\2\u0274\u0275\7>\2\2\u0275\u0277\3\2\2\2\u0276\u0273")
        buf.write("\3\2\2\2\u0276\u0277\3\2\2\2\u0277\u0278\3\2\2\2\u0278")
        buf.write("\u0279\5\u0082B\2\u0279\u0081\3\2\2\2\u027a\u027b\7A\2")
        buf.write("\2\u027b\u027d\7$\2\2\u027c\u027e\5\u0088E\2\u027d\u027c")
        buf.write("\3\2\2\2\u027d\u027e\3\2\2\2\u027e\u027f\3\2\2\2\u027f")
        buf.write("\u0280\7%\2\2\u0280\u0083\3\2\2\2\u0281\u0282\5H%\2\u0282")
        buf.write("\u0283\7?\2\2\u0283\u0285\3\2\2\2\u0284\u0281\3\2\2\2")
        buf.write("\u0284\u0285\3\2\2\2\u0285\u0286\3\2\2\2\u0286\u0287\7")
        buf.write("B\2\2\u0287\u0289\7$\2\2\u0288\u028a\5\u0088E\2\u0289")
        buf.write("\u0288\3\2\2\2\u0289\u028a\3\2\2\2\u028a\u028b\3\2\2\2")
        buf.write("\u028b\u028c\7%\2\2\u028c\u0085\3\2\2\2\u028d\u028e\7")
        buf.write("\33\2\2\u028e\u028f\7A\2\2\u028f\u0291\7$\2\2\u0290\u0292")
        buf.write("\5\u0088E\2\u0291\u0290\3\2\2\2\u0291\u0292\3\2\2\2\u0292")
        buf.write("\u0293\3\2\2\2\u0293\u0294\7%\2\2\u0294\u0087\3\2\2\2")
        buf.write("\u0295\u0297\5X-\2\u0296\u0298\7+\2\2\u0297\u0296\3\2")
        buf.write("\2\2\u0297\u0298\3\2\2\2\u0298\u029a\3\2\2\2\u0299\u0295")
        buf.write("\3\2\2\2\u029a\u029b\3\2\2\2\u029b\u0299\3\2\2\2\u029b")
        buf.write("\u029c\3\2\2\2\u029c\u0089\3\2\2\2\u029d\u029e\t\r\2\2")
        buf.write("\u029e\u008b\3\2\2\2L\u008f\u0097\u009f\u00a1\u00a9\u00ae")
        buf.write("\u00b5\u00bd\u00c2\u00c4\u00d1\u00d7\u00e0\u00e5\u00ec")
        buf.write("\u00f1\u00fa\u0106\u010b\u0112\u011a\u011f\u0121\u012e")
        buf.write("\u0134\u0149\u014c\u0152\u0155\u0157\u0159\u015e\u0165")
        buf.write("\u016d\u0178\u0180\u0184\u018c\u0190\u01a1\u01a4\u01b2")
        buf.write("\u01bb\u01c4\u01cc\u01d2\u01d6\u01df\u01e3\u01ea\u01ee")
        buf.write("\u01f3\u01fa\u0201\u020b\u0216\u0221\u0227\u022c\u0232")
        buf.write("\u023c\u0242\u024c\u025d\u0263\u0268\u026f\u0276\u027d")
        buf.write("\u0284\u0289\u0291\u0297\u029b")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'Val'", "'Var'", "'$'", "'Break'", "'Foreach'", 
                     "'Int'", "'Null'", "'Constructor'", "'Continue'", "'True'", 
                     "'Float'", "'Class'", "'Destructor'", "'If'", "'False'", 
                     "'Boolean'", "'New'", "'Elseif'", "'Array'", "'String'", 
                     "'By'", "'Else'", "'In'", "'Return'", "'Self'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "';'", "','", "'..'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'==.'", "'+.'", "'.'", "'::'", "':'" ]

    symbolicNames = [ "<INVALID>", "LITERAL_INT", "LITERAL_INT_DEC", "LITERAL_INT_HEX", 
                      "LITERAL_INT_OCT", "LITERAL_INT_BIN", "LITERAL_FLOAT", 
                      "LITERAL_STRING", "DOUBLE_QUOTE", "VAL", "VAR", "STATIC", 
                      "BREAK", "FOREACH", "INT", "NULL", "CONSTRUCTOR", 
                      "CONTINUE", "TRUE", "FLOAT", "CLASS", "DESTRUCTOR", 
                      "IF", "FALSE", "BOOLEAN", "NEW", "ELSEIF", "ARRAY", 
                      "STRING", "BY", "ELSE", "IN", "RETURN", "SELF", "LB", 
                      "RB", "LS", "RS", "LP", "RP", "SEMI", "COMMA", "DOTDOT", 
                      "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", "MODULO", 
                      "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", 
                      "LESS_THAN", "LEQ", "GREATER_THAN", "GEQ", "EQUAL_STRING", 
                      "STRING_CONCAT", "DOT", "DOUBLE_COLON", "COLON", "ID", 
                      "DOLLAR_ID", "BLOCK_COMMENT", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_class_body = 2
    RULE_class_attr = 3
    RULE_class_method = 4
    RULE_attr_var_decl = 5
    RULE_attr_pair_list = 6
    RULE_attr_pair = 7
    RULE_attr_pair_list_arr = 8
    RULE_attr_pair_arr = 9
    RULE_attr_array_decl_tail = 10
    RULE_normal_method = 11
    RULE_constructor = 12
    RULE_destructor = 13
    RULE_stmt = 14
    RULE_var_decl = 15
    RULE_pair_list = 16
    RULE_pair = 17
    RULE_pair_list_arr = 18
    RULE_pair_arr = 19
    RULE_array_decl_tail = 20
    RULE_object_decl = 21
    RULE_assign_stmt = 22
    RULE_assign_lhs = 23
    RULE_params_list = 24
    RULE_params = 25
    RULE_data_type = 26
    RULE_if_stmt = 27
    RULE_else_if_body = 28
    RULE_for_in_stmt = 29
    RULE_for_in_body = 30
    RULE_for_in_expr = 31
    RULE_break_stmt = 32
    RULE_continue_stmt = 33
    RULE_return_stmt = 34
    RULE_class_name = 35
    RULE_method_invoc = 36
    RULE_expr_list = 37
    RULE_block_stmt = 38
    RULE_literal_idx_array = 39
    RULE_literal_mtd_array = 40
    RULE_array_element = 41
    RULE_all_expr = 42
    RULE_op = 43
    RULE_op1 = 44
    RULE_op2 = 45
    RULE_op3 = 46
    RULE_op4 = 47
    RULE_op5 = 48
    RULE_op6 = 49
    RULE_op7 = 50
    RULE_op8 = 51
    RULE_op9 = 52
    RULE_operands = 53
    RULE_arithmetic_ops = 54
    RULE_boolean_ops = 55
    RULE_string_ops = 56
    RULE_relational_ops = 57
    RULE_element_expr = 58
    RULE_index_ops = 59
    RULE_member_access = 60
    RULE_instance_attr = 61
    RULE_static_attr = 62
    RULE_instance_method = 63
    RULE_instance_method_tail = 64
    RULE_static_method = 65
    RULE_object_create = 66
    RULE_list_of_expr = 67
    RULE_literal = 68

    ruleNames =  [ "program", "class_decl", "class_body", "class_attr", 
                   "class_method", "attr_var_decl", "attr_pair_list", "attr_pair", 
                   "attr_pair_list_arr", "attr_pair_arr", "attr_array_decl_tail", 
                   "normal_method", "constructor", "destructor", "stmt", 
                   "var_decl", "pair_list", "pair", "pair_list_arr", "pair_arr", 
                   "array_decl_tail", "object_decl", "assign_stmt", "assign_lhs", 
                   "params_list", "params", "data_type", "if_stmt", "else_if_body", 
                   "for_in_stmt", "for_in_body", "for_in_expr", "break_stmt", 
                   "continue_stmt", "return_stmt", "class_name", "method_invoc", 
                   "expr_list", "block_stmt", "literal_idx_array", "literal_mtd_array", 
                   "array_element", "all_expr", "op", "op1", "op2", "op3", 
                   "op4", "op5", "op6", "op7", "op8", "op9", "operands", 
                   "arithmetic_ops", "boolean_ops", "string_ops", "relational_ops", 
                   "element_expr", "index_ops", "member_access", "instance_attr", 
                   "static_attr", "instance_method", "instance_method_tail", 
                   "static_method", "object_create", "list_of_expr", "literal" ]

    EOF = Token.EOF
    LITERAL_INT=1
    LITERAL_INT_DEC=2
    LITERAL_INT_HEX=3
    LITERAL_INT_OCT=4
    LITERAL_INT_BIN=5
    LITERAL_FLOAT=6
    LITERAL_STRING=7
    DOUBLE_QUOTE=8
    VAL=9
    VAR=10
    STATIC=11
    BREAK=12
    FOREACH=13
    INT=14
    NULL=15
    CONSTRUCTOR=16
    CONTINUE=17
    TRUE=18
    FLOAT=19
    CLASS=20
    DESTRUCTOR=21
    IF=22
    FALSE=23
    BOOLEAN=24
    NEW=25
    ELSEIF=26
    ARRAY=27
    STRING=28
    BY=29
    ELSE=30
    IN=31
    RETURN=32
    SELF=33
    LB=34
    RB=35
    LS=36
    RS=37
    LP=38
    RP=39
    SEMI=40
    COMMA=41
    DOTDOT=42
    ADD=43
    SUBTRACT=44
    MULTIPLY=45
    DIVIDE=46
    MODULO=47
    NOT=48
    AND=49
    OR=50
    EQUAL=51
    ASSIGN=52
    NOT_EQUAL=53
    LESS_THAN=54
    LEQ=55
    GREATER_THAN=56
    GEQ=57
    EQUAL_STRING=58
    STRING_CONCAT=59
    DOT=60
    DOUBLE_COLON=61
    COLON=62
    ID=63
    DOLLAR_ID=64
    BLOCK_COMMENT=65
    WS=66
    UNCLOSE_STRING=67
    ILLEGAL_ESCAPE=68
    ERROR_CHAR=69

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
            self.state = 139 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 138
                self.class_decl()
                self.state = 141 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 143
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

        def class_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_nameContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_nameContext,i)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def class_body(self):
            return self.getTypedRuleContext(D96Parser.Class_bodyContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_decl




    def class_decl(self):

        localctx = D96Parser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(D96Parser.CLASS)
            self.state = 146
            self.class_name()
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 147
                self.match(D96Parser.COLON)
                self.state = 148
                self.class_name()


            self.state = 151
            self.match(D96Parser.LP)
            self.state = 152
            self.class_body()
            self.state = 153
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

        def class_attr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_attrContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_attrContext,i)


        def class_method(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_methodContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_methodContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_class_body




    def class_body(self):

        localctx = D96Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (D96Parser.VAL - 9)) | (1 << (D96Parser.VAR - 9)) | (1 << (D96Parser.CONSTRUCTOR - 9)) | (1 << (D96Parser.DESTRUCTOR - 9)) | (1 << (D96Parser.ID - 9)) | (1 << (D96Parser.DOLLAR_ID - 9)))) != 0):
                self.state = 157
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 155
                    self.class_attr()
                    pass
                elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.DOLLAR_ID]:
                    self.state = 156
                    self.class_method()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def attr_var_decl(self):
            return self.getTypedRuleContext(D96Parser.Attr_var_declContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_attr




    def class_attr(self):

        localctx = D96Parser.Class_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.attr_var_decl()
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
        self.enterRule(localctx, 8, self.RULE_class_method)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.normal_method()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 166
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


    class Attr_var_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def attr_pair_list(self):
            return self.getTypedRuleContext(D96Parser.Attr_pair_listContext,0)


        def attr_pair_list_arr(self):
            return self.getTypedRuleContext(D96Parser.Attr_pair_list_arrContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attr_var_decl




    def attr_var_decl(self):

        localctx = D96Parser.Attr_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attr_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 170
                self.attr_pair_list()
                pass

            elif la_ == 2:
                self.state = 171
                self.attr_pair_list_arr()
                pass


            self.state = 174
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_pair_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_pair(self):
            return self.getTypedRuleContext(D96Parser.Attr_pairContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attr_pair_list




    def attr_pair_list(self):

        localctx = D96Parser.Attr_pair_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attr_pair_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 177
            self.attr_pair()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (D96Parser.LITERAL_INT - 1)) | (1 << (D96Parser.LITERAL_FLOAT - 1)) | (1 << (D96Parser.LITERAL_STRING - 1)) | (1 << (D96Parser.NULL - 1)) | (1 << (D96Parser.NEW - 1)) | (1 << (D96Parser.SELF - 1)) | (1 << (D96Parser.LB - 1)) | (1 << (D96Parser.SUBTRACT - 1)) | (1 << (D96Parser.NOT - 1)) | (1 << (D96Parser.ID - 1)) | (1 << (D96Parser.DOLLAR_ID - 1)))) != 0):
                self.state = 178
                self.all_expr()


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

        def attr_pair(self):
            return self.getTypedRuleContext(D96Parser.Attr_pairContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

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
        self.enterRule(localctx, 14, self.RULE_attr_pair)
        self._la = 0 # Token type
        try:
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(D96Parser.COMMA)
                self.state = 182
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 183
                self.attr_pair()
                self.state = 187
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 184
                    self.all_expr()
                    self.state = 185
                    self.match(D96Parser.COMMA)


                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.match(D96Parser.COLON)
                self.state = 190
                self.data_type()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.ASSIGN:
                    self.state = 191
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


    class Attr_pair_list_arrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_pair_arr(self):
            return self.getTypedRuleContext(D96Parser.Attr_pair_arrContext,0)


        def attr_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Attr_array_decl_tailContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_pair_list_arr




    def attr_pair_list_arr(self):

        localctx = D96Parser.Attr_pair_list_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attr_pair_list_arr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 197
            self.attr_pair_arr()
            self.state = 198
            self.attr_array_decl_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_pair_arrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def attr_pair_arr(self):
            return self.getTypedRuleContext(D96Parser.Attr_pair_arrContext,0)


        def attr_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Attr_array_decl_tailContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_pair_arr




    def attr_pair_arr(self):

        localctx = D96Parser.Attr_pair_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attr_pair_arr)
        self._la = 0 # Token type
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.match(D96Parser.COMMA)
                self.state = 201
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 202
                self.attr_pair_arr()
                self.state = 203
                self.attr_array_decl_tail()
                self.state = 204
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.match(D96Parser.COLON)
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

        def ARRAY(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ARRAY)
            else:
                return self.getToken(D96Parser.ARRAY, i)

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def LITERAL_INT(self):
            return self.getToken(D96Parser.LITERAL_INT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_array_decl_tail




    def attr_array_decl_tail(self):

        localctx = D96Parser.Attr_array_decl_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attr_array_decl_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(D96Parser.ARRAY)
            self.state = 210
            self.match(D96Parser.LS)
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.SELF, D96Parser.ID]:
                self.state = 211
                self.data_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 212
                self.match(D96Parser.ARRAY)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 215
            self.match(D96Parser.COMMA)

            self.state = 216
            self.match(D96Parser.LITERAL_INT)
            self.state = 217
            self.match(D96Parser.RS)
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

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def params_list(self):
            return self.getTypedRuleContext(D96Parser.Params_listContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_normal_method




    def normal_method(self):

        localctx = D96Parser.Normal_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_normal_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 220
            self.match(D96Parser.LB)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 221
                self.params_list()


            self.state = 224
            self.match(D96Parser.RB)
            self.state = 225
            self.match(D96Parser.LP)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (D96Parser.VAL - 9)) | (1 << (D96Parser.VAR - 9)) | (1 << (D96Parser.BREAK - 9)) | (1 << (D96Parser.FOREACH - 9)) | (1 << (D96Parser.CONTINUE - 9)) | (1 << (D96Parser.IF - 9)) | (1 << (D96Parser.RETURN - 9)) | (1 << (D96Parser.SELF - 9)) | (1 << (D96Parser.ID - 9)) | (1 << (D96Parser.DOLLAR_ID - 9)))) != 0):
                self.state = 226
                self.block_stmt()


            self.state = 229
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
        self.enterRule(localctx, 24, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 232
            self.match(D96Parser.LB)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 233
                self.params_list()


            self.state = 236
            self.match(D96Parser.RB)
            self.state = 237
            self.match(D96Parser.LP)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (D96Parser.VAL - 9)) | (1 << (D96Parser.VAR - 9)) | (1 << (D96Parser.BREAK - 9)) | (1 << (D96Parser.FOREACH - 9)) | (1 << (D96Parser.CONTINUE - 9)) | (1 << (D96Parser.IF - 9)) | (1 << (D96Parser.RETURN - 9)) | (1 << (D96Parser.SELF - 9)) | (1 << (D96Parser.ID - 9)) | (1 << (D96Parser.DOLLAR_ID - 9)))) != 0):
                self.state = 238
                self.block_stmt()


            self.state = 241
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
        self.enterRule(localctx, 26, self.RULE_destructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(D96Parser.DESTRUCTOR)
            self.state = 244
            self.match(D96Parser.LB)
            self.state = 245
            self.match(D96Parser.RB)
            self.state = 246
            self.match(D96Parser.LP)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (D96Parser.VAL - 9)) | (1 << (D96Parser.VAR - 9)) | (1 << (D96Parser.BREAK - 9)) | (1 << (D96Parser.FOREACH - 9)) | (1 << (D96Parser.CONTINUE - 9)) | (1 << (D96Parser.IF - 9)) | (1 << (D96Parser.RETURN - 9)) | (1 << (D96Parser.SELF - 9)) | (1 << (D96Parser.ID - 9)) | (1 << (D96Parser.DOLLAR_ID - 9)))) != 0):
                self.state = 247
                self.block_stmt()


            self.state = 250
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


        def getRuleIndex(self):
            return D96Parser.RULE_stmt




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 252
                self.var_decl()
                pass

            elif la_ == 2:
                self.state = 253
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.state = 254
                self.if_stmt()
                pass

            elif la_ == 4:
                self.state = 255
                self.for_in_stmt()
                pass

            elif la_ == 5:
                self.state = 256
                self.break_stmt()
                pass

            elif la_ == 6:
                self.state = 257
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.state = 258
                self.return_stmt()
                pass

            elif la_ == 8:
                self.state = 259
                self.method_invoc()
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

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def pair_list(self):
            return self.getTypedRuleContext(D96Parser.Pair_listContext,0)


        def pair_list_arr(self):
            return self.getTypedRuleContext(D96Parser.Pair_list_arrContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_decl




    def var_decl(self):

        localctx = D96Parser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 263
                self.pair_list()
                pass

            elif la_ == 2:
                self.state = 264
                self.pair_list_arr()
                pass


            self.state = 267
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pair_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def pair(self):
            return self.getTypedRuleContext(D96Parser.PairContext,0)


        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_pair_list




    def pair_list(self):

        localctx = D96Parser.Pair_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_pair_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(D96Parser.ID)
            self.state = 270
            self.pair()
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (D96Parser.LITERAL_INT - 1)) | (1 << (D96Parser.LITERAL_FLOAT - 1)) | (1 << (D96Parser.LITERAL_STRING - 1)) | (1 << (D96Parser.NULL - 1)) | (1 << (D96Parser.NEW - 1)) | (1 << (D96Parser.SELF - 1)) | (1 << (D96Parser.LB - 1)) | (1 << (D96Parser.SUBTRACT - 1)) | (1 << (D96Parser.NOT - 1)) | (1 << (D96Parser.ID - 1)) | (1 << (D96Parser.DOLLAR_ID - 1)))) != 0):
                self.state = 271
                self.all_expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):

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

        def pair(self):
            return self.getTypedRuleContext(D96Parser.PairContext,0)


        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_pair




    def pair(self):

        localctx = D96Parser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_pair)
        self._la = 0 # Token type
        try:
            self.state = 287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.match(D96Parser.COMMA)
                self.state = 275
                self.match(D96Parser.ID)
                self.state = 276
                self.pair()
                self.state = 280
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 277
                    self.all_expr()
                    self.state = 278
                    self.match(D96Parser.COMMA)


                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.match(D96Parser.COLON)
                self.state = 283
                self.data_type()
                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.ASSIGN:
                    self.state = 284
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


    class Pair_list_arrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def pair_arr(self):
            return self.getTypedRuleContext(D96Parser.Pair_arrContext,0)


        def array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Array_decl_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_pair_list_arr




    def pair_list_arr(self):

        localctx = D96Parser.Pair_list_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_pair_list_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(D96Parser.ID)
            self.state = 290
            self.pair_arr()
            self.state = 291
            self.array_decl_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pair_arrContext(ParserRuleContext):

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

        def pair_arr(self):
            return self.getTypedRuleContext(D96Parser.Pair_arrContext,0)


        def array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Array_decl_tailContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_pair_arr




    def pair_arr(self):

        localctx = D96Parser.Pair_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_pair_arr)
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.match(D96Parser.COMMA)
                self.state = 294
                self.match(D96Parser.ID)
                self.state = 295
                self.pair_arr()
                self.state = 296
                self.array_decl_tail()
                self.state = 297
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.match(D96Parser.COLON)
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


    class Array_decl_tailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Array_decl_tailContext,0)


        def LITERAL_INT(self):
            return self.getToken(D96Parser.LITERAL_INT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_decl_tail




    def array_decl_tail(self):

        localctx = D96Parser.Array_decl_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_array_decl_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(D96Parser.ARRAY)
            self.state = 303
            self.match(D96Parser.LS)
            self.state = 306
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.SELF, D96Parser.ID]:
                self.state = 304
                self.data_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 305
                self.array_decl_tail()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 308
            self.match(D96Parser.COMMA)

            self.state = 309
            self.match(D96Parser.LITERAL_INT)
            self.state = 310
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_declContext(ParserRuleContext):

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

        def getRuleIndex(self):
            return D96Parser.RULE_object_decl




    def object_decl(self):

        localctx = D96Parser.Object_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_object_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(D96Parser.NEW)
            self.state = 313
            self.match(D96Parser.ID)
            self.state = 314
            self.match(D96Parser.LB)
            self.state = 315
            self.match(D96Parser.RB)
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
        self.enterRule(localctx, 44, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.assign_lhs()
            self.state = 318
            self.match(D96Parser.ASSIGN)
            self.state = 319
            self.all_expr()
            self.state = 320
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

        def class_name(self):
            return self.getTypedRuleContext(D96Parser.Class_nameContext,0)


        def DOUBLE_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOUBLE_COLON)
            else:
                return self.getToken(D96Parser.DOUBLE_COLON, i)

        def DOLLAR_ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOLLAR_ID)
            else:
                return self.getToken(D96Parser.DOLLAR_ID, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOT)
            else:
                return self.getToken(D96Parser.DOT, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LB)
            else:
                return self.getToken(D96Parser.LB, i)

        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RB)
            else:
                return self.getToken(D96Parser.RB, i)

        def params_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Params_listContext)
            else:
                return self.getTypedRuleContext(D96Parser.Params_listContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_lhs




    def assign_lhs(self):

        localctx = D96Parser.Assign_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assign_lhs)
        self._la = 0 # Token type
        try:
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.class_name()
                self.state = 343
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.DOT or _la==D96Parser.DOUBLE_COLON:
                    self.state = 341
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [D96Parser.DOUBLE_COLON]:
                        self.state = 323
                        self.match(D96Parser.DOUBLE_COLON)
                        self.state = 324
                        self.match(D96Parser.DOLLAR_ID)
                        self.state = 330
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==D96Parser.LB:
                            self.state = 325
                            self.match(D96Parser.LB)
                            self.state = 327
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if _la==D96Parser.ID:
                                self.state = 326
                                self.params_list()


                            self.state = 329
                            self.match(D96Parser.RB)


                        pass
                    elif token in [D96Parser.DOT]:
                        self.state = 332
                        self.match(D96Parser.DOT)
                        self.state = 333
                        self.match(D96Parser.ID)
                        self.state = 339
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==D96Parser.LB:
                            self.state = 334
                            self.match(D96Parser.LB)
                            self.state = 336
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if _la==D96Parser.ID:
                                self.state = 335
                                self.params_list()


                            self.state = 338
                            self.match(D96Parser.RB)


                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 345
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 347
                self.match(D96Parser.DOLLAR_ID)
                pass


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
        self.enterRule(localctx, 48, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.params()
            self.state = 355
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 351
                self.match(D96Parser.SEMI)
                self.state = 352
                self.params()
                self.state = 357
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


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_params




    def params(self):

        localctx = D96Parser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(D96Parser.ID)
            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 359
                self.match(D96Parser.COMMA)
                self.state = 360
                self.match(D96Parser.ID)
                self.state = 365
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 366
            self.match(D96Parser.COLON)
            self.state = 367
            self.data_type()
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

        def class_name(self):
            return self.getTypedRuleContext(D96Parser.Class_nameContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_data_type




    def data_type(self):

        localctx = D96Parser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_data_type)
        try:
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 371
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 372
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.SELF, D96Parser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 373
                self.class_name()
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


        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(D96Parser.IF)
            self.state = 377
            self.match(D96Parser.LB)
            self.state = 378
            self.all_expr()
            self.state = 379
            self.match(D96Parser.RB)
            self.state = 380
            self.match(D96Parser.LP)
            self.state = 382
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (D96Parser.VAL - 9)) | (1 << (D96Parser.VAR - 9)) | (1 << (D96Parser.BREAK - 9)) | (1 << (D96Parser.FOREACH - 9)) | (1 << (D96Parser.CONTINUE - 9)) | (1 << (D96Parser.IF - 9)) | (1 << (D96Parser.RETURN - 9)) | (1 << (D96Parser.SELF - 9)) | (1 << (D96Parser.ID - 9)) | (1 << (D96Parser.DOLLAR_ID - 9)))) != 0):
                self.state = 381
                self.block_stmt()


            self.state = 384
            self.match(D96Parser.RP)
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSEIF:
                self.state = 385
                self.else_if_body()


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


        def getRuleIndex(self):
            return D96Parser.RULE_else_if_body




    def else_if_body(self):

        localctx = D96Parser.Else_if_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_else_if_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(D96Parser.ELSEIF)
            self.state = 389
            self.match(D96Parser.LB)
            self.state = 390
            self.all_expr()
            self.state = 391
            self.match(D96Parser.RB)
            self.state = 392
            self.match(D96Parser.LP)
            self.state = 394
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (D96Parser.VAL - 9)) | (1 << (D96Parser.VAR - 9)) | (1 << (D96Parser.BREAK - 9)) | (1 << (D96Parser.FOREACH - 9)) | (1 << (D96Parser.CONTINUE - 9)) | (1 << (D96Parser.IF - 9)) | (1 << (D96Parser.RETURN - 9)) | (1 << (D96Parser.SELF - 9)) | (1 << (D96Parser.ID - 9)) | (1 << (D96Parser.DOLLAR_ID - 9)))) != 0):
                self.state = 393
                self.block_stmt()


            self.state = 396
            self.match(D96Parser.RP)
            self.state = 398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSEIF:
                self.state = 397
                self.else_if_body()


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

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_for_in_stmt




    def for_in_stmt(self):

        localctx = D96Parser.For_in_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_for_in_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(D96Parser.FOREACH)
            self.state = 401
            self.match(D96Parser.LB)
            self.state = 402
            self.for_in_body()
            self.state = 403
            self.match(D96Parser.RB)
            self.state = 404
            self.match(D96Parser.LP)
            self.state = 405
            self.block_stmt()
            self.state = 406
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

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

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
        self.enterRule(localctx, 60, self.RULE_for_in_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(D96Parser.ID)
            self.state = 409
            self.match(D96Parser.IN)
            self.state = 410
            self.for_in_expr()
            self.state = 411
            self.match(D96Parser.DOTDOT)
            self.state = 412
            self.for_in_expr()
            self.state = 415
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 413
                self.match(D96Parser.BY)
                self.state = 414
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

        def LITERAL_INT(self):
            return self.getToken(D96Parser.LITERAL_INT, 0)

        def SUBTRACT(self):
            return self.getToken(D96Parser.SUBTRACT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_for_in_expr




    def for_in_expr(self):

        localctx = D96Parser.For_in_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_for_in_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.SUBTRACT:
                self.state = 417
                self.match(D96Parser.SUBTRACT)


            self.state = 420
            self.match(D96Parser.LITERAL_INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 64, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(D96Parser.BREAK)
            self.state = 423
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
        self.enterRule(localctx, 66, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(D96Parser.CONTINUE)
            self.state = 426
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

        def all_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.All_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.All_exprContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_return_stmt




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(D96Parser.RETURN)
            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (D96Parser.LITERAL_INT - 1)) | (1 << (D96Parser.LITERAL_FLOAT - 1)) | (1 << (D96Parser.LITERAL_STRING - 1)) | (1 << (D96Parser.NULL - 1)) | (1 << (D96Parser.NEW - 1)) | (1 << (D96Parser.SELF - 1)) | (1 << (D96Parser.LB - 1)) | (1 << (D96Parser.SUBTRACT - 1)) | (1 << (D96Parser.NOT - 1)) | (1 << (D96Parser.ID - 1)) | (1 << (D96Parser.DOLLAR_ID - 1)))) != 0):
                self.state = 429
                self.all_expr()
                self.state = 434
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 435
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_name




    def class_name(self):

        localctx = D96Parser.Class_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_class_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            _la = self._input.LA(1)
            if not(_la==D96Parser.SELF or _la==D96Parser.ID):
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


    class Method_invocContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def instance_method(self):
            return self.getTypedRuleContext(D96Parser.Instance_methodContext,0)


        def static_method(self):
            return self.getTypedRuleContext(D96Parser.Static_methodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invoc




    def method_invoc(self):

        localctx = D96Parser.Method_invocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_method_invoc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 439
                self.instance_method()
                pass

            elif la_ == 2:
                self.state = 440
                self.static_method()
                pass


            self.state = 443
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 74, self.RULE_expr_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 445
                    self.all_expr()
                    self.state = 446
                    self.match(D96Parser.COMMA) 
                self.state = 452
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

            self.state = 453
            self.all_expr()
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
        self.enterRule(localctx, 76, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 455
                self.stmt()
                self.state = 458 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (D96Parser.VAL - 9)) | (1 << (D96Parser.VAR - 9)) | (1 << (D96Parser.BREAK - 9)) | (1 << (D96Parser.FOREACH - 9)) | (1 << (D96Parser.CONTINUE - 9)) | (1 << (D96Parser.IF - 9)) | (1 << (D96Parser.RETURN - 9)) | (1 << (D96Parser.SELF - 9)) | (1 << (D96Parser.ID - 9)) | (1 << (D96Parser.DOLLAR_ID - 9)))) != 0)):
                    break

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

        def array_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Array_elementContext)
            else:
                return self.getTypedRuleContext(D96Parser.Array_elementContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_literal_idx_array




    def literal_idx_array(self):

        localctx = D96Parser.Literal_idx_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_literal_idx_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(D96Parser.ARRAY)
            self.state = 461
            self.match(D96Parser.LB)
            self.state = 468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING))) != 0):
                self.state = 462
                self.array_element()
                self.state = 464
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.COMMA:
                    self.state = 463
                    self.match(D96Parser.COMMA)


                self.state = 470
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 471
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

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def literal_idx_array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Literal_idx_arrayContext)
            else:
                return self.getTypedRuleContext(D96Parser.Literal_idx_arrayContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_literal_mtd_array




    def literal_mtd_array(self):

        localctx = D96Parser.Literal_mtd_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_literal_mtd_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(D96Parser.ARRAY)
            self.state = 474
            self.match(D96Parser.LB)
            self.state = 481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ARRAY:
                self.state = 475
                self.literal_idx_array()
                self.state = 477
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.COMMA:
                    self.state = 476
                    self.match(D96Parser.COMMA)


                self.state = 483
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 484
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

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.LiteralContext)
            else:
                return self.getTypedRuleContext(D96Parser.LiteralContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_array_element




    def array_element(self):

        localctx = D96Parser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_array_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 486
                    self.literal()
                    self.state = 488
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                    if la_ == 1:
                        self.state = 487
                        self.match(D96Parser.COMMA)



                else:
                    raise NoViableAltException(self)
                self.state = 492 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

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


        def member_access(self):
            return self.getTypedRuleContext(D96Parser.Member_accessContext,0)


        def object_create(self):
            return self.getTypedRuleContext(D96Parser.Object_createContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_all_expr




    def all_expr(self):

        localctx = D96Parser.All_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_all_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 494
                self.op()
                pass

            elif la_ == 2:
                self.state = 495
                self.member_access()
                pass

            elif la_ == 3:
                self.state = 496
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
        self.enterRule(localctx, 86, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.state = 504
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self.op1()
                self.state = 500
                _la = self._input.LA(1)
                if not(_la==D96Parser.EQUAL_STRING or _la==D96Parser.STRING_CONCAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 501
                self.op1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 503
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
        self.enterRule(localctx, 88, self.RULE_op1)
        self._la = 0 # Token type
        try:
            self.state = 511
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 506
                self.op2(0)
                self.state = 507
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.LESS_THAN) | (1 << D96Parser.LEQ) | (1 << D96Parser.GREATER_THAN) | (1 << D96Parser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 508
                self.op2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 510
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
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_op2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.op3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 521
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,54,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op2)
                    self.state = 516
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 517
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 518
                    self.op3(0) 
                self.state = 523
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

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
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_op3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            self.op4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 532
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op3)
                    self.state = 527
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 528
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUBTRACT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 529
                    self.op4(0) 
                self.state = 534
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

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
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_op4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.op5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 543
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op4)
                    self.state = 538
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 539
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLY) | (1 << D96Parser.DIVIDE) | (1 << D96Parser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 540
                    self.op5() 
                self.state = 545
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

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
        self.enterRule(localctx, 96, self.RULE_op5)
        try:
            self.state = 549
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 546
                self.match(D96Parser.NOT)
                self.state = 547
                self.op5()
                pass
            elif token in [D96Parser.LITERAL_INT, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.SUBTRACT, D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 548
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
        self.enterRule(localctx, 98, self.RULE_op6)
        try:
            self.state = 554
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUBTRACT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 551
                self.match(D96Parser.SUBTRACT)
                self.state = 552
                self.op6()
                pass
            elif token in [D96Parser.LITERAL_INT, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 553
                self.op7()
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


        def index_ops(self):
            return self.getTypedRuleContext(D96Parser.Index_opsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_op7




    def op7(self):

        localctx = D96Parser.Op7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_op7)
        try:
            self.state = 560
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 556
                self.op8(0)
                self.state = 557
                self.index_ops()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 559
                self.op8(0)
                pass


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

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_op8



    def op8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Op8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_op8, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            self.op9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 570
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op8)
                    self.state = 565
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 566
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.DOT or _la==D96Parser.DOUBLE_COLON):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 567
                    self.op9() 
                self.state = 572
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

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

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def op9(self):
            return self.getTypedRuleContext(D96Parser.Op9Context,0)


        def operands(self):
            return self.getTypedRuleContext(D96Parser.OperandsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_op9




    def op9(self):

        localctx = D96Parser.Op9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_op9)
        try:
            self.state = 576
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 573
                self.match(D96Parser.NEW)
                self.state = 574
                self.op9()
                pass
            elif token in [D96Parser.LITERAL_INT, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.SELF, D96Parser.LB, D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 575
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

        def member_access(self):
            return self.getTypedRuleContext(D96Parser.Member_accessContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_operands




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_operands)
        try:
            self.state = 586
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 578
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 579
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 580
                self.match(D96Parser.LB)
                self.state = 581
                self.op()
                self.state = 582
                self.match(D96Parser.RB)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 584
                self.match(D96Parser.NULL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 585
                self.member_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arithmetic_opsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBTRACT(self):
            return self.getToken(D96Parser.SUBTRACT, 0)

        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def MULTIPLY(self):
            return self.getToken(D96Parser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(D96Parser.DIVIDE, 0)

        def MODULO(self):
            return self.getToken(D96Parser.MODULO, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arithmetic_ops




    def arithmetic_ops(self):

        localctx = D96Parser.Arithmetic_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_arithmetic_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ADD) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.MULTIPLY) | (1 << D96Parser.DIVIDE) | (1 << D96Parser.MODULO))) != 0)):
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


    class Boolean_opsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def EQUAL_STRING(self):
            return self.getToken(D96Parser.EQUAL_STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_boolean_ops




    def boolean_ops(self):

        localctx = D96Parser.Boolean_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_boolean_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 590
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.NOT) | (1 << D96Parser.AND) | (1 << D96Parser.OR) | (1 << D96Parser.EQUAL_STRING))) != 0)):
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


    class String_opsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_CONCAT(self):
            return self.getToken(D96Parser.STRING_CONCAT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_string_ops




    def string_ops(self):

        localctx = D96Parser.String_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_string_ops)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.match(D96Parser.STRING_CONCAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_opsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            return D96Parser.RULE_relational_ops




    def relational_ops(self):

        localctx = D96Parser.Relational_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_relational_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.LESS_THAN) | (1 << D96Parser.LEQ) | (1 << D96Parser.GREATER_THAN) | (1 << D96Parser.GEQ))) != 0)):
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


    class Element_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def index_ops(self):
            return self.getTypedRuleContext(D96Parser.Index_opsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_element_expr




    def element_expr(self):

        localctx = D96Parser.Element_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_element_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
            self.all_expr()
            self.state = 597
            self.index_ops()
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




    def index_ops(self):

        localctx = D96Parser.Index_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_index_ops)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599
            self.match(D96Parser.LS)
            self.state = 600
            self.all_expr()
            self.state = 601
            self.match(D96Parser.RS)
            self.state = 603
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.state = 602
                self.index_ops()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_attr(self):
            return self.getTypedRuleContext(D96Parser.Instance_attrContext,0)


        def static_attr(self):
            return self.getTypedRuleContext(D96Parser.Static_attrContext,0)


        def instance_method(self):
            return self.getTypedRuleContext(D96Parser.Instance_methodContext,0)


        def static_method(self):
            return self.getTypedRuleContext(D96Parser.Static_methodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member_access




    def member_access(self):

        localctx = D96Parser.Member_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_member_access)
        try:
            self.state = 609
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 605
                self.instance_attr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 606
                self.static_attr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 607
                self.instance_method()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 608
                self.static_method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_attrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def class_name(self):
            return self.getTypedRuleContext(D96Parser.Class_nameContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_attr




    def instance_attr(self):

        localctx = D96Parser.Instance_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_instance_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.state = 611
                self.class_name()
                self.state = 612
                self.match(D96Parser.DOT)


            self.state = 616
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_attrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def class_name(self):
            return self.getTypedRuleContext(D96Parser.Class_nameContext,0)


        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_attr




    def static_attr(self):

        localctx = D96Parser.Static_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_static_attr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 621
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.SELF or _la==D96Parser.ID:
                self.state = 618
                self.class_name()
                self.state = 619
                self.match(D96Parser.DOUBLE_COLON)


            self.state = 623
            self.match(D96Parser.DOLLAR_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_methodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_method_tail(self):
            return self.getTypedRuleContext(D96Parser.Instance_method_tailContext,0)


        def class_name(self):
            return self.getTypedRuleContext(D96Parser.Class_nameContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_method




    def instance_method(self):

        localctx = D96Parser.Instance_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_instance_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 628
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.state = 625
                self.class_name()
                self.state = 626
                self.match(D96Parser.DOT)


            self.state = 630
            self.instance_method_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_method_tailContext(ParserRuleContext):

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
            return D96Parser.RULE_instance_method_tail




    def instance_method_tail(self):

        localctx = D96Parser.Instance_method_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_instance_method_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 632
            self.match(D96Parser.ID)
            self.state = 633
            self.match(D96Parser.LB)
            self.state = 635
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (D96Parser.LITERAL_INT - 1)) | (1 << (D96Parser.LITERAL_FLOAT - 1)) | (1 << (D96Parser.LITERAL_STRING - 1)) | (1 << (D96Parser.NULL - 1)) | (1 << (D96Parser.NEW - 1)) | (1 << (D96Parser.SELF - 1)) | (1 << (D96Parser.LB - 1)) | (1 << (D96Parser.SUBTRACT - 1)) | (1 << (D96Parser.NOT - 1)) | (1 << (D96Parser.ID - 1)) | (1 << (D96Parser.DOLLAR_ID - 1)))) != 0):
                self.state = 634
                self.list_of_expr()


            self.state = 637
            self.match(D96Parser.RB)
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

        def class_name(self):
            return self.getTypedRuleContext(D96Parser.Class_nameContext,0)


        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

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
            self.state = 642
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.SELF or _la==D96Parser.ID:
                self.state = 639
                self.class_name()
                self.state = 640
                self.match(D96Parser.DOUBLE_COLON)


            self.state = 644
            self.match(D96Parser.DOLLAR_ID)
            self.state = 645
            self.match(D96Parser.LB)
            self.state = 647
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (D96Parser.LITERAL_INT - 1)) | (1 << (D96Parser.LITERAL_FLOAT - 1)) | (1 << (D96Parser.LITERAL_STRING - 1)) | (1 << (D96Parser.NULL - 1)) | (1 << (D96Parser.NEW - 1)) | (1 << (D96Parser.SELF - 1)) | (1 << (D96Parser.LB - 1)) | (1 << (D96Parser.SUBTRACT - 1)) | (1 << (D96Parser.NOT - 1)) | (1 << (D96Parser.ID - 1)) | (1 << (D96Parser.DOLLAR_ID - 1)))) != 0):
                self.state = 646
                self.list_of_expr()


            self.state = 649
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
            self.state = 651
            self.match(D96Parser.NEW)
            self.state = 652
            self.match(D96Parser.ID)
            self.state = 653
            self.match(D96Parser.LB)
            self.state = 655
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (D96Parser.LITERAL_INT - 1)) | (1 << (D96Parser.LITERAL_FLOAT - 1)) | (1 << (D96Parser.LITERAL_STRING - 1)) | (1 << (D96Parser.NULL - 1)) | (1 << (D96Parser.NEW - 1)) | (1 << (D96Parser.SELF - 1)) | (1 << (D96Parser.LB - 1)) | (1 << (D96Parser.SUBTRACT - 1)) | (1 << (D96Parser.NOT - 1)) | (1 << (D96Parser.ID - 1)) | (1 << (D96Parser.DOLLAR_ID - 1)))) != 0):
                self.state = 654
                self.list_of_expr()


            self.state = 657
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
            self.state = 663 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 659
                self.op()
                self.state = 661
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.COMMA:
                    self.state = 660
                    self.match(D96Parser.COMMA)


                self.state = 665 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (D96Parser.LITERAL_INT - 1)) | (1 << (D96Parser.LITERAL_FLOAT - 1)) | (1 << (D96Parser.LITERAL_STRING - 1)) | (1 << (D96Parser.NULL - 1)) | (1 << (D96Parser.NEW - 1)) | (1 << (D96Parser.SELF - 1)) | (1 << (D96Parser.LB - 1)) | (1 << (D96Parser.SUBTRACT - 1)) | (1 << (D96Parser.NOT - 1)) | (1 << (D96Parser.ID - 1)) | (1 << (D96Parser.DOLLAR_ID - 1)))) != 0)):
                    break

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

        def getRuleIndex(self):
            return D96Parser.RULE_literal




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 667
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING))) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[45] = self.op2_sempred
        self._predicates[46] = self.op3_sempred
        self._predicates[47] = self.op4_sempred
        self._predicates[51] = self.op8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def op2_sempred(self, localctx:Op2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def op3_sempred(self, localctx:Op3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def op4_sempred(self, localctx:Op4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def op8_sempred(self, localctx:Op8Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




