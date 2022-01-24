# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
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
        buf.write("\u0284\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\n\4\f\4\16\4\u00a1\13\4\3\5\3\5\3\6\3\6\3\6\5\6\u00a8")
        buf.write("\n\6\3\6\3\6\3\7\3\7\3\7\5\7\u00af\n\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\5\b\u00b7\n\b\3\b\3\b\3\b\5\b\u00bc\n\b\5\b\u00be")
        buf.write("\n\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00cb")
        buf.write("\n\n\3\13\3\13\3\13\3\13\5\13\u00d1\n\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\5\f\u00da\n\f\3\r\3\r\3\r\5\r\u00df")
        buf.write("\n\r\3\r\3\r\3\r\5\r\u00e4\n\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\5\16\u00eb\n\16\3\16\3\16\3\16\5\16\u00f0\n\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\5\17\u00f9\n\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\7\20\u0100\n\20\f\20\16\20\u0103\13\20")
        buf.write("\3\21\3\21\3\21\7\21\u0108\n\21\f\21\16\21\u010b\13\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\5\22\u0115\n")
        buf.write("\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u011f")
        buf.write("\n\23\3\24\3\24\3\24\5\24\u0124\n\24\3\24\3\24\3\25\3")
        buf.write("\25\3\25\5\25\u012b\n\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\5\26\u0133\n\26\3\26\3\26\3\26\5\26\u0138\n\26\5\26\u013a")
        buf.write("\n\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\5\30\u0147\n\30\3\31\3\31\3\31\3\31\5\31\u014d\n")
        buf.write("\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\7\33\u0159\n\33\f\33\16\33\u015c\13\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\5\34\u0164\n\34\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\5\35\u016c\n\35\3\35\3\35\5\35\u0170\n\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\5\36\u0178\n\36\3\36\3\36\5")
        buf.write("\36\u017c\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \5 \u018d\n \3!\5!\u0190\n!\3!\3")
        buf.write("!\3\"\3\"\3\"\3#\3#\3#\3$\3$\7$\u019c\n$\f$\16$\u019f")
        buf.write("\13$\3$\3$\3%\3%\3&\3&\5&\u01a7\n&\3&\3&\3\'\3\'\3\'\7")
        buf.write("\'\u01ae\n\'\f\'\16\'\u01b1\13\'\3\'\3\'\3(\6(\u01b6\n")
        buf.write("(\r(\16(\u01b7\3)\3)\3)\3)\5)\u01be\n)\7)\u01c0\n)\f)")
        buf.write("\16)\u01c3\13)\3)\3)\3*\3*\3*\3*\5*\u01cb\n*\7*\u01cd")
        buf.write("\n*\f*\16*\u01d0\13*\3*\3*\3+\3+\5+\u01d6\n+\6+\u01d8")
        buf.write("\n+\r+\16+\u01d9\3,\3,\3,\5,\u01df\n,\3-\3-\3-\3-\3-\5")
        buf.write("-\u01e6\n-\3.\3.\3.\3.\3.\5.\u01ed\n.\3/\3/\3/\3/\3/\3")
        buf.write("/\7/\u01f5\n/\f/\16/\u01f8\13/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\7\60\u0200\n\60\f\60\16\60\u0203\13\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\7\61\u020b\n\61\f\61\16\61\u020e")
        buf.write("\13\61\3\62\3\62\3\62\5\62\u0213\n\62\3\63\3\63\3\63\5")
        buf.write("\63\u0218\n\63\3\64\3\64\3\64\3\64\5\64\u021e\n\64\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\7\65\u0226\n\65\f\65\16\65\u0229")
        buf.write("\13\65\3\66\3\66\3\66\5\66\u022e\n\66\3\67\3\67\3\67\3")
        buf.write("\67\3\67\3\67\3\67\3\67\5\67\u0238\n\67\38\38\39\39\3")
        buf.write(":\3:\3;\3;\3<\3<\3<\3=\3=\3=\3=\5=\u0249\n=\3>\5>\u024c")
        buf.write("\n>\3>\3>\3>\3>\5>\u0252\n>\3?\5?\u0255\n?\3?\3?\3@\5")
        buf.write("@\u025a\n@\3@\3@\3A\5A\u025f\nA\3A\3A\3A\5A\u0264\nA\3")
        buf.write("A\3A\3B\5B\u0269\nB\3B\3B\3B\5B\u026e\nB\3B\3B\3C\3C\3")
        buf.write("C\3C\5C\u0276\nC\3C\3C\3D\3D\5D\u027c\nD\6D\u027e\nD\r")
        buf.write("D\16D\u027f\3E\3E\3E\2\6\\^`hF\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\2\16")
        buf.write("\3\2\13\f\3\2@A\4\2\"\"@@\3\2;<\4\2\64\64\66:\3\2\62\63")
        buf.write("\3\2,-\3\2.\60\3\2=>\3\2,\60\4\2\61\63;;\4\2\3\3\b\t\2")
        buf.write("\u0295\2\u008b\3\2\2\2\4\u0091\3\2\2\2\6\u009f\3\2\2\2")
        buf.write("\b\u00a2\3\2\2\2\n\u00a4\3\2\2\2\f\u00ab\3\2\2\2\16\u00bd")
        buf.write("\3\2\2\2\20\u00bf\3\2\2\2\22\u00ca\3\2\2\2\24\u00cc\3")
        buf.write("\2\2\2\26\u00d9\3\2\2\2\30\u00db\3\2\2\2\32\u00e7\3\2")
        buf.write("\2\2\34\u00f3\3\2\2\2\36\u00fc\3\2\2\2 \u0104\3\2\2\2")
        buf.write("\"\u0114\3\2\2\2$\u011e\3\2\2\2&\u0120\3\2\2\2(\u0127")
        buf.write("\3\2\2\2*\u0139\3\2\2\2,\u013b\3\2\2\2.\u0146\3\2\2\2")
        buf.write("\60\u0148\3\2\2\2\62\u0152\3\2\2\2\64\u015a\3\2\2\2\66")
        buf.write("\u0163\3\2\2\28\u0165\3\2\2\2:\u0171\3\2\2\2<\u017d\3")
        buf.write("\2\2\2>\u0185\3\2\2\2@\u018f\3\2\2\2B\u0193\3\2\2\2D\u0196")
        buf.write("\3\2\2\2F\u0199\3\2\2\2H\u01a2\3\2\2\2J\u01a6\3\2\2\2")
        buf.write("L\u01af\3\2\2\2N\u01b5\3\2\2\2P\u01b9\3\2\2\2R\u01c6\3")
        buf.write("\2\2\2T\u01d7\3\2\2\2V\u01de\3\2\2\2X\u01e5\3\2\2\2Z\u01ec")
        buf.write("\3\2\2\2\\\u01ee\3\2\2\2^\u01f9\3\2\2\2`\u0204\3\2\2\2")
        buf.write("b\u0212\3\2\2\2d\u0217\3\2\2\2f\u021d\3\2\2\2h\u021f\3")
        buf.write("\2\2\2j\u022d\3\2\2\2l\u0237\3\2\2\2n\u0239\3\2\2\2p\u023b")
        buf.write("\3\2\2\2r\u023d\3\2\2\2t\u023f\3\2\2\2v\u0241\3\2\2\2")
        buf.write("x\u0244\3\2\2\2z\u024b\3\2\2\2|\u0254\3\2\2\2~\u0259\3")
        buf.write("\2\2\2\u0080\u025e\3\2\2\2\u0082\u0268\3\2\2\2\u0084\u0271")
        buf.write("\3\2\2\2\u0086\u027d\3\2\2\2\u0088\u0281\3\2\2\2\u008a")
        buf.write("\u008c\5\4\3\2\u008b\u008a\3\2\2\2\u008c\u008d\3\2\2\2")
        buf.write("\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008f\3")
        buf.write("\2\2\2\u008f\u0090\7\2\2\3\u0090\3\3\2\2\2\u0091\u0092")
        buf.write("\7\25\2\2\u0092\u0095\7@\2\2\u0093\u0094\7?\2\2\u0094")
        buf.write("\u0096\7@\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2")
        buf.write("\u0096\u0097\3\2\2\2\u0097\u0098\7\'\2\2\u0098\u0099\5")
        buf.write("\6\4\2\u0099\u009a\7(\2\2\u009a\5\3\2\2\2\u009b\u009e")
        buf.write("\5\b\5\2\u009c\u009e\5\26\f\2\u009d\u009b\3\2\2\2\u009d")
        buf.write("\u009c\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d\3\2\2\2")
        buf.write("\u009f\u00a0\3\2\2\2\u00a0\7\3\2\2\2\u00a1\u009f\3\2\2")
        buf.write("\2\u00a2\u00a3\5\n\6\2\u00a3\t\3\2\2\2\u00a4\u00a7\t\2")
        buf.write("\2\2\u00a5\u00a8\5\f\7\2\u00a6\u00a8\5\20\t\2\u00a7\u00a5")
        buf.write("\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9")
        buf.write("\u00aa\7)\2\2\u00aa\13\3\2\2\2\u00ab\u00ac\t\3\2\2\u00ac")
        buf.write("\u00ae\5\16\b\2\u00ad\u00af\5V,\2\u00ae\u00ad\3\2\2\2")
        buf.write("\u00ae\u00af\3\2\2\2\u00af\r\3\2\2\2\u00b0\u00b1\7*\2")
        buf.write("\2\u00b1\u00b2\t\3\2\2\u00b2\u00b6\5\16\b\2\u00b3\u00b4")
        buf.write("\5V,\2\u00b4\u00b5\7*\2\2\u00b5\u00b7\3\2\2\2\u00b6\u00b3")
        buf.write("\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00be\3\2\2\2\u00b8")
        buf.write("\u00b9\7?\2\2\u00b9\u00bb\5\"\22\2\u00ba\u00bc\7\65\2")
        buf.write("\2\u00bb\u00ba\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00be")
        buf.write("\3\2\2\2\u00bd\u00b0\3\2\2\2\u00bd\u00b8\3\2\2\2\u00be")
        buf.write("\17\3\2\2\2\u00bf\u00c0\t\3\2\2\u00c0\u00c1\5\22\n\2\u00c1")
        buf.write("\u00c2\5\24\13\2\u00c2\21\3\2\2\2\u00c3\u00c4\7*\2\2\u00c4")
        buf.write("\u00c5\t\3\2\2\u00c5\u00c6\5\22\n\2\u00c6\u00c7\5\24\13")
        buf.write("\2\u00c7\u00c8\7*\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00cb")
        buf.write("\7?\2\2\u00ca\u00c3\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb")
        buf.write("\23\3\2\2\2\u00cc\u00cd\7\34\2\2\u00cd\u00d0\7%\2\2\u00ce")
        buf.write("\u00d1\5\"\22\2\u00cf\u00d1\7\34\2\2\u00d0\u00ce\3\2\2")
        buf.write("\2\u00d0\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3")
        buf.write("\7*\2\2\u00d3\u00d4\7\3\2\2\u00d4\u00d5\7&\2\2\u00d5\25")
        buf.write("\3\2\2\2\u00d6\u00da\5\30\r\2\u00d7\u00da\5\32\16\2\u00d8")
        buf.write("\u00da\5\34\17\2\u00d9\u00d6\3\2\2\2\u00d9\u00d7\3\2\2")
        buf.write("\2\u00d9\u00d8\3\2\2\2\u00da\27\3\2\2\2\u00db\u00dc\t")
        buf.write("\3\2\2\u00dc\u00de\7#\2\2\u00dd\u00df\5\36\20\2\u00de")
        buf.write("\u00dd\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e0\3\2\2\2")
        buf.write("\u00e0\u00e1\7$\2\2\u00e1\u00e3\7\'\2\2\u00e2\u00e4\5")
        buf.write("N(\2\u00e3\u00e2\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5")
        buf.write("\3\2\2\2\u00e5\u00e6\7(\2\2\u00e6\31\3\2\2\2\u00e7\u00e8")
        buf.write("\7\21\2\2\u00e8\u00ea\7#\2\2\u00e9\u00eb\5\36\20\2\u00ea")
        buf.write("\u00e9\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ec\3\2\2\2")
        buf.write("\u00ec\u00ed\7$\2\2\u00ed\u00ef\7\'\2\2\u00ee\u00f0\5")
        buf.write("N(\2\u00ef\u00ee\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f1")
        buf.write("\3\2\2\2\u00f1\u00f2\7(\2\2\u00f2\33\3\2\2\2\u00f3\u00f4")
        buf.write("\7\26\2\2\u00f4\u00f5\7#\2\2\u00f5\u00f6\7$\2\2\u00f6")
        buf.write("\u00f8\7\'\2\2\u00f7\u00f9\5N(\2\u00f8\u00f7\3\2\2\2\u00f8")
        buf.write("\u00f9\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\7(\2\2")
        buf.write("\u00fb\35\3\2\2\2\u00fc\u0101\5 \21\2\u00fd\u00fe\7)\2")
        buf.write("\2\u00fe\u0100\5 \21\2\u00ff\u00fd\3\2\2\2\u0100\u0103")
        buf.write("\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0102\3\2\2\2\u0102")
        buf.write("\37\3\2\2\2\u0103\u0101\3\2\2\2\u0104\u0109\7@\2\2\u0105")
        buf.write("\u0106\7*\2\2\u0106\u0108\7@\2\2\u0107\u0105\3\2\2\2\u0108")
        buf.write("\u010b\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a\3\2\2\2")
        buf.write("\u010a\u010c\3\2\2\2\u010b\u0109\3\2\2\2\u010c\u010d\7")
        buf.write("?\2\2\u010d\u010e\5\"\22\2\u010e!\3\2\2\2\u010f\u0115")
        buf.write("\7\17\2\2\u0110\u0115\7\24\2\2\u0111\u0115\7\31\2\2\u0112")
        buf.write("\u0115\7\35\2\2\u0113\u0115\5H%\2\u0114\u010f\3\2\2\2")
        buf.write("\u0114\u0110\3\2\2\2\u0114\u0111\3\2\2\2\u0114\u0112\3")
        buf.write("\2\2\2\u0114\u0113\3\2\2\2\u0115#\3\2\2\2\u0116\u011f")
        buf.write("\5&\24\2\u0117\u011f\5\64\33\2\u0118\u011f\58\35\2\u0119")
        buf.write("\u011f\5<\37\2\u011a\u011f\5B\"\2\u011b\u011f\5D#\2\u011c")
        buf.write("\u011f\5F$\2\u011d\u011f\5J&\2\u011e\u0116\3\2\2\2\u011e")
        buf.write("\u0117\3\2\2\2\u011e\u0118\3\2\2\2\u011e\u0119\3\2\2\2")
        buf.write("\u011e\u011a\3\2\2\2\u011e\u011b\3\2\2\2\u011e\u011c\3")
        buf.write("\2\2\2\u011e\u011d\3\2\2\2\u011f%\3\2\2\2\u0120\u0123")
        buf.write("\t\2\2\2\u0121\u0124\5(\25\2\u0122\u0124\5,\27\2\u0123")
        buf.write("\u0121\3\2\2\2\u0123\u0122\3\2\2\2\u0124\u0125\3\2\2\2")
        buf.write("\u0125\u0126\7)\2\2\u0126\'\3\2\2\2\u0127\u0128\7@\2\2")
        buf.write("\u0128\u012a\5*\26\2\u0129\u012b\5V,\2\u012a\u0129\3\2")
        buf.write("\2\2\u012a\u012b\3\2\2\2\u012b)\3\2\2\2\u012c\u012d\7")
        buf.write("*\2\2\u012d\u012e\7@\2\2\u012e\u0132\5*\26\2\u012f\u0130")
        buf.write("\5V,\2\u0130\u0131\7*\2\2\u0131\u0133\3\2\2\2\u0132\u012f")
        buf.write("\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u013a\3\2\2\2\u0134")
        buf.write("\u0135\7?\2\2\u0135\u0137\5\"\22\2\u0136\u0138\7\65\2")
        buf.write("\2\u0137\u0136\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u013a")
        buf.write("\3\2\2\2\u0139\u012c\3\2\2\2\u0139\u0134\3\2\2\2\u013a")
        buf.write("+\3\2\2\2\u013b\u013c\7@\2\2\u013c\u013d\5.\30\2\u013d")
        buf.write("\u013e\5\60\31\2\u013e-\3\2\2\2\u013f\u0140\7*\2\2\u0140")
        buf.write("\u0141\7@\2\2\u0141\u0142\5.\30\2\u0142\u0143\5\60\31")
        buf.write("\2\u0143\u0144\7*\2\2\u0144\u0147\3\2\2\2\u0145\u0147")
        buf.write("\7?\2\2\u0146\u013f\3\2\2\2\u0146\u0145\3\2\2\2\u0147")
        buf.write("/\3\2\2\2\u0148\u0149\7\34\2\2\u0149\u014c\7%\2\2\u014a")
        buf.write("\u014d\5\"\22\2\u014b\u014d\7\34\2\2\u014c\u014a\3\2\2")
        buf.write("\2\u014c\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u014f")
        buf.write("\7*\2\2\u014f\u0150\7\3\2\2\u0150\u0151\7&\2\2\u0151\61")
        buf.write("\3\2\2\2\u0152\u0153\7\32\2\2\u0153\u0154\7@\2\2\u0154")
        buf.write("\u0155\7#\2\2\u0155\u0156\7$\2\2\u0156\63\3\2\2\2\u0157")
        buf.write("\u0159\5\66\34\2\u0158\u0157\3\2\2\2\u0159\u015c\3\2\2")
        buf.write("\2\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015d")
        buf.write("\3\2\2\2\u015c\u015a\3\2\2\2\u015d\u015e\7\65\2\2\u015e")
        buf.write("\u015f\5V,\2\u015f\u0160\7)\2\2\u0160\65\3\2\2\2\u0161")
        buf.write("\u0164\5z>\2\u0162\u0164\5v<\2\u0163\u0161\3\2\2\2\u0163")
        buf.write("\u0162\3\2\2\2\u0164\67\3\2\2\2\u0165\u0166\7\27\2\2\u0166")
        buf.write("\u0167\7#\2\2\u0167\u0168\5V,\2\u0168\u0169\7$\2\2\u0169")
        buf.write("\u016b\7\'\2\2\u016a\u016c\5N(\2\u016b\u016a\3\2\2\2\u016b")
        buf.write("\u016c\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016f\7(\2\2")
        buf.write("\u016e\u0170\5:\36\2\u016f\u016e\3\2\2\2\u016f\u0170\3")
        buf.write("\2\2\2\u01709\3\2\2\2\u0171\u0172\7\33\2\2\u0172\u0173")
        buf.write("\7#\2\2\u0173\u0174\5V,\2\u0174\u0175\7$\2\2\u0175\u0177")
        buf.write("\7\'\2\2\u0176\u0178\5N(\2\u0177\u0176\3\2\2\2\u0177\u0178")
        buf.write("\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017b\7(\2\2\u017a")
        buf.write("\u017c\5:\36\2\u017b\u017a\3\2\2\2\u017b\u017c\3\2\2\2")
        buf.write("\u017c;\3\2\2\2\u017d\u017e\7\16\2\2\u017e\u017f\7#\2")
        buf.write("\2\u017f\u0180\5> \2\u0180\u0181\7$\2\2\u0181\u0182\7")
        buf.write("\'\2\2\u0182\u0183\5N(\2\u0183\u0184\7(\2\2\u0184=\3\2")
        buf.write("\2\2\u0185\u0186\7@\2\2\u0186\u0187\7 \2\2\u0187\u0188")
        buf.write("\5@!\2\u0188\u0189\7+\2\2\u0189\u018c\5@!\2\u018a\u018b")
        buf.write("\7\36\2\2\u018b\u018d\5@!\2\u018c\u018a\3\2\2\2\u018c")
        buf.write("\u018d\3\2\2\2\u018d?\3\2\2\2\u018e\u0190\7-\2\2\u018f")
        buf.write("\u018e\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0191\3\2\2\2")
        buf.write("\u0191\u0192\7\3\2\2\u0192A\3\2\2\2\u0193\u0194\7\r\2")
        buf.write("\2\u0194\u0195\7)\2\2\u0195C\3\2\2\2\u0196\u0197\7\22")
        buf.write("\2\2\u0197\u0198\7)\2\2\u0198E\3\2\2\2\u0199\u019d\7!")
        buf.write("\2\2\u019a\u019c\5V,\2\u019b\u019a\3\2\2\2\u019c\u019f")
        buf.write("\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e")
        buf.write("\u01a0\3\2\2\2\u019f\u019d\3\2\2\2\u01a0\u01a1\7)\2\2")
        buf.write("\u01a1G\3\2\2\2\u01a2\u01a3\t\4\2\2\u01a3I\3\2\2\2\u01a4")
        buf.write("\u01a7\5\u0080A\2\u01a5\u01a7\5\u0082B\2\u01a6\u01a4\3")
        buf.write("\2\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a9")
        buf.write("\7)\2\2\u01a9K\3\2\2\2\u01aa\u01ab\5V,\2\u01ab\u01ac\7")
        buf.write("*\2\2\u01ac\u01ae\3\2\2\2\u01ad\u01aa\3\2\2\2\u01ae\u01b1")
        buf.write("\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0")
        buf.write("\u01b2\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01b3\5V,\2\u01b3")
        buf.write("M\3\2\2\2\u01b4\u01b6\5$\23\2\u01b5\u01b4\3\2\2\2\u01b6")
        buf.write("\u01b7\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2")
        buf.write("\u01b8O\3\2\2\2\u01b9\u01ba\7\34\2\2\u01ba\u01c1\7#\2")
        buf.write("\2\u01bb\u01bd\5T+\2\u01bc\u01be\7*\2\2\u01bd\u01bc\3")
        buf.write("\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01c0\3\2\2\2\u01bf\u01bb")
        buf.write("\3\2\2\2\u01c0\u01c3\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1")
        buf.write("\u01c2\3\2\2\2\u01c2\u01c4\3\2\2\2\u01c3\u01c1\3\2\2\2")
        buf.write("\u01c4\u01c5\7$\2\2\u01c5Q\3\2\2\2\u01c6\u01c7\7\34\2")
        buf.write("\2\u01c7\u01ce\7#\2\2\u01c8\u01ca\5P)\2\u01c9\u01cb\7")
        buf.write("*\2\2\u01ca\u01c9\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cd")
        buf.write("\3\2\2\2\u01cc\u01c8\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce")
        buf.write("\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d1\3\2\2\2")
        buf.write("\u01d0\u01ce\3\2\2\2\u01d1\u01d2\7$\2\2\u01d2S\3\2\2\2")
        buf.write("\u01d3\u01d5\5\u0088E\2\u01d4\u01d6\7*\2\2\u01d5\u01d4")
        buf.write("\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d8\3\2\2\2\u01d7")
        buf.write("\u01d3\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01d7\3\2\2\2")
        buf.write("\u01d9\u01da\3\2\2\2\u01daU\3\2\2\2\u01db\u01df\5X-\2")
        buf.write("\u01dc\u01df\5z>\2\u01dd\u01df\5\u0084C\2\u01de\u01db")
        buf.write("\3\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01dd\3\2\2\2\u01df")
        buf.write("W\3\2\2\2\u01e0\u01e1\5Z.\2\u01e1\u01e2\t\5\2\2\u01e2")
        buf.write("\u01e3\5Z.\2\u01e3\u01e6\3\2\2\2\u01e4\u01e6\5Z.\2\u01e5")
        buf.write("\u01e0\3\2\2\2\u01e5\u01e4\3\2\2\2\u01e6Y\3\2\2\2\u01e7")
        buf.write("\u01e8\5\\/\2\u01e8\u01e9\t\6\2\2\u01e9\u01ea\5\\/\2\u01ea")
        buf.write("\u01ed\3\2\2\2\u01eb\u01ed\5\\/\2\u01ec\u01e7\3\2\2\2")
        buf.write("\u01ec\u01eb\3\2\2\2\u01ed[\3\2\2\2\u01ee\u01ef\b/\1\2")
        buf.write("\u01ef\u01f0\5^\60\2\u01f0\u01f6\3\2\2\2\u01f1\u01f2\f")
        buf.write("\4\2\2\u01f2\u01f3\t\7\2\2\u01f3\u01f5\5^\60\2\u01f4\u01f1")
        buf.write("\3\2\2\2\u01f5\u01f8\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f6")
        buf.write("\u01f7\3\2\2\2\u01f7]\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f9")
        buf.write("\u01fa\b\60\1\2\u01fa\u01fb\5`\61\2\u01fb\u0201\3\2\2")
        buf.write("\2\u01fc\u01fd\f\4\2\2\u01fd\u01fe\t\b\2\2\u01fe\u0200")
        buf.write("\5`\61\2\u01ff\u01fc\3\2\2\2\u0200\u0203\3\2\2\2\u0201")
        buf.write("\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202_\3\2\2\2\u0203")
        buf.write("\u0201\3\2\2\2\u0204\u0205\b\61\1\2\u0205\u0206\5b\62")
        buf.write("\2\u0206\u020c\3\2\2\2\u0207\u0208\f\4\2\2\u0208\u0209")
        buf.write("\t\t\2\2\u0209\u020b\5b\62\2\u020a\u0207\3\2\2\2\u020b")
        buf.write("\u020e\3\2\2\2\u020c\u020a\3\2\2\2\u020c\u020d\3\2\2\2")
        buf.write("\u020da\3\2\2\2\u020e\u020c\3\2\2\2\u020f\u0210\7\61\2")
        buf.write("\2\u0210\u0213\5b\62\2\u0211\u0213\5d\63\2\u0212\u020f")
        buf.write("\3\2\2\2\u0212\u0211\3\2\2\2\u0213c\3\2\2\2\u0214\u0215")
        buf.write("\7-\2\2\u0215\u0218\5d\63\2\u0216\u0218\5f\64\2\u0217")
        buf.write("\u0214\3\2\2\2\u0217\u0216\3\2\2\2\u0218e\3\2\2\2\u0219")
        buf.write("\u021a\5h\65\2\u021a\u021b\5x=\2\u021b\u021e\3\2\2\2\u021c")
        buf.write("\u021e\5h\65\2\u021d\u0219\3\2\2\2\u021d\u021c\3\2\2\2")
        buf.write("\u021eg\3\2\2\2\u021f\u0220\b\65\1\2\u0220\u0221\5j\66")
        buf.write("\2\u0221\u0227\3\2\2\2\u0222\u0223\f\4\2\2\u0223\u0224")
        buf.write("\t\n\2\2\u0224\u0226\5j\66\2\u0225\u0222\3\2\2\2\u0226")
        buf.write("\u0229\3\2\2\2\u0227\u0225\3\2\2\2\u0227\u0228\3\2\2\2")
        buf.write("\u0228i\3\2\2\2\u0229\u0227\3\2\2\2\u022a\u022b\7\32\2")
        buf.write("\2\u022b\u022e\5j\66\2\u022c\u022e\5l\67\2\u022d\u022a")
        buf.write("\3\2\2\2\u022d\u022c\3\2\2\2\u022ek\3\2\2\2\u022f\u0238")
        buf.write("\5\u0088E\2\u0230\u0238\7@\2\2\u0231\u0232\7#\2\2\u0232")
        buf.write("\u0233\5X-\2\u0233\u0234\7$\2\2\u0234\u0238\3\2\2\2\u0235")
        buf.write("\u0238\7\20\2\2\u0236\u0238\5z>\2\u0237\u022f\3\2\2\2")
        buf.write("\u0237\u0230\3\2\2\2\u0237\u0231\3\2\2\2\u0237\u0235\3")
        buf.write("\2\2\2\u0237\u0236\3\2\2\2\u0238m\3\2\2\2\u0239\u023a")
        buf.write("\t\13\2\2\u023ao\3\2\2\2\u023b\u023c\t\f\2\2\u023cq\3")
        buf.write("\2\2\2\u023d\u023e\7<\2\2\u023es\3\2\2\2\u023f\u0240\t")
        buf.write("\6\2\2\u0240u\3\2\2\2\u0241\u0242\5V,\2\u0242\u0243\5")
        buf.write("x=\2\u0243w\3\2\2\2\u0244\u0245\7%\2\2\u0245\u0246\5V")
        buf.write(",\2\u0246\u0248\7&\2\2\u0247\u0249\5x=\2\u0248\u0247\3")
        buf.write("\2\2\2\u0248\u0249\3\2\2\2\u0249y\3\2\2\2\u024a\u024c")
        buf.write("\5H%\2\u024b\u024a\3\2\2\2\u024b\u024c\3\2\2\2\u024c\u0251")
        buf.write("\3\2\2\2\u024d\u0252\5|?\2\u024e\u0252\5~@\2\u024f\u0252")
        buf.write("\5\u0080A\2\u0250\u0252\5\u0082B\2\u0251\u024d\3\2\2\2")
        buf.write("\u0251\u024e\3\2\2\2\u0251\u024f\3\2\2\2\u0251\u0250\3")
        buf.write("\2\2\2\u0252{\3\2\2\2\u0253\u0255\7=\2\2\u0254\u0253\3")
        buf.write("\2\2\2\u0254\u0255\3\2\2\2\u0255\u0256\3\2\2\2\u0256\u0257")
        buf.write("\7@\2\2\u0257}\3\2\2\2\u0258\u025a\7>\2\2\u0259\u0258")
        buf.write("\3\2\2\2\u0259\u025a\3\2\2\2\u025a\u025b\3\2\2\2\u025b")
        buf.write("\u025c\7A\2\2\u025c\177\3\2\2\2\u025d\u025f\7=\2\2\u025e")
        buf.write("\u025d\3\2\2\2\u025e\u025f\3\2\2\2\u025f\u0260\3\2\2\2")
        buf.write("\u0260\u0261\7@\2\2\u0261\u0263\7#\2\2\u0262\u0264\5\u0086")
        buf.write("D\2\u0263\u0262\3\2\2\2\u0263\u0264\3\2\2\2\u0264\u0265")
        buf.write("\3\2\2\2\u0265\u0266\7$\2\2\u0266\u0081\3\2\2\2\u0267")
        buf.write("\u0269\7>\2\2\u0268\u0267\3\2\2\2\u0268\u0269\3\2\2\2")
        buf.write("\u0269\u026a\3\2\2\2\u026a\u026b\7A\2\2\u026b\u026d\7")
        buf.write("#\2\2\u026c\u026e\5\u0086D\2\u026d\u026c\3\2\2\2\u026d")
        buf.write("\u026e\3\2\2\2\u026e\u026f\3\2\2\2\u026f\u0270\7$\2\2")
        buf.write("\u0270\u0083\3\2\2\2\u0271\u0272\7\32\2\2\u0272\u0273")
        buf.write("\7@\2\2\u0273\u0275\7#\2\2\u0274\u0276\5\u0086D\2\u0275")
        buf.write("\u0274\3\2\2\2\u0275\u0276\3\2\2\2\u0276\u0277\3\2\2\2")
        buf.write("\u0277\u0278\7$\2\2\u0278\u0085\3\2\2\2\u0279\u027b\5")
        buf.write("X-\2\u027a\u027c\7*\2\2\u027b\u027a\3\2\2\2\u027b\u027c")
        buf.write("\3\2\2\2\u027c\u027e\3\2\2\2\u027d\u0279\3\2\2\2\u027e")
        buf.write("\u027f\3\2\2\2\u027f\u027d\3\2\2\2\u027f\u0280\3\2\2\2")
        buf.write("\u0280\u0087\3\2\2\2\u0281\u0282\t\r\2\2\u0282\u0089\3")
        buf.write("\2\2\2H\u008d\u0095\u009d\u009f\u00a7\u00ae\u00b6\u00bb")
        buf.write("\u00bd\u00ca\u00d0\u00d9\u00de\u00e3\u00ea\u00ef\u00f8")
        buf.write("\u0101\u0109\u0114\u011e\u0123\u012a\u0132\u0137\u0139")
        buf.write("\u0146\u014c\u015a\u0163\u016b\u016f\u0177\u017b\u018c")
        buf.write("\u018f\u019d\u01a6\u01af\u01b7\u01bd\u01c1\u01ca\u01ce")
        buf.write("\u01d5\u01d9\u01de\u01e5\u01ec\u01f6\u0201\u020c\u0212")
        buf.write("\u0217\u021d\u0227\u022d\u0237\u0248\u024b\u0251\u0254")
        buf.write("\u0259\u025e\u0263\u0268\u026d\u0275\u027b\u027f")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'Val'", "'Var'", "'Break'", "'Foreach'", 
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
                      "LITERAL_STRING", "DOUBLE_QUOTE", "VAL", "VAR", "BREAK", 
                      "FOREACH", "INT", "NULL", "CONSTRUCTOR", "CONTINUE", 
                      "TRUE", "FLOAT", "CLASS", "DESTRUCTOR", "IF", "FALSE", 
                      "BOOLEAN", "NEW", "ELSEIF", "ARRAY", "STRING", "BY", 
                      "ELSE", "IN", "RETURN", "SELF", "LB", "RB", "LS", 
                      "RS", "LP", "RP", "SEMI", "COMMA", "DOTDOT", "ADD", 
                      "SUBTRACT", "MULTIPLY", "DIVIDE", "MODULO", "NOT", 
                      "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", "LESS_THAN", 
                      "LEQ", "GREATER_THAN", "GEQ", "EQUAL_STRING", "STRING_CONCAT", 
                      "DOT", "DOUBLE_COLON", "COLON", "ID", "DOLLAR_ID", 
                      "BLOCK_COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_class_body = 2
    RULE_class_attr = 3
    RULE_attr_var_decl = 4
    RULE_attr_pair_list = 5
    RULE_attr_pair = 6
    RULE_attr_pair_list_arr = 7
    RULE_attr_pair_arr = 8
    RULE_attr_array_decl_tail = 9
    RULE_class_method = 10
    RULE_normal_method = 11
    RULE_constructor = 12
    RULE_destructor = 13
    RULE_params_list = 14
    RULE_params = 15
    RULE_data_type = 16
    RULE_stmt = 17
    RULE_var_decl = 18
    RULE_pair_list = 19
    RULE_pair = 20
    RULE_pair_list_arr = 21
    RULE_pair_arr = 22
    RULE_array_decl_tail = 23
    RULE_object_decl = 24
    RULE_assign_stmt = 25
    RULE_assign_lhs = 26
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
    RULE_static_method = 64
    RULE_object_create = 65
    RULE_list_of_expr = 66
    RULE_literal = 67

    ruleNames =  [ "program", "class_decl", "class_body", "class_attr", 
                   "attr_var_decl", "attr_pair_list", "attr_pair", "attr_pair_list_arr", 
                   "attr_pair_arr", "attr_array_decl_tail", "class_method", 
                   "normal_method", "constructor", "destructor", "params_list", 
                   "params", "data_type", "stmt", "var_decl", "pair_list", 
                   "pair", "pair_list_arr", "pair_arr", "array_decl_tail", 
                   "object_decl", "assign_stmt", "assign_lhs", "if_stmt", 
                   "else_if_body", "for_in_stmt", "for_in_body", "for_in_expr", 
                   "break_stmt", "continue_stmt", "return_stmt", "class_name", 
                   "method_invoc", "expr_list", "block_stmt", "literal_idx_array", 
                   "literal_mtd_array", "array_element", "all_expr", "op", 
                   "op1", "op2", "op3", "op4", "op5", "op6", "op7", "op8", 
                   "op9", "operands", "arithmetic_ops", "boolean_ops", "string_ops", 
                   "relational_ops", "element_expr", "index_ops", "member_access", 
                   "instance_attr", "static_attr", "instance_method", "static_method", 
                   "object_create", "list_of_expr", "literal" ]

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
    BREAK=11
    FOREACH=12
    INT=13
    NULL=14
    CONSTRUCTOR=15
    CONTINUE=16
    TRUE=17
    FLOAT=18
    CLASS=19
    DESTRUCTOR=20
    IF=21
    FALSE=22
    BOOLEAN=23
    NEW=24
    ELSEIF=25
    ARRAY=26
    STRING=27
    BY=28
    ELSE=29
    IN=30
    RETURN=31
    SELF=32
    LB=33
    RB=34
    LS=35
    RS=36
    LP=37
    RP=38
    SEMI=39
    COMMA=40
    DOTDOT=41
    ADD=42
    SUBTRACT=43
    MULTIPLY=44
    DIVIDE=45
    MODULO=46
    NOT=47
    AND=48
    OR=49
    EQUAL=50
    ASSIGN=51
    NOT_EQUAL=52
    LESS_THAN=53
    LEQ=54
    GREATER_THAN=55
    GEQ=56
    EQUAL_STRING=57
    STRING_CONCAT=58
    DOT=59
    DOUBLE_COLON=60
    COLON=61
    ID=62
    DOLLAR_ID=63
    BLOCK_COMMENT=64
    WS=65
    UNCLOSE_STRING=66
    ILLEGAL_ESCAPE=67
    ERROR_CHAR=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def class_body(self):
            return self.getTypedRuleContext(D96Parser.Class_bodyContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = D96Parser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(D96Parser.CLASS)
            self.state = 144
            self.match(D96Parser.ID)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 145
                self.match(D96Parser.COLON)
                self.state = 146
                self.match(D96Parser.ID)


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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body" ):
                return visitor.visitClass_body(self)
            else:
                return visitor.visitChildren(self)




    def class_body(self):

        localctx = D96Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 155
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 153
                    self.class_attr()
                    pass
                elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.DOLLAR_ID]:
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_var_decl(self):
            return self.getTypedRuleContext(D96Parser.Attr_var_declContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_attr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_attr" ):
                return visitor.visitClass_attr(self)
            else:
                return visitor.visitChildren(self)




    def class_attr(self):

        localctx = D96Parser.Class_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.attr_var_decl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_var_decl" ):
                return visitor.visitAttr_var_decl(self)
            else:
                return visitor.visitChildren(self)




    def attr_var_decl(self):

        localctx = D96Parser.Attr_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attr_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 163
                self.attr_pair_list()
                pass

            elif la_ == 2:
                self.state = 164
                self.attr_pair_list_arr()
                pass


            self.state = 167
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_pair_listContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_pair_list" ):
                return visitor.visitAttr_pair_list(self)
            else:
                return visitor.visitChildren(self)




    def attr_pair_list(self):

        localctx = D96Parser.Attr_pair_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attr_pair_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 170
            self.attr_pair()
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.DOT) | (1 << D96Parser.DOUBLE_COLON) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 171
                self.all_expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_pairContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_pair" ):
                return visitor.visitAttr_pair(self)
            else:
                return visitor.visitChildren(self)




    def attr_pair(self):

        localctx = D96Parser.Attr_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attr_pair)
        self._la = 0 # Token type
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(D96Parser.COMMA)
                self.state = 175
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 176
                self.attr_pair()
                self.state = 180
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 177
                    self.all_expr()
                    self.state = 178
                    self.match(D96Parser.COMMA)


                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.match(D96Parser.COLON)
                self.state = 183
                self.data_type()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.ASSIGN:
                    self.state = 184
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_pair_list_arr" ):
                return visitor.visitAttr_pair_list_arr(self)
            else:
                return visitor.visitChildren(self)




    def attr_pair_list_arr(self):

        localctx = D96Parser.Attr_pair_list_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attr_pair_list_arr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 190
            self.attr_pair_arr()
            self.state = 191
            self.attr_array_decl_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_pair_arrContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_pair_arr" ):
                return visitor.visitAttr_pair_arr(self)
            else:
                return visitor.visitChildren(self)




    def attr_pair_arr(self):

        localctx = D96Parser.Attr_pair_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attr_pair_arr)
        self._la = 0 # Token type
        try:
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.match(D96Parser.COMMA)
                self.state = 194
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 195
                self.attr_pair_arr()
                self.state = 196
                self.attr_array_decl_tail()
                self.state = 197
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_array_decl_tail" ):
                return visitor.visitAttr_array_decl_tail(self)
            else:
                return visitor.visitChildren(self)




    def attr_array_decl_tail(self):

        localctx = D96Parser.Attr_array_decl_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attr_array_decl_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(D96Parser.ARRAY)
            self.state = 203
            self.match(D96Parser.LS)
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.SELF, D96Parser.ID]:
                self.state = 204
                self.data_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 205
                self.match(D96Parser.ARRAY)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 208
            self.match(D96Parser.COMMA)

            self.state = 209
            self.match(D96Parser.LITERAL_INT)
            self.state = 210
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_methodContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_method" ):
                return visitor.visitClass_method(self)
            else:
                return visitor.visitChildren(self)




    def class_method(self):

        localctx = D96Parser.Class_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_class_method)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.normal_method()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 214
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_method" ):
                return visitor.visitNormal_method(self)
            else:
                return visitor.visitChildren(self)




    def normal_method(self):

        localctx = D96Parser.Normal_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_normal_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 218
            self.match(D96Parser.LB)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 219
                self.params_list()


            self.state = 222
            self.match(D96Parser.RB)
            self.state = 223
            self.match(D96Parser.LP)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.NULL) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ASSIGN) | (1 << D96Parser.DOT) | (1 << D96Parser.DOUBLE_COLON) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 224
                self.block_stmt()


            self.state = 227
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 230
            self.match(D96Parser.LB)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 231
                self.params_list()


            self.state = 234
            self.match(D96Parser.RB)
            self.state = 235
            self.match(D96Parser.LP)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.NULL) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ASSIGN) | (1 << D96Parser.DOT) | (1 << D96Parser.DOUBLE_COLON) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 236
                self.block_stmt()


            self.state = 239
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor" ):
                return visitor.visitDestructor(self)
            else:
                return visitor.visitChildren(self)




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_destructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(D96Parser.DESTRUCTOR)
            self.state = 242
            self.match(D96Parser.LB)
            self.state = 243
            self.match(D96Parser.RB)
            self.state = 244
            self.match(D96Parser.LP)
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.NULL) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ASSIGN) | (1 << D96Parser.DOT) | (1 << D96Parser.DOUBLE_COLON) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 245
                self.block_stmt()


            self.state = 248
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_listContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_list" ):
                return visitor.visitParams_list(self)
            else:
                return visitor.visitChildren(self)




    def params_list(self):

        localctx = D96Parser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.params()
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 251
                self.match(D96Parser.SEMI)
                self.state = 252
                self.params()
                self.state = 257
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = D96Parser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(D96Parser.ID)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 259
                self.match(D96Parser.COMMA)
                self.state = 260
                self.match(D96Parser.ID)
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 266
            self.match(D96Parser.COLON)
            self.state = 267
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = D96Parser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_data_type)
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 271
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 272
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.SELF, D96Parser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 273
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 276
                self.var_decl()
                pass

            elif la_ == 2:
                self.state = 277
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.state = 278
                self.if_stmt()
                pass

            elif la_ == 4:
                self.state = 279
                self.for_in_stmt()
                pass

            elif la_ == 5:
                self.state = 280
                self.break_stmt()
                pass

            elif la_ == 6:
                self.state = 281
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.state = 282
                self.return_stmt()
                pass

            elif la_ == 8:
                self.state = 283
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = D96Parser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 287
                self.pair_list()
                pass

            elif la_ == 2:
                self.state = 288
                self.pair_list_arr()
                pass


            self.state = 291
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pair_listContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair_list" ):
                return visitor.visitPair_list(self)
            else:
                return visitor.visitChildren(self)




    def pair_list(self):

        localctx = D96Parser.Pair_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_pair_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(D96Parser.ID)
            self.state = 294
            self.pair()
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.DOT) | (1 << D96Parser.DOUBLE_COLON) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 295
                self.all_expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair" ):
                return visitor.visitPair(self)
            else:
                return visitor.visitChildren(self)




    def pair(self):

        localctx = D96Parser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_pair)
        self._la = 0 # Token type
        try:
            self.state = 311
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.match(D96Parser.COMMA)
                self.state = 299
                self.match(D96Parser.ID)
                self.state = 300
                self.pair()
                self.state = 304
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 301
                    self.all_expr()
                    self.state = 302
                    self.match(D96Parser.COMMA)


                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.match(D96Parser.COLON)
                self.state = 307
                self.data_type()
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.ASSIGN:
                    self.state = 308
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair_list_arr" ):
                return visitor.visitPair_list_arr(self)
            else:
                return visitor.visitChildren(self)




    def pair_list_arr(self):

        localctx = D96Parser.Pair_list_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_pair_list_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(D96Parser.ID)
            self.state = 314
            self.pair_arr()
            self.state = 315
            self.array_decl_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pair_arrContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair_arr" ):
                return visitor.visitPair_arr(self)
            else:
                return visitor.visitChildren(self)




    def pair_arr(self):

        localctx = D96Parser.Pair_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_pair_arr)
        try:
            self.state = 324
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.match(D96Parser.COMMA)
                self.state = 318
                self.match(D96Parser.ID)
                self.state = 319
                self.pair_arr()
                self.state = 320
                self.array_decl_tail()
                self.state = 321
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
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
        __slots__ = 'parser'

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
            return D96Parser.RULE_array_decl_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl_tail" ):
                return visitor.visitArray_decl_tail(self)
            else:
                return visitor.visitChildren(self)




    def array_decl_tail(self):

        localctx = D96Parser.Array_decl_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_array_decl_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(D96Parser.ARRAY)
            self.state = 327
            self.match(D96Parser.LS)
            self.state = 330
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.SELF, D96Parser.ID]:
                self.state = 328
                self.data_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 329
                self.match(D96Parser.ARRAY)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 332
            self.match(D96Parser.COMMA)

            self.state = 333
            self.match(D96Parser.LITERAL_INT)
            self.state = 334
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_declContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_decl" ):
                return visitor.visitObject_decl(self)
            else:
                return visitor.visitChildren(self)




    def object_decl(self):

        localctx = D96Parser.Object_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_object_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(D96Parser.NEW)
            self.state = 337
            self.match(D96Parser.ID)
            self.state = 338
            self.match(D96Parser.LB)
            self.state = 339
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def assign_lhs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Assign_lhsContext)
            else:
                return self.getTypedRuleContext(D96Parser.Assign_lhsContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assign_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.DOT) | (1 << D96Parser.DOUBLE_COLON) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 341
                self.assign_lhs()
                self.state = 346
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 347
            self.match(D96Parser.ASSIGN)
            self.state = 348
            self.all_expr()
            self.state = 349
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_access(self):
            return self.getTypedRuleContext(D96Parser.Member_accessContext,0)


        def element_expr(self):
            return self.getTypedRuleContext(D96Parser.Element_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_lhs" ):
                return visitor.visitAssign_lhs(self)
            else:
                return visitor.visitChildren(self)




    def assign_lhs(self):

        localctx = D96Parser.Assign_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assign_lhs)
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.member_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.element_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(D96Parser.IF)
            self.state = 356
            self.match(D96Parser.LB)
            self.state = 357
            self.all_expr()
            self.state = 358
            self.match(D96Parser.RB)
            self.state = 359
            self.match(D96Parser.LP)
            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.NULL) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ASSIGN) | (1 << D96Parser.DOT) | (1 << D96Parser.DOUBLE_COLON) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 360
                self.block_stmt()


            self.state = 363
            self.match(D96Parser.RP)
            self.state = 365
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSEIF:
                self.state = 364
                self.else_if_body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_body" ):
                return visitor.visitElse_if_body(self)
            else:
                return visitor.visitChildren(self)




    def else_if_body(self):

        localctx = D96Parser.Else_if_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_else_if_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(D96Parser.ELSEIF)
            self.state = 368
            self.match(D96Parser.LB)
            self.state = 369
            self.all_expr()
            self.state = 370
            self.match(D96Parser.RB)
            self.state = 371
            self.match(D96Parser.LP)
            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.NULL) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ASSIGN) | (1 << D96Parser.DOT) | (1 << D96Parser.DOUBLE_COLON) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 372
                self.block_stmt()


            self.state = 375
            self.match(D96Parser.RP)
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSEIF:
                self.state = 376
                self.else_if_body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_in_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_in_stmt" ):
                return visitor.visitFor_in_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_in_stmt(self):

        localctx = D96Parser.For_in_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_for_in_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(D96Parser.FOREACH)
            self.state = 380
            self.match(D96Parser.LB)
            self.state = 381
            self.for_in_body()
            self.state = 382
            self.match(D96Parser.RB)
            self.state = 383
            self.match(D96Parser.LP)
            self.state = 384
            self.block_stmt()
            self.state = 385
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_in_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_in_body" ):
                return visitor.visitFor_in_body(self)
            else:
                return visitor.visitChildren(self)




    def for_in_body(self):

        localctx = D96Parser.For_in_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_for_in_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(D96Parser.ID)
            self.state = 388
            self.match(D96Parser.IN)
            self.state = 389
            self.for_in_expr()
            self.state = 390
            self.match(D96Parser.DOTDOT)
            self.state = 391
            self.for_in_expr()
            self.state = 394
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 392
                self.match(D96Parser.BY)
                self.state = 393
                self.for_in_expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_in_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LITERAL_INT(self):
            return self.getToken(D96Parser.LITERAL_INT, 0)

        def SUBTRACT(self):
            return self.getToken(D96Parser.SUBTRACT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_for_in_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_in_expr" ):
                return visitor.visitFor_in_expr(self)
            else:
                return visitor.visitChildren(self)




    def for_in_expr(self):

        localctx = D96Parser.For_in_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_for_in_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.SUBTRACT:
                self.state = 396
                self.match(D96Parser.SUBTRACT)


            self.state = 399
            self.match(D96Parser.LITERAL_INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(D96Parser.BREAK)
            self.state = 402
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = D96Parser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(D96Parser.CONTINUE)
            self.state = 405
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(D96Parser.RETURN)
            self.state = 411
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.DOT) | (1 << D96Parser.DOUBLE_COLON) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 408
                self.all_expr()
                self.state = 413
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 414
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_name" ):
                return visitor.visitClass_name(self)
            else:
                return visitor.visitChildren(self)




    def class_name(self):

        localctx = D96Parser.Class_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_class_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invoc" ):
                return visitor.visitMethod_invoc(self)
            else:
                return visitor.visitChildren(self)




    def method_invoc(self):

        localctx = D96Parser.Method_invocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_method_invoc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.DOT, D96Parser.ID]:
                self.state = 418
                self.instance_method()
                pass
            elif token in [D96Parser.DOUBLE_COLON, D96Parser.DOLLAR_ID]:
                self.state = 419
                self.static_method()
                pass
            else:
                raise NoViableAltException(self)

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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = D96Parser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 424
                    self.all_expr()
                    self.state = 425
                    self.match(D96Parser.COMMA) 
                self.state = 431
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.NULL) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ASSIGN) | (1 << D96Parser.DOT) | (1 << D96Parser.DOUBLE_COLON) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_idx_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_idx_array" ):
                return visitor.visitLiteral_idx_array(self)
            else:
                return visitor.visitChildren(self)




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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING))) != 0):
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_mtd_array" ):
                return visitor.visitLiteral_mtd_array(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element" ):
                return visitor.visitArray_element(self)
            else:
                return visitor.visitChildren(self)




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
                    self.literal()
                    self.state = 467
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                    if la_ == 1:
                        self.state = 466
                        self.match(D96Parser.COMMA)



                else:
                    raise NoViableAltException(self)
                self.state = 471 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_exprContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_expr" ):
                return visitor.visitAll_expr(self)
            else:
                return visitor.visitChildren(self)




    def all_expr(self):

        localctx = D96Parser.All_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_all_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)




    def op(self):

        localctx = D96Parser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.state = 483
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp1" ):
                return visitor.visitOp1(self)
            else:
                return visitor.visitChildren(self)




    def op1(self):

        localctx = D96Parser.Op1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_op1)
        self._la = 0 # Token type
        try:
            self.state = 490
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp2" ):
                return visitor.visitOp2(self)
            else:
                return visitor.visitChildren(self)



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
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
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
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Op3Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp3" ):
                return visitor.visitOp3(self)
            else:
                return visitor.visitChildren(self)



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
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
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
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Op4Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp4" ):
                return visitor.visitOp4(self)
            else:
                return visitor.visitChildren(self)



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
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
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
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Op5Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp5" ):
                return visitor.visitOp5(self)
            else:
                return visitor.visitChildren(self)




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
            elif token in [D96Parser.LITERAL_INT, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.SUBTRACT, D96Parser.DOT, D96Parser.DOUBLE_COLON, D96Parser.ID, D96Parser.DOLLAR_ID]:
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp6" ):
                return visitor.visitOp6(self)
            else:
                return visitor.visitChildren(self)




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
            elif token in [D96Parser.LITERAL_INT, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.DOT, D96Parser.DOUBLE_COLON, D96Parser.ID, D96Parser.DOLLAR_ID]:
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op8(self):
            return self.getTypedRuleContext(D96Parser.Op8Context,0)


        def index_ops(self):
            return self.getTypedRuleContext(D96Parser.Index_opsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_op7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp7" ):
                return visitor.visitOp7(self)
            else:
                return visitor.visitChildren(self)




    def op7(self):

        localctx = D96Parser.Op7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_op7)
        try:
            self.state = 539
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp8" ):
                return visitor.visitOp8(self)
            else:
                return visitor.visitChildren(self)



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
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
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
                    if not(_la==D96Parser.DOT or _la==D96Parser.DOUBLE_COLON):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 546
                    self.op9() 
                self.state = 551
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Op9Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp9" ):
                return visitor.visitOp9(self)
            else:
                return visitor.visitChildren(self)




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
            elif token in [D96Parser.LITERAL_INT, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.SELF, D96Parser.LB, D96Parser.DOT, D96Parser.DOUBLE_COLON, D96Parser.ID, D96Parser.DOLLAR_ID]:
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_operands)
        try:
            self.state = 565
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 557
                self.literal()
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic_ops" ):
                return visitor.visitArithmetic_ops(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_ops" ):
                return visitor.visitBoolean_ops(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_CONCAT(self):
            return self.getToken(D96Parser.STRING_CONCAT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_string_ops

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_ops" ):
                return visitor.visitString_ops(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_ops" ):
                return visitor.visitRelational_ops(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def index_ops(self):
            return self.getTypedRuleContext(D96Parser.Index_opsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_element_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_expr" ):
                return visitor.visitElement_expr(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_ops" ):
                return visitor.visitIndex_ops(self)
            else:
                return visitor.visitChildren(self)




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
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
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
        __slots__ = 'parser'

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


        def class_name(self):
            return self.getTypedRuleContext(D96Parser.Class_nameContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_access" ):
                return visitor.visitMember_access(self)
            else:
                return visitor.visitChildren(self)




    def member_access(self):

        localctx = D96Parser.Member_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_member_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.state = 584
                self.class_name()


            self.state = 591
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.state = 587
                self.instance_attr()
                pass

            elif la_ == 2:
                self.state = 588
                self.static_attr()
                pass

            elif la_ == 3:
                self.state = 589
                self.instance_method()
                pass

            elif la_ == 4:
                self.state = 590
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_attr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_attr" ):
                return visitor.visitInstance_attr(self)
            else:
                return visitor.visitChildren(self)




    def instance_attr(self):

        localctx = D96Parser.Instance_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_instance_attr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.DOT:
                self.state = 593
                self.match(D96Parser.DOT)


            self.state = 596
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_attrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_attr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_attr" ):
                return visitor.visitStatic_attr(self)
            else:
                return visitor.visitChildren(self)




    def static_attr(self):

        localctx = D96Parser.Static_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_static_attr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.DOUBLE_COLON:
                self.state = 598
                self.match(D96Parser.DOUBLE_COLON)


            self.state = 601
            self.match(D96Parser.DOLLAR_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def list_of_expr(self):
            return self.getTypedRuleContext(D96Parser.List_of_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_instance_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method" ):
                return visitor.visitInstance_method(self)
            else:
                return visitor.visitChildren(self)




    def instance_method(self):

        localctx = D96Parser.Instance_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_instance_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.DOT:
                self.state = 603
                self.match(D96Parser.DOT)


            self.state = 606
            self.match(D96Parser.ID)
            self.state = 607
            self.match(D96Parser.LB)
            self.state = 609
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.DOT) | (1 << D96Parser.DOUBLE_COLON) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 608
                self.list_of_expr()


            self.state = 611
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def list_of_expr(self):
            return self.getTypedRuleContext(D96Parser.List_of_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method" ):
                return visitor.visitStatic_method(self)
            else:
                return visitor.visitChildren(self)




    def static_method(self):

        localctx = D96Parser.Static_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_static_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.DOUBLE_COLON:
                self.state = 613
                self.match(D96Parser.DOUBLE_COLON)


            self.state = 616
            self.match(D96Parser.DOLLAR_ID)
            self.state = 617
            self.match(D96Parser.LB)
            self.state = 619
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.DOT) | (1 << D96Parser.DOUBLE_COLON) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 618
                self.list_of_expr()


            self.state = 621
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_createContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_create" ):
                return visitor.visitObject_create(self)
            else:
                return visitor.visitChildren(self)




    def object_create(self):

        localctx = D96Parser.Object_createContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_object_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 623
            self.match(D96Parser.NEW)
            self.state = 624
            self.match(D96Parser.ID)
            self.state = 625
            self.match(D96Parser.LB)
            self.state = 627
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.DOT) | (1 << D96Parser.DOUBLE_COLON) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 626
                self.list_of_expr()


            self.state = 629
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_exprContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_expr" ):
                return visitor.visitList_of_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_of_expr(self):

        localctx = D96Parser.List_of_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_list_of_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 631
                self.op()
                self.state = 633
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.COMMA:
                    self.state = 632
                    self.match(D96Parser.COMMA)


                self.state = 637 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.DOT) | (1 << D96Parser.DOUBLE_COLON) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 639
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
         




