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
        buf.write("\u0303\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2\6\2\u0098")
        buf.write("\n\2\r\2\16\2\u0099\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u00a2")
        buf.write("\n\3\3\3\3\3\7\3\u00a6\n\3\f\3\16\3\u00a9\13\3\3\3\3\3")
        buf.write("\3\4\3\4\5\4\u00af\n\4\3\5\3\5\3\5\3\5\5\5\u00b5\n\5\3")
        buf.write("\6\3\6\3\6\3\6\7\6\u00bb\n\6\f\6\16\6\u00be\13\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\5\b\u00d4\n\b\3\t\3\t\3\t\3\t\7\t")
        buf.write("\u00da\n\t\f\t\16\t\u00dd\13\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\5\13\u00f3\n\13\3\f\3\f\3\f\3\f\5\f\u00f9")
        buf.write("\n\f\3\f\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16\5\16\u0104")
        buf.write("\n\16\3\17\3\17\3\17\5\17\u0109\n\17\3\17\3\17\3\17\5")
        buf.write("\17\u010e\n\17\3\17\3\17\3\20\3\20\3\20\5\20\u0115\n\20")
        buf.write("\3\20\3\20\3\20\5\20\u011a\n\20\3\20\3\20\3\21\3\21\3")
        buf.write("\21\3\21\3\21\5\21\u0123\n\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u0131\n\22\3")
        buf.write("\23\3\23\3\23\3\23\5\23\u0137\n\23\3\24\3\24\3\24\3\24")
        buf.write("\7\24\u013d\n\24\f\24\16\24\u0140\13\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0156\n\26\3\27\3")
        buf.write("\27\3\27\3\27\7\27\u015c\n\27\f\27\16\27\u015f\13\27\3")
        buf.write("\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0175")
        buf.write("\n\31\3\32\3\32\3\32\3\32\5\32\u017b\n\32\3\32\3\32\3")
        buf.write("\32\3\32\3\33\3\33\5\33\u0183\n\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\5\35\u018c\n\35\3\36\3\36\3\36\7\36\u0191")
        buf.write("\n\36\f\36\16\36\u0194\13\36\3\37\3\37\3\37\7\37\u0199")
        buf.write("\n\37\f\37\16\37\u019c\13\37\3\37\3\37\3\37\5\37\u01a1")
        buf.write("\n\37\3 \3 \5 \u01a5\n \3!\3!\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\5\"\u01af\n\"\3\"\3\"\3\"\5\"\u01b4\n\"\3#\3#\3#\3#\3")
        buf.write("#\3#\5#\u01bc\n#\3#\3#\3#\5#\u01c1\n#\3$\3$\3$\5$\u01c6")
        buf.write("\n$\3$\3$\3%\3%\3%\3%\3%\3%\5%\u01d0\n%\3%\3%\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\5&\u01db\n&\3\'\3\'\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\5(\u01e7\n(\3(\3(\3(\7(\u01ec\n(\f(\16(\u01ef\13")
        buf.write("(\3)\3)\3)\3*\3*\3*\3+\3+\5+\u01f9\n+\3+\3+\3,\3,\3,\3")
        buf.write(",\3,\3-\3-\3-\3-\3-\3.\3.\5.\u0209\n.\3.\3.\3/\6/\u020e")
        buf.write("\n/\r/\16/\u020f\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u0218")
        buf.write("\n\60\3\60\3\60\3\60\3\60\5\60\u021e\n\60\3\60\3\60\7")
        buf.write("\60\u0222\n\60\f\60\16\60\u0225\13\60\3\61\3\61\3\61\7")
        buf.write("\61\u022a\n\61\f\61\16\61\u022d\13\61\3\61\3\61\3\62\3")
        buf.write("\62\3\62\5\62\u0234\n\62\3\62\3\62\3\63\3\63\5\63\u023a")
        buf.write("\n\63\3\64\3\64\3\64\3\64\3\64\5\64\u0241\n\64\3\65\3")
        buf.write("\65\3\65\3\65\3\65\5\65\u0248\n\65\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\7\66\u0250\n\66\f\66\16\66\u0253\13\66\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\7\67\u025b\n\67\f\67\16\67\u025e")
        buf.write("\13\67\38\38\38\38\38\38\78\u0266\n8\f8\168\u0269\138")
        buf.write("\39\39\39\59\u026e\n9\3:\3:\3:\5:\u0273\n:\3;\3;\3;\3")
        buf.write(";\3;\6;\u027a\n;\r;\16;\u027b\7;\u027e\n;\f;\16;\u0281")
        buf.write("\13;\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\5=\u028e\n=\7=\u0290")
        buf.write("\n=\f=\16=\u0293\13=\3>\3>\3>\3>\5>\u0299\n>\3>\5>\u029c")
        buf.write("\n>\3?\3?\3?\3?\5?\u02a2\n?\3?\3?\3?\5?\u02a7\n?\3@\3")
        buf.write("@\3@\3@\3@\3@\3@\3@\3@\5@\u02b2\n@\3A\3A\3B\3B\3B\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\7B\u02c0\nB\fB\16B\u02c3\13B\3C\3C\3")
        buf.write("C\3C\5C\u02c9\nC\3D\3D\3D\5D\u02ce\nD\3D\3D\3E\3E\3E\3")
        buf.write("E\5E\u02d6\nE\3E\3E\3F\3F\3F\7F\u02dd\nF\fF\16F\u02e0")
        buf.write("\13F\3G\3G\3H\3H\5H\u02e6\nH\3I\3I\3I\5I\u02eb\nI\3I\3")
        buf.write("I\3J\3J\3J\3J\3J\7J\u02f4\nJ\fJ\16J\u02f7\13J\3J\3J\3")
        buf.write("K\3K\3K\7K\u02fe\nK\fK\16K\u0301\13K\3K\2\nN^jlntx\u0082")
        buf.write("L\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094")
        buf.write("\2\f\3\2\r\16\3\2CD\6\2\22\22\27\27\34\34  \4\2%%CC\3")
        buf.write("\2>?\4\2\67\679=\3\2\65\66\3\2/\60\3\2\61\63\4\2\3\5\n")
        buf.write("\13\2\u0317\2\u0097\3\2\2\2\4\u009d\3\2\2\2\6\u00ae\3")
        buf.write("\2\2\2\b\u00b4\3\2\2\2\n\u00b6\3\2\2\2\f\u00c3\3\2\2\2")
        buf.write("\16\u00d3\3\2\2\2\20\u00d5\3\2\2\2\22\u00e2\3\2\2\2\24")
        buf.write("\u00f2\3\2\2\2\26\u00f4\3\2\2\2\30\u00fe\3\2\2\2\32\u0103")
        buf.write("\3\2\2\2\34\u0105\3\2\2\2\36\u0111\3\2\2\2 \u011d\3\2")
        buf.write("\2\2\"\u0130\3\2\2\2$\u0136\3\2\2\2&\u0138\3\2\2\2(\u0145")
        buf.write("\3\2\2\2*\u0155\3\2\2\2,\u0157\3\2\2\2.\u0164\3\2\2\2")
        buf.write("\60\u0174\3\2\2\2\62\u0176\3\2\2\2\64\u0182\3\2\2\2\66")
        buf.write("\u0184\3\2\2\28\u0189\3\2\2\2:\u018d\3\2\2\2<\u0195\3")
        buf.write("\2\2\2>\u01a4\3\2\2\2@\u01a6\3\2\2\2B\u01a8\3\2\2\2D\u01b5")
        buf.write("\3\2\2\2F\u01c2\3\2\2\2H\u01c9\3\2\2\2J\u01d3\3\2\2\2")
        buf.write("L\u01dc\3\2\2\2N\u01e6\3\2\2\2P\u01f0\3\2\2\2R\u01f3\3")
        buf.write("\2\2\2T\u01f6\3\2\2\2V\u01fc\3\2\2\2X\u0201\3\2\2\2Z\u0206")
        buf.write("\3\2\2\2\\\u020d\3\2\2\2^\u0217\3\2\2\2`\u022b\3\2\2\2")
        buf.write("b\u0230\3\2\2\2d\u0239\3\2\2\2f\u0240\3\2\2\2h\u0247\3")
        buf.write("\2\2\2j\u0249\3\2\2\2l\u0254\3\2\2\2n\u025f\3\2\2\2p\u026d")
        buf.write("\3\2\2\2r\u0272\3\2\2\2t\u0274\3\2\2\2v\u0282\3\2\2\2")
        buf.write("x\u0286\3\2\2\2z\u029b\3\2\2\2|\u02a6\3\2\2\2~\u02b1\3")
        buf.write("\2\2\2\u0080\u02b3\3\2\2\2\u0082\u02b5\3\2\2\2\u0084\u02c4")
        buf.write("\3\2\2\2\u0086\u02ca\3\2\2\2\u0088\u02d1\3\2\2\2\u008a")
        buf.write("\u02d9\3\2\2\2\u008c\u02e1\3\2\2\2\u008e\u02e5\3\2\2\2")
        buf.write("\u0090\u02e7\3\2\2\2\u0092\u02ee\3\2\2\2\u0094\u02fa\3")
        buf.write("\2\2\2\u0096\u0098\5\4\3\2\u0097\u0096\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a")
        buf.write("\u009b\3\2\2\2\u009b\u009c\7\2\2\3\u009c\3\3\2\2\2\u009d")
        buf.write("\u009e\7\30\2\2\u009e\u00a1\7C\2\2\u009f\u00a0\7B\2\2")
        buf.write("\u00a0\u00a2\7C\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3")
        buf.write("\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a7\7*\2\2\u00a4\u00a6")
        buf.write("\5\6\4\2\u00a5\u00a4\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7")
        buf.write("\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00aa\3\2\2\2")
        buf.write("\u00a9\u00a7\3\2\2\2\u00aa\u00ab\7+\2\2\u00ab\5\3\2\2")
        buf.write("\2\u00ac\u00af\5\b\5\2\u00ad\u00af\5\32\16\2\u00ae\u00ac")
        buf.write("\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\7\3\2\2\2\u00b0\u00b5")
        buf.write("\5\n\6\2\u00b1\u00b5\5\f\7\2\u00b2\u00b5\5\20\t\2\u00b3")
        buf.write("\u00b5\5\22\n\2\u00b4\u00b0\3\2\2\2\u00b4\u00b1\3\2\2")
        buf.write("\2\u00b4\u00b2\3\2\2\2\u00b4\u00b3\3\2\2\2\u00b5\t\3\2")
        buf.write("\2\2\u00b6\u00b7\t\2\2\2\u00b7\u00bc\5\30\r\2\u00b8\u00b9")
        buf.write("\7-\2\2\u00b9\u00bb\5\30\r\2\u00ba\u00b8\3\2\2\2\u00bb")
        buf.write("\u00be\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2")
        buf.write("\u00bd\u00bf\3\2\2\2\u00be\u00bc\3\2\2\2\u00bf\u00c0\7")
        buf.write("B\2\2\u00c0\u00c1\5> \2\u00c1\u00c2\7,\2\2\u00c2\13\3")
        buf.write("\2\2\2\u00c3\u00c4\t\2\2\2\u00c4\u00c5\5\30\r\2\u00c5")
        buf.write("\u00c6\5\16\b\2\u00c6\u00c7\5d\63\2\u00c7\u00c8\7,\2\2")
        buf.write("\u00c8\r\3\2\2\2\u00c9\u00ca\7-\2\2\u00ca\u00cb\5\30\r")
        buf.write("\2\u00cb\u00cc\5\16\b\2\u00cc\u00cd\5d\63\2\u00cd\u00ce")
        buf.write("\7-\2\2\u00ce\u00d4\3\2\2\2\u00cf\u00d0\7B\2\2\u00d0\u00d1")
        buf.write("\5> \2\u00d1\u00d2\78\2\2\u00d2\u00d4\3\2\2\2\u00d3\u00c9")
        buf.write("\3\2\2\2\u00d3\u00cf\3\2\2\2\u00d4\17\3\2\2\2\u00d5\u00d6")
        buf.write("\t\2\2\2\u00d6\u00db\5\30\r\2\u00d7\u00d8\7-\2\2\u00d8")
        buf.write("\u00da\5\30\r\2\u00d9\u00d7\3\2\2\2\u00da\u00dd\3\2\2")
        buf.write("\2\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00de")
        buf.write("\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00df\7B\2\2\u00df")
        buf.write("\u00e0\5\26\f\2\u00e0\u00e1\7,\2\2\u00e1\21\3\2\2\2\u00e2")
        buf.write("\u00e3\t\2\2\2\u00e3\u00e4\5\30\r\2\u00e4\u00e5\5\24\13")
        buf.write("\2\u00e5\u00e6\5\64\33\2\u00e6\u00e7\7,\2\2\u00e7\23\3")
        buf.write("\2\2\2\u00e8\u00e9\7-\2\2\u00e9\u00ea\5\30\r\2\u00ea\u00eb")
        buf.write("\5\24\13\2\u00eb\u00ec\5\64\33\2\u00ec\u00ed\7-\2\2\u00ed")
        buf.write("\u00f3\3\2\2\2\u00ee\u00ef\7B\2\2\u00ef\u00f0\5\26\f\2")
        buf.write("\u00f0\u00f1\78\2\2\u00f1\u00f3\3\2\2\2\u00f2\u00e8\3")
        buf.write("\2\2\2\u00f2\u00ee\3\2\2\2\u00f3\25\3\2\2\2\u00f4\u00f5")
        buf.write("\7\37\2\2\u00f5\u00f8\7(\2\2\u00f6\u00f9\5@!\2\u00f7\u00f9")
        buf.write("\5\26\f\2\u00f8\u00f6\3\2\2\2\u00f8\u00f7\3\2\2\2\u00f9")
        buf.write("\u00fa\3\2\2\2\u00fa\u00fb\7-\2\2\u00fb\u00fc\7\4\2\2")
        buf.write("\u00fc\u00fd\7)\2\2\u00fd\27\3\2\2\2\u00fe\u00ff\t\3\2")
        buf.write("\2\u00ff\31\3\2\2\2\u0100\u0104\5\34\17\2\u0101\u0104")
        buf.write("\5\36\20\2\u0102\u0104\5 \21\2\u0103\u0100\3\2\2\2\u0103")
        buf.write("\u0101\3\2\2\2\u0103\u0102\3\2\2\2\u0104\33\3\2\2\2\u0105")
        buf.write("\u0106\5\30\r\2\u0106\u0108\7&\2\2\u0107\u0109\5:\36\2")
        buf.write("\u0108\u0107\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010a\3")
        buf.write("\2\2\2\u010a\u010b\7\'\2\2\u010b\u010d\7*\2\2\u010c\u010e")
        buf.write("\5\\/\2\u010d\u010c\3\2\2\2\u010d\u010e\3\2\2\2\u010e")
        buf.write("\u010f\3\2\2\2\u010f\u0110\7+\2\2\u0110\35\3\2\2\2\u0111")
        buf.write("\u0112\7\24\2\2\u0112\u0114\7&\2\2\u0113\u0115\5:\36\2")
        buf.write("\u0114\u0113\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0116\3")
        buf.write("\2\2\2\u0116\u0117\7\'\2\2\u0117\u0119\7*\2\2\u0118\u011a")
        buf.write("\5\\/\2\u0119\u0118\3\2\2\2\u0119\u011a\3\2\2\2\u011a")
        buf.write("\u011b\3\2\2\2\u011b\u011c\7+\2\2\u011c\37\3\2\2\2\u011d")
        buf.write("\u011e\7\31\2\2\u011e\u011f\7&\2\2\u011f\u0120\7\'\2\2")
        buf.write("\u0120\u0122\7*\2\2\u0121\u0123\5\\/\2\u0122\u0121\3\2")
        buf.write("\2\2\u0122\u0123\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0125")
        buf.write("\7+\2\2\u0125!\3\2\2\2\u0126\u0131\5$\23\2\u0127\u0131")
        buf.write("\5\66\34\2\u0128\u0131\5B\"\2\u0129\u0131\5H%\2\u012a")
        buf.write("\u0131\5P)\2\u012b\u0131\5R*\2\u012c\u0131\5T+\2\u012d")
        buf.write("\u0131\5V,\2\u012e\u0131\5X-\2\u012f\u0131\5Z.\2\u0130")
        buf.write("\u0126\3\2\2\2\u0130\u0127\3\2\2\2\u0130\u0128\3\2\2\2")
        buf.write("\u0130\u0129\3\2\2\2\u0130\u012a\3\2\2\2\u0130\u012b\3")
        buf.write("\2\2\2\u0130\u012c\3\2\2\2\u0130\u012d\3\2\2\2\u0130\u012e")
        buf.write("\3\2\2\2\u0130\u012f\3\2\2\2\u0131#\3\2\2\2\u0132\u0137")
        buf.write("\5&\24\2\u0133\u0137\5(\25\2\u0134\u0137\5,\27\2\u0135")
        buf.write("\u0137\5.\30\2\u0136\u0132\3\2\2\2\u0136\u0133\3\2\2\2")
        buf.write("\u0136\u0134\3\2\2\2\u0136\u0135\3\2\2\2\u0137%\3\2\2")
        buf.write("\2\u0138\u0139\t\2\2\2\u0139\u013e\7C\2\2\u013a\u013b")
        buf.write("\7-\2\2\u013b\u013d\7C\2\2\u013c\u013a\3\2\2\2\u013d\u0140")
        buf.write("\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f")
        buf.write("\u0141\3\2\2\2\u0140\u013e\3\2\2\2\u0141\u0142\7B\2\2")
        buf.write("\u0142\u0143\5> \2\u0143\u0144\7,\2\2\u0144\'\3\2\2\2")
        buf.write("\u0145\u0146\t\2\2\2\u0146\u0147\7C\2\2\u0147\u0148\5")
        buf.write("*\26\2\u0148\u0149\5d\63\2\u0149\u014a\7,\2\2\u014a)\3")
        buf.write("\2\2\2\u014b\u014c\7-\2\2\u014c\u014d\7C\2\2\u014d\u014e")
        buf.write("\5*\26\2\u014e\u014f\5d\63\2\u014f\u0150\7-\2\2\u0150")
        buf.write("\u0156\3\2\2\2\u0151\u0152\7B\2\2\u0152\u0153\5> \2\u0153")
        buf.write("\u0154\78\2\2\u0154\u0156\3\2\2\2\u0155\u014b\3\2\2\2")
        buf.write("\u0155\u0151\3\2\2\2\u0156+\3\2\2\2\u0157\u0158\t\2\2")
        buf.write("\2\u0158\u015d\7C\2\2\u0159\u015a\7-\2\2\u015a\u015c\7")
        buf.write("C\2\2\u015b\u0159\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b")
        buf.write("\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u0160\3\2\2\2\u015f")
        buf.write("\u015d\3\2\2\2\u0160\u0161\7B\2\2\u0161\u0162\5\62\32")
        buf.write("\2\u0162\u0163\7,\2\2\u0163-\3\2\2\2\u0164\u0165\t\2\2")
        buf.write("\2\u0165\u0166\7C\2\2\u0166\u0167\5\60\31\2\u0167\u0168")
        buf.write("\5\64\33\2\u0168\u0169\7,\2\2\u0169/\3\2\2\2\u016a\u016b")
        buf.write("\7-\2\2\u016b\u016c\7C\2\2\u016c\u016d\5\60\31\2\u016d")
        buf.write("\u016e\5\64\33\2\u016e\u016f\7-\2\2\u016f\u0175\3\2\2")
        buf.write("\2\u0170\u0171\7B\2\2\u0171\u0172\5\62\32\2\u0172\u0173")
        buf.write("\78\2\2\u0173\u0175\3\2\2\2\u0174\u016a\3\2\2\2\u0174")
        buf.write("\u0170\3\2\2\2\u0175\61\3\2\2\2\u0176\u0177\7\37\2\2\u0177")
        buf.write("\u017a\7(\2\2\u0178\u017b\5@!\2\u0179\u017b\5\62\32\2")
        buf.write("\u017a\u0178\3\2\2\2\u017a\u0179\3\2\2\2\u017b\u017c\3")
        buf.write("\2\2\2\u017c\u017d\7-\2\2\u017d\u017e\7\4\2\2\u017e\u017f")
        buf.write("\7)\2\2\u017f\63\3\2\2\2\u0180\u0183\5\u008eH\2\u0181")
        buf.write("\u0183\5\u0088E\2\u0182\u0180\3\2\2\2\u0182\u0181\3\2")
        buf.write("\2\2\u0183\65\3\2\2\2\u0184\u0185\58\35\2\u0185\u0186")
        buf.write("\78\2\2\u0186\u0187\5d\63\2\u0187\u0188\7,\2\2\u0188\67")
        buf.write("\3\2\2\2\u0189\u018b\5N(\2\u018a\u018c\5\u0080A\2\u018b")
        buf.write("\u018a\3\2\2\2\u018b\u018c\3\2\2\2\u018c9\3\2\2\2\u018d")
        buf.write("\u0192\5<\37\2\u018e\u018f\7,\2\2\u018f\u0191\5<\37\2")
        buf.write("\u0190\u018e\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190\3")
        buf.write("\2\2\2\u0192\u0193\3\2\2\2\u0193;\3\2\2\2\u0194\u0192")
        buf.write("\3\2\2\2\u0195\u019a\7C\2\2\u0196\u0197\7-\2\2\u0197\u0199")
        buf.write("\7C\2\2\u0198\u0196\3\2\2\2\u0199\u019c\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019d\3\2\2\2")
        buf.write("\u019c\u019a\3\2\2\2\u019d\u01a0\7B\2\2\u019e\u01a1\5")
        buf.write("> \2\u019f\u01a1\5\62\32\2\u01a0\u019e\3\2\2\2\u01a0\u019f")
        buf.write("\3\2\2\2\u01a1=\3\2\2\2\u01a2\u01a5\5@!\2\u01a3\u01a5")
        buf.write("\7C\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5")
        buf.write("?\3\2\2\2\u01a6\u01a7\t\4\2\2\u01a7A\3\2\2\2\u01a8\u01a9")
        buf.write("\7\32\2\2\u01a9\u01aa\7&\2\2\u01aa\u01ab\5d\63\2\u01ab")
        buf.write("\u01ac\7\'\2\2\u01ac\u01ae\7*\2\2\u01ad\u01af\5\\/\2\u01ae")
        buf.write("\u01ad\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b0\3\2\2\2")
        buf.write("\u01b0\u01b3\7+\2\2\u01b1\u01b4\5D#\2\u01b2\u01b4\5F$")
        buf.write("\2\u01b3\u01b1\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b3\u01b4")
        buf.write("\3\2\2\2\u01b4C\3\2\2\2\u01b5\u01b6\7\36\2\2\u01b6\u01b7")
        buf.write("\7&\2\2\u01b7\u01b8\5d\63\2\u01b8\u01b9\7\'\2\2\u01b9")
        buf.write("\u01bb\7*\2\2\u01ba\u01bc\5\\/\2\u01bb\u01ba\3\2\2\2\u01bb")
        buf.write("\u01bc\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01c0\7+\2\2")
        buf.write("\u01be\u01c1\5D#\2\u01bf\u01c1\5F$\2\u01c0\u01be\3\2\2")
        buf.write("\2\u01c0\u01bf\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1E\3\2")
        buf.write("\2\2\u01c2\u01c3\7\"\2\2\u01c3\u01c5\7*\2\2\u01c4\u01c6")
        buf.write("\5\\/\2\u01c5\u01c4\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6")
        buf.write("\u01c7\3\2\2\2\u01c7\u01c8\7+\2\2\u01c8G\3\2\2\2\u01c9")
        buf.write("\u01ca\7\21\2\2\u01ca\u01cb\7&\2\2\u01cb\u01cc\5J&\2\u01cc")
        buf.write("\u01cd\7\'\2\2\u01cd\u01cf\7*\2\2\u01ce\u01d0\5\\/\2\u01cf")
        buf.write("\u01ce\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1\3\2\2\2")
        buf.write("\u01d1\u01d2\7+\2\2\u01d2I\3\2\2\2\u01d3\u01d4\5N(\2\u01d4")
        buf.write("\u01d5\7#\2\2\u01d5\u01d6\5L\'\2\u01d6\u01d7\7.\2\2\u01d7")
        buf.write("\u01da\5L\'\2\u01d8\u01d9\7!\2\2\u01d9\u01db\5L\'\2\u01da")
        buf.write("\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01dbK\3\2\2\2\u01dc")
        buf.write("\u01dd\5d\63\2\u01ddM\3\2\2\2\u01de\u01df\b(\1\2\u01df")
        buf.write("\u01e7\7C\2\2\u01e0\u01e1\7%\2\2\u01e1\u01e2\7@\2\2\u01e2")
        buf.write("\u01e7\7C\2\2\u01e3\u01e4\7C\2\2\u01e4\u01e5\7A\2\2\u01e5")
        buf.write("\u01e7\7D\2\2\u01e6\u01de\3\2\2\2\u01e6\u01e0\3\2\2\2")
        buf.write("\u01e6\u01e3\3\2\2\2\u01e7\u01ed\3\2\2\2\u01e8\u01e9\f")
        buf.write("\6\2\2\u01e9\u01ea\7@\2\2\u01ea\u01ec\7C\2\2\u01eb\u01e8")
        buf.write("\3\2\2\2\u01ec\u01ef\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed")
        buf.write("\u01ee\3\2\2\2\u01eeO\3\2\2\2\u01ef\u01ed\3\2\2\2\u01f0")
        buf.write("\u01f1\7\20\2\2\u01f1\u01f2\7,\2\2\u01f2Q\3\2\2\2\u01f3")
        buf.write("\u01f4\7\25\2\2\u01f4\u01f5\7,\2\2\u01f5S\3\2\2\2\u01f6")
        buf.write("\u01f8\7$\2\2\u01f7\u01f9\5d\63\2\u01f8\u01f7\3\2\2\2")
        buf.write("\u01f8\u01f9\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01fb\7")
        buf.write(",\2\2\u01fbU\3\2\2\2\u01fc\u01fd\5^\60\2\u01fd\u01fe\7")
        buf.write("@\2\2\u01fe\u01ff\5b\62\2\u01ff\u0200\7,\2\2\u0200W\3")
        buf.write("\2\2\2\u0201\u0202\t\5\2\2\u0202\u0203\7A\2\2\u0203\u0204")
        buf.write("\5\u0086D\2\u0204\u0205\7,\2\2\u0205Y\3\2\2\2\u0206\u0208")
        buf.write("\7*\2\2\u0207\u0209\5\\/\2\u0208\u0207\3\2\2\2\u0208\u0209")
        buf.write("\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u020b\7+\2\2\u020b")
        buf.write("[\3\2\2\2\u020c\u020e\5\"\22\2\u020d\u020c\3\2\2\2\u020e")
        buf.write("\u020f\3\2\2\2\u020f\u020d\3\2\2\2\u020f\u0210\3\2\2\2")
        buf.write("\u0210]\3\2\2\2\u0211\u0212\b\60\1\2\u0212\u0213\7\35")
        buf.write("\2\2\u0213\u0218\5b\62\2\u0214\u0218\5\u0084C\2\u0215")
        buf.write("\u0218\7%\2\2\u0216\u0218\7C\2\2\u0217\u0211\3\2\2\2\u0217")
        buf.write("\u0214\3\2\2\2\u0217\u0215\3\2\2\2\u0217\u0216\3\2\2\2")
        buf.write("\u0218\u0223\3\2\2\2\u0219\u021a\f\b\2\2\u021a\u021d\7")
        buf.write("@\2\2\u021b\u021e\7C\2\2\u021c\u021e\5b\62\2\u021d\u021b")
        buf.write("\3\2\2\2\u021d\u021c\3\2\2\2\u021e\u0222\3\2\2\2\u021f")
        buf.write("\u0220\f\6\2\2\u0220\u0222\5\u0080A\2\u0221\u0219\3\2")
        buf.write("\2\2\u0221\u021f\3\2\2\2\u0222\u0225\3\2\2\2\u0223\u0221")
        buf.write("\3\2\2\2\u0223\u0224\3\2\2\2\u0224_\3\2\2\2\u0225\u0223")
        buf.write("\3\2\2\2\u0226\u0227\5d\63\2\u0227\u0228\7-\2\2\u0228")
        buf.write("\u022a\3\2\2\2\u0229\u0226\3\2\2\2\u022a\u022d\3\2\2\2")
        buf.write("\u022b\u0229\3\2\2\2\u022b\u022c\3\2\2\2\u022c\u022e\3")
        buf.write("\2\2\2\u022d\u022b\3\2\2\2\u022e\u022f\5d\63\2\u022fa")
        buf.write("\3\2\2\2\u0230\u0231\7C\2\2\u0231\u0233\7&\2\2\u0232\u0234")
        buf.write("\5\u008aF\2\u0233\u0232\3\2\2\2\u0233\u0234\3\2\2\2\u0234")
        buf.write("\u0235\3\2\2\2\u0235\u0236\7\'\2\2\u0236c\3\2\2\2\u0237")
        buf.write("\u023a\5f\64\2\u0238\u023a\5\u0088E\2\u0239\u0237\3\2")
        buf.write("\2\2\u0239\u0238\3\2\2\2\u023ae\3\2\2\2\u023b\u023c\5")
        buf.write("h\65\2\u023c\u023d\t\6\2\2\u023d\u023e\5h\65\2\u023e\u0241")
        buf.write("\3\2\2\2\u023f\u0241\5h\65\2\u0240\u023b\3\2\2\2\u0240")
        buf.write("\u023f\3\2\2\2\u0241g\3\2\2\2\u0242\u0243\5j\66\2\u0243")
        buf.write("\u0244\t\7\2\2\u0244\u0245\5j\66\2\u0245\u0248\3\2\2\2")
        buf.write("\u0246\u0248\5j\66\2\u0247\u0242\3\2\2\2\u0247\u0246\3")
        buf.write("\2\2\2\u0248i\3\2\2\2\u0249\u024a\b\66\1\2\u024a\u024b")
        buf.write("\5l\67\2\u024b\u0251\3\2\2\2\u024c\u024d\f\4\2\2\u024d")
        buf.write("\u024e\t\b\2\2\u024e\u0250\5l\67\2\u024f\u024c\3\2\2\2")
        buf.write("\u0250\u0253\3\2\2\2\u0251\u024f\3\2\2\2\u0251\u0252\3")
        buf.write("\2\2\2\u0252k\3\2\2\2\u0253\u0251\3\2\2\2\u0254\u0255")
        buf.write("\b\67\1\2\u0255\u0256\5n8\2\u0256\u025c\3\2\2\2\u0257")
        buf.write("\u0258\f\4\2\2\u0258\u0259\t\t\2\2\u0259\u025b\5n8\2\u025a")
        buf.write("\u0257\3\2\2\2\u025b\u025e\3\2\2\2\u025c\u025a\3\2\2\2")
        buf.write("\u025c\u025d\3\2\2\2\u025dm\3\2\2\2\u025e\u025c\3\2\2")
        buf.write("\2\u025f\u0260\b8\1\2\u0260\u0261\5p9\2\u0261\u0267\3")
        buf.write("\2\2\2\u0262\u0263\f\4\2\2\u0263\u0264\t\n\2\2\u0264\u0266")
        buf.write("\5p9\2\u0265\u0262\3\2\2\2\u0266\u0269\3\2\2\2\u0267\u0265")
        buf.write("\3\2\2\2\u0267\u0268\3\2\2\2\u0268o\3\2\2\2\u0269\u0267")
        buf.write("\3\2\2\2\u026a\u026b\7\64\2\2\u026b\u026e\5p9\2\u026c")
        buf.write("\u026e\5r:\2\u026d\u026a\3\2\2\2\u026d\u026c\3\2\2\2\u026e")
        buf.write("q\3\2\2\2\u026f\u0270\7\60\2\2\u0270\u0273\5r:\2\u0271")
        buf.write("\u0273\5t;\2\u0272\u026f\3\2\2\2\u0272\u0271\3\2\2\2\u0273")
        buf.write("s\3\2\2\2\u0274\u0275\b;\1\2\u0275\u0276\5x=\2\u0276\u027f")
        buf.write("\3\2\2\2\u0277\u0279\f\4\2\2\u0278\u027a\5v<\2\u0279\u0278")
        buf.write("\3\2\2\2\u027a\u027b\3\2\2\2\u027b\u0279\3\2\2\2\u027b")
        buf.write("\u027c\3\2\2\2\u027c\u027e\3\2\2\2\u027d\u0277\3\2\2\2")
        buf.write("\u027e\u0281\3\2\2\2\u027f\u027d\3\2\2\2\u027f\u0280\3")
        buf.write("\2\2\2\u0280u\3\2\2\2\u0281\u027f\3\2\2\2\u0282\u0283")
        buf.write("\7(\2\2\u0283\u0284\5d\63\2\u0284\u0285\7)\2\2\u0285w")
        buf.write("\3\2\2\2\u0286\u0287\b=\1\2\u0287\u0288\5z>\2\u0288\u0291")
        buf.write("\3\2\2\2\u0289\u028a\f\4\2\2\u028a\u028d\7@\2\2\u028b")
        buf.write("\u028e\7C\2\2\u028c\u028e\5b\62\2\u028d\u028b\3\2\2\2")
        buf.write("\u028d\u028c\3\2\2\2\u028e\u0290\3\2\2\2\u028f\u0289\3")
        buf.write("\2\2\2\u0290\u0293\3\2\2\2\u0291\u028f\3\2\2\2\u0291\u0292")
        buf.write("\3\2\2\2\u0292y\3\2\2\2\u0293\u0291\3\2\2\2\u0294\u0295")
        buf.write("\7C\2\2\u0295\u0298\7A\2\2\u0296\u0299\5\u0086D\2\u0297")
        buf.write("\u0299\7D\2\2\u0298\u0296\3\2\2\2\u0298\u0297\3\2\2\2")
        buf.write("\u0299\u029c\3\2\2\2\u029a\u029c\5|?\2\u029b\u0294\3\2")
        buf.write("\2\2\u029b\u029a\3\2\2\2\u029c{\3\2\2\2\u029d\u029e\7")
        buf.write("\35\2\2\u029e\u029f\5~@\2\u029f\u02a1\7&\2\2\u02a0\u02a2")
        buf.write("\5\u008aF\2\u02a1\u02a0\3\2\2\2\u02a1\u02a2\3\2\2\2\u02a2")
        buf.write("\u02a3\3\2\2\2\u02a3\u02a4\7\'\2\2\u02a4\u02a7\3\2\2\2")
        buf.write("\u02a5\u02a7\5~@\2\u02a6\u029d\3\2\2\2\u02a6\u02a5\3\2")
        buf.write("\2\2\u02a7}\3\2\2\2\u02a8\u02b2\5\u008cG\2\u02a9\u02b2")
        buf.write("\7%\2\2\u02aa\u02b2\7C\2\2\u02ab\u02ac\7&\2\2\u02ac\u02ad")
        buf.write("\5f\64\2\u02ad\u02ae\7\'\2\2\u02ae\u02b2\3\2\2\2\u02af")
        buf.write("\u02b2\7\23\2\2\u02b0\u02b2\5\u008eH\2\u02b1\u02a8\3\2")
        buf.write("\2\2\u02b1\u02a9\3\2\2\2\u02b1\u02aa\3\2\2\2\u02b1\u02ab")
        buf.write("\3\2\2\2\u02b1\u02af\3\2\2\2\u02b1\u02b0\3\2\2\2\u02b2")
        buf.write("\177\3\2\2\2\u02b3\u02b4\5\u0082B\2\u02b4\u0081\3\2\2")
        buf.write("\2\u02b5\u02b6\bB\1\2\u02b6\u02b7\7(\2\2\u02b7\u02b8\5")
        buf.write("d\63\2\u02b8\u02b9\7)\2\2\u02b9\u02c1\3\2\2\2\u02ba\u02bb")
        buf.write("\f\4\2\2\u02bb\u02bc\7(\2\2\u02bc\u02bd\5d\63\2\u02bd")
        buf.write("\u02be\7)\2\2\u02be\u02c0\3\2\2\2\u02bf\u02ba\3\2\2\2")
        buf.write("\u02c0\u02c3\3\2\2\2\u02c1\u02bf\3\2\2\2\u02c1\u02c2\3")
        buf.write("\2\2\2\u02c2\u0083\3\2\2\2\u02c3\u02c1\3\2\2\2\u02c4\u02c5")
        buf.write("\7C\2\2\u02c5\u02c8\7A\2\2\u02c6\u02c9\7D\2\2\u02c7\u02c9")
        buf.write("\5\u0086D\2\u02c8\u02c6\3\2\2\2\u02c8\u02c7\3\2\2\2\u02c9")
        buf.write("\u0085\3\2\2\2\u02ca\u02cb\7D\2\2\u02cb\u02cd\7&\2\2\u02cc")
        buf.write("\u02ce\5\u008aF\2\u02cd\u02cc\3\2\2\2\u02cd\u02ce\3\2")
        buf.write("\2\2\u02ce\u02cf\3\2\2\2\u02cf\u02d0\7\'\2\2\u02d0\u0087")
        buf.write("\3\2\2\2\u02d1\u02d2\7\35\2\2\u02d2\u02d3\7C\2\2\u02d3")
        buf.write("\u02d5\7&\2\2\u02d4\u02d6\5\u008aF\2\u02d5\u02d4\3\2\2")
        buf.write("\2\u02d5\u02d6\3\2\2\2\u02d6\u02d7\3\2\2\2\u02d7\u02d8")
        buf.write("\7\'\2\2\u02d8\u0089\3\2\2\2\u02d9\u02de\5f\64\2\u02da")
        buf.write("\u02db\7-\2\2\u02db\u02dd\5f\64\2\u02dc\u02da\3\2\2\2")
        buf.write("\u02dd\u02e0\3\2\2\2\u02de\u02dc\3\2\2\2\u02de\u02df\3")
        buf.write("\2\2\2\u02df\u008b\3\2\2\2\u02e0\u02de\3\2\2\2\u02e1\u02e2")
        buf.write("\t\13\2\2\u02e2\u008d\3\2\2\2\u02e3\u02e6\5\u0090I\2\u02e4")
        buf.write("\u02e6\5\u0092J\2\u02e5\u02e3\3\2\2\2\u02e5\u02e4\3\2")
        buf.write("\2\2\u02e6\u008f\3\2\2\2\u02e7\u02e8\7\37\2\2\u02e8\u02ea")
        buf.write("\7&\2\2\u02e9\u02eb\5\u0094K\2\u02ea\u02e9\3\2\2\2\u02ea")
        buf.write("\u02eb\3\2\2\2\u02eb\u02ec\3\2\2\2\u02ec\u02ed\7\'\2\2")
        buf.write("\u02ed\u0091\3\2\2\2\u02ee\u02ef\7\37\2\2\u02ef\u02f0")
        buf.write("\7&\2\2\u02f0\u02f5\5\u0090I\2\u02f1\u02f2\7-\2\2\u02f2")
        buf.write("\u02f4\5\u0090I\2\u02f3\u02f1\3\2\2\2\u02f4\u02f7\3\2")
        buf.write("\2\2\u02f5\u02f3\3\2\2\2\u02f5\u02f6\3\2\2\2\u02f6\u02f8")
        buf.write("\3\2\2\2\u02f7\u02f5\3\2\2\2\u02f8\u02f9\7\'\2\2\u02f9")
        buf.write("\u0093\3\2\2\2\u02fa\u02ff\5d\63\2\u02fb\u02fc\7-\2\2")
        buf.write("\u02fc\u02fe\5d\63\2\u02fd\u02fb\3\2\2\2\u02fe\u0301\3")
        buf.write("\2\2\2\u02ff\u02fd\3\2\2\2\u02ff\u0300\3\2\2\2\u0300\u0095")
        buf.write("\3\2\2\2\u0301\u02ff\3\2\2\2K\u0099\u00a1\u00a7\u00ae")
        buf.write("\u00b4\u00bc\u00d3\u00db\u00f2\u00f8\u0103\u0108\u010d")
        buf.write("\u0114\u0119\u0122\u0130\u0136\u013e\u0155\u015d\u0174")
        buf.write("\u017a\u0182\u018b\u0192\u019a\u01a0\u01a4\u01ae\u01b3")
        buf.write("\u01bb\u01c0\u01c5\u01cf\u01da\u01e6\u01ed\u01f8\u0208")
        buf.write("\u020f\u0217\u021d\u0221\u0223\u022b\u0233\u0239\u0240")
        buf.write("\u0247\u0251\u025c\u0267\u026d\u0272\u027b\u027f\u028d")
        buf.write("\u0291\u0298\u029b\u02a1\u02a6\u02b1\u02c1\u02c8\u02cd")
        buf.write("\u02d5\u02de\u02e5\u02ea\u02f5\u02ff")
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
    RULE_prim_type = 31
    RULE_if_stmt = 32
    RULE_else_if_body = 33
    RULE_else_body = 34
    RULE_for_in_stmt = 35
    RULE_for_in_body = 36
    RULE_for_in_expr = 37
    RULE_scalar_variable = 38
    RULE_break_stmt = 39
    RULE_continue_stmt = 40
    RULE_return_stmt = 41
    RULE_method_invoc = 42
    RULE_static_method_invoc = 43
    RULE_block_stmt_stmt = 44
    RULE_block_stmt = 45
    RULE_method_invoc_literal = 46
    RULE_expr_list = 47
    RULE_funcall = 48
    RULE_all_expr = 49
    RULE_op = 50
    RULE_op1 = 51
    RULE_op2 = 52
    RULE_op3 = 53
    RULE_op4 = 54
    RULE_op5 = 55
    RULE_op6 = 56
    RULE_op7 = 57
    RULE_postfix_array_exp = 58
    RULE_op8 = 59
    RULE_op9 = 60
    RULE_op10 = 61
    RULE_operands = 62
    RULE_element_expr = 63
    RULE_index_ops = 64
    RULE_static_member_access = 65
    RULE_static_method = 66
    RULE_object_create = 67
    RULE_list_of_expr = 68
    RULE_literal = 69
    RULE_literal_array = 70
    RULE_literal_idx_array = 71
    RULE_literal_mtd_array = 72
    RULE_array_element = 73

    ruleNames =  [ "program", "class_decl", "class_body", "class_attr", 
                   "attr_no_value", "attr_with_value", "attr_pair", "attr_array_no_value", 
                   "attr_array_with_value", "attr_array_pair", "attr_array_decl_tail", 
                   "any_id", "class_method", "normal_method", "constructor", 
                   "destructor", "stmt", "var_decl", "var_no_value", "var_with_value", 
                   "var_pair", "var_array_no_value", "var_array_with_value", 
                   "var_array_pair", "var_array_decl_tail", "array_rhs", 
                   "assign_stmt", "assign_lhs", "params_list", "params", 
                   "data_type", "prim_type", "if_stmt", "else_if_body", 
                   "else_body", "for_in_stmt", "for_in_body", "for_in_expr", 
                   "scalar_variable", "break_stmt", "continue_stmt", "return_stmt", 
                   "method_invoc", "static_method_invoc", "block_stmt_stmt", 
                   "block_stmt", "method_invoc_literal", "expr_list", "funcall", 
                   "all_expr", "op", "op1", "op2", "op3", "op4", "op5", 
                   "op6", "op7", "postfix_array_exp", "op8", "op9", "op10", 
                   "operands", "element_expr", "index_ops", "static_member_access", 
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
            self.state = 149 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 148
                self.class_decl()
                self.state = 151 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 153
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
            self.state = 155
            self.match(D96Parser.CLASS)
            self.state = 156
            self.match(D96Parser.ID)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 157
                self.match(D96Parser.COLON)
                self.state = 158
                self.match(D96Parser.ID)


            self.state = 161
            self.match(D96Parser.LP)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.CONSTRUCTOR - 11)) | (1 << (D96Parser.DESTRUCTOR - 11)) | (1 << (D96Parser.ID - 11)) | (1 << (D96Parser.DOLLAR_ID - 11)))) != 0):
                self.state = 162
                self.class_body()
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 168
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
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.class_attr()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
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
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.attr_no_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.attr_with_value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.attr_array_no_value()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 177
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
            self.state = 180
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 181
            self.any_id()
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 182
                self.match(D96Parser.COMMA)
                self.state = 183
                self.any_id()
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 189
            self.match(D96Parser.COLON)
            self.state = 190
            self.data_type()
            self.state = 191
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
            self.state = 193
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 194
            self.any_id()
            self.state = 195
            self.attr_pair()
            self.state = 196
            self.all_expr()
            self.state = 197
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
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.match(D96Parser.COMMA)
                self.state = 200
                self.any_id()
                self.state = 201
                self.attr_pair()
                self.state = 202
                self.all_expr()
                self.state = 203
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.match(D96Parser.COLON)
                self.state = 206
                self.data_type()
                self.state = 207
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
            self.state = 211
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 212
            self.any_id()
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 213
                self.match(D96Parser.COMMA)
                self.state = 214
                self.any_id()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 220
            self.match(D96Parser.COLON)
            self.state = 221
            self.attr_array_decl_tail()
            self.state = 222
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
            self.state = 224
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 225
            self.any_id()
            self.state = 226
            self.attr_array_pair()
            self.state = 227
            self.array_rhs()
            self.state = 228
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
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(D96Parser.COMMA)
                self.state = 231
                self.any_id()
                self.state = 232
                self.attr_array_pair()
                self.state = 233
                self.array_rhs()
                self.state = 234
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.match(D96Parser.COLON)
                self.state = 237
                self.attr_array_decl_tail()
                self.state = 238
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

        def prim_type(self):
            return self.getTypedRuleContext(D96Parser.Prim_typeContext,0)


        def attr_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Attr_array_decl_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attr_array_decl_tail




    def attr_array_decl_tail(self):

        localctx = D96Parser.Attr_array_decl_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attr_array_decl_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(D96Parser.ARRAY)
            self.state = 243
            self.match(D96Parser.LS)
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.state = 244
                self.prim_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 245
                self.attr_array_decl_tail()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 248
            self.match(D96Parser.COMMA)
            self.state = 249
            self.match(D96Parser.LITERAL_INT)
            self.state = 250
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
            self.state = 252
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
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.normal_method()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 256
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
            self.state = 259
            self.any_id()
            self.state = 260
            self.match(D96Parser.LB)
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 261
                self.params_list()


            self.state = 264
            self.match(D96Parser.RB)
            self.state = 265
            self.match(D96Parser.LP)
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 266
                self.block_stmt()


            self.state = 269
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
            self.state = 271
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 272
            self.match(D96Parser.LB)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 273
                self.params_list()


            self.state = 276
            self.match(D96Parser.RB)
            self.state = 277
            self.match(D96Parser.LP)
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 278
                self.block_stmt()


            self.state = 281
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
            self.state = 283
            self.match(D96Parser.DESTRUCTOR)
            self.state = 284
            self.match(D96Parser.LB)
            self.state = 285
            self.match(D96Parser.RB)
            self.state = 286
            self.match(D96Parser.LP)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 287
                self.block_stmt()


            self.state = 290
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
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 294
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 295
                self.for_in_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 296
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 297
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 298
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 299
                self.method_invoc()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 300
                self.static_method_invoc()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 301
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
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.var_no_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.var_with_value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 306
                self.var_array_no_value()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 307
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
            self.state = 310
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 311
            self.match(D96Parser.ID)
            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 312
                self.match(D96Parser.COMMA)
                self.state = 313
                self.match(D96Parser.ID)
                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 319
            self.match(D96Parser.COLON)
            self.state = 320
            self.data_type()
            self.state = 321
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
            self.state = 323
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 324
            self.match(D96Parser.ID)
            self.state = 325
            self.var_pair()
            self.state = 326
            self.all_expr()
            self.state = 327
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
            self.state = 339
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.match(D96Parser.COMMA)
                self.state = 330
                self.match(D96Parser.ID)
                self.state = 331
                self.var_pair()
                self.state = 332
                self.all_expr()
                self.state = 333
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.match(D96Parser.COLON)
                self.state = 336
                self.data_type()
                self.state = 337
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
            self.state = 341
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 342
            self.match(D96Parser.ID)
            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 343
                self.match(D96Parser.COMMA)
                self.state = 344
                self.match(D96Parser.ID)
                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 350
            self.match(D96Parser.COLON)
            self.state = 351
            self.var_array_decl_tail()
            self.state = 352
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
            self.state = 354
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 355
            self.match(D96Parser.ID)
            self.state = 356
            self.var_array_pair()
            self.state = 357
            self.array_rhs()
            self.state = 358
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
            self.state = 370
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.match(D96Parser.COMMA)
                self.state = 361
                self.match(D96Parser.ID)
                self.state = 362
                self.var_array_pair()
                self.state = 363
                self.array_rhs()
                self.state = 364
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.match(D96Parser.COLON)
                self.state = 367
                self.var_array_decl_tail()
                self.state = 368
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

        def prim_type(self):
            return self.getTypedRuleContext(D96Parser.Prim_typeContext,0)


        def var_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Var_array_decl_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_array_decl_tail




    def var_array_decl_tail(self):

        localctx = D96Parser.Var_array_decl_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_var_array_decl_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(D96Parser.ARRAY)
            self.state = 373
            self.match(D96Parser.LS)
            self.state = 376
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.state = 374
                self.prim_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 375
                self.var_array_decl_tail()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 378
            self.match(D96Parser.COMMA)
            self.state = 379
            self.match(D96Parser.LITERAL_INT)
            self.state = 380
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
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.literal_array()
                pass
            elif token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
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
            self.state = 386
            self.assign_lhs()
            self.state = 387
            self.match(D96Parser.ASSIGN)
            self.state = 388
            self.all_expr()
            self.state = 389
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
            self.state = 391
            self.scalar_variable(0)
            self.state = 393
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.LS:
                self.state = 392
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
            self.state = 395
            self.params()
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 396
                self.match(D96Parser.SEMI)
                self.state = 397
                self.params()
                self.state = 402
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
            self.state = 403
            self.match(D96Parser.ID)
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 404
                self.match(D96Parser.COMMA)
                self.state = 405
                self.match(D96Parser.ID)
                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 411
            self.match(D96Parser.COLON)
            self.state = 414
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.ID]:
                self.state = 412
                self.data_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 413
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

        def prim_type(self):
            return self.getTypedRuleContext(D96Parser.Prim_typeContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_data_type




    def data_type(self):

        localctx = D96Parser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_data_type)
        try:
            self.state = 418
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.prim_type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
                self.match(D96Parser.ID)
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


    class Prim_typeContext(ParserRuleContext):

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

        def getRuleIndex(self):
            return D96Parser.RULE_prim_type




    def prim_type(self):

        localctx = D96Parser.Prim_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_prim_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT) | (1 << D96Parser.FLOAT) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING))) != 0)):
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
        self.enterRule(localctx, 64, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(D96Parser.IF)
            self.state = 423
            self.match(D96Parser.LB)
            self.state = 424
            self.all_expr()
            self.state = 425
            self.match(D96Parser.RB)
            self.state = 426
            self.match(D96Parser.LP)
            self.state = 428
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 427
                self.block_stmt()


            self.state = 430
            self.match(D96Parser.RP)
            self.state = 433
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.state = 431
                self.else_if_body()
                pass
            elif token in [D96Parser.ELSE]:
                self.state = 432
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
        self.enterRule(localctx, 66, self.RULE_else_if_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(D96Parser.ELSEIF)
            self.state = 436
            self.match(D96Parser.LB)
            self.state = 437
            self.all_expr()
            self.state = 438
            self.match(D96Parser.RB)
            self.state = 439
            self.match(D96Parser.LP)
            self.state = 441
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 440
                self.block_stmt()


            self.state = 443
            self.match(D96Parser.RP)
            self.state = 446
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.state = 444
                self.else_if_body()
                pass
            elif token in [D96Parser.ELSE]:
                self.state = 445
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
        self.enterRule(localctx, 68, self.RULE_else_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(D96Parser.ELSE)
            self.state = 449
            self.match(D96Parser.LP)
            self.state = 451
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 450
                self.block_stmt()


            self.state = 453
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
        self.enterRule(localctx, 70, self.RULE_for_in_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.match(D96Parser.FOREACH)
            self.state = 456
            self.match(D96Parser.LB)
            self.state = 457
            self.for_in_body()
            self.state = 458
            self.match(D96Parser.RB)
            self.state = 459
            self.match(D96Parser.LP)
            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 460
                self.block_stmt()


            self.state = 463
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
        self.enterRule(localctx, 72, self.RULE_for_in_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.scalar_variable(0)
            self.state = 466
            self.match(D96Parser.IN)
            self.state = 467
            self.for_in_expr()
            self.state = 468
            self.match(D96Parser.DOTDOT)
            self.state = 469
            self.for_in_expr()
            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 470
                self.match(D96Parser.BY)
                self.state = 471
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
        self.enterRule(localctx, 74, self.RULE_for_in_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
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

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def scalar_variable(self):
            return self.getTypedRuleContext(D96Parser.Scalar_variableContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_scalar_variable



    def scalar_variable(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Scalar_variableContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_scalar_variable, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 477
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 478
                self.match(D96Parser.SELF)
                self.state = 479
                self.match(D96Parser.DOT)
                self.state = 480
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.state = 481
                self.match(D96Parser.ID)
                self.state = 482
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 483
                self.match(D96Parser.DOLLAR_ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 491
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Scalar_variableContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_scalar_variable)
                    self.state = 486
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 487
                    self.match(D96Parser.DOT)
                    self.state = 488
                    self.match(D96Parser.ID) 
                self.state = 493
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
        self.enterRule(localctx, 78, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(D96Parser.BREAK)
            self.state = 495
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
        self.enterRule(localctx, 80, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.match(D96Parser.CONTINUE)
            self.state = 498
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
        self.enterRule(localctx, 82, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(D96Parser.RETURN)
            self.state = 502
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_ZERO) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.ID:
                self.state = 501
                self.all_expr()


            self.state = 504
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
        self.enterRule(localctx, 84, self.RULE_method_invoc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.method_invoc_literal(0)
            self.state = 507
            self.match(D96Parser.DOT)
            self.state = 508
            self.funcall()
            self.state = 509
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
        self.enterRule(localctx, 86, self.RULE_static_method_invoc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            _la = self._input.LA(1)
            if not(_la==D96Parser.SELF or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 512
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 513
            self.static_method()
            self.state = 514
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
        self.enterRule(localctx, 88, self.RULE_block_stmt_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.match(D96Parser.LP)
            self.state = 518
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 517
                self.block_stmt()


            self.state = 520
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
        self.enterRule(localctx, 90, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 522
                self.stmt()
                self.state = 525 
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
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_method_invoc_literal, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 528
                self.match(D96Parser.NEW)
                self.state = 529
                self.funcall()
                pass

            elif la_ == 2:
                self.state = 530
                self.static_member_access()
                pass

            elif la_ == 3:
                self.state = 531
                self.match(D96Parser.SELF)
                pass

            elif la_ == 4:
                self.state = 532
                self.match(D96Parser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 545
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 543
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Method_invoc_literalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_method_invoc_literal)
                        self.state = 535
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 536
                        self.match(D96Parser.DOT)
                        self.state = 539
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                        if la_ == 1:
                            self.state = 537
                            self.match(D96Parser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 538
                            self.funcall()
                            pass


                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Method_invoc_literalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_method_invoc_literal)
                        self.state = 541
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 542
                        self.element_expr()
                        pass

             
                self.state = 547
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
        self.enterRule(localctx, 94, self.RULE_expr_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 548
                    self.all_expr()
                    self.state = 549
                    self.match(D96Parser.COMMA) 
                self.state = 555
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

            self.state = 556
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
        self.enterRule(localctx, 96, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
            self.match(D96Parser.ID)
            self.state = 559
            self.match(D96Parser.LB)
            self.state = 561
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_ZERO) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.ID:
                self.state = 560
                self.list_of_expr()


            self.state = 563
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
        self.enterRule(localctx, 98, self.RULE_all_expr)
        try:
            self.state = 567
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 565
                self.op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 566
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
        self.enterRule(localctx, 100, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.state = 574
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 569
                self.op1()
                self.state = 570
                _la = self._input.LA(1)
                if not(_la==D96Parser.EQUAL_STRING or _la==D96Parser.STRING_CONCAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 571
                self.op1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 573
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
        self.enterRule(localctx, 102, self.RULE_op1)
        self._la = 0 # Token type
        try:
            self.state = 581
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 576
                self.op2(0)
                self.state = 577
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.LESS_THAN) | (1 << D96Parser.LEQ) | (1 << D96Parser.GREATER_THAN) | (1 << D96Parser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 578
                self.op2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 580
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
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_op2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
            self.op3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 591
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op2)
                    self.state = 586
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 587
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 588
                    self.op3(0) 
                self.state = 593
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
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_op3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 595
            self.op4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 602
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op3)
                    self.state = 597
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 598
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUBTRACT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 599
                    self.op4(0) 
                self.state = 604
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
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_op4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 606
            self.op5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 613
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op4)
                    self.state = 608
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 609
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLY) | (1 << D96Parser.DIVIDE) | (1 << D96Parser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 610
                    self.op5() 
                self.state = 615
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
        self.enterRule(localctx, 110, self.RULE_op5)
        try:
            self.state = 619
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 616
                self.match(D96Parser.NOT)
                self.state = 617
                self.op5()
                pass
            elif token in [D96Parser.LITERAL_BOOLEAN, D96Parser.LITERAL_INT, D96Parser.LITERAL_ZERO, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.SUBTRACT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 618
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
        self.enterRule(localctx, 112, self.RULE_op6)
        try:
            self.state = 624
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUBTRACT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 621
                self.match(D96Parser.SUBTRACT)
                self.state = 622
                self.op6()
                pass
            elif token in [D96Parser.LITERAL_BOOLEAN, D96Parser.LITERAL_INT, D96Parser.LITERAL_ZERO, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 623
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
        _startState = 114
        self.enterRecursionRule(localctx, 114, self.RULE_op7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 627
            self.op8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 637
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op7)
                    self.state = 629
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 631 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 630
                            self.postfix_array_exp()

                        else:
                            raise NoViableAltException(self)
                        self.state = 633 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
             
                self.state = 639
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
        self.enterRule(localctx, 116, self.RULE_postfix_array_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 640
            self.match(D96Parser.LS)
            self.state = 641
            self.all_expr()
            self.state = 642
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
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_op8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 645
            self.op9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 655
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,58,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op8)
                    self.state = 647
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 648
                    self.match(D96Parser.DOT)
                    self.state = 651
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                    if la_ == 1:
                        self.state = 649
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 650
                        self.funcall()
                        pass

             
                self.state = 657
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

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

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
        self.enterRule(localctx, 120, self.RULE_op9)
        try:
            self.state = 665
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 658
                self.match(D96Parser.ID)
                self.state = 659
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 662
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                if la_ == 1:
                    self.state = 660
                    self.static_method()
                    pass

                elif la_ == 2:
                    self.state = 661
                    self.match(D96Parser.DOLLAR_ID)
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 664
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
        self.enterRule(localctx, 122, self.RULE_op10)
        self._la = 0 # Token type
        try:
            self.state = 676
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 667
                self.match(D96Parser.NEW)
                self.state = 668
                self.operands()
                self.state = 669
                self.match(D96Parser.LB)
                self.state = 671
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_ZERO) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.ID:
                    self.state = 670
                    self.list_of_expr()


                self.state = 673
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.LITERAL_BOOLEAN, D96Parser.LITERAL_INT, D96Parser.LITERAL_ZERO, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 675
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
        self.enterRule(localctx, 124, self.RULE_operands)
        try:
            self.state = 687
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LITERAL_BOOLEAN, D96Parser.LITERAL_INT, D96Parser.LITERAL_ZERO, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 678
                self.literal()
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 679
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 680
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 681
                self.match(D96Parser.LB)
                self.state = 682
                self.op()
                self.state = 683
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 685
                self.match(D96Parser.NULL)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 686
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
        self.enterRule(localctx, 126, self.RULE_element_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 689
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
        _startState = 128
        self.enterRecursionRule(localctx, 128, self.RULE_index_ops, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 692
            self.match(D96Parser.LS)
            self.state = 693
            self.all_expr()
            self.state = 694
            self.match(D96Parser.RS)
            self._ctx.stop = self._input.LT(-1)
            self.state = 703
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_opsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_ops)
                    self.state = 696
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 697
                    self.match(D96Parser.LS)
                    self.state = 698
                    self.all_expr()
                    self.state = 699
                    self.match(D96Parser.RS) 
                self.state = 705
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

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def static_method(self):
            return self.getTypedRuleContext(D96Parser.Static_methodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_member_access




    def static_member_access(self):

        localctx = D96Parser.Static_member_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_static_member_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 706
            self.match(D96Parser.ID)
            self.state = 707
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 710
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.state = 708
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 2:
                self.state = 709
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
        self.enterRule(localctx, 132, self.RULE_static_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 712
            self.match(D96Parser.DOLLAR_ID)
            self.state = 713
            self.match(D96Parser.LB)
            self.state = 715
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_ZERO) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.ID:
                self.state = 714
                self.list_of_expr()


            self.state = 717
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
        self.enterRule(localctx, 134, self.RULE_object_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 719
            self.match(D96Parser.NEW)
            self.state = 720
            self.match(D96Parser.ID)
            self.state = 721
            self.match(D96Parser.LB)
            self.state = 723
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_ZERO) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.ID:
                self.state = 722
                self.list_of_expr()


            self.state = 725
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
        self.enterRule(localctx, 136, self.RULE_list_of_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 727
            self.op()
            self.state = 732
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 728
                self.match(D96Parser.COMMA)
                self.state = 729
                self.op()
                self.state = 734
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
        self.enterRule(localctx, 138, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 735
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
        self.enterRule(localctx, 140, self.RULE_literal_array)
        try:
            self.state = 739
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 737
                self.literal_idx_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 738
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
        self.enterRule(localctx, 142, self.RULE_literal_idx_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 741
            self.match(D96Parser.ARRAY)
            self.state = 742
            self.match(D96Parser.LB)
            self.state = 744
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_ZERO) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.ID:
                self.state = 743
                self.array_element()


            self.state = 746
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
        self.enterRule(localctx, 144, self.RULE_literal_mtd_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 748
            self.match(D96Parser.ARRAY)
            self.state = 749
            self.match(D96Parser.LB)
            self.state = 750
            self.literal_idx_array()
            self.state = 755
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 751
                self.match(D96Parser.COMMA)
                self.state = 752
                self.literal_idx_array()
                self.state = 757
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 758
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
        self.enterRule(localctx, 146, self.RULE_array_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 760
            self.all_expr()
            self.state = 765
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 761
                self.match(D96Parser.COMMA)
                self.state = 762
                self.all_expr()
                self.state = 767
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
        self._predicates[38] = self.scalar_variable_sempred
        self._predicates[46] = self.method_invoc_literal_sempred
        self._predicates[52] = self.op2_sempred
        self._predicates[53] = self.op3_sempred
        self._predicates[54] = self.op4_sempred
        self._predicates[57] = self.op7_sempred
        self._predicates[59] = self.op8_sempred
        self._predicates[64] = self.index_ops_sempred
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
         




