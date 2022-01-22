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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u027d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\3\2\6\2\u008c\n\2\r\2\16\2\u008d\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\5\3\u0096\n\3\3\3\3\3\3\3\3\3\3\4\3\4\7\4\u009e")
        buf.write("\n\4\f\4\16\4\u00a1\13\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\5")
        buf.write("\6\u00aa\n\6\3\7\3\7\3\7\7\7\u00af\n\7\f\7\16\7\u00b2")
        buf.write("\13\7\3\7\3\7\3\7\3\7\5\7\u00b8\n\7\3\b\3\b\3\b\7\b\u00bd")
        buf.write("\n\b\f\b\16\b\u00c0\13\b\3\t\3\t\3\t\5\t\u00c5\n\t\3\t")
        buf.write("\3\t\3\t\5\t\u00ca\n\t\3\t\3\t\3\n\3\n\3\n\5\n\u00d1\n")
        buf.write("\n\3\n\3\n\3\n\5\n\u00d6\n\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\5\13\u00df\n\13\3\13\3\13\3\f\3\f\3\f\7\f\u00e6")
        buf.write("\n\f\f\f\16\f\u00e9\13\f\3\r\3\r\3\r\7\r\u00ee\n\r\f\r")
        buf.write("\16\r\u00f1\13\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00fb\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\5\17\u0105\n\17\3\20\3\20\3\20\5\20\u010a\n\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\5\22\u011c\n\22\3\23\3\23\3\23\3")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0129\n\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\7\30\u013c\n\30\f\30\16")
        buf.write("\30\u013f\13\30\3\30\3\30\3\31\3\31\3\31\7\31\u0146\n")
        buf.write("\31\f\31\16\31\u0149\13\31\3\31\3\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\33\3\33\3\33\5\33\u0157\n\33\3\33")
        buf.write("\3\33\5\33\u015b\n\33\3\33\3\33\3\33\3\33\3\34\3\34\3")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u016a\n\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\5\36\u0172\n\36\3\36\3\36\7")
        buf.write("\36\u0176\n\36\f\36\16\36\u0179\13\36\3\37\3\37\3\37\3")
        buf.write("\37\3 \3 \3 \3 \3 \3 \3 \3 \5 \u0187\n \3 \3 \3!\3!\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3$\3$\7$\u0195\n$\f$\16$\u0198\13")
        buf.write("$\3$\3$\3%\3%\3&\3&\3&\5&\u01a1\n&\3&\3&\3&\5&\u01a6\n")
        buf.write("&\3&\3&\3&\3\'\3\'\3\'\7\'\u01ae\n\'\f\'\16\'\u01b1\13")
        buf.write("\'\3\'\3\'\3(\6(\u01b6\n(\r(\16(\u01b7\3)\3)\3)\3)\5)")
        buf.write("\u01be\n)\7)\u01c0\n)\f)\16)\u01c3\13)\3)\3)\3*\3*\3*")
        buf.write("\3*\5*\u01cb\n*\7*\u01cd\n*\f*\16*\u01d0\13*\3*\3*\3+")
        buf.write("\3+\5+\u01d6\n+\6+\u01d8\n+\r+\16+\u01d9\3,\3,\3,\5,\u01df")
        buf.write("\n,\3-\3-\3-\3-\3-\5-\u01e6\n-\3.\3.\3.\3.\3.\5.\u01ed")
        buf.write("\n.\3/\3/\3/\3/\3/\3/\7/\u01f5\n/\f/\16/\u01f8\13/\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\7\60\u0200\n\60\f\60\16\60\u0203")
        buf.write("\13\60\3\61\3\61\3\61\3\61\3\61\3\61\7\61\u020b\n\61\f")
        buf.write("\61\16\61\u020e\13\61\3\62\3\62\3\62\5\62\u0213\n\62\3")
        buf.write("\63\3\63\3\63\5\63\u0218\n\63\3\64\3\64\3\64\3\64\5\64")
        buf.write("\u021e\n\64\3\65\3\65\3\65\3\65\3\65\3\65\7\65\u0226\n")
        buf.write("\65\f\65\16\65\u0229\13\65\3\66\3\66\3\66\5\66\u022e\n")
        buf.write("\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u0238")
        buf.write("\n\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3<\3=\3=\3=\3=\5=")
        buf.write("\u0249\n=\3>\3>\3>\3>\5>\u024f\n>\3?\3?\3?\3?\3@\3@\3")
        buf.write("@\3@\3A\3A\3A\3B\3B\3B\3B\5B\u0260\nB\3B\3B\3C\3C\3C\3")
        buf.write("C\3C\5C\u0269\nC\3C\3C\3D\3D\3D\3D\5D\u0271\nD\3D\3D\3")
        buf.write("E\3E\5E\u0277\nE\6E\u0279\nE\rE\16E\u027a\3E\2\6\\^`h")
        buf.write("F\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\u0086\u0088\2\r\3\2\13\f\3\2\4\7\4\2##AA\3\2>?")
        buf.write("\3\2<=\4\2\65\65\67;\3\2\63\64\3\2-.\3\2/\61\3\2-\61\4")
        buf.write("\2\62\64<<\2\u0282\2\u008b\3\2\2\2\4\u0091\3\2\2\2\6\u009f")
        buf.write("\3\2\2\2\b\u00a2\3\2\2\2\n\u00a9\3\2\2\2\f\u00ab\3\2\2")
        buf.write("\2\16\u00b9\3\2\2\2\20\u00c1\3\2\2\2\22\u00cd\3\2\2\2")
        buf.write("\24\u00d9\3\2\2\2\26\u00e2\3\2\2\2\30\u00ea\3\2\2\2\32")
        buf.write("\u00fa\3\2\2\2\34\u0104\3\2\2\2\36\u0106\3\2\2\2 \u010d")
        buf.write("\3\2\2\2\"\u011b\3\2\2\2$\u011d\3\2\2\2&\u0128\3\2\2\2")
        buf.write("(\u012a\3\2\2\2*\u0131\3\2\2\2,\u0133\3\2\2\2.\u013d\3")
        buf.write("\2\2\2\60\u0147\3\2\2\2\62\u014c\3\2\2\2\64\u015a\3\2")
        buf.write("\2\2\66\u0160\3\2\2\28\u0163\3\2\2\2:\u0177\3\2\2\2<\u017a")
        buf.write("\3\2\2\2>\u017e\3\2\2\2@\u018a\3\2\2\2B\u018c\3\2\2\2")
        buf.write("D\u018f\3\2\2\2F\u0192\3\2\2\2H\u019b\3\2\2\2J\u019d\3")
        buf.write("\2\2\2L\u01af\3\2\2\2N\u01b5\3\2\2\2P\u01b9\3\2\2\2R\u01c6")
        buf.write("\3\2\2\2T\u01d7\3\2\2\2V\u01de\3\2\2\2X\u01e5\3\2\2\2")
        buf.write("Z\u01ec\3\2\2\2\\\u01ee\3\2\2\2^\u01f9\3\2\2\2`\u0204")
        buf.write("\3\2\2\2b\u0212\3\2\2\2d\u0217\3\2\2\2f\u021d\3\2\2\2")
        buf.write("h\u021f\3\2\2\2j\u022d\3\2\2\2l\u0237\3\2\2\2n\u0239\3")
        buf.write("\2\2\2p\u023b\3\2\2\2r\u023d\3\2\2\2t\u023f\3\2\2\2v\u0241")
        buf.write("\3\2\2\2x\u0244\3\2\2\2z\u024e\3\2\2\2|\u0250\3\2\2\2")
        buf.write("~\u0254\3\2\2\2\u0080\u0258\3\2\2\2\u0082\u025b\3\2\2")
        buf.write("\2\u0084\u0263\3\2\2\2\u0086\u026c\3\2\2\2\u0088\u0278")
        buf.write("\3\2\2\2\u008a\u008c\5\4\3\2\u008b\u008a\3\2\2\2\u008c")
        buf.write("\u008d\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2")
        buf.write("\u008e\u008f\3\2\2\2\u008f\u0090\7\2\2\3\u0090\3\3\2\2")
        buf.write("\2\u0091\u0092\7\26\2\2\u0092\u0095\5H%\2\u0093\u0094")
        buf.write("\7@\2\2\u0094\u0096\5H%\2\u0095\u0093\3\2\2\2\u0095\u0096")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098\7(\2\2\u0098")
        buf.write("\u0099\5\6\4\2\u0099\u009a\7)\2\2\u009a\5\3\2\2\2\u009b")
        buf.write("\u009e\5\b\5\2\u009c\u009e\5\n\6\2\u009d\u009b\3\2\2\2")
        buf.write("\u009d\u009c\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d\3")
        buf.write("\2\2\2\u009f\u00a0\3\2\2\2\u00a0\7\3\2\2\2\u00a1\u009f")
        buf.write("\3\2\2\2\u00a2\u00a3\t\2\2\2\u00a3\u00a4\5\f\7\2\u00a4")
        buf.write("\u00a5\7*\2\2\u00a5\t\3\2\2\2\u00a6\u00aa\5\20\t\2\u00a7")
        buf.write("\u00aa\5\22\n\2\u00a8\u00aa\5\24\13\2\u00a9\u00a6\3\2")
        buf.write("\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa\13")
        buf.write("\3\2\2\2\u00ab\u00b0\7A\2\2\u00ac\u00ad\7+\2\2\u00ad\u00af")
        buf.write("\7A\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0")
        buf.write("\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b3\3\2\2\2")
        buf.write("\u00b2\u00b0\3\2\2\2\u00b3\u00b4\7@\2\2\u00b4\u00b7\5")
        buf.write("\32\16\2\u00b5\u00b6\7\66\2\2\u00b6\u00b8\5\16\b\2\u00b7")
        buf.write("\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\r\3\2\2\2\u00b9")
        buf.write("\u00be\5V,\2\u00ba\u00bb\7+\2\2\u00bb\u00bd\5V,\2\u00bc")
        buf.write("\u00ba\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2")
        buf.write("\u00be\u00bf\3\2\2\2\u00bf\17\3\2\2\2\u00c0\u00be\3\2")
        buf.write("\2\2\u00c1\u00c2\7A\2\2\u00c2\u00c4\7$\2\2\u00c3\u00c5")
        buf.write("\5\26\f\2\u00c4\u00c3\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5")
        buf.write("\u00c6\3\2\2\2\u00c6\u00c7\7%\2\2\u00c7\u00c9\7(\2\2\u00c8")
        buf.write("\u00ca\5N(\2\u00c9\u00c8\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca")
        buf.write("\u00cb\3\2\2\2\u00cb\u00cc\7)\2\2\u00cc\21\3\2\2\2\u00cd")
        buf.write("\u00ce\7\22\2\2\u00ce\u00d0\7$\2\2\u00cf\u00d1\5\26\f")
        buf.write("\2\u00d0\u00cf\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2")
        buf.write("\3\2\2\2\u00d2\u00d3\7%\2\2\u00d3\u00d5\7(\2\2\u00d4\u00d6")
        buf.write("\5N(\2\u00d5\u00d4\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d7")
        buf.write("\3\2\2\2\u00d7\u00d8\7)\2\2\u00d8\23\3\2\2\2\u00d9\u00da")
        buf.write("\7\27\2\2\u00da\u00db\7$\2\2\u00db\u00dc\7%\2\2\u00dc")
        buf.write("\u00de\7(\2\2\u00dd\u00df\5N(\2\u00de\u00dd\3\2\2\2\u00de")
        buf.write("\u00df\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1\7)\2\2")
        buf.write("\u00e1\25\3\2\2\2\u00e2\u00e7\5\30\r\2\u00e3\u00e4\7*")
        buf.write("\2\2\u00e4\u00e6\5\30\r\2\u00e5\u00e3\3\2\2\2\u00e6\u00e9")
        buf.write("\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8")
        buf.write("\27\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea\u00ef\7A\2\2\u00eb")
        buf.write("\u00ec\7+\2\2\u00ec\u00ee\7A\2\2\u00ed\u00eb\3\2\2\2\u00ee")
        buf.write("\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2")
        buf.write("\u00f0\u00f2\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f3\7")
        buf.write("@\2\2\u00f3\u00f4\5\32\16\2\u00f4\31\3\2\2\2\u00f5\u00fb")
        buf.write("\7\20\2\2\u00f6\u00fb\7\25\2\2\u00f7\u00fb\7\32\2\2\u00f8")
        buf.write("\u00fb\7\36\2\2\u00f9\u00fb\5H%\2\u00fa\u00f5\3\2\2\2")
        buf.write("\u00fa\u00f6\3\2\2\2\u00fa\u00f7\3\2\2\2\u00fa\u00f8\3")
        buf.write("\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\33\3\2\2\2\u00fc\u0105")
        buf.write("\5\36\20\2\u00fd\u0105\5\64\33\2\u00fe\u0105\5\66\34\2")
        buf.write("\u00ff\u0105\5<\37\2\u0100\u0105\5B\"\2\u0101\u0105\5")
        buf.write("D#\2\u0102\u0105\5F$\2\u0103\u0105\5J&\2\u0104\u00fc\3")
        buf.write("\2\2\2\u0104\u00fd\3\2\2\2\u0104\u00fe\3\2\2\2\u0104\u00ff")
        buf.write("\3\2\2\2\u0104\u0100\3\2\2\2\u0104\u0101\3\2\2\2\u0104")
        buf.write("\u0102\3\2\2\2\u0104\u0103\3\2\2\2\u0105\35\3\2\2\2\u0106")
        buf.write("\u0109\t\2\2\2\u0107\u010a\5 \21\2\u0108\u010a\5$\23\2")
        buf.write("\u0109\u0107\3\2\2\2\u0109\u0108\3\2\2\2\u010a\u010b\3")
        buf.write("\2\2\2\u010b\u010c\7*\2\2\u010c\37\3\2\2\2\u010d\u010e")
        buf.write("\7A\2\2\u010e\u010f\5\"\22\2\u010f\u0110\5V,\2\u0110!")
        buf.write("\3\2\2\2\u0111\u0112\7+\2\2\u0112\u0113\7A\2\2\u0113\u0114")
        buf.write("\5\"\22\2\u0114\u0115\5V,\2\u0115\u0116\7+\2\2\u0116\u011c")
        buf.write("\3\2\2\2\u0117\u0118\7@\2\2\u0118\u0119\5\32\16\2\u0119")
        buf.write("\u011a\7\66\2\2\u011a\u011c\3\2\2\2\u011b\u0111\3\2\2")
        buf.write("\2\u011b\u0117\3\2\2\2\u011c#\3\2\2\2\u011d\u011e\7A\2")
        buf.write("\2\u011e\u011f\5&\24\2\u011f\u0120\5(\25\2\u0120%\3\2")
        buf.write("\2\2\u0121\u0122\7+\2\2\u0122\u0123\7A\2\2\u0123\u0124")
        buf.write("\5&\24\2\u0124\u0125\5(\25\2\u0125\u0126\7+\2\2\u0126")
        buf.write("\u0129\3\2\2\2\u0127\u0129\7@\2\2\u0128\u0121\3\2\2\2")
        buf.write("\u0128\u0127\3\2\2\2\u0129\'\3\2\2\2\u012a\u012b\7\35")
        buf.write("\2\2\u012b\u012c\7&\2\2\u012c\u012d\5\32\16\2\u012d\u012e")
        buf.write("\7+\2\2\u012e\u012f\5*\26\2\u012f\u0130\7\'\2\2\u0130")
        buf.write(")\3\2\2\2\u0131\u0132\t\3\2\2\u0132+\3\2\2\2\u0133\u0134")
        buf.write("\7\33\2\2\u0134\u0135\7A\2\2\u0135\u0136\7$\2\2\u0136")
        buf.write("\u0137\7%\2\2\u0137-\3\2\2\2\u0138\u0139\5V,\2\u0139\u013a")
        buf.write("\7+\2\2\u013a\u013c\3\2\2\2\u013b\u0138\3\2\2\2\u013c")
        buf.write("\u013f\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e\3\2\2\2")
        buf.write("\u013e\u0140\3\2\2\2\u013f\u013d\3\2\2\2\u0140\u0141\5")
        buf.write("V,\2\u0141/\3\2\2\2\u0142\u0143\5\62\32\2\u0143\u0144")
        buf.write("\7+\2\2\u0144\u0146\3\2\2\2\u0145\u0142\3\2\2\2\u0146")
        buf.write("\u0149\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0148\3\2\2\2")
        buf.write("\u0148\u014a\3\2\2\2\u0149\u0147\3\2\2\2\u014a\u014b\5")
        buf.write("\62\32\2\u014b\61\3\2\2\2\u014c\u014d\7\35\2\2\u014d\u014e")
        buf.write("\7&\2\2\u014e\u014f\5\32\16\2\u014f\u0150\7+\2\2\u0150")
        buf.write("\u0151\7\4\2\2\u0151\u0152\7\'\2\2\u0152\63\3\2\2\2\u0153")
        buf.write("\u0154\5H%\2\u0154\u0155\7>\2\2\u0155\u0157\3\2\2\2\u0156")
        buf.write("\u0153\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\3\2\2\2")
        buf.write("\u0158\u015b\7A\2\2\u0159\u015b\5v<\2\u015a\u0156\3\2")
        buf.write("\2\2\u015a\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015d")
        buf.write("\7\66\2\2\u015d\u015e\5V,\2\u015e\u015f\7*\2\2\u015f\65")
        buf.write("\3\2\2\2\u0160\u0161\58\35\2\u0161\u0162\7*\2\2\u0162")
        buf.write("\67\3\2\2\2\u0163\u0164\7\30\2\2\u0164\u0165\5V,\2\u0165")
        buf.write("\u0166\5:\36\2\u0166\u0167\7 \2\2\u0167\u0169\7(\2\2\u0168")
        buf.write("\u016a\5N(\2\u0169\u0168\3\2\2\2\u0169\u016a\3\2\2\2\u016a")
        buf.write("\u016b\3\2\2\2\u016b\u016c\7)\2\2\u016c9\3\2\2\2\u016d")
        buf.write("\u016e\7\34\2\2\u016e\u016f\5V,\2\u016f\u0171\7(\2\2\u0170")
        buf.write("\u0172\5N(\2\u0171\u0170\3\2\2\2\u0171\u0172\3\2\2\2\u0172")
        buf.write("\u0173\3\2\2\2\u0173\u0174\7)\2\2\u0174\u0176\3\2\2\2")
        buf.write("\u0175\u016d\3\2\2\2\u0176\u0179\3\2\2\2\u0177\u0175\3")
        buf.write("\2\2\2\u0177\u0178\3\2\2\2\u0178;\3\2\2\2\u0179\u0177")
        buf.write("\3\2\2\2\u017a\u017b\7\17\2\2\u017b\u017c\5> \2\u017c")
        buf.write("\u017d\7*\2\2\u017d=\3\2\2\2\u017e\u017f\7$\2\2\u017f")
        buf.write("\u0180\7A\2\2\u0180\u0181\7!\2\2\u0181\u0182\5@!\2\u0182")
        buf.write("\u0183\7,\2\2\u0183\u0186\5@!\2\u0184\u0185\7\37\2\2\u0185")
        buf.write("\u0187\5@!\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187")
        buf.write("\u0188\3\2\2\2\u0188\u0189\7%\2\2\u0189?\3\2\2\2\u018a")
        buf.write("\u018b\7\4\2\2\u018bA\3\2\2\2\u018c\u018d\7\16\2\2\u018d")
        buf.write("\u018e\7*\2\2\u018eC\3\2\2\2\u018f\u0190\7\23\2\2\u0190")
        buf.write("\u0191\7*\2\2\u0191E\3\2\2\2\u0192\u0196\7\"\2\2\u0193")
        buf.write("\u0195\5V,\2\u0194\u0193\3\2\2\2\u0195\u0198\3\2\2\2\u0196")
        buf.write("\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0199\3\2\2\2")
        buf.write("\u0198\u0196\3\2\2\2\u0199\u019a\7*\2\2\u019aG\3\2\2\2")
        buf.write("\u019b\u019c\t\4\2\2\u019cI\3\2\2\2\u019d\u019e\7A\2\2")
        buf.write("\u019e\u01a0\t\5\2\2\u019f\u01a1\7\r\2\2\u01a0\u019f\3")
        buf.write("\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a3")
        buf.write("\7A\2\2\u01a3\u01a5\7$\2\2\u01a4\u01a6\5L\'\2\u01a5\u01a4")
        buf.write("\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7")
        buf.write("\u01a8\7%\2\2\u01a8\u01a9\7*\2\2\u01a9K\3\2\2\2\u01aa")
        buf.write("\u01ab\5V,\2\u01ab\u01ac\7+\2\2\u01ac\u01ae\3\2\2\2\u01ad")
        buf.write("\u01aa\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2")
        buf.write("\u01af\u01b0\3\2\2\2\u01b0\u01b2\3\2\2\2\u01b1\u01af\3")
        buf.write("\2\2\2\u01b2\u01b3\5V,\2\u01b3M\3\2\2\2\u01b4\u01b6\5")
        buf.write("\34\17\2\u01b5\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7")
        buf.write("\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8O\3\2\2\2\u01b9")
        buf.write("\u01ba\7\35\2\2\u01ba\u01c1\7$\2\2\u01bb\u01bd\5T+\2\u01bc")
        buf.write("\u01be\7+\2\2\u01bd\u01bc\3\2\2\2\u01bd\u01be\3\2\2\2")
        buf.write("\u01be\u01c0\3\2\2\2\u01bf\u01bb\3\2\2\2\u01c0\u01c3\3")
        buf.write("\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c4")
        buf.write("\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4\u01c5\7%\2\2\u01c5")
        buf.write("Q\3\2\2\2\u01c6\u01c7\7\35\2\2\u01c7\u01ce\7$\2\2\u01c8")
        buf.write("\u01ca\5P)\2\u01c9\u01cb\7+\2\2\u01ca\u01c9\3\2\2\2\u01ca")
        buf.write("\u01cb\3\2\2\2\u01cb\u01cd\3\2\2\2\u01cc\u01c8\3\2\2\2")
        buf.write("\u01cd\u01d0\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3")
        buf.write("\2\2\2\u01cf\u01d1\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d1\u01d2")
        buf.write("\7%\2\2\u01d2S\3\2\2\2\u01d3\u01d5\7\3\2\2\u01d4\u01d6")
        buf.write("\7+\2\2\u01d5\u01d4\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6")
        buf.write("\u01d8\3\2\2\2\u01d7\u01d3\3\2\2\2\u01d8\u01d9\3\2\2\2")
        buf.write("\u01d9\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2\u01daU\3\2\2")
        buf.write("\2\u01db\u01df\5X-\2\u01dc\u01df\5z>\2\u01dd\u01df\5\u0086")
        buf.write("D\2\u01de\u01db\3\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01dd")
        buf.write("\3\2\2\2\u01dfW\3\2\2\2\u01e0\u01e1\5Z.\2\u01e1\u01e2")
        buf.write("\t\6\2\2\u01e2\u01e3\5Z.\2\u01e3\u01e6\3\2\2\2\u01e4\u01e6")
        buf.write("\5Z.\2\u01e5\u01e0\3\2\2\2\u01e5\u01e4\3\2\2\2\u01e6Y")
        buf.write("\3\2\2\2\u01e7\u01e8\5\\/\2\u01e8\u01e9\t\7\2\2\u01e9")
        buf.write("\u01ea\5\\/\2\u01ea\u01ed\3\2\2\2\u01eb\u01ed\5\\/\2\u01ec")
        buf.write("\u01e7\3\2\2\2\u01ec\u01eb\3\2\2\2\u01ed[\3\2\2\2\u01ee")
        buf.write("\u01ef\b/\1\2\u01ef\u01f0\5^\60\2\u01f0\u01f6\3\2\2\2")
        buf.write("\u01f1\u01f2\f\4\2\2\u01f2\u01f3\t\b\2\2\u01f3\u01f5\5")
        buf.write("^\60\2\u01f4\u01f1\3\2\2\2\u01f5\u01f8\3\2\2\2\u01f6\u01f4")
        buf.write("\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7]\3\2\2\2\u01f8\u01f6")
        buf.write("\3\2\2\2\u01f9\u01fa\b\60\1\2\u01fa\u01fb\5`\61\2\u01fb")
        buf.write("\u0201\3\2\2\2\u01fc\u01fd\f\4\2\2\u01fd\u01fe\t\t\2\2")
        buf.write("\u01fe\u0200\5`\61\2\u01ff\u01fc\3\2\2\2\u0200\u0203\3")
        buf.write("\2\2\2\u0201\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202_")
        buf.write("\3\2\2\2\u0203\u0201\3\2\2\2\u0204\u0205\b\61\1\2\u0205")
        buf.write("\u0206\5b\62\2\u0206\u020c\3\2\2\2\u0207\u0208\f\4\2\2")
        buf.write("\u0208\u0209\t\n\2\2\u0209\u020b\5b\62\2\u020a\u0207\3")
        buf.write("\2\2\2\u020b\u020e\3\2\2\2\u020c\u020a\3\2\2\2\u020c\u020d")
        buf.write("\3\2\2\2\u020da\3\2\2\2\u020e\u020c\3\2\2\2\u020f\u0210")
        buf.write("\7\62\2\2\u0210\u0213\5b\62\2\u0211\u0213\5d\63\2\u0212")
        buf.write("\u020f\3\2\2\2\u0212\u0211\3\2\2\2\u0213c\3\2\2\2\u0214")
        buf.write("\u0215\7.\2\2\u0215\u0218\5d\63\2\u0216\u0218\5f\64\2")
        buf.write("\u0217\u0214\3\2\2\2\u0217\u0216\3\2\2\2\u0218e\3\2\2")
        buf.write("\2\u0219\u021a\5h\65\2\u021a\u021b\5x=\2\u021b\u021e\3")
        buf.write("\2\2\2\u021c\u021e\5h\65\2\u021d\u0219\3\2\2\2\u021d\u021c")
        buf.write("\3\2\2\2\u021eg\3\2\2\2\u021f\u0220\b\65\1\2\u0220\u0221")
        buf.write("\5j\66\2\u0221\u0227\3\2\2\2\u0222\u0223\f\4\2\2\u0223")
        buf.write("\u0224\t\5\2\2\u0224\u0226\5j\66\2\u0225\u0222\3\2\2\2")
        buf.write("\u0226\u0229\3\2\2\2\u0227\u0225\3\2\2\2\u0227\u0228\3")
        buf.write("\2\2\2\u0228i\3\2\2\2\u0229\u0227\3\2\2\2\u022a\u022b")
        buf.write("\7\33\2\2\u022b\u022e\5j\66\2\u022c\u022e\5l\67\2\u022d")
        buf.write("\u022a\3\2\2\2\u022d\u022c\3\2\2\2\u022ek\3\2\2\2\u022f")
        buf.write("\u0238\7\3\2\2\u0230\u0238\7A\2\2\u0231\u0232\7$\2\2\u0232")
        buf.write("\u0233\5X-\2\u0233\u0234\7%\2\2\u0234\u0238\3\2\2\2\u0235")
        buf.write("\u0238\7\21\2\2\u0236\u0238\5z>\2\u0237\u022f\3\2\2\2")
        buf.write("\u0237\u0230\3\2\2\2\u0237\u0231\3\2\2\2\u0237\u0235\3")
        buf.write("\2\2\2\u0237\u0236\3\2\2\2\u0238m\3\2\2\2\u0239\u023a")
        buf.write("\t\13\2\2\u023ao\3\2\2\2\u023b\u023c\t\f\2\2\u023cq\3")
        buf.write("\2\2\2\u023d\u023e\7=\2\2\u023es\3\2\2\2\u023f\u0240\t")
        buf.write("\7\2\2\u0240u\3\2\2\2\u0241\u0242\5V,\2\u0242\u0243\5")
        buf.write("x=\2\u0243w\3\2\2\2\u0244\u0245\7&\2\2\u0245\u0246\5V")
        buf.write(",\2\u0246\u0248\7\'\2\2\u0247\u0249\5x=\2\u0248\u0247")
        buf.write("\3\2\2\2\u0248\u0249\3\2\2\2\u0249y\3\2\2\2\u024a\u024f")
        buf.write("\5|?\2\u024b\u024f\5~@\2\u024c\u024f\5\u0080A\2\u024d")
        buf.write("\u024f\5\u0084C\2\u024e\u024a\3\2\2\2\u024e\u024b\3\2")
        buf.write("\2\2\u024e\u024c\3\2\2\2\u024e\u024d\3\2\2\2\u024f{\3")
        buf.write("\2\2\2\u0250\u0251\5H%\2\u0251\u0252\7>\2\2\u0252\u0253")
        buf.write("\7A\2\2\u0253}\3\2\2\2\u0254\u0255\7A\2\2\u0255\u0256")
        buf.write("\7?\2\2\u0256\u0257\7A\2\2\u0257\177\3\2\2\2\u0258\u0259")
        buf.write("\5H%\2\u0259\u025a\5\u0082B\2\u025a\u0081\3\2\2\2\u025b")
        buf.write("\u025c\7>\2\2\u025c\u025d\7A\2\2\u025d\u025f\7$\2\2\u025e")
        buf.write("\u0260\5\u0088E\2\u025f\u025e\3\2\2\2\u025f\u0260\3\2")
        buf.write("\2\2\u0260\u0261\3\2\2\2\u0261\u0262\7%\2\2\u0262\u0083")
        buf.write("\3\2\2\2\u0263\u0264\7A\2\2\u0264\u0265\7?\2\2\u0265\u0266")
        buf.write("\7A\2\2\u0266\u0268\7$\2\2\u0267\u0269\5\u0088E\2\u0268")
        buf.write("\u0267\3\2\2\2\u0268\u0269\3\2\2\2\u0269\u026a\3\2\2\2")
        buf.write("\u026a\u026b\7%\2\2\u026b\u0085\3\2\2\2\u026c\u026d\7")
        buf.write("\33\2\2\u026d\u026e\7A\2\2\u026e\u0270\7$\2\2\u026f\u0271")
        buf.write("\5\u0088E\2\u0270\u026f\3\2\2\2\u0270\u0271\3\2\2\2\u0271")
        buf.write("\u0272\3\2\2\2\u0272\u0273\7%\2\2\u0273\u0087\3\2\2\2")
        buf.write("\u0274\u0276\5X-\2\u0275\u0277\7+\2\2\u0276\u0275\3\2")
        buf.write("\2\2\u0276\u0277\3\2\2\2\u0277\u0279\3\2\2\2\u0278\u0274")
        buf.write("\3\2\2\2\u0279\u027a\3\2\2\2\u027a\u0278\3\2\2\2\u027a")
        buf.write("\u027b\3\2\2\2\u027b\u0089\3\2\2\2<\u008d\u0095\u009d")
        buf.write("\u009f\u00a9\u00b0\u00b7\u00be\u00c4\u00c9\u00d0\u00d5")
        buf.write("\u00de\u00e7\u00ef\u00fa\u0104\u0109\u011b\u0128\u013d")
        buf.write("\u0147\u0156\u015a\u0169\u0171\u0177\u0186\u0196\u01a0")
        buf.write("\u01a5\u01af\u01b7\u01bd\u01c1\u01ca\u01ce\u01d5\u01d9")
        buf.write("\u01de\u01e5\u01ec\u01f6\u0201\u020c\u0212\u0217\u021d")
        buf.write("\u0227\u022d\u0237\u0248\u024e\u025f\u0268\u0270\u0276")
        buf.write("\u027a")
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

    symbolicNames = [ "<INVALID>", "LITERAL", "LITERAL_INT_DEC", "LITERAL_INT_HEX", 
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
                      "STRING_CONCAT", "DOT", "DOUBLE_SEMI", "COLON", "ID", 
                      "WS", "BLOCK_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_class_body = 2
    RULE_class_attr = 3
    RULE_class_method = 4
    RULE_data_list = 5
    RULE_data_tail = 6
    RULE_normal_method = 7
    RULE_constructor = 8
    RULE_destructor = 9
    RULE_params_list = 10
    RULE_params = 11
    RULE_data_type = 12
    RULE_stmt = 13
    RULE_var_decl = 14
    RULE_pair_list = 15
    RULE_pair = 16
    RULE_pair_list_arr = 17
    RULE_pair_arr = 18
    RULE_array_decl_tail = 19
    RULE_intlit = 20
    RULE_object_decl = 21
    RULE_expr_tail = 22
    RULE_array_type = 23
    RULE_array_type_tail = 24
    RULE_assign_stmt = 25
    RULE_if_stmt = 26
    RULE_if_body = 27
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

    ruleNames =  [ "program", "class_decl", "class_body", "class_attr", 
                   "class_method", "data_list", "data_tail", "normal_method", 
                   "constructor", "destructor", "params_list", "params", 
                   "data_type", "stmt", "var_decl", "pair_list", "pair", 
                   "pair_list_arr", "pair_arr", "array_decl_tail", "intlit", 
                   "object_decl", "expr_tail", "array_type", "array_type_tail", 
                   "assign_stmt", "if_stmt", "if_body", "else_if_body", 
                   "for_in_stmt", "for_in_body", "for_in_expr", "break_stmt", 
                   "continue_stmt", "return_stmt", "class_name", "method_invoc", 
                   "expr_list", "block_stmt", "literal_idx_array", "literal_mtd_array", 
                   "array_element", "all_expr", "op", "op1", "op2", "op3", 
                   "op4", "op5", "op6", "op7", "op8", "op9", "operands", 
                   "arithmetic_ops", "boolean_ops", "string_ops", "relational_ops", 
                   "element_expr", "index_ops", "member_access", "instance_attr", 
                   "static_attr", "instance_method", "instance_method_tail", 
                   "static_method", "object_create", "list_of_expr" ]

    EOF = Token.EOF
    LITERAL=1
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
    DOUBLE_SEMI=61
    COLON=62
    ID=63
    WS=64
    BLOCK_COMMENT=65
    ERROR_CHAR=66
    UNCLOSE_STRING=67
    ILLEGAL_ESCAPE=68

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
            self.state = 137 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 136
                self.class_decl()
                self.state = 139 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 141
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
            self.state = 143
            self.match(D96Parser.CLASS)
            self.state = 144
            self.class_name()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 145
                self.match(D96Parser.COLON)
                self.state = 146
                self.class_name()


            self.state = 149
            self.match(D96Parser.LP)
            self.state = 150
            self.class_body()
            self.state = 151
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
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID))) != 0):
                self.state = 155
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 153
                    self.class_attr()
                    pass
                elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID]:
                    self.state = 154
                    self.class_method()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 159
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

        def data_list(self):
            return self.getTypedRuleContext(D96Parser.Data_listContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_attr




    def class_attr(self):

        localctx = D96Parser.Class_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_attr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 161
            self.data_list()
            self.state = 162
            self.match(D96Parser.SEMI)
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
            if token in [D96Parser.ID]:
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


    class Data_listContext(ParserRuleContext):

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

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def data_tail(self):
            return self.getTypedRuleContext(D96Parser.Data_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_data_list




    def data_list(self):

        localctx = D96Parser.Data_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_data_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(D96Parser.ID)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 170
                self.match(D96Parser.COMMA)
                self.state = 171
                self.match(D96Parser.ID)
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 177
            self.match(D96Parser.COLON)
            self.state = 178
            self.data_type()
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 179
                self.match(D96Parser.ASSIGN)
                self.state = 180
                self.data_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_tailContext(ParserRuleContext):

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
            return D96Parser.RULE_data_tail




    def data_tail(self):

        localctx = D96Parser.Data_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_data_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.all_expr()
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 184
                self.match(D96Parser.COMMA)
                self.state = 185
                self.all_expr()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

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
        self.enterRule(localctx, 14, self.RULE_normal_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(D96Parser.ID)
            self.state = 192
            self.match(D96Parser.LB)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 193
                self.params_list()


            self.state = 196
            self.match(D96Parser.RB)
            self.state = 197
            self.match(D96Parser.LP)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.NULL) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 198
                self.block_stmt()


            self.state = 201
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
        self.enterRule(localctx, 16, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 204
            self.match(D96Parser.LB)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 205
                self.params_list()


            self.state = 208
            self.match(D96Parser.RB)
            self.state = 209
            self.match(D96Parser.LP)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.NULL) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 210
                self.block_stmt()


            self.state = 213
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
        self.enterRule(localctx, 18, self.RULE_destructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(D96Parser.DESTRUCTOR)
            self.state = 216
            self.match(D96Parser.LB)
            self.state = 217
            self.match(D96Parser.RB)
            self.state = 218
            self.match(D96Parser.LP)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.NULL) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 219
                self.block_stmt()


            self.state = 222
            self.match(D96Parser.RP)
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
        self.enterRule(localctx, 20, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.params()
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 225
                self.match(D96Parser.SEMI)
                self.state = 226
                self.params()
                self.state = 231
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
        self.enterRule(localctx, 22, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(D96Parser.ID)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 233
                self.match(D96Parser.COMMA)
                self.state = 234
                self.match(D96Parser.ID)
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 240
            self.match(D96Parser.COLON)
            self.state = 241
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
        self.enterRule(localctx, 24, self.RULE_data_type)
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 245
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 246
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.SELF, D96Parser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 247
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
        self.enterRule(localctx, 26, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 250
                self.var_decl()
                pass

            elif la_ == 2:
                self.state = 251
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.state = 252
                self.if_stmt()
                pass

            elif la_ == 4:
                self.state = 253
                self.for_in_stmt()
                pass

            elif la_ == 5:
                self.state = 254
                self.break_stmt()
                pass

            elif la_ == 6:
                self.state = 255
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.state = 256
                self.return_stmt()
                pass

            elif la_ == 8:
                self.state = 257
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
        self.enterRule(localctx, 28, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 261
                self.pair_list()
                pass

            elif la_ == 2:
                self.state = 262
                self.pair_list_arr()
                pass


            self.state = 265
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
        self.enterRule(localctx, 30, self.RULE_pair_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(D96Parser.ID)
            self.state = 268
            self.pair()
            self.state = 269
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
        self.enterRule(localctx, 32, self.RULE_pair)
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.match(D96Parser.COMMA)
                self.state = 272
                self.match(D96Parser.ID)
                self.state = 273
                self.pair()
                self.state = 274
                self.all_expr()
                self.state = 275
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.match(D96Parser.COLON)
                self.state = 278
                self.data_type()
                self.state = 279
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
        self.enterRule(localctx, 34, self.RULE_pair_list_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(D96Parser.ID)
            self.state = 284
            self.pair_arr()
            self.state = 285
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
        self.enterRule(localctx, 36, self.RULE_pair_arr)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.match(D96Parser.COMMA)
                self.state = 288
                self.match(D96Parser.ID)
                self.state = 289
                self.pair_arr()
                self.state = 290
                self.array_decl_tail()
                self.state = 291
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
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

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def intlit(self):
            return self.getTypedRuleContext(D96Parser.IntlitContext,0)


        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_decl_tail




    def array_decl_tail(self):

        localctx = D96Parser.Array_decl_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_array_decl_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(D96Parser.ARRAY)
            self.state = 297
            self.match(D96Parser.LS)
            self.state = 298
            self.data_type()
            self.state = 299
            self.match(D96Parser.COMMA)
            self.state = 300
            self.intlit()
            self.state = 301
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntlitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LITERAL_INT_BIN(self):
            return self.getToken(D96Parser.LITERAL_INT_BIN, 0)

        def LITERAL_INT_DEC(self):
            return self.getToken(D96Parser.LITERAL_INT_DEC, 0)

        def LITERAL_INT_HEX(self):
            return self.getToken(D96Parser.LITERAL_INT_HEX, 0)

        def LITERAL_INT_OCT(self):
            return self.getToken(D96Parser.LITERAL_INT_OCT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_intlit




    def intlit(self):

        localctx = D96Parser.IntlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_intlit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT_DEC) | (1 << D96Parser.LITERAL_INT_HEX) | (1 << D96Parser.LITERAL_INT_OCT) | (1 << D96Parser.LITERAL_INT_BIN))) != 0)):
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
            self.state = 305
            self.match(D96Parser.NEW)
            self.state = 306
            self.match(D96Parser.ID)
            self.state = 307
            self.match(D96Parser.LB)
            self.state = 308
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_tailContext(ParserRuleContext):

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
            return D96Parser.RULE_expr_tail




    def expr_tail(self):

        localctx = D96Parser.Expr_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 310
                    self.all_expr()
                    self.state = 311
                    self.match(D96Parser.COMMA) 
                self.state = 317
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            self.state = 318
            self.all_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type_tail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Array_type_tailContext)
            else:
                return self.getTypedRuleContext(D96Parser.Array_type_tailContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_array_type




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 320
                    self.array_type_tail()
                    self.state = 321
                    self.match(D96Parser.COMMA) 
                self.state = 327
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 328
            self.array_type_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_type_tailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def LITERAL_INT_DEC(self):
            return self.getToken(D96Parser.LITERAL_INT_DEC, 0)

        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_type_tail




    def array_type_tail(self):

        localctx = D96Parser.Array_type_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_array_type_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(D96Parser.ARRAY)
            self.state = 331
            self.match(D96Parser.LS)
            self.state = 332
            self.data_type()
            self.state = 333
            self.match(D96Parser.COMMA)
            self.state = 334
            self.match(D96Parser.LITERAL_INT_DEC)
            self.state = 335
            self.match(D96Parser.RS)
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

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def element_expr(self):
            return self.getTypedRuleContext(D96Parser.Element_exprContext,0)


        def class_name(self):
            return self.getTypedRuleContext(D96Parser.Class_nameContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 340
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 337
                    self.class_name()
                    self.state = 338
                    self.match(D96Parser.DOT)


                self.state = 342
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 343
                self.element_expr()
                pass


            self.state = 346
            self.match(D96Parser.ASSIGN)
            self.state = 347
            self.all_expr()
            self.state = 348
            self.match(D96Parser.SEMI)
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

        def if_body(self):
            return self.getTypedRuleContext(D96Parser.If_bodyContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.if_body()
            self.state = 351
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def else_if_body(self):
            return self.getTypedRuleContext(D96Parser.Else_if_bodyContext,0)


        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_body




    def if_body(self):

        localctx = D96Parser.If_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_if_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(D96Parser.IF)
            self.state = 354
            self.all_expr()
            self.state = 355
            self.else_if_body()
            self.state = 356
            self.match(D96Parser.ELSE)
            self.state = 357
            self.match(D96Parser.LP)
            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.NULL) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 358
                self.block_stmt()


            self.state = 361
            self.match(D96Parser.RP)
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

        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ELSEIF)
            else:
                return self.getToken(D96Parser.ELSEIF, i)

        def all_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.All_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.All_exprContext,i)


        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LP)
            else:
                return self.getToken(D96Parser.LP, i)

        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RP)
            else:
                return self.getToken(D96Parser.RP, i)

        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.Block_stmtContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_else_if_body




    def else_if_body(self):

        localctx = D96Parser.Else_if_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_else_if_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 363
                self.match(D96Parser.ELSEIF)
                self.state = 364
                self.all_expr()
                self.state = 365
                self.match(D96Parser.LP)
                self.state = 367
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.NULL) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                    self.state = 366
                    self.block_stmt()


                self.state = 369
                self.match(D96Parser.RP)
                self.state = 375
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def for_in_body(self):
            return self.getTypedRuleContext(D96Parser.For_in_bodyContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_for_in_stmt




    def for_in_stmt(self):

        localctx = D96Parser.For_in_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_for_in_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(D96Parser.FOREACH)
            self.state = 377
            self.for_in_body()
            self.state = 378
            self.match(D96Parser.SEMI)
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

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

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

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

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
            self.state = 380
            self.match(D96Parser.LB)
            self.state = 381
            self.match(D96Parser.ID)
            self.state = 382
            self.match(D96Parser.IN)
            self.state = 383
            self.for_in_expr()
            self.state = 384
            self.match(D96Parser.DOTDOT)
            self.state = 385
            self.for_in_expr()
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 386
                self.match(D96Parser.BY)
                self.state = 387
                self.for_in_expr()


            self.state = 390
            self.match(D96Parser.RB)
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

        def LITERAL_INT_DEC(self):
            return self.getToken(D96Parser.LITERAL_INT_DEC, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_for_in_expr




    def for_in_expr(self):

        localctx = D96Parser.For_in_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_for_in_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(D96Parser.LITERAL_INT_DEC)
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
            self.state = 394
            self.match(D96Parser.BREAK)
            self.state = 395
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
            self.state = 397
            self.match(D96Parser.CONTINUE)
            self.state = 398
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
            self.state = 400
            self.match(D96Parser.RETURN)
            self.state = 404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 401
                self.all_expr()
                self.state = 406
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 407
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
            self.state = 409
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def DOUBLE_SEMI(self):
            return self.getToken(D96Parser.DOUBLE_SEMI, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invoc




    def method_invoc(self):

        localctx = D96Parser.Method_invocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_method_invoc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(D96Parser.ID)
            self.state = 412
            _la = self._input.LA(1)
            if not(_la==D96Parser.DOT or _la==D96Parser.DOUBLE_SEMI):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.STATIC:
                self.state = 413
                self.match(D96Parser.STATIC)


            self.state = 416
            self.match(D96Parser.ID)
            self.state = 417
            self.match(D96Parser.LB)
            self.state = 419
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 418
                self.expr_list()


            self.state = 421
            self.match(D96Parser.RB)
            self.state = 422
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
            self.state = 429
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 424
                    self.all_expr()
                    self.state = 425
                    self.match(D96Parser.COMMA) 
                self.state = 431
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

            self.state = 432
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
            self.state = 435 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 434
                self.stmt()
                self.state = 437 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.NULL) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0)):
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
            self.state = 439
            self.match(D96Parser.ARRAY)
            self.state = 440
            self.match(D96Parser.LB)
            self.state = 447
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.LITERAL:
                self.state = 441
                self.array_element()
                self.state = 443
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.COMMA:
                    self.state = 442
                    self.match(D96Parser.COMMA)


                self.state = 449
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 450
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
            self.state = 452
            self.match(D96Parser.ARRAY)
            self.state = 453
            self.match(D96Parser.LB)
            self.state = 460
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ARRAY:
                self.state = 454
                self.literal_idx_array()
                self.state = 456
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.COMMA:
                    self.state = 455
                    self.match(D96Parser.COMMA)


                self.state = 462
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 463
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

        def LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LITERAL)
            else:
                return self.getToken(D96Parser.LITERAL, i)

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
            self.state = 469 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 465
                    self.match(D96Parser.LITERAL)
                    self.state = 467
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        self.state = 466
                        self.match(D96Parser.COMMA)



                else:
                    raise NoViableAltException(self)
                self.state = 471 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

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
            self.state = 476
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 473
                self.op()
                pass

            elif la_ == 2:
                self.state = 474
                self.member_access()
                pass

            elif la_ == 3:
                self.state = 475
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
            self.state = 483
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.op1()
                self.state = 479
                _la = self._input.LA(1)
                if not(_la==D96Parser.EQUAL_STRING or _la==D96Parser.STRING_CONCAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 480
                self.op1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
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
            self.state = 490
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.op2(0)
                self.state = 486
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.LESS_THAN) | (1 << D96Parser.LEQ) | (1 << D96Parser.GREATER_THAN) | (1 << D96Parser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 487
                self.op2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
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
            self.state = 493
            self.op3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 500
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op2)
                    self.state = 495
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 496
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 497
                    self.op3(0) 
                self.state = 502
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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
            self.state = 504
            self.op4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 511
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op3)
                    self.state = 506
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 507
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUBTRACT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 508
                    self.op4(0) 
                self.state = 513
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

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
            self.state = 515
            self.op5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 522
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op4)
                    self.state = 517
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 518
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLY) | (1 << D96Parser.DIVIDE) | (1 << D96Parser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 519
                    self.op5() 
                self.state = 524
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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
            self.state = 528
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 525
                self.match(D96Parser.NOT)
                self.state = 526
                self.op5()
                pass
            elif token in [D96Parser.LITERAL, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.SUBTRACT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 527
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
            self.state = 533
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUBTRACT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self.match(D96Parser.SUBTRACT)
                self.state = 531
                self.op6()
                pass
            elif token in [D96Parser.LITERAL, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 532
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
            self.state = 539
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 535
                self.op8(0)
                self.state = 536
                self.index_ops()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 538
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

        def DOUBLE_SEMI(self):
            return self.getToken(D96Parser.DOUBLE_SEMI, 0)

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
            self.state = 542
            self.op9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 549
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op8)
                    self.state = 544
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 545
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.DOT or _la==D96Parser.DOUBLE_SEMI):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 546
                    self.op9() 
                self.state = 551
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

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
            self.state = 555
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 552
                self.match(D96Parser.NEW)
                self.state = 553
                self.op9()
                pass
            elif token in [D96Parser.LITERAL, D96Parser.NULL, D96Parser.SELF, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 554
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

        def LITERAL(self):
            return self.getToken(D96Parser.LITERAL, 0)

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
            self.state = 565
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 557
                self.match(D96Parser.LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 558
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 559
                self.match(D96Parser.LB)
                self.state = 560
                self.op()
                self.state = 561
                self.match(D96Parser.RB)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 563
                self.match(D96Parser.NULL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 564
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
            self.state = 567
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
            self.state = 569
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
            self.state = 571
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
            self.state = 573
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
            self.state = 575
            self.all_expr()
            self.state = 576
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
            self.state = 578
            self.match(D96Parser.LS)
            self.state = 579
            self.all_expr()
            self.state = 580
            self.match(D96Parser.RS)
            self.state = 582
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 581
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
            self.state = 588
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 584
                self.instance_attr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 585
                self.static_attr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 586
                self.instance_method()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 587
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

        def class_name(self):
            return self.getTypedRuleContext(D96Parser.Class_nameContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_attr




    def instance_attr(self):

        localctx = D96Parser.Instance_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_instance_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 590
            self.class_name()
            self.state = 591
            self.match(D96Parser.DOT)
            self.state = 592
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def DOUBLE_SEMI(self):
            return self.getToken(D96Parser.DOUBLE_SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_attr




    def static_attr(self):

        localctx = D96Parser.Static_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_static_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.match(D96Parser.ID)
            self.state = 595
            self.match(D96Parser.DOUBLE_SEMI)
            self.state = 596
            self.match(D96Parser.ID)
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

        def class_name(self):
            return self.getTypedRuleContext(D96Parser.Class_nameContext,0)


        def instance_method_tail(self):
            return self.getTypedRuleContext(D96Parser.Instance_method_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_instance_method




    def instance_method(self):

        localctx = D96Parser.Instance_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_instance_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 598
            self.class_name()
            self.state = 599
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

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

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
            self.state = 601
            self.match(D96Parser.DOT)
            self.state = 602
            self.match(D96Parser.ID)
            self.state = 603
            self.match(D96Parser.LB)
            self.state = 605
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 604
                self.list_of_expr()


            self.state = 607
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def DOUBLE_SEMI(self):
            return self.getToken(D96Parser.DOUBLE_SEMI, 0)

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
            self.state = 609
            self.match(D96Parser.ID)
            self.state = 610
            self.match(D96Parser.DOUBLE_SEMI)
            self.state = 611
            self.match(D96Parser.ID)
            self.state = 612
            self.match(D96Parser.LB)
            self.state = 614
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 613
                self.list_of_expr()


            self.state = 616
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
            self.state = 618
            self.match(D96Parser.NEW)
            self.state = 619
            self.match(D96Parser.ID)
            self.state = 620
            self.match(D96Parser.LB)
            self.state = 622
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 621
                self.list_of_expr()


            self.state = 624
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
            self.state = 630 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 626
                self.op()
                self.state = 628
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.COMMA:
                    self.state = 627
                    self.match(D96Parser.COMMA)


                self.state = 632 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0)):
                    break

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
         




