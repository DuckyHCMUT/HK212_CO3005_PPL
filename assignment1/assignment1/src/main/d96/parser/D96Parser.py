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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3H")
        buf.write("\u0311\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\3\3\3\3\3\3\3\3\3\3\4\3\4\7\4\u00a8\n\4\f\4\16\4\u00ab")
        buf.write("\13\4\3\5\3\5\3\5\3\5\3\5\5\5\u00b2\n\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\7\6\u00b9\n\6\f\6\16\6\u00bc\13\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\5\b\u00cf\n\b\3\t\3\t\3\t\7\t\u00d4\n\t\f\t\16\t\u00d7")
        buf.write("\13\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00ea\n\13\3\f\3\f")
        buf.write("\3\f\3\f\5\f\u00f0\n\f\3\f\3\f\3\f\3\f\3\r\3\r\3\16\3")
        buf.write("\16\3\16\5\16\u00fb\n\16\3\17\3\17\3\17\5\17\u0100\n\17")
        buf.write("\3\17\3\17\3\17\5\17\u0105\n\17\3\17\3\17\3\20\3\20\3")
        buf.write("\20\5\20\u010c\n\20\3\20\3\20\3\20\5\20\u0111\n\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\5\21\u011a\n\21\3\21\3")
        buf.write("\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u0131")
        buf.write("\n\22\3\22\5\22\u0134\n\22\3\23\3\23\3\23\3\23\3\23\5")
        buf.write("\23\u013b\n\23\3\23\3\23\3\24\3\24\3\24\7\24\u0142\n\24")
        buf.write("\f\24\16\24\u0145\13\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\5\26\u0158\n\26\3\27\3\27\3\27\7\27\u015d\n\27\f\27\16")
        buf.write("\27\u0160\13\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u016a\n\30\5\30\u016c\n\30\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\5\31\u0174\n\31\5\31\u0176\n\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\5\31\u017e\n\31\3\32\3\32\3\32\3\32\5")
        buf.write("\32\u0184\n\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\5\34\u0193\n\34\3\35\3\35\3")
        buf.write("\35\7\35\u0198\n\35\f\35\16\35\u019b\13\35\3\36\3\36\3")
        buf.write("\36\7\36\u01a0\n\36\f\36\16\36\u01a3\13\36\3\36\3\36\3")
        buf.write("\36\5\36\u01a8\n\36\3\37\3\37\3\37\3\37\3\37\5\37\u01af")
        buf.write("\n\37\3 \3 \3 \3 \3 \3 \5 \u01b7\n \3 \3 \5 \u01bb\n ")
        buf.write("\3 \5 \u01be\n \3!\3!\3!\3!\3!\3!\5!\u01c6\n!\3!\3!\5")
        buf.write("!\u01ca\n!\3\"\3\"\3\"\5\"\u01cf\n\"\3\"\3\"\3#\3#\3#")
        buf.write("\3#\3#\3#\5#\u01d9\n#\3#\3#\3$\3$\3$\3$\3$\3$\3$\5$\u01e4")
        buf.write("\n$\3%\3%\3&\3&\3&\3&\5&\u01ec\n&\3&\3&\3&\3&\5&\u01f2")
        buf.write("\n&\7&\u01f4\n&\f&\16&\u01f7\13&\3\'\3\'\3\'\3(\3(\3(")
        buf.write("\3)\3)\7)\u0201\n)\f)\16)\u0204\13)\3)\3)\3*\3*\3+\3+")
        buf.write("\3+\3+\3+\3+\5+\u0210\n+\3+\3+\3+\3+\5+\u0216\n+\3+\3")
        buf.write("+\7+\u021a\n+\f+\16+\u021d\13+\3,\3,\5,\u0221\n,\3-\3")
        buf.write("-\3-\7-\u0226\n-\f-\16-\u0229\13-\3-\3-\3.\3.\3.\5.\u0230")
        buf.write("\n.\3.\3.\3/\6/\u0235\n/\r/\16/\u0236\3\60\3\60\5\60\u023b")
        buf.write("\n\60\3\61\3\61\3\61\3\61\3\61\5\61\u0242\n\61\3\62\3")
        buf.write("\62\3\62\3\62\3\62\5\62\u0249\n\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\7\63\u0251\n\63\f\63\16\63\u0254\13\63\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\7\64\u025c\n\64\f\64\16\64\u025f")
        buf.write("\13\64\3\65\3\65\3\65\3\65\3\65\3\65\7\65\u0267\n\65\f")
        buf.write("\65\16\65\u026a\13\65\3\66\3\66\3\66\5\66\u026f\n\66\3")
        buf.write("\67\3\67\3\67\5\67\u0274\n\67\38\38\38\38\38\38\38\38")
        buf.write("\78\u027e\n8\f8\168\u0281\138\39\39\39\39\39\39\39\59")
        buf.write("\u028a\n9\79\u028c\n9\f9\169\u028f\139\3:\3:\3:\3:\5:")
        buf.write("\u0295\n:\3:\5:\u0298\n:\3;\3;\3;\3;\5;\u029e\n;\3;\3")
        buf.write(";\3;\5;\u02a3\n;\3<\3<\3<\3<\3<\3<\3<\3<\3<\5<\u02ae\n")
        buf.write("<\3=\3=\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\7>\u02bc\n>\f>\16")
        buf.write(">\u02bf\13>\3?\3?\3?\3?\5?\u02c5\n?\3?\3?\3?\5?\u02ca")
        buf.write("\n?\3@\3@\3@\3A\3A\3A\3B\3B\3B\3B\5B\u02d6\nB\3B\3B\3")
        buf.write("C\3C\3C\5C\u02dd\nC\3C\3C\3D\3D\3D\3D\5D\u02e5\nD\3D\3")
        buf.write("D\3E\3E\3E\7E\u02ec\nE\fE\16E\u02ef\13E\3F\3F\3G\3G\5")
        buf.write("G\u02f5\nG\3H\3H\3H\3H\3H\3I\3I\3I\3I\5I\u0300\nI\7I\u0302")
        buf.write("\nI\fI\16I\u0305\13I\3I\3I\3J\3J\3J\7J\u030c\nJ\fJ\16")
        buf.write("J\u030f\13J\3J\2\nJTdfhnpzK\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a")
        buf.write("\u008c\u008e\u0090\u0092\2\13\3\2\f\r\3\2BC\4\2$$BB\3")
        buf.write("\2=>\4\2\66\668<\3\2\64\65\3\2./\3\2\60\62\4\2\3\4\t\n")
        buf.write("\2\u032f\2\u0095\3\2\2\2\4\u009b\3\2\2\2\6\u00a9\3\2\2")
        buf.write("\2\b\u00ac\3\2\2\2\n\u00b5\3\2\2\2\f\u00c0\3\2\2\2\16")
        buf.write("\u00ce\3\2\2\2\20\u00d0\3\2\2\2\22\u00db\3\2\2\2\24\u00e9")
        buf.write("\3\2\2\2\26\u00eb\3\2\2\2\30\u00f5\3\2\2\2\32\u00fa\3")
        buf.write("\2\2\2\34\u00fc\3\2\2\2\36\u0108\3\2\2\2 \u0114\3\2\2")
        buf.write("\2\"\u0133\3\2\2\2$\u0135\3\2\2\2&\u013e\3\2\2\2(\u0149")
        buf.write("\3\2\2\2*\u0157\3\2\2\2,\u0159\3\2\2\2.\u0164\3\2\2\2")
        buf.write("\60\u017d\3\2\2\2\62\u017f\3\2\2\2\64\u0189\3\2\2\2\66")
        buf.write("\u0192\3\2\2\28\u0194\3\2\2\2:\u019c\3\2\2\2<\u01ae\3")
        buf.write("\2\2\2>\u01b0\3\2\2\2@\u01bf\3\2\2\2B\u01cb\3\2\2\2D\u01d2")
        buf.write("\3\2\2\2F\u01dc\3\2\2\2H\u01e5\3\2\2\2J\u01eb\3\2\2\2")
        buf.write("L\u01f8\3\2\2\2N\u01fb\3\2\2\2P\u01fe\3\2\2\2R\u0207\3")
        buf.write("\2\2\2T\u020f\3\2\2\2V\u0220\3\2\2\2X\u0227\3\2\2\2Z\u022c")
        buf.write("\3\2\2\2\\\u0234\3\2\2\2^\u023a\3\2\2\2`\u0241\3\2\2\2")
        buf.write("b\u0248\3\2\2\2d\u024a\3\2\2\2f\u0255\3\2\2\2h\u0260\3")
        buf.write("\2\2\2j\u026e\3\2\2\2l\u0273\3\2\2\2n\u0275\3\2\2\2p\u0282")
        buf.write("\3\2\2\2r\u0297\3\2\2\2t\u02a2\3\2\2\2v\u02ad\3\2\2\2")
        buf.write("x\u02af\3\2\2\2z\u02b1\3\2\2\2|\u02c4\3\2\2\2~\u02cb\3")
        buf.write("\2\2\2\u0080\u02ce\3\2\2\2\u0082\u02d1\3\2\2\2\u0084\u02d9")
        buf.write("\3\2\2\2\u0086\u02e0\3\2\2\2\u0088\u02e8\3\2\2\2\u008a")
        buf.write("\u02f0\3\2\2\2\u008c\u02f4\3\2\2\2\u008e\u02f6\3\2\2\2")
        buf.write("\u0090\u02fb\3\2\2\2\u0092\u0308\3\2\2\2\u0094\u0096\5")
        buf.write("\4\3\2\u0095\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0095")
        buf.write("\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099\3\2\2\2\u0099")
        buf.write("\u009a\7\2\2\3\u009a\3\3\2\2\2\u009b\u009c\7\27\2\2\u009c")
        buf.write("\u009f\5R*\2\u009d\u009e\7A\2\2\u009e\u00a0\5R*\2\u009f")
        buf.write("\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2")
        buf.write("\u00a1\u00a2\7)\2\2\u00a2\u00a3\5\6\4\2\u00a3\u00a4\7")
        buf.write("*\2\2\u00a4\5\3\2\2\2\u00a5\u00a8\5\b\5\2\u00a6\u00a8")
        buf.write("\5\32\16\2\u00a7\u00a5\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8")
        buf.write("\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2")
        buf.write("\u00aa\7\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00b1\t\2\2")
        buf.write("\2\u00ad\u00b2\5\n\6\2\u00ae\u00b2\5\f\7\2\u00af\u00b2")
        buf.write("\5\20\t\2\u00b0\u00b2\5\22\n\2\u00b1\u00ad\3\2\2\2\u00b1")
        buf.write("\u00ae\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b0\3\2\2\2")
        buf.write("\u00b2\u00b3\3\2\2\2\u00b3\u00b4\7+\2\2\u00b4\t\3\2\2")
        buf.write("\2\u00b5\u00ba\5\30\r\2\u00b6\u00b7\7,\2\2\u00b7\u00b9")
        buf.write("\5\30\r\2\u00b8\u00b6\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba")
        buf.write("\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bd\3\2\2\2")
        buf.write("\u00bc\u00ba\3\2\2\2\u00bd\u00be\7A\2\2\u00be\u00bf\5")
        buf.write("<\37\2\u00bf\13\3\2\2\2\u00c0\u00c1\5\30\r\2\u00c1\u00c2")
        buf.write("\5\16\b\2\u00c2\u00c3\5^\60\2\u00c3\r\3\2\2\2\u00c4\u00c5")
        buf.write("\7,\2\2\u00c5\u00c6\5\30\r\2\u00c6\u00c7\5\16\b\2\u00c7")
        buf.write("\u00c8\5^\60\2\u00c8\u00c9\7,\2\2\u00c9\u00cf\3\2\2\2")
        buf.write("\u00ca\u00cb\7A\2\2\u00cb\u00cc\5<\37\2\u00cc\u00cd\7")
        buf.write("\67\2\2\u00cd\u00cf\3\2\2\2\u00ce\u00c4\3\2\2\2\u00ce")
        buf.write("\u00ca\3\2\2\2\u00cf\17\3\2\2\2\u00d0\u00d5\5\30\r\2\u00d1")
        buf.write("\u00d2\7,\2\2\u00d2\u00d4\5\30\r\2\u00d3\u00d1\3\2\2\2")
        buf.write("\u00d4\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3")
        buf.write("\2\2\2\u00d6\u00d8\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00d9")
        buf.write("\7A\2\2\u00d9\u00da\5\26\f\2\u00da\21\3\2\2\2\u00db\u00dc")
        buf.write("\5\30\r\2\u00dc\u00dd\5\24\13\2\u00dd\u00de\5\u008cG\2")
        buf.write("\u00de\23\3\2\2\2\u00df\u00e0\7,\2\2\u00e0\u00e1\5\30")
        buf.write("\r\2\u00e1\u00e2\5\24\13\2\u00e2\u00e3\5\u008cG\2\u00e3")
        buf.write("\u00e4\7,\2\2\u00e4\u00ea\3\2\2\2\u00e5\u00e6\7A\2\2\u00e6")
        buf.write("\u00e7\5\26\f\2\u00e7\u00e8\7\67\2\2\u00e8\u00ea\3\2\2")
        buf.write("\2\u00e9\u00df\3\2\2\2\u00e9\u00e5\3\2\2\2\u00ea\25\3")
        buf.write("\2\2\2\u00eb\u00ec\7\36\2\2\u00ec\u00ef\7\'\2\2\u00ed")
        buf.write("\u00f0\5<\37\2\u00ee\u00f0\5\26\f\2\u00ef\u00ed\3\2\2")
        buf.write("\2\u00ef\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f2")
        buf.write("\7,\2\2\u00f2\u00f3\7\4\2\2\u00f3\u00f4\7(\2\2\u00f4\27")
        buf.write("\3\2\2\2\u00f5\u00f6\t\3\2\2\u00f6\31\3\2\2\2\u00f7\u00fb")
        buf.write("\5\34\17\2\u00f8\u00fb\5\36\20\2\u00f9\u00fb\5 \21\2\u00fa")
        buf.write("\u00f7\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00f9\3\2\2\2")
        buf.write("\u00fb\33\3\2\2\2\u00fc\u00fd\5\30\r\2\u00fd\u00ff\7%")
        buf.write("\2\2\u00fe\u0100\58\35\2\u00ff\u00fe\3\2\2\2\u00ff\u0100")
        buf.write("\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0102\7&\2\2\u0102")
        buf.write("\u0104\7)\2\2\u0103\u0105\5\\/\2\u0104\u0103\3\2\2\2\u0104")
        buf.write("\u0105\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0107\7*\2\2")
        buf.write("\u0107\35\3\2\2\2\u0108\u0109\7\23\2\2\u0109\u010b\7%")
        buf.write("\2\2\u010a\u010c\58\35\2\u010b\u010a\3\2\2\2\u010b\u010c")
        buf.write("\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010e\7&\2\2\u010e")
        buf.write("\u0110\7)\2\2\u010f\u0111\5\\/\2\u0110\u010f\3\2\2\2\u0110")
        buf.write("\u0111\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0113\7*\2\2")
        buf.write("\u0113\37\3\2\2\2\u0114\u0115\7\30\2\2\u0115\u0116\7%")
        buf.write("\2\2\u0116\u0117\7&\2\2\u0117\u0119\7)\2\2\u0118\u011a")
        buf.write("\5\\/\2\u0119\u0118\3\2\2\2\u0119\u011a\3\2\2\2\u011a")
        buf.write("\u011b\3\2\2\2\u011b\u011c\7*\2\2\u011c!\3\2\2\2\u011d")
        buf.write("\u0134\5$\23\2\u011e\u0134\5\64\33\2\u011f\u0134\5> \2")
        buf.write("\u0120\u0134\5D#\2\u0121\u0134\5L\'\2\u0122\u0134\5N(")
        buf.write("\2\u0123\u0134\5P)\2\u0124\u0125\5T+\2\u0125\u0126\7?")
        buf.write("\2\2\u0126\u0127\5Z.\2\u0127\u0128\7+\2\2\u0128\u0134")
        buf.write("\3\2\2\2\u0129\u012a\t\4\2\2\u012a\u012b\7@\2\2\u012b")
        buf.write("\u012c\5\u0084C\2\u012c\u012d\7+\2\2\u012d\u0134\3\2\2")
        buf.write("\2\u012e\u0130\7)\2\2\u012f\u0131\5\\/\2\u0130\u012f\3")
        buf.write("\2\2\2\u0130\u0131\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0134")
        buf.write("\7*\2\2\u0133\u011d\3\2\2\2\u0133\u011e\3\2\2\2\u0133")
        buf.write("\u011f\3\2\2\2\u0133\u0120\3\2\2\2\u0133\u0121\3\2\2\2")
        buf.write("\u0133\u0122\3\2\2\2\u0133\u0123\3\2\2\2\u0133\u0124\3")
        buf.write("\2\2\2\u0133\u0129\3\2\2\2\u0133\u012e\3\2\2\2\u0134#")
        buf.write("\3\2\2\2\u0135\u013a\t\2\2\2\u0136\u013b\5&\24\2\u0137")
        buf.write("\u013b\5(\25\2\u0138\u013b\5,\27\2\u0139\u013b\5.\30\2")
        buf.write("\u013a\u0136\3\2\2\2\u013a\u0137\3\2\2\2\u013a\u0138\3")
        buf.write("\2\2\2\u013a\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d")
        buf.write("\7+\2\2\u013d%\3\2\2\2\u013e\u0143\7B\2\2\u013f\u0140")
        buf.write("\7,\2\2\u0140\u0142\7B\2\2\u0141\u013f\3\2\2\2\u0142\u0145")
        buf.write("\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144")
        buf.write("\u0146\3\2\2\2\u0145\u0143\3\2\2\2\u0146\u0147\7A\2\2")
        buf.write("\u0147\u0148\5<\37\2\u0148\'\3\2\2\2\u0149\u014a\7B\2")
        buf.write("\2\u014a\u014b\5*\26\2\u014b\u014c\5^\60\2\u014c)\3\2")
        buf.write("\2\2\u014d\u014e\7,\2\2\u014e\u014f\7B\2\2\u014f\u0150")
        buf.write("\5*\26\2\u0150\u0151\5^\60\2\u0151\u0152\7,\2\2\u0152")
        buf.write("\u0158\3\2\2\2\u0153\u0154\7A\2\2\u0154\u0155\5<\37\2")
        buf.write("\u0155\u0156\7\67\2\2\u0156\u0158\3\2\2\2\u0157\u014d")
        buf.write("\3\2\2\2\u0157\u0153\3\2\2\2\u0158+\3\2\2\2\u0159\u015e")
        buf.write("\7B\2\2\u015a\u015b\7,\2\2\u015b\u015d\7B\2\2\u015c\u015a")
        buf.write("\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e")
        buf.write("\u015f\3\2\2\2\u015f\u0161\3\2\2\2\u0160\u015e\3\2\2\2")
        buf.write("\u0161\u0162\7A\2\2\u0162\u0163\5\62\32\2\u0163-\3\2\2")
        buf.write("\2\u0164\u0165\7B\2\2\u0165\u016b\5\60\31\2\u0166\u016c")
        buf.write("\5\u008cG\2\u0167\u0169\5\u0086D\2\u0168\u016a\5^\60\2")
        buf.write("\u0169\u0168\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016c\3")
        buf.write("\2\2\2\u016b\u0166\3\2\2\2\u016b\u0167\3\2\2\2\u016c/")
        buf.write("\3\2\2\2\u016d\u016e\7,\2\2\u016e\u016f\7B\2\2\u016f\u0175")
        buf.write("\5\60\31\2\u0170\u0176\5\u008cG\2\u0171\u0173\5\u0086")
        buf.write("D\2\u0172\u0174\5^\60\2\u0173\u0172\3\2\2\2\u0173\u0174")
        buf.write("\3\2\2\2\u0174\u0176\3\2\2\2\u0175\u0170\3\2\2\2\u0175")
        buf.write("\u0171\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0178\7,\2\2")
        buf.write("\u0178\u017e\3\2\2\2\u0179\u017a\7A\2\2\u017a\u017b\5")
        buf.write("\62\32\2\u017b\u017c\7\67\2\2\u017c\u017e\3\2\2\2\u017d")
        buf.write("\u016d\3\2\2\2\u017d\u0179\3\2\2\2\u017e\61\3\2\2\2\u017f")
        buf.write("\u0180\7\36\2\2\u0180\u0183\7\'\2\2\u0181\u0184\5<\37")
        buf.write("\2\u0182\u0184\5\62\32\2\u0183\u0181\3\2\2\2\u0183\u0182")
        buf.write("\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186\7,\2\2\u0186")
        buf.write("\u0187\7\4\2\2\u0187\u0188\7(\2\2\u0188\63\3\2\2\2\u0189")
        buf.write("\u018a\5\66\34\2\u018a\u018b\7\67\2\2\u018b\u018c\5^\60")
        buf.write("\2\u018c\u018d\7+\2\2\u018d\65\3\2\2\2\u018e\u0193\5J")
        buf.write("&\2\u018f\u0190\5J&\2\u0190\u0191\5x=\2\u0191\u0193\3")
        buf.write("\2\2\2\u0192\u018e\3\2\2\2\u0192\u018f\3\2\2\2\u0193\67")
        buf.write("\3\2\2\2\u0194\u0199\5:\36\2\u0195\u0196\7+\2\2\u0196")
        buf.write("\u0198\5:\36\2\u0197\u0195\3\2\2\2\u0198\u019b\3\2\2\2")
        buf.write("\u0199\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a9\3\2\2")
        buf.write("\2\u019b\u0199\3\2\2\2\u019c\u01a1\7B\2\2\u019d\u019e")
        buf.write("\7,\2\2\u019e\u01a0\7B\2\2\u019f\u019d\3\2\2\2\u01a0\u01a3")
        buf.write("\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2")
        buf.write("\u01a4\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a7\7A\2\2")
        buf.write("\u01a5\u01a8\5<\37\2\u01a6\u01a8\5\62\32\2\u01a7\u01a5")
        buf.write("\3\2\2\2\u01a7\u01a6\3\2\2\2\u01a8;\3\2\2\2\u01a9\u01af")
        buf.write("\7\21\2\2\u01aa\u01af\7\26\2\2\u01ab\u01af\7\33\2\2\u01ac")
        buf.write("\u01af\7\37\2\2\u01ad\u01af\5R*\2\u01ae\u01a9\3\2\2\2")
        buf.write("\u01ae\u01aa\3\2\2\2\u01ae\u01ab\3\2\2\2\u01ae\u01ac\3")
        buf.write("\2\2\2\u01ae\u01ad\3\2\2\2\u01af=\3\2\2\2\u01b0\u01b1")
        buf.write("\7\31\2\2\u01b1\u01b2\7%\2\2\u01b2\u01b3\5^\60\2\u01b3")
        buf.write("\u01b4\7&\2\2\u01b4\u01b6\7)\2\2\u01b5\u01b7\5\\/\2\u01b6")
        buf.write("\u01b5\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b8\3\2\2\2")
        buf.write("\u01b8\u01ba\7*\2\2\u01b9\u01bb\5@!\2\u01ba\u01b9\3\2")
        buf.write("\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bd\3\2\2\2\u01bc\u01be")
        buf.write("\5B\"\2\u01bd\u01bc\3\2\2\2\u01bd\u01be\3\2\2\2\u01be")
        buf.write("?\3\2\2\2\u01bf\u01c0\7\35\2\2\u01c0\u01c1\7%\2\2\u01c1")
        buf.write("\u01c2\5^\60\2\u01c2\u01c3\7&\2\2\u01c3\u01c5\7)\2\2\u01c4")
        buf.write("\u01c6\5\\/\2\u01c5\u01c4\3\2\2\2\u01c5\u01c6\3\2\2\2")
        buf.write("\u01c6\u01c7\3\2\2\2\u01c7\u01c9\7*\2\2\u01c8\u01ca\5")
        buf.write("@!\2\u01c9\u01c8\3\2\2\2\u01c9\u01ca\3\2\2\2\u01caA\3")
        buf.write("\2\2\2\u01cb\u01cc\7!\2\2\u01cc\u01ce\7)\2\2\u01cd\u01cf")
        buf.write("\5\\/\2\u01ce\u01cd\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf")
        buf.write("\u01d0\3\2\2\2\u01d0\u01d1\7*\2\2\u01d1C\3\2\2\2\u01d2")
        buf.write("\u01d3\7\20\2\2\u01d3\u01d4\7%\2\2\u01d4\u01d5\5F$\2\u01d5")
        buf.write("\u01d6\7&\2\2\u01d6\u01d8\7)\2\2\u01d7\u01d9\5\\/\2\u01d8")
        buf.write("\u01d7\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da\3\2\2\2")
        buf.write("\u01da\u01db\7*\2\2\u01dbE\3\2\2\2\u01dc\u01dd\5J&\2\u01dd")
        buf.write("\u01de\7\"\2\2\u01de\u01df\5H%\2\u01df\u01e0\7-\2\2\u01e0")
        buf.write("\u01e3\5H%\2\u01e1\u01e2\7 \2\2\u01e2\u01e4\5H%\2\u01e3")
        buf.write("\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4G\3\2\2\2\u01e5")
        buf.write("\u01e6\5^\60\2\u01e6I\3\2\2\2\u01e7\u01e8\b&\1\2\u01e8")
        buf.write("\u01ec\5|?\2\u01e9\u01ec\7$\2\2\u01ea\u01ec\7B\2\2\u01eb")
        buf.write("\u01e7\3\2\2\2\u01eb\u01e9\3\2\2\2\u01eb\u01ea\3\2\2\2")
        buf.write("\u01ec\u01f5\3\2\2\2\u01ed\u01ee\f\6\2\2\u01ee\u01f1\7")
        buf.write("?\2\2\u01ef\u01f2\7B\2\2\u01f0\u01f2\5Z.\2\u01f1\u01ef")
        buf.write("\3\2\2\2\u01f1\u01f0\3\2\2\2\u01f2\u01f4\3\2\2\2\u01f3")
        buf.write("\u01ed\3\2\2\2\u01f4\u01f7\3\2\2\2\u01f5\u01f3\3\2\2\2")
        buf.write("\u01f5\u01f6\3\2\2\2\u01f6K\3\2\2\2\u01f7\u01f5\3\2\2")
        buf.write("\2\u01f8\u01f9\7\17\2\2\u01f9\u01fa\7+\2\2\u01faM\3\2")
        buf.write("\2\2\u01fb\u01fc\7\24\2\2\u01fc\u01fd\7+\2\2\u01fdO\3")
        buf.write("\2\2\2\u01fe\u0202\7#\2\2\u01ff\u0201\5^\60\2\u0200\u01ff")
        buf.write("\3\2\2\2\u0201\u0204\3\2\2\2\u0202\u0200\3\2\2\2\u0202")
        buf.write("\u0203\3\2\2\2\u0203\u0205\3\2\2\2\u0204\u0202\3\2\2\2")
        buf.write("\u0205\u0206\7+\2\2\u0206Q\3\2\2\2\u0207\u0208\t\4\2\2")
        buf.write("\u0208S\3\2\2\2\u0209\u020a\b+\1\2\u020a\u020b\7\34\2")
        buf.write("\2\u020b\u0210\5Z.\2\u020c\u0210\5|?\2\u020d\u0210\7$")
        buf.write("\2\2\u020e\u0210\7B\2\2\u020f\u0209\3\2\2\2\u020f\u020c")
        buf.write("\3\2\2\2\u020f\u020d\3\2\2\2\u020f\u020e\3\2\2\2\u0210")
        buf.write("\u021b\3\2\2\2\u0211\u0212\f\b\2\2\u0212\u0215\7?\2\2")
        buf.write("\u0213\u0216\7B\2\2\u0214\u0216\5Z.\2\u0215\u0213\3\2")
        buf.write("\2\2\u0215\u0214\3\2\2\2\u0216\u021a\3\2\2\2\u0217\u0218")
        buf.write("\f\6\2\2\u0218\u021a\5x=\2\u0219\u0211\3\2\2\2\u0219\u0217")
        buf.write("\3\2\2\2\u021a\u021d\3\2\2\2\u021b\u0219\3\2\2\2\u021b")
        buf.write("\u021c\3\2\2\2\u021cU\3\2\2\2\u021d\u021b\3\2\2\2\u021e")
        buf.write("\u0221\5T+\2\u021f\u0221\7+\2\2\u0220\u021e\3\2\2\2\u0220")
        buf.write("\u021f\3\2\2\2\u0221W\3\2\2\2\u0222\u0223\5^\60\2\u0223")
        buf.write("\u0224\7,\2\2\u0224\u0226\3\2\2\2\u0225\u0222\3\2\2\2")
        buf.write("\u0226\u0229\3\2\2\2\u0227\u0225\3\2\2\2\u0227\u0228\3")
        buf.write("\2\2\2\u0228\u022a\3\2\2\2\u0229\u0227\3\2\2\2\u022a\u022b")
        buf.write("\5^\60\2\u022bY\3\2\2\2\u022c\u022d\7B\2\2\u022d\u022f")
        buf.write("\7%\2\2\u022e\u0230\5\u0088E\2\u022f\u022e\3\2\2\2\u022f")
        buf.write("\u0230\3\2\2\2\u0230\u0231\3\2\2\2\u0231\u0232\7&\2\2")
        buf.write("\u0232[\3\2\2\2\u0233\u0235\5\"\22\2\u0234\u0233\3\2\2")
        buf.write("\2\u0235\u0236\3\2\2\2\u0236\u0234\3\2\2\2\u0236\u0237")
        buf.write("\3\2\2\2\u0237]\3\2\2\2\u0238\u023b\5`\61\2\u0239\u023b")
        buf.write("\5\u0086D\2\u023a\u0238\3\2\2\2\u023a\u0239\3\2\2\2\u023b")
        buf.write("_\3\2\2\2\u023c\u023d\5b\62\2\u023d\u023e\t\5\2\2\u023e")
        buf.write("\u023f\5b\62\2\u023f\u0242\3\2\2\2\u0240\u0242\5b\62\2")
        buf.write("\u0241\u023c\3\2\2\2\u0241\u0240\3\2\2\2\u0242a\3\2\2")
        buf.write("\2\u0243\u0244\5d\63\2\u0244\u0245\t\6\2\2\u0245\u0246")
        buf.write("\5d\63\2\u0246\u0249\3\2\2\2\u0247\u0249\5d\63\2\u0248")
        buf.write("\u0243\3\2\2\2\u0248\u0247\3\2\2\2\u0249c\3\2\2\2\u024a")
        buf.write("\u024b\b\63\1\2\u024b\u024c\5f\64\2\u024c\u0252\3\2\2")
        buf.write("\2\u024d\u024e\f\4\2\2\u024e\u024f\t\7\2\2\u024f\u0251")
        buf.write("\5f\64\2\u0250\u024d\3\2\2\2\u0251\u0254\3\2\2\2\u0252")
        buf.write("\u0250\3\2\2\2\u0252\u0253\3\2\2\2\u0253e\3\2\2\2\u0254")
        buf.write("\u0252\3\2\2\2\u0255\u0256\b\64\1\2\u0256\u0257\5h\65")
        buf.write("\2\u0257\u025d\3\2\2\2\u0258\u0259\f\4\2\2\u0259\u025a")
        buf.write("\t\b\2\2\u025a\u025c\5h\65\2\u025b\u0258\3\2\2\2\u025c")
        buf.write("\u025f\3\2\2\2\u025d\u025b\3\2\2\2\u025d\u025e\3\2\2\2")
        buf.write("\u025eg\3\2\2\2\u025f\u025d\3\2\2\2\u0260\u0261\b\65\1")
        buf.write("\2\u0261\u0262\5j\66\2\u0262\u0268\3\2\2\2\u0263\u0264")
        buf.write("\f\4\2\2\u0264\u0265\t\t\2\2\u0265\u0267\5j\66\2\u0266")
        buf.write("\u0263\3\2\2\2\u0267\u026a\3\2\2\2\u0268\u0266\3\2\2\2")
        buf.write("\u0268\u0269\3\2\2\2\u0269i\3\2\2\2\u026a\u0268\3\2\2")
        buf.write("\2\u026b\u026c\7\63\2\2\u026c\u026f\5j\66\2\u026d\u026f")
        buf.write("\5l\67\2\u026e\u026b\3\2\2\2\u026e\u026d\3\2\2\2\u026f")
        buf.write("k\3\2\2\2\u0270\u0271\7/\2\2\u0271\u0274\5l\67\2\u0272")
        buf.write("\u0274\5n8\2\u0273\u0270\3\2\2\2\u0273\u0272\3\2\2\2\u0274")
        buf.write("m\3\2\2\2\u0275\u0276\b8\1\2\u0276\u0277\5p9\2\u0277\u027f")
        buf.write("\3\2\2\2\u0278\u0279\f\4\2\2\u0279\u027a\7\'\2\2\u027a")
        buf.write("\u027b\5n8\2\u027b\u027c\7(\2\2\u027c\u027e\3\2\2\2\u027d")
        buf.write("\u0278\3\2\2\2\u027e\u0281\3\2\2\2\u027f\u027d\3\2\2\2")
        buf.write("\u027f\u0280\3\2\2\2\u0280o\3\2\2\2\u0281\u027f\3\2\2")
        buf.write("\2\u0282\u0283\b9\1\2\u0283\u0284\5r:\2\u0284\u028d\3")
        buf.write("\2\2\2\u0285\u0286\f\4\2\2\u0286\u0289\7?\2\2\u0287\u028a")
        buf.write("\7B\2\2\u0288\u028a\5Z.\2\u0289\u0287\3\2\2\2\u0289\u0288")
        buf.write("\3\2\2\2\u028a\u028c\3\2\2\2\u028b\u0285\3\2\2\2\u028c")
        buf.write("\u028f\3\2\2\2\u028d\u028b\3\2\2\2\u028d\u028e\3\2\2\2")
        buf.write("\u028eq\3\2\2\2\u028f\u028d\3\2\2\2\u0290\u0291\t\4\2")
        buf.write("\2\u0291\u0294\7@\2\2\u0292\u0295\5\u0084C\2\u0293\u0295")
        buf.write("\7C\2\2\u0294\u0292\3\2\2\2\u0294\u0293\3\2\2\2\u0295")
        buf.write("\u0298\3\2\2\2\u0296\u0298\5t;\2\u0297\u0290\3\2\2\2\u0297")
        buf.write("\u0296\3\2\2\2\u0298s\3\2\2\2\u0299\u029a\7\34\2\2\u029a")
        buf.write("\u029b\5v<\2\u029b\u029d\7%\2\2\u029c\u029e\5\u0088E\2")
        buf.write("\u029d\u029c\3\2\2\2\u029d\u029e\3\2\2\2\u029e\u029f\3")
        buf.write("\2\2\2\u029f\u02a0\7&\2\2\u02a0\u02a3\3\2\2\2\u02a1\u02a3")
        buf.write("\5v<\2\u02a2\u0299\3\2\2\2\u02a2\u02a1\3\2\2\2\u02a3u")
        buf.write("\3\2\2\2\u02a4\u02ae\5\u008aF\2\u02a5\u02ae\7$\2\2\u02a6")
        buf.write("\u02ae\7B\2\2\u02a7\u02a8\7%\2\2\u02a8\u02a9\5`\61\2\u02a9")
        buf.write("\u02aa\7&\2\2\u02aa\u02ae\3\2\2\2\u02ab\u02ae\7\22\2\2")
        buf.write("\u02ac\u02ae\5\u008cG\2\u02ad\u02a4\3\2\2\2\u02ad\u02a5")
        buf.write("\3\2\2\2\u02ad\u02a6\3\2\2\2\u02ad\u02a7\3\2\2\2\u02ad")
        buf.write("\u02ab\3\2\2\2\u02ad\u02ac\3\2\2\2\u02aew\3\2\2\2\u02af")
        buf.write("\u02b0\5z>\2\u02b0y\3\2\2\2\u02b1\u02b2\b>\1\2\u02b2\u02b3")
        buf.write("\7\'\2\2\u02b3\u02b4\5^\60\2\u02b4\u02b5\7(\2\2\u02b5")
        buf.write("\u02bd\3\2\2\2\u02b6\u02b7\f\4\2\2\u02b7\u02b8\7\'\2\2")
        buf.write("\u02b8\u02b9\5^\60\2\u02b9\u02ba\7(\2\2\u02ba\u02bc\3")
        buf.write("\2\2\2\u02bb\u02b6\3\2\2\2\u02bc\u02bf\3\2\2\2\u02bd\u02bb")
        buf.write("\3\2\2\2\u02bd\u02be\3\2\2\2\u02be{\3\2\2\2\u02bf\u02bd")
        buf.write("\3\2\2\2\u02c0\u02c1\7\34\2\2\u02c1\u02c5\5Z.\2\u02c2")
        buf.write("\u02c5\7$\2\2\u02c3\u02c5\7B\2\2\u02c4\u02c0\3\2\2\2\u02c4")
        buf.write("\u02c2\3\2\2\2\u02c4\u02c3\3\2\2\2\u02c5\u02c6\3\2\2\2")
        buf.write("\u02c6\u02c9\7@\2\2\u02c7\u02ca\7C\2\2\u02c8\u02ca\5\u0084")
        buf.write("C\2\u02c9\u02c7\3\2\2\2\u02c9\u02c8\3\2\2\2\u02ca}\3\2")
        buf.write("\2\2\u02cb\u02cc\7?\2\2\u02cc\u02cd\7B\2\2\u02cd\177\3")
        buf.write("\2\2\2\u02ce\u02cf\7@\2\2\u02cf\u02d0\7C\2\2\u02d0\u0081")
        buf.write("\3\2\2\2\u02d1\u02d2\7?\2\2\u02d2\u02d3\7B\2\2\u02d3\u02d5")
        buf.write("\7%\2\2\u02d4\u02d6\5\u0088E\2\u02d5\u02d4\3\2\2\2\u02d5")
        buf.write("\u02d6\3\2\2\2\u02d6\u02d7\3\2\2\2\u02d7\u02d8\7&\2\2")
        buf.write("\u02d8\u0083\3\2\2\2\u02d9\u02da\7C\2\2\u02da\u02dc\7")
        buf.write("%\2\2\u02db\u02dd\5\u0088E\2\u02dc\u02db\3\2\2\2\u02dc")
        buf.write("\u02dd\3\2\2\2\u02dd\u02de\3\2\2\2\u02de\u02df\7&\2\2")
        buf.write("\u02df\u0085\3\2\2\2\u02e0\u02e1\7\34\2\2\u02e1\u02e2")
        buf.write("\7B\2\2\u02e2\u02e4\7%\2\2\u02e3\u02e5\5\u0088E\2\u02e4")
        buf.write("\u02e3\3\2\2\2\u02e4\u02e5\3\2\2\2\u02e5\u02e6\3\2\2\2")
        buf.write("\u02e6\u02e7\7&\2\2\u02e7\u0087\3\2\2\2\u02e8\u02ed\5")
        buf.write("`\61\2\u02e9\u02ea\7,\2\2\u02ea\u02ec\5`\61\2\u02eb\u02e9")
        buf.write("\3\2\2\2\u02ec\u02ef\3\2\2\2\u02ed\u02eb\3\2\2\2\u02ed")
        buf.write("\u02ee\3\2\2\2\u02ee\u0089\3\2\2\2\u02ef\u02ed\3\2\2\2")
        buf.write("\u02f0\u02f1\t\n\2\2\u02f1\u008b\3\2\2\2\u02f2\u02f5\5")
        buf.write("\u008eH\2\u02f3\u02f5\5\u0090I\2\u02f4\u02f2\3\2\2\2\u02f4")
        buf.write("\u02f3\3\2\2\2\u02f5\u008d\3\2\2\2\u02f6\u02f7\7\36\2")
        buf.write("\2\u02f7\u02f8\7%\2\2\u02f8\u02f9\5\u0092J\2\u02f9\u02fa")
        buf.write("\7&\2\2\u02fa\u008f\3\2\2\2\u02fb\u02fc\7\36\2\2\u02fc")
        buf.write("\u0303\7%\2\2\u02fd\u02ff\5\u008eH\2\u02fe\u0300\7,\2")
        buf.write("\2\u02ff\u02fe\3\2\2\2\u02ff\u0300\3\2\2\2\u0300\u0302")
        buf.write("\3\2\2\2\u0301\u02fd\3\2\2\2\u0302\u0305\3\2\2\2\u0303")
        buf.write("\u0301\3\2\2\2\u0303\u0304\3\2\2\2\u0304\u0306\3\2\2\2")
        buf.write("\u0305\u0303\3\2\2\2\u0306\u0307\7&\2\2\u0307\u0091\3")
        buf.write("\2\2\2\u0308\u030d\5^\60\2\u0309\u030a\7,\2\2\u030a\u030c")
        buf.write("\5^\60\2\u030b\u0309\3\2\2\2\u030c\u030f\3\2\2\2\u030d")
        buf.write("\u030b\3\2\2\2\u030d\u030e\3\2\2\2\u030e\u0093\3\2\2\2")
        buf.write("\u030f\u030d\3\2\2\2R\u0097\u009f\u00a7\u00a9\u00b1\u00ba")
        buf.write("\u00ce\u00d5\u00e9\u00ef\u00fa\u00ff\u0104\u010b\u0110")
        buf.write("\u0119\u0130\u0133\u013a\u0143\u0157\u015e\u0169\u016b")
        buf.write("\u0173\u0175\u017d\u0183\u0192\u0199\u01a1\u01a7\u01ae")
        buf.write("\u01b6\u01ba\u01bd\u01c5\u01c9\u01ce\u01d8\u01e3\u01eb")
        buf.write("\u01f1\u01f5\u0202\u020f\u0215\u0219\u021b\u0220\u0227")
        buf.write("\u022f\u0236\u023a\u0241\u0248\u0252\u025d\u0268\u026e")
        buf.write("\u0273\u027f\u0289\u028d\u0294\u0297\u029d\u02a2\u02ad")
        buf.write("\u02bd\u02c4\u02c9\u02d5\u02dc\u02e4\u02ed\u02f4\u02ff")
        buf.write("\u0303\u030d")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'Val'", "'Var'", "'$'", 
                     "'Break'", "'Foreach'", "'Int'", "'Null'", "'Constructor'", 
                     "'Continue'", "'True'", "'Float'", "'Class'", "'Destructor'", 
                     "'If'", "'False'", "'Boolean'", "'New'", "'Elseif'", 
                     "'Array'", "'String'", "'By'", "'Else'", "'In'", "'Return'", 
                     "'Self'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "';'", "','", "'..'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'==.'", "'+.'", "'.'", "'::'", 
                     "':'" ]

    symbolicNames = [ "<INVALID>", "LITERAL_BOOLEAN", "LITERAL_INT", "LITERAL_INT_DEC", 
                      "LITERAL_INT_HEX", "LITERAL_INT_OCT", "LITERAL_INT_BIN", 
                      "LITERAL_FLOAT", "LITERAL_STRING", "DOUBLE_QUOTE", 
                      "VAL", "VAR", "STATIC", "BREAK", "FOREACH", "INT", 
                      "NULL", "CONSTRUCTOR", "CONTINUE", "TRUE", "FLOAT", 
                      "CLASS", "DESTRUCTOR", "IF", "FALSE", "BOOLEAN", "NEW", 
                      "ELSEIF", "ARRAY", "STRING", "BY", "ELSE", "IN", "RETURN", 
                      "SELF", "LB", "RB", "LS", "RS", "LP", "RP", "SEMI", 
                      "COMMA", "DOTDOT", "ADD", "SUBTRACT", "MULTIPLY", 
                      "DIVIDE", "MODULO", "NOT", "AND", "OR", "EQUAL", "ASSIGN", 
                      "NOT_EQUAL", "LESS_THAN", "LEQ", "GREATER_THAN", "GEQ", 
                      "EQUAL_STRING", "STRING_CONCAT", "DOT", "DOUBLE_COLON", 
                      "COLON", "ID", "DOLLAR_ID", "BLOCK_COMMENT", "WS", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
    RULE_assign_stmt = 25
    RULE_assign_lhs = 26
    RULE_params_list = 27
    RULE_params = 28
    RULE_data_type = 29
    RULE_if_stmt = 30
    RULE_else_if_body = 31
    RULE_else_body = 32
    RULE_for_in_stmt = 33
    RULE_for_in_body = 34
    RULE_for_in_expr = 35
    RULE_scalar_variable = 36
    RULE_break_stmt = 37
    RULE_continue_stmt = 38
    RULE_return_stmt = 39
    RULE_class_name = 40
    RULE_method_invoc_literal = 41
    RULE_method_invoc = 42
    RULE_expr_list = 43
    RULE_funcall = 44
    RULE_block_stmt = 45
    RULE_all_expr = 46
    RULE_op = 47
    RULE_op1 = 48
    RULE_op2 = 49
    RULE_op3 = 50
    RULE_op4 = 51
    RULE_op5 = 52
    RULE_op6 = 53
    RULE_op7 = 54
    RULE_op8 = 55
    RULE_op9 = 56
    RULE_op10 = 57
    RULE_operands = 58
    RULE_element_expr = 59
    RULE_index_ops = 60
    RULE_static_member_access = 61
    RULE_instance_attr = 62
    RULE_static_attr = 63
    RULE_instance_method = 64
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
                   "var_array_pair", "var_array_decl_tail", "assign_stmt", 
                   "assign_lhs", "params_list", "params", "data_type", "if_stmt", 
                   "else_if_body", "else_body", "for_in_stmt", "for_in_body", 
                   "for_in_expr", "scalar_variable", "break_stmt", "continue_stmt", 
                   "return_stmt", "class_name", "method_invoc_literal", 
                   "method_invoc", "expr_list", "funcall", "block_stmt", 
                   "all_expr", "op", "op1", "op2", "op3", "op4", "op5", 
                   "op6", "op7", "op8", "op9", "op10", "operands", "element_expr", 
                   "index_ops", "static_member_access", "instance_attr", 
                   "static_attr", "instance_method", "static_method", "object_create", 
                   "list_of_expr", "literal", "literal_array", "literal_idx_array", 
                   "literal_mtd_array", "array_element" ]

    EOF = Token.EOF
    LITERAL_BOOLEAN=1
    LITERAL_INT=2
    LITERAL_INT_DEC=3
    LITERAL_INT_HEX=4
    LITERAL_INT_OCT=5
    LITERAL_INT_BIN=6
    LITERAL_FLOAT=7
    LITERAL_STRING=8
    DOUBLE_QUOTE=9
    VAL=10
    VAR=11
    STATIC=12
    BREAK=13
    FOREACH=14
    INT=15
    NULL=16
    CONSTRUCTOR=17
    CONTINUE=18
    TRUE=19
    FLOAT=20
    CLASS=21
    DESTRUCTOR=22
    IF=23
    FALSE=24
    BOOLEAN=25
    NEW=26
    ELSEIF=27
    ARRAY=28
    STRING=29
    BY=30
    ELSE=31
    IN=32
    RETURN=33
    SELF=34
    LB=35
    RB=36
    LS=37
    RS=38
    LP=39
    RP=40
    SEMI=41
    COMMA=42
    DOTDOT=43
    ADD=44
    SUBTRACT=45
    MULTIPLY=46
    DIVIDE=47
    MODULO=48
    NOT=49
    AND=50
    OR=51
    EQUAL=52
    ASSIGN=53
    NOT_EQUAL=54
    LESS_THAN=55
    LEQ=56
    GREATER_THAN=57
    GEQ=58
    EQUAL_STRING=59
    STRING_CONCAT=60
    DOT=61
    DOUBLE_COLON=62
    COLON=63
    ID=64
    DOLLAR_ID=65
    BLOCK_COMMENT=66
    WS=67
    UNCLOSE_STRING=68
    ILLEGAL_ESCAPE=69
    ERROR_CHAR=70

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
        __slots__ = 'parser'

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
            self.state = 153
            self.match(D96Parser.CLASS)
            self.state = 154
            self.class_name()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 155
                self.match(D96Parser.COLON)
                self.state = 156
                self.class_name()


            self.state = 159
            self.match(D96Parser.LP)
            self.state = 160
            self.class_body()
            self.state = 161
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
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (D96Parser.VAL - 10)) | (1 << (D96Parser.VAR - 10)) | (1 << (D96Parser.CONSTRUCTOR - 10)) | (1 << (D96Parser.DESTRUCTOR - 10)) | (1 << (D96Parser.ID - 10)) | (1 << (D96Parser.DOLLAR_ID - 10)))) != 0):
                self.state = 165
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 163
                    self.class_attr()
                    pass
                elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.DOLLAR_ID]:
                    self.state = 164
                    self.class_method()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 169
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

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_attr" ):
                return visitor.visitClass_attr(self)
            else:
                return visitor.visitChildren(self)




    def class_attr(self):

        localctx = D96Parser.Class_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_attr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 171
                self.attr_no_value()
                pass

            elif la_ == 2:
                self.state = 172
                self.attr_with_value()
                pass

            elif la_ == 3:
                self.state = 173
                self.attr_array_no_value()
                pass

            elif la_ == 4:
                self.state = 174
                self.attr_array_with_value()
                pass


            self.state = 177
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_no_valueContext(ParserRuleContext):
        __slots__ = 'parser'

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


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_no_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_no_value" ):
                return visitor.visitAttr_no_value(self)
            else:
                return visitor.visitChildren(self)




    def attr_no_value(self):

        localctx = D96Parser.Attr_no_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attr_no_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
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
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_with_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def any_id(self):
            return self.getTypedRuleContext(D96Parser.Any_idContext,0)


        def attr_pair(self):
            return self.getTypedRuleContext(D96Parser.Attr_pairContext,0)


        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attr_with_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_with_value" ):
                return visitor.visitAttr_with_value(self)
            else:
                return visitor.visitChildren(self)




    def attr_with_value(self):

        localctx = D96Parser.Attr_with_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attr_with_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.any_id()
            self.state = 191
            self.attr_pair()
            self.state = 192
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_pair" ):
                return visitor.visitAttr_pair(self)
            else:
                return visitor.visitChildren(self)




    def attr_pair(self):

        localctx = D96Parser.Attr_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attr_pair)
        try:
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(D96Parser.COMMA)
                self.state = 195
                self.any_id()
                self.state = 196
                self.attr_pair()
                self.state = 197
                self.all_expr()
                self.state = 198
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.match(D96Parser.COLON)
                self.state = 201
                self.data_type()
                self.state = 202
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
        __slots__ = 'parser'

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


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_array_no_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_array_no_value" ):
                return visitor.visitAttr_array_no_value(self)
            else:
                return visitor.visitChildren(self)




    def attr_array_no_value(self):

        localctx = D96Parser.Attr_array_no_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attr_array_no_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.any_id()
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 207
                self.match(D96Parser.COMMA)
                self.state = 208
                self.any_id()
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 214
            self.match(D96Parser.COLON)
            self.state = 215
            self.attr_array_decl_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_array_with_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def any_id(self):
            return self.getTypedRuleContext(D96Parser.Any_idContext,0)


        def attr_array_pair(self):
            return self.getTypedRuleContext(D96Parser.Attr_array_pairContext,0)


        def literal_array(self):
            return self.getTypedRuleContext(D96Parser.Literal_arrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attr_array_with_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_array_with_value" ):
                return visitor.visitAttr_array_with_value(self)
            else:
                return visitor.visitChildren(self)




    def attr_array_with_value(self):

        localctx = D96Parser.Attr_array_with_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attr_array_with_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.any_id()
            self.state = 218
            self.attr_array_pair()
            self.state = 219
            self.literal_array()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_array_pairContext(ParserRuleContext):
        __slots__ = 'parser'

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


        def literal_array(self):
            return self.getTypedRuleContext(D96Parser.Literal_arrayContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def attr_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Attr_array_decl_tailContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_array_pair

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_array_pair" ):
                return visitor.visitAttr_array_pair(self)
            else:
                return visitor.visitChildren(self)




    def attr_array_pair(self):

        localctx = D96Parser.Attr_array_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attr_array_pair)
        try:
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(D96Parser.COMMA)
                self.state = 222
                self.any_id()
                self.state = 223
                self.attr_array_pair()
                self.state = 224
                self.literal_array()
                self.state = 225
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.match(D96Parser.COLON)
                self.state = 228
                self.attr_array_decl_tail()
                self.state = 229
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
        __slots__ = 'parser'

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


        def attr_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Attr_array_decl_tailContext,0)


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
        self.enterRule(localctx, 20, self.RULE_attr_array_decl_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(D96Parser.ARRAY)
            self.state = 234
            self.match(D96Parser.LS)
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.SELF, D96Parser.ID]:
                self.state = 235
                self.data_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 236
                self.attr_array_decl_tail()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 239
            self.match(D96Parser.COMMA)

            self.state = 240
            self.match(D96Parser.LITERAL_INT)
            self.state = 241
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Any_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_any_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAny_id" ):
                return visitor.visitAny_id(self)
            else:
                return visitor.visitChildren(self)




    def any_id(self):

        localctx = D96Parser.Any_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_any_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
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
        self.enterRule(localctx, 24, self.RULE_class_method)
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.normal_method()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 247
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_method" ):
                return visitor.visitNormal_method(self)
            else:
                return visitor.visitChildren(self)




    def normal_method(self):

        localctx = D96Parser.Normal_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_normal_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.any_id()
            self.state = 251
            self.match(D96Parser.LB)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 252
                self.params_list()


            self.state = 255
            self.match(D96Parser.RB)
            self.state = 256
            self.match(D96Parser.LP)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (D96Parser.VAL - 10)) | (1 << (D96Parser.VAR - 10)) | (1 << (D96Parser.BREAK - 10)) | (1 << (D96Parser.FOREACH - 10)) | (1 << (D96Parser.CONTINUE - 10)) | (1 << (D96Parser.IF - 10)) | (1 << (D96Parser.NEW - 10)) | (1 << (D96Parser.RETURN - 10)) | (1 << (D96Parser.SELF - 10)) | (1 << (D96Parser.LP - 10)) | (1 << (D96Parser.ID - 10)))) != 0):
                self.state = 257
                self.block_stmt()


            self.state = 260
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
        self.enterRule(localctx, 28, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 263
            self.match(D96Parser.LB)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 264
                self.params_list()


            self.state = 267
            self.match(D96Parser.RB)
            self.state = 268
            self.match(D96Parser.LP)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (D96Parser.VAL - 10)) | (1 << (D96Parser.VAR - 10)) | (1 << (D96Parser.BREAK - 10)) | (1 << (D96Parser.FOREACH - 10)) | (1 << (D96Parser.CONTINUE - 10)) | (1 << (D96Parser.IF - 10)) | (1 << (D96Parser.NEW - 10)) | (1 << (D96Parser.RETURN - 10)) | (1 << (D96Parser.SELF - 10)) | (1 << (D96Parser.LP - 10)) | (1 << (D96Parser.ID - 10)))) != 0):
                self.state = 269
                self.block_stmt()


            self.state = 272
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
        self.enterRule(localctx, 30, self.RULE_destructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(D96Parser.DESTRUCTOR)
            self.state = 275
            self.match(D96Parser.LB)
            self.state = 276
            self.match(D96Parser.RB)
            self.state = 277
            self.match(D96Parser.LP)
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (D96Parser.VAL - 10)) | (1 << (D96Parser.VAR - 10)) | (1 << (D96Parser.BREAK - 10)) | (1 << (D96Parser.FOREACH - 10)) | (1 << (D96Parser.CONTINUE - 10)) | (1 << (D96Parser.IF - 10)) | (1 << (D96Parser.NEW - 10)) | (1 << (D96Parser.RETURN - 10)) | (1 << (D96Parser.SELF - 10)) | (1 << (D96Parser.LP - 10)) | (1 << (D96Parser.ID - 10)))) != 0):
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


        def method_invoc_literal(self):
            return self.getTypedRuleContext(D96Parser.Method_invoc_literalContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def static_method(self):
            return self.getTypedRuleContext(D96Parser.Static_methodContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 285
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 286
                self.for_in_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 287
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 288
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 289
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 290
                self.method_invoc_literal(0)
                self.state = 291
                self.match(D96Parser.DOT)
                self.state = 292
                self.funcall()
                self.state = 293
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 295
                _la = self._input.LA(1)
                if not(_la==D96Parser.SELF or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 296
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 297
                self.static_method()
                self.state = 298
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 300
                self.match(D96Parser.LP)
                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (D96Parser.VAL - 10)) | (1 << (D96Parser.VAR - 10)) | (1 << (D96Parser.BREAK - 10)) | (1 << (D96Parser.FOREACH - 10)) | (1 << (D96Parser.CONTINUE - 10)) | (1 << (D96Parser.IF - 10)) | (1 << (D96Parser.NEW - 10)) | (1 << (D96Parser.RETURN - 10)) | (1 << (D96Parser.SELF - 10)) | (1 << (D96Parser.LP - 10)) | (1 << (D96Parser.ID - 10)))) != 0):
                    self.state = 301
                    self.block_stmt()


                self.state = 304
                self.match(D96Parser.RP)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = D96Parser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 308
                self.var_no_value()
                pass

            elif la_ == 2:
                self.state = 309
                self.var_with_value()
                pass

            elif la_ == 3:
                self.state = 310
                self.var_array_no_value()
                pass

            elif la_ == 4:
                self.state = 311
                self.var_array_with_value()
                pass


            self.state = 314
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_no_valueContext(ParserRuleContext):
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
            return D96Parser.RULE_var_no_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_no_value" ):
                return visitor.visitVar_no_value(self)
            else:
                return visitor.visitChildren(self)




    def var_no_value(self):

        localctx = D96Parser.Var_no_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_var_no_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(D96Parser.ID)
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 317
                self.match(D96Parser.COMMA)
                self.state = 318
                self.match(D96Parser.ID)
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 324
            self.match(D96Parser.COLON)
            self.state = 325
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_with_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def var_pair(self):
            return self.getTypedRuleContext(D96Parser.Var_pairContext,0)


        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_with_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_with_value" ):
                return visitor.visitVar_with_value(self)
            else:
                return visitor.visitChildren(self)




    def var_with_value(self):

        localctx = D96Parser.Var_with_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_with_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(D96Parser.ID)
            self.state = 328
            self.var_pair()
            self.state = 329
            self.all_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_pairContext(ParserRuleContext):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_pair" ):
                return visitor.visitVar_pair(self)
            else:
                return visitor.visitChildren(self)




    def var_pair(self):

        localctx = D96Parser.Var_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_var_pair)
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.match(D96Parser.COMMA)
                self.state = 332
                self.match(D96Parser.ID)
                self.state = 333
                self.var_pair()
                self.state = 334
                self.all_expr()
                self.state = 335
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
                self.match(D96Parser.COLON)
                self.state = 338
                self.data_type()
                self.state = 339
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

        def var_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Var_array_decl_tailContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_var_array_no_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_array_no_value" ):
                return visitor.visitVar_array_no_value(self)
            else:
                return visitor.visitChildren(self)




    def var_array_no_value(self):

        localctx = D96Parser.Var_array_no_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_var_array_no_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(D96Parser.ID)
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 344
                self.match(D96Parser.COMMA)
                self.state = 345
                self.match(D96Parser.ID)
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 351
            self.match(D96Parser.COLON)
            self.state = 352
            self.var_array_decl_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_array_with_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def var_array_pair(self):
            return self.getTypedRuleContext(D96Parser.Var_array_pairContext,0)


        def literal_array(self):
            return self.getTypedRuleContext(D96Parser.Literal_arrayContext,0)


        def object_create(self):
            return self.getTypedRuleContext(D96Parser.Object_createContext,0)


        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_array_with_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_array_with_value" ):
                return visitor.visitVar_array_with_value(self)
            else:
                return visitor.visitChildren(self)




    def var_array_with_value(self):

        localctx = D96Parser.Var_array_with_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_var_array_with_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(D96Parser.ID)
            self.state = 355
            self.var_array_pair()
            self.state = 361
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.state = 356
                self.literal_array()
                pass
            elif token in [D96Parser.NEW]:
                self.state = 357
                self.object_create()
                self.state = 359
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (D96Parser.LITERAL_BOOLEAN - 1)) | (1 << (D96Parser.LITERAL_INT - 1)) | (1 << (D96Parser.LITERAL_FLOAT - 1)) | (1 << (D96Parser.LITERAL_STRING - 1)) | (1 << (D96Parser.NULL - 1)) | (1 << (D96Parser.NEW - 1)) | (1 << (D96Parser.ARRAY - 1)) | (1 << (D96Parser.SELF - 1)) | (1 << (D96Parser.LB - 1)) | (1 << (D96Parser.SUBTRACT - 1)) | (1 << (D96Parser.NOT - 1)) | (1 << (D96Parser.ID - 1)))) != 0):
                    self.state = 358
                    self.all_expr()


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


    class Var_array_pairContext(ParserRuleContext):
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

        def var_array_pair(self):
            return self.getTypedRuleContext(D96Parser.Var_array_pairContext,0)


        def literal_array(self):
            return self.getTypedRuleContext(D96Parser.Literal_arrayContext,0)


        def object_create(self):
            return self.getTypedRuleContext(D96Parser.Object_createContext,0)


        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def var_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Var_array_decl_tailContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_array_pair

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_array_pair" ):
                return visitor.visitVar_array_pair(self)
            else:
                return visitor.visitChildren(self)




    def var_array_pair(self):

        localctx = D96Parser.Var_array_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_var_array_pair)
        self._la = 0 # Token type
        try:
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.match(D96Parser.COMMA)
                self.state = 364
                self.match(D96Parser.ID)
                self.state = 365
                self.var_array_pair()
                self.state = 371
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.ARRAY]:
                    self.state = 366
                    self.literal_array()
                    pass
                elif token in [D96Parser.NEW]:
                    self.state = 367
                    self.object_create()
                    self.state = 369
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (D96Parser.LITERAL_BOOLEAN - 1)) | (1 << (D96Parser.LITERAL_INT - 1)) | (1 << (D96Parser.LITERAL_FLOAT - 1)) | (1 << (D96Parser.LITERAL_STRING - 1)) | (1 << (D96Parser.NULL - 1)) | (1 << (D96Parser.NEW - 1)) | (1 << (D96Parser.ARRAY - 1)) | (1 << (D96Parser.SELF - 1)) | (1 << (D96Parser.LB - 1)) | (1 << (D96Parser.SUBTRACT - 1)) | (1 << (D96Parser.NOT - 1)) | (1 << (D96Parser.ID - 1)))) != 0):
                        self.state = 368
                        self.all_expr()


                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 373
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.match(D96Parser.COLON)
                self.state = 376
                self.var_array_decl_tail()
                self.state = 377
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
        __slots__ = 'parser'

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


        def var_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Var_array_decl_tailContext,0)


        def LITERAL_INT(self):
            return self.getToken(D96Parser.LITERAL_INT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_array_decl_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_array_decl_tail" ):
                return visitor.visitVar_array_decl_tail(self)
            else:
                return visitor.visitChildren(self)




    def var_array_decl_tail(self):

        localctx = D96Parser.Var_array_decl_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_var_array_decl_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(D96Parser.ARRAY)
            self.state = 382
            self.match(D96Parser.LS)
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.SELF, D96Parser.ID]:
                self.state = 383
                self.data_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 384
                self.var_array_decl_tail()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 387
            self.match(D96Parser.COMMA)

            self.state = 388
            self.match(D96Parser.LITERAL_INT)
            self.state = 389
            self.match(D96Parser.RS)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.assign_lhs()
            self.state = 392
            self.match(D96Parser.ASSIGN)
            self.state = 393
            self.all_expr()
            self.state = 394
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

        def scalar_variable(self):
            return self.getTypedRuleContext(D96Parser.Scalar_variableContext,0)


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
            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.scalar_variable(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.scalar_variable(0)
                self.state = 398
                self.element_expr()
                pass


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
        self.enterRule(localctx, 54, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.params()
            self.state = 407
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 403
                self.match(D96Parser.SEMI)
                self.state = 404
                self.params()
                self.state = 409
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


        def var_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Var_array_decl_tailContext,0)


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
        self.enterRule(localctx, 56, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(D96Parser.ID)

            self.state = 415
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 411
                self.match(D96Parser.COMMA)
                self.state = 412
                self.match(D96Parser.ID)
                self.state = 417
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 418
            self.match(D96Parser.COLON)
            self.state = 421
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.SELF, D96Parser.ID]:
                self.state = 419
                self.data_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 420
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
        self.enterRule(localctx, 58, self.RULE_data_type)
        try:
            self.state = 428
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 425
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 426
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.SELF, D96Parser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 427
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


        def else_body(self):
            return self.getTypedRuleContext(D96Parser.Else_bodyContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(D96Parser.IF)
            self.state = 431
            self.match(D96Parser.LB)
            self.state = 432
            self.all_expr()
            self.state = 433
            self.match(D96Parser.RB)
            self.state = 434
            self.match(D96Parser.LP)
            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (D96Parser.VAL - 10)) | (1 << (D96Parser.VAR - 10)) | (1 << (D96Parser.BREAK - 10)) | (1 << (D96Parser.FOREACH - 10)) | (1 << (D96Parser.CONTINUE - 10)) | (1 << (D96Parser.IF - 10)) | (1 << (D96Parser.NEW - 10)) | (1 << (D96Parser.RETURN - 10)) | (1 << (D96Parser.SELF - 10)) | (1 << (D96Parser.LP - 10)) | (1 << (D96Parser.ID - 10)))) != 0):
                self.state = 435
                self.block_stmt()


            self.state = 438
            self.match(D96Parser.RP)
            self.state = 440
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSEIF:
                self.state = 439
                self.else_if_body()


            self.state = 443
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 442
                self.else_body()


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
        self.enterRule(localctx, 62, self.RULE_else_if_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(D96Parser.ELSEIF)
            self.state = 446
            self.match(D96Parser.LB)
            self.state = 447
            self.all_expr()
            self.state = 448
            self.match(D96Parser.RB)
            self.state = 449
            self.match(D96Parser.LP)
            self.state = 451
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (D96Parser.VAL - 10)) | (1 << (D96Parser.VAR - 10)) | (1 << (D96Parser.BREAK - 10)) | (1 << (D96Parser.FOREACH - 10)) | (1 << (D96Parser.CONTINUE - 10)) | (1 << (D96Parser.IF - 10)) | (1 << (D96Parser.NEW - 10)) | (1 << (D96Parser.RETURN - 10)) | (1 << (D96Parser.SELF - 10)) | (1 << (D96Parser.LP - 10)) | (1 << (D96Parser.ID - 10)))) != 0):
                self.state = 450
                self.block_stmt()


            self.state = 453
            self.match(D96Parser.RP)
            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSEIF:
                self.state = 454
                self.else_if_body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_body" ):
                return visitor.visitElse_body(self)
            else:
                return visitor.visitChildren(self)




    def else_body(self):

        localctx = D96Parser.Else_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_else_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(D96Parser.ELSE)
            self.state = 458
            self.match(D96Parser.LP)
            self.state = 460
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (D96Parser.VAL - 10)) | (1 << (D96Parser.VAR - 10)) | (1 << (D96Parser.BREAK - 10)) | (1 << (D96Parser.FOREACH - 10)) | (1 << (D96Parser.CONTINUE - 10)) | (1 << (D96Parser.IF - 10)) | (1 << (D96Parser.NEW - 10)) | (1 << (D96Parser.RETURN - 10)) | (1 << (D96Parser.SELF - 10)) | (1 << (D96Parser.LP - 10)) | (1 << (D96Parser.ID - 10)))) != 0):
                self.state = 459
                self.block_stmt()


            self.state = 462
            self.match(D96Parser.RP)
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

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_for_in_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_in_stmt" ):
                return visitor.visitFor_in_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_in_stmt(self):

        localctx = D96Parser.For_in_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_for_in_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.match(D96Parser.FOREACH)
            self.state = 465
            self.match(D96Parser.LB)
            self.state = 466
            self.for_in_body()
            self.state = 467
            self.match(D96Parser.RB)
            self.state = 468
            self.match(D96Parser.LP)
            self.state = 470
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (D96Parser.VAL - 10)) | (1 << (D96Parser.VAR - 10)) | (1 << (D96Parser.BREAK - 10)) | (1 << (D96Parser.FOREACH - 10)) | (1 << (D96Parser.CONTINUE - 10)) | (1 << (D96Parser.IF - 10)) | (1 << (D96Parser.NEW - 10)) | (1 << (D96Parser.RETURN - 10)) | (1 << (D96Parser.SELF - 10)) | (1 << (D96Parser.LP - 10)) | (1 << (D96Parser.ID - 10)))) != 0):
                self.state = 469
                self.block_stmt()


            self.state = 472
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_in_body" ):
                return visitor.visitFor_in_body(self)
            else:
                return visitor.visitChildren(self)




    def for_in_body(self):

        localctx = D96Parser.For_in_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_for_in_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.scalar_variable(0)
            self.state = 475
            self.match(D96Parser.IN)
            self.state = 476
            self.for_in_expr()
            self.state = 477
            self.match(D96Parser.DOTDOT)
            self.state = 478
            self.for_in_expr()
            self.state = 481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 479
                self.match(D96Parser.BY)
                self.state = 480
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

        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_for_in_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_in_expr" ):
                return visitor.visitFor_in_expr(self)
            else:
                return visitor.visitChildren(self)




    def for_in_expr(self):

        localctx = D96Parser.For_in_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_for_in_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.all_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_variableContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_variable" ):
                return visitor.visitScalar_variable(self)
            else:
                return visitor.visitChildren(self)



    def scalar_variable(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Scalar_variableContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_scalar_variable, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 486
                self.static_member_access()
                pass

            elif la_ == 2:
                self.state = 487
                self.match(D96Parser.SELF)
                pass

            elif la_ == 3:
                self.state = 488
                self.match(D96Parser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 499
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Scalar_variableContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_scalar_variable)
                    self.state = 491
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 492
                    self.match(D96Parser.DOT)
                    self.state = 495
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                    if la_ == 1:
                        self.state = 493
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 494
                        self.funcall()
                        pass

             
                self.state = 501
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 74, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self.match(D96Parser.BREAK)
            self.state = 503
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
        self.enterRule(localctx, 76, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(D96Parser.CONTINUE)
            self.state = 506
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
        self.enterRule(localctx, 78, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.match(D96Parser.RETURN)
            self.state = 512
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (D96Parser.LITERAL_BOOLEAN - 1)) | (1 << (D96Parser.LITERAL_INT - 1)) | (1 << (D96Parser.LITERAL_FLOAT - 1)) | (1 << (D96Parser.LITERAL_STRING - 1)) | (1 << (D96Parser.NULL - 1)) | (1 << (D96Parser.NEW - 1)) | (1 << (D96Parser.ARRAY - 1)) | (1 << (D96Parser.SELF - 1)) | (1 << (D96Parser.LB - 1)) | (1 << (D96Parser.SUBTRACT - 1)) | (1 << (D96Parser.NOT - 1)) | (1 << (D96Parser.ID - 1)))) != 0):
                self.state = 509
                self.all_expr()
                self.state = 514
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 515
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
        self.enterRule(localctx, 80, self.RULE_class_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
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


    class Method_invoc_literalContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invoc_literal" ):
                return visitor.visitMethod_invoc_literal(self)
            else:
                return visitor.visitChildren(self)



    def method_invoc_literal(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Method_invoc_literalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_method_invoc_literal, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 520
                self.match(D96Parser.NEW)
                self.state = 521
                self.funcall()
                pass

            elif la_ == 2:
                self.state = 522
                self.static_member_access()
                pass

            elif la_ == 3:
                self.state = 523
                self.match(D96Parser.SELF)
                pass

            elif la_ == 4:
                self.state = 524
                self.match(D96Parser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 537
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 535
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Method_invoc_literalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_method_invoc_literal)
                        self.state = 527
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 528
                        self.match(D96Parser.DOT)
                        self.state = 531
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                        if la_ == 1:
                            self.state = 529
                            self.match(D96Parser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 530
                            self.funcall()
                            pass


                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Method_invoc_literalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_method_invoc_literal)
                        self.state = 533
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 534
                        self.element_expr()
                        pass

             
                self.state = 539
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Method_invocContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_invoc_literal(self):
            return self.getTypedRuleContext(D96Parser.Method_invoc_literalContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_invoc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invoc" ):
                return visitor.visitMethod_invoc(self)
            else:
                return visitor.visitChildren(self)




    def method_invoc(self):

        localctx = D96Parser.Method_invocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_method_invoc)
        try:
            self.state = 542
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW, D96Parser.SELF, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 540
                self.method_invoc_literal(0)
                pass
            elif token in [D96Parser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 541
                self.match(D96Parser.SEMI)
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
        self.enterRule(localctx, 86, self.RULE_expr_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 544
                    self.all_expr()
                    self.state = 545
                    self.match(D96Parser.COMMA) 
                self.state = 551
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

            self.state = 552
            self.all_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):
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

        def list_of_expr(self):
            return self.getTypedRuleContext(D96Parser.List_of_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = D96Parser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self.match(D96Parser.ID)
            self.state = 555
            self.match(D96Parser.LB)
            self.state = 557
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (D96Parser.LITERAL_BOOLEAN - 1)) | (1 << (D96Parser.LITERAL_INT - 1)) | (1 << (D96Parser.LITERAL_FLOAT - 1)) | (1 << (D96Parser.LITERAL_STRING - 1)) | (1 << (D96Parser.NULL - 1)) | (1 << (D96Parser.NEW - 1)) | (1 << (D96Parser.ARRAY - 1)) | (1 << (D96Parser.SELF - 1)) | (1 << (D96Parser.LB - 1)) | (1 << (D96Parser.SUBTRACT - 1)) | (1 << (D96Parser.NOT - 1)) | (1 << (D96Parser.ID - 1)))) != 0):
                self.state = 556
                self.list_of_expr()


            self.state = 559
            self.match(D96Parser.RB)
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
        self.enterRule(localctx, 90, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 561
                self.stmt()
                self.state = 564 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (D96Parser.VAL - 10)) | (1 << (D96Parser.VAR - 10)) | (1 << (D96Parser.BREAK - 10)) | (1 << (D96Parser.FOREACH - 10)) | (1 << (D96Parser.CONTINUE - 10)) | (1 << (D96Parser.IF - 10)) | (1 << (D96Parser.NEW - 10)) | (1 << (D96Parser.RETURN - 10)) | (1 << (D96Parser.SELF - 10)) | (1 << (D96Parser.LP - 10)) | (1 << (D96Parser.ID - 10)))) != 0)):
                    break

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
        self.enterRule(localctx, 92, self.RULE_all_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 566
                self.op()
                pass

            elif la_ == 2:
                self.state = 567
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
        self.enterRule(localctx, 94, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.state = 575
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 570
                self.op1()
                self.state = 571
                _la = self._input.LA(1)
                if not(_la==D96Parser.EQUAL_STRING or _la==D96Parser.STRING_CONCAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 572
                self.op1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 574
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
        self.enterRule(localctx, 96, self.RULE_op1)
        self._la = 0 # Token type
        try:
            self.state = 582
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 577
                self.op2(0)
                self.state = 578
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.LESS_THAN) | (1 << D96Parser.LEQ) | (1 << D96Parser.GREATER_THAN) | (1 << D96Parser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 579
                self.op2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 581
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
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_op2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.op3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 592
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op2)
                    self.state = 587
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 588
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 589
                    self.op3(0) 
                self.state = 594
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

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
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_op3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
            self.op4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 603
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op3)
                    self.state = 598
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 599
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUBTRACT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 600
                    self.op4(0) 
                self.state = 605
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

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
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_op4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            self.op5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 614
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,58,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op4)
                    self.state = 609
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 610
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLY) | (1 << D96Parser.DIVIDE) | (1 << D96Parser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 611
                    self.op5() 
                self.state = 616
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,58,self._ctx)

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
        self.enterRule(localctx, 104, self.RULE_op5)
        try:
            self.state = 620
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 617
                self.match(D96Parser.NOT)
                self.state = 618
                self.op5()
                pass
            elif token in [D96Parser.LITERAL_BOOLEAN, D96Parser.LITERAL_INT, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.SUBTRACT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 619
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
        self.enterRule(localctx, 106, self.RULE_op6)
        try:
            self.state = 625
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUBTRACT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 622
                self.match(D96Parser.SUBTRACT)
                self.state = 623
                self.op6()
                pass
            elif token in [D96Parser.LITERAL_BOOLEAN, D96Parser.LITERAL_INT, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 624
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op8(self):
            return self.getTypedRuleContext(D96Parser.Op8Context,0)


        def op7(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Op7Context)
            else:
                return self.getTypedRuleContext(D96Parser.Op7Context,i)


        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_op7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp7" ):
                return visitor.visitOp7(self)
            else:
                return visitor.visitChildren(self)



    def op7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Op7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_op7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 628
            self.op8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 637
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,61,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op7)
                    self.state = 630
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 631
                    self.match(D96Parser.LS)
                    self.state = 632
                    self.op7(0)
                    self.state = 633
                    self.match(D96Parser.RS) 
                self.state = 639
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,61,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


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
        _startState = 110
        self.enterRecursionRule(localctx, 110, self.RULE_op8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 641
            self.op9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 651
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,63,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op8)
                    self.state = 643
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 644
                    self.match(D96Parser.DOT)
                    self.state = 647
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
                    if la_ == 1:
                        self.state = 645
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 646
                        self.funcall()
                        pass

             
                self.state = 653
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,63,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp9" ):
                return visitor.visitOp9(self)
            else:
                return visitor.visitChildren(self)




    def op9(self):

        localctx = D96Parser.Op9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_op9)
        self._la = 0 # Token type
        try:
            self.state = 661
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 654
                _la = self._input.LA(1)
                if not(_la==D96Parser.SELF or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 655
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 658
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                if la_ == 1:
                    self.state = 656
                    self.static_method()
                    pass

                elif la_ == 2:
                    self.state = 657
                    self.match(D96Parser.DOLLAR_ID)
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 660
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp10" ):
                return visitor.visitOp10(self)
            else:
                return visitor.visitChildren(self)




    def op10(self):

        localctx = D96Parser.Op10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_op10)
        self._la = 0 # Token type
        try:
            self.state = 672
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 663
                self.match(D96Parser.NEW)
                self.state = 664
                self.operands()
                self.state = 665
                self.match(D96Parser.LB)
                self.state = 667
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (D96Parser.LITERAL_BOOLEAN - 1)) | (1 << (D96Parser.LITERAL_INT - 1)) | (1 << (D96Parser.LITERAL_FLOAT - 1)) | (1 << (D96Parser.LITERAL_STRING - 1)) | (1 << (D96Parser.NULL - 1)) | (1 << (D96Parser.NEW - 1)) | (1 << (D96Parser.ARRAY - 1)) | (1 << (D96Parser.SELF - 1)) | (1 << (D96Parser.LB - 1)) | (1 << (D96Parser.SUBTRACT - 1)) | (1 << (D96Parser.NOT - 1)) | (1 << (D96Parser.ID - 1)))) != 0):
                    self.state = 666
                    self.list_of_expr()


                self.state = 669
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.LITERAL_BOOLEAN, D96Parser.LITERAL_INT, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 671
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_operands)
        try:
            self.state = 683
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LITERAL_BOOLEAN, D96Parser.LITERAL_INT, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 674
                self.literal()
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 675
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 676
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 677
                self.match(D96Parser.LB)
                self.state = 678
                self.op()
                self.state = 679
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 681
                self.match(D96Parser.NULL)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 682
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
        self.enterRule(localctx, 118, self.RULE_element_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 685
            self.index_ops(0)
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



    def index_ops(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Index_opsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 120
        self.enterRecursionRule(localctx, 120, self.RULE_index_ops, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 688
            self.match(D96Parser.LS)
            self.state = 689
            self.all_expr()
            self.state = 690
            self.match(D96Parser.RS)
            self._ctx.stop = self._input.LT(-1)
            self.state = 699
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,69,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_opsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_ops)
                    self.state = 692
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 693
                    self.match(D96Parser.LS)
                    self.state = 694
                    self.all_expr()
                    self.state = 695
                    self.match(D96Parser.RS) 
                self.state = 701
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,69,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Static_member_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_member_access" ):
                return visitor.visitStatic_member_access(self)
            else:
                return visitor.visitChildren(self)




    def static_member_access(self):

        localctx = D96Parser.Static_member_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_static_member_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 706
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.state = 702
                self.match(D96Parser.NEW)
                self.state = 703
                self.funcall()
                pass
            elif token in [D96Parser.SELF]:
                self.state = 704
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.ID]:
                self.state = 705
                self.match(D96Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 708
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 711
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                self.state = 709
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 2:
                self.state = 710
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

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_attr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_attr" ):
                return visitor.visitInstance_attr(self)
            else:
                return visitor.visitChildren(self)




    def instance_attr(self):

        localctx = D96Parser.Instance_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_instance_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 713
            self.match(D96Parser.DOT)
            self.state = 714
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

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_attr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_attr" ):
                return visitor.visitStatic_attr(self)
            else:
                return visitor.visitChildren(self)




    def static_attr(self):

        localctx = D96Parser.Static_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_static_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 716
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 717
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
            return D96Parser.RULE_instance_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method" ):
                return visitor.visitInstance_method(self)
            else:
                return visitor.visitChildren(self)




    def instance_method(self):

        localctx = D96Parser.Instance_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_instance_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 719
            self.match(D96Parser.DOT)
            self.state = 720
            self.match(D96Parser.ID)
            self.state = 721
            self.match(D96Parser.LB)
            self.state = 723
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (D96Parser.LITERAL_BOOLEAN - 1)) | (1 << (D96Parser.LITERAL_INT - 1)) | (1 << (D96Parser.LITERAL_FLOAT - 1)) | (1 << (D96Parser.LITERAL_STRING - 1)) | (1 << (D96Parser.NULL - 1)) | (1 << (D96Parser.NEW - 1)) | (1 << (D96Parser.ARRAY - 1)) | (1 << (D96Parser.SELF - 1)) | (1 << (D96Parser.LB - 1)) | (1 << (D96Parser.SUBTRACT - 1)) | (1 << (D96Parser.NOT - 1)) | (1 << (D96Parser.ID - 1)))) != 0):
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
        self.enterRule(localctx, 130, self.RULE_static_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 727
            self.match(D96Parser.DOLLAR_ID)
            self.state = 728
            self.match(D96Parser.LB)
            self.state = 730
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (D96Parser.LITERAL_BOOLEAN - 1)) | (1 << (D96Parser.LITERAL_INT - 1)) | (1 << (D96Parser.LITERAL_FLOAT - 1)) | (1 << (D96Parser.LITERAL_STRING - 1)) | (1 << (D96Parser.NULL - 1)) | (1 << (D96Parser.NEW - 1)) | (1 << (D96Parser.ARRAY - 1)) | (1 << (D96Parser.SELF - 1)) | (1 << (D96Parser.LB - 1)) | (1 << (D96Parser.SUBTRACT - 1)) | (1 << (D96Parser.NOT - 1)) | (1 << (D96Parser.ID - 1)))) != 0):
                self.state = 729
                self.list_of_expr()


            self.state = 732
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
        self.enterRule(localctx, 132, self.RULE_object_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 734
            self.match(D96Parser.NEW)
            self.state = 735
            self.match(D96Parser.ID)
            self.state = 736
            self.match(D96Parser.LB)
            self.state = 738
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (D96Parser.LITERAL_BOOLEAN - 1)) | (1 << (D96Parser.LITERAL_INT - 1)) | (1 << (D96Parser.LITERAL_FLOAT - 1)) | (1 << (D96Parser.LITERAL_STRING - 1)) | (1 << (D96Parser.NULL - 1)) | (1 << (D96Parser.NEW - 1)) | (1 << (D96Parser.ARRAY - 1)) | (1 << (D96Parser.SELF - 1)) | (1 << (D96Parser.LB - 1)) | (1 << (D96Parser.SUBTRACT - 1)) | (1 << (D96Parser.NOT - 1)) | (1 << (D96Parser.ID - 1)))) != 0):
                self.state = 737
                self.list_of_expr()


            self.state = 740
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
        self.enterRule(localctx, 134, self.RULE_list_of_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 742
            self.op()
            self.state = 747
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 743
                self.match(D96Parser.COMMA)
                self.state = 744
                self.op()
                self.state = 749
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

        def LITERAL_BOOLEAN(self):
            return self.getToken(D96Parser.LITERAL_BOOLEAN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 750
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING))) != 0)):
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_idx_array(self):
            return self.getTypedRuleContext(D96Parser.Literal_idx_arrayContext,0)


        def literal_mtd_array(self):
            return self.getTypedRuleContext(D96Parser.Literal_mtd_arrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_array" ):
                return visitor.visitLiteral_array(self)
            else:
                return visitor.visitChildren(self)




    def literal_array(self):

        localctx = D96Parser.Literal_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_literal_array)
        try:
            self.state = 754
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 752
                self.literal_idx_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 753
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def array_element(self):
            return self.getTypedRuleContext(D96Parser.Array_elementContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_literal_idx_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_idx_array" ):
                return visitor.visitLiteral_idx_array(self)
            else:
                return visitor.visitChildren(self)




    def literal_idx_array(self):

        localctx = D96Parser.Literal_idx_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_literal_idx_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 756
            self.match(D96Parser.ARRAY)
            self.state = 757
            self.match(D96Parser.LB)
            self.state = 758
            self.array_element()
            self.state = 759
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
        self.enterRule(localctx, 142, self.RULE_literal_mtd_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 761
            self.match(D96Parser.ARRAY)
            self.state = 762
            self.match(D96Parser.LB)
            self.state = 769
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ARRAY:
                self.state = 763
                self.literal_idx_array()
                self.state = 765
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.COMMA:
                    self.state = 764
                    self.match(D96Parser.COMMA)


                self.state = 771
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 772
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element" ):
                return visitor.visitArray_element(self)
            else:
                return visitor.visitChildren(self)




    def array_element(self):

        localctx = D96Parser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_array_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 774
            self.all_expr()
            self.state = 779
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 775
                self.match(D96Parser.COMMA)
                self.state = 776
                self.all_expr()
                self.state = 781
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
        self._predicates[36] = self.scalar_variable_sempred
        self._predicates[41] = self.method_invoc_literal_sempred
        self._predicates[49] = self.op2_sempred
        self._predicates[50] = self.op3_sempred
        self._predicates[51] = self.op4_sempred
        self._predicates[54] = self.op7_sempred
        self._predicates[55] = self.op8_sempred
        self._predicates[60] = self.index_ops_sempred
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
         




