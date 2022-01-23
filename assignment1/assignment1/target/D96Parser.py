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
        buf.write("\u0257\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\6\2\u0082\n\2\r\2")
        buf.write("\16\2\u0083\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u008c\n\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\7\4\u0094\n\4\f\4\16\4\u0097\13\4")
        buf.write("\3\5\3\5\3\6\3\6\3\6\5\6\u009e\n\6\3\7\3\7\3\7\5\7\u00a3")
        buf.write("\n\7\3\7\3\7\3\7\5\7\u00a8\n\7\3\7\3\7\3\b\3\b\3\b\5\b")
        buf.write("\u00af\n\b\3\b\3\b\3\b\5\b\u00b4\n\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\5\t\u00bd\n\t\3\t\3\t\3\n\3\n\3\n\7\n\u00c4")
        buf.write("\n\n\f\n\16\n\u00c7\13\n\3\13\3\13\3\13\7\13\u00cc\n\13")
        buf.write("\f\13\16\13\u00cf\13\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\5\f\u00d9\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r")
        buf.write("\u00e3\n\r\3\16\3\16\3\16\5\16\u00e8\n\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\5\17\u00ef\n\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\5\20\u00f7\n\20\3\20\3\20\3\20\5\20\u00fc\n\20\5")
        buf.write("\20\u00fe\n\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\5\22\u010b\n\22\3\23\3\23\3\23\3\23\5")
        buf.write("\23\u0111\n\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\7\25\u011f\n\25\f\25\16\25\u0122")
        buf.write("\13\25\3\25\3\25\3\26\3\26\3\26\5\26\u0129\n\26\3\26\3")
        buf.write("\26\7\26\u012d\n\26\f\26\16\26\u0130\13\26\3\26\3\26\5")
        buf.write("\26\u0134\n\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\5\27\u0140\n\27\3\27\3\27\5\27\u0144\n\27\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\5\30\u014c\n\30\3\30\3\30")
        buf.write("\5\30\u0150\n\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\5\32\u015e\n\32\3\32\3\32\3\33")
        buf.write("\5\33\u0163\n\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3")
        buf.write("\35\3\36\3\36\7\36\u016f\n\36\f\36\16\36\u0172\13\36\3")
        buf.write("\36\3\36\3\37\3\37\3 \3 \5 \u017a\n \3 \3 \3!\3!\3!\7")
        buf.write("!\u0181\n!\f!\16!\u0184\13!\3!\3!\3\"\6\"\u0189\n\"\r")
        buf.write("\"\16\"\u018a\3#\3#\3#\3#\5#\u0191\n#\7#\u0193\n#\f#\16")
        buf.write("#\u0196\13#\3#\3#\3$\3$\3$\3$\5$\u019e\n$\7$\u01a0\n$")
        buf.write("\f$\16$\u01a3\13$\3$\3$\3%\3%\5%\u01a9\n%\6%\u01ab\n%")
        buf.write("\r%\16%\u01ac\3&\3&\3&\5&\u01b2\n&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\5\'\u01b9\n\'\3(\3(\3(\3(\3(\5(\u01c0\n(\3)\3)\3)\3)")
        buf.write("\3)\3)\7)\u01c8\n)\f)\16)\u01cb\13)\3*\3*\3*\3*\3*\3*")
        buf.write("\7*\u01d3\n*\f*\16*\u01d6\13*\3+\3+\3+\3+\3+\3+\7+\u01de")
        buf.write("\n+\f+\16+\u01e1\13+\3,\3,\3,\5,\u01e6\n,\3-\3-\3-\5-")
        buf.write("\u01eb\n-\3.\3.\3.\3.\5.\u01f1\n.\3/\3/\3/\3/\3/\3/\7")
        buf.write("/\u01f9\n/\f/\16/\u01fc\13/\3\60\3\60\3\60\5\60\u0201")
        buf.write("\n\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u020b")
        buf.write("\n\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\3\67\5\67\u021c\n\67\38\38\38\38")
        buf.write("\58\u0222\n8\39\39\39\39\3:\3:\3:\3:\3;\3;\3;\5;\u022f")
        buf.write("\n;\3;\3;\3<\3<\3<\5<\u0236\n<\3<\3<\3=\3=\5=\u023c\n")
        buf.write("=\3=\3=\3=\5=\u0241\n=\3=\3=\3>\3>\3>\3>\5>\u0249\n>\3")
        buf.write(">\3>\3?\3?\5?\u024f\n?\6?\u0251\n?\r?\16?\u0252\3@\3@")
        buf.write("\3@\2\6PRT\\A\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 ")
        buf.write("\"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtv")
        buf.write("xz|~\2\r\3\2\13\f\4\2##AA\3\2<=\4\2\65\65\67;\3\2\63\64")
        buf.write("\3\2-.\3\2/\61\3\2>?\3\2-\61\4\2\62\64<<\4\2\3\3\b\t\2")
        buf.write("\u0265\2\u0081\3\2\2\2\4\u0087\3\2\2\2\6\u0095\3\2\2\2")
        buf.write("\b\u0098\3\2\2\2\n\u009d\3\2\2\2\f\u009f\3\2\2\2\16\u00ab")
        buf.write("\3\2\2\2\20\u00b7\3\2\2\2\22\u00c0\3\2\2\2\24\u00c8\3")
        buf.write("\2\2\2\26\u00d8\3\2\2\2\30\u00e2\3\2\2\2\32\u00e4\3\2")
        buf.write("\2\2\34\u00eb\3\2\2\2\36\u00fd\3\2\2\2 \u00ff\3\2\2\2")
        buf.write("\"\u010a\3\2\2\2$\u010c\3\2\2\2&\u0116\3\2\2\2(\u0120")
        buf.write("\3\2\2\2*\u0133\3\2\2\2,\u0139\3\2\2\2.\u0145\3\2\2\2")
        buf.write("\60\u0151\3\2\2\2\62\u0155\3\2\2\2\64\u0162\3\2\2\2\66")
        buf.write("\u0166\3\2\2\28\u0169\3\2\2\2:\u016c\3\2\2\2<\u0175\3")
        buf.write("\2\2\2>\u0179\3\2\2\2@\u0182\3\2\2\2B\u0188\3\2\2\2D\u018c")
        buf.write("\3\2\2\2F\u0199\3\2\2\2H\u01aa\3\2\2\2J\u01b1\3\2\2\2")
        buf.write("L\u01b8\3\2\2\2N\u01bf\3\2\2\2P\u01c1\3\2\2\2R\u01cc\3")
        buf.write("\2\2\2T\u01d7\3\2\2\2V\u01e5\3\2\2\2X\u01ea\3\2\2\2Z\u01f0")
        buf.write("\3\2\2\2\\\u01f2\3\2\2\2^\u0200\3\2\2\2`\u020a\3\2\2\2")
        buf.write("b\u020c\3\2\2\2d\u020e\3\2\2\2f\u0210\3\2\2\2h\u0212\3")
        buf.write("\2\2\2j\u0214\3\2\2\2l\u0217\3\2\2\2n\u0221\3\2\2\2p\u0223")
        buf.write("\3\2\2\2r\u0227\3\2\2\2t\u022e\3\2\2\2v\u0232\3\2\2\2")
        buf.write("x\u023b\3\2\2\2z\u0244\3\2\2\2|\u0250\3\2\2\2~\u0254\3")
        buf.write("\2\2\2\u0080\u0082\5\4\3\2\u0081\u0080\3\2\2\2\u0082\u0083")
        buf.write("\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\u0086\7\2\2\3\u0086\3\3\2\2\2\u0087")
        buf.write("\u0088\7\26\2\2\u0088\u008b\5<\37\2\u0089\u008a\7@\2\2")
        buf.write("\u008a\u008c\5<\37\2\u008b\u0089\3\2\2\2\u008b\u008c\3")
        buf.write("\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e\7(\2\2\u008e\u008f")
        buf.write("\5\6\4\2\u008f\u0090\7)\2\2\u0090\5\3\2\2\2\u0091\u0094")
        buf.write("\5\b\5\2\u0092\u0094\5\n\6\2\u0093\u0091\3\2\2\2\u0093")
        buf.write("\u0092\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\7\3\2\2\2\u0097\u0095\3\2\2")
        buf.write("\2\u0098\u0099\5\32\16\2\u0099\t\3\2\2\2\u009a\u009e\5")
        buf.write("\f\7\2\u009b\u009e\5\16\b\2\u009c\u009e\5\20\t\2\u009d")
        buf.write("\u009a\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009c\3\2\2\2")
        buf.write("\u009e\13\3\2\2\2\u009f\u00a0\7A\2\2\u00a0\u00a2\7$\2")
        buf.write("\2\u00a1\u00a3\5\22\n\2\u00a2\u00a1\3\2\2\2\u00a2\u00a3")
        buf.write("\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\7%\2\2\u00a5")
        buf.write("\u00a7\7(\2\2\u00a6\u00a8\5B\"\2\u00a7\u00a6\3\2\2\2\u00a7")
        buf.write("\u00a8\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\7)\2\2")
        buf.write("\u00aa\r\3\2\2\2\u00ab\u00ac\7\22\2\2\u00ac\u00ae\7$\2")
        buf.write("\2\u00ad\u00af\5\22\n\2\u00ae\u00ad\3\2\2\2\u00ae\u00af")
        buf.write("\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1\7%\2\2\u00b1")
        buf.write("\u00b3\7(\2\2\u00b2\u00b4\5B\"\2\u00b3\u00b2\3\2\2\2\u00b3")
        buf.write("\u00b4\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\7)\2\2")
        buf.write("\u00b6\17\3\2\2\2\u00b7\u00b8\7\27\2\2\u00b8\u00b9\7$")
        buf.write("\2\2\u00b9\u00ba\7%\2\2\u00ba\u00bc\7(\2\2\u00bb\u00bd")
        buf.write("\5B\"\2\u00bc\u00bb\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write("\u00be\3\2\2\2\u00be\u00bf\7)\2\2\u00bf\21\3\2\2\2\u00c0")
        buf.write("\u00c5\5\24\13\2\u00c1\u00c2\7*\2\2\u00c2\u00c4\5\24\13")
        buf.write("\2\u00c3\u00c1\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c3")
        buf.write("\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\23\3\2\2\2\u00c7\u00c5")
        buf.write("\3\2\2\2\u00c8\u00cd\7A\2\2\u00c9\u00ca\7+\2\2\u00ca\u00cc")
        buf.write("\7A\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd")
        buf.write("\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00d0\3\2\2\2")
        buf.write("\u00cf\u00cd\3\2\2\2\u00d0\u00d1\7@\2\2\u00d1\u00d2\5")
        buf.write("\26\f\2\u00d2\25\3\2\2\2\u00d3\u00d9\7\20\2\2\u00d4\u00d9")
        buf.write("\7\25\2\2\u00d5\u00d9\7\32\2\2\u00d6\u00d9\7\36\2\2\u00d7")
        buf.write("\u00d9\5<\37\2\u00d8\u00d3\3\2\2\2\u00d8\u00d4\3\2\2\2")
        buf.write("\u00d8\u00d5\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d7\3")
        buf.write("\2\2\2\u00d9\27\3\2\2\2\u00da\u00e3\5\32\16\2\u00db\u00e3")
        buf.write("\5*\26\2\u00dc\u00e3\5,\27\2\u00dd\u00e3\5\60\31\2\u00de")
        buf.write("\u00e3\5\66\34\2\u00df\u00e3\58\35\2\u00e0\u00e3\5:\36")
        buf.write("\2\u00e1\u00e3\5> \2\u00e2\u00da\3\2\2\2\u00e2\u00db\3")
        buf.write("\2\2\2\u00e2\u00dc\3\2\2\2\u00e2\u00dd\3\2\2\2\u00e2\u00de")
        buf.write("\3\2\2\2\u00e2\u00df\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2")
        buf.write("\u00e1\3\2\2\2\u00e3\31\3\2\2\2\u00e4\u00e7\t\2\2\2\u00e5")
        buf.write("\u00e8\5\34\17\2\u00e6\u00e8\5 \21\2\u00e7\u00e5\3\2\2")
        buf.write("\2\u00e7\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea")
        buf.write("\7*\2\2\u00ea\33\3\2\2\2\u00eb\u00ec\7A\2\2\u00ec\u00ee")
        buf.write("\5\36\20\2\u00ed\u00ef\5J&\2\u00ee\u00ed\3\2\2\2\u00ee")
        buf.write("\u00ef\3\2\2\2\u00ef\35\3\2\2\2\u00f0\u00f1\7+\2\2\u00f1")
        buf.write("\u00f2\7A\2\2\u00f2\u00f6\5\36\20\2\u00f3\u00f4\5J&\2")
        buf.write("\u00f4\u00f5\7+\2\2\u00f5\u00f7\3\2\2\2\u00f6\u00f3\3")
        buf.write("\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00fe\3\2\2\2\u00f8\u00f9")
        buf.write("\7@\2\2\u00f9\u00fb\5\26\f\2\u00fa\u00fc\7\66\2\2\u00fb")
        buf.write("\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fe\3\2\2\2")
        buf.write("\u00fd\u00f0\3\2\2\2\u00fd\u00f8\3\2\2\2\u00fe\37\3\2")
        buf.write("\2\2\u00ff\u0100\7A\2\2\u0100\u0101\5\"\22\2\u0101\u0102")
        buf.write("\5$\23\2\u0102!\3\2\2\2\u0103\u0104\7+\2\2\u0104\u0105")
        buf.write("\7A\2\2\u0105\u0106\5\"\22\2\u0106\u0107\5$\23\2\u0107")
        buf.write("\u0108\7+\2\2\u0108\u010b\3\2\2\2\u0109\u010b\7@\2\2\u010a")
        buf.write("\u0103\3\2\2\2\u010a\u0109\3\2\2\2\u010b#\3\2\2\2\u010c")
        buf.write("\u010d\7\35\2\2\u010d\u0110\7&\2\2\u010e\u0111\5\26\f")
        buf.write("\2\u010f\u0111\7\35\2\2\u0110\u010e\3\2\2\2\u0110\u010f")
        buf.write("\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0113\7+\2\2\u0113")
        buf.write("\u0114\7\3\2\2\u0114\u0115\7\'\2\2\u0115%\3\2\2\2\u0116")
        buf.write("\u0117\7\33\2\2\u0117\u0118\7A\2\2\u0118\u0119\7$\2\2")
        buf.write("\u0119\u011a\7%\2\2\u011a\'\3\2\2\2\u011b\u011c\5J&\2")
        buf.write("\u011c\u011d\7+\2\2\u011d\u011f\3\2\2\2\u011e\u011b\3")
        buf.write("\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u0121")
        buf.write("\3\2\2\2\u0121\u0123\3\2\2\2\u0122\u0120\3\2\2\2\u0123")
        buf.write("\u0124\5J&\2\u0124)\3\2\2\2\u0125\u0126\5<\37\2\u0126")
        buf.write("\u0127\7>\2\2\u0127\u0129\3\2\2\2\u0128\u0125\3\2\2\2")
        buf.write("\u0128\u0129\3\2\2\2\u0129\u012e\3\2\2\2\u012a\u012b\7")
        buf.write("A\2\2\u012b\u012d\7>\2\2\u012c\u012a\3\2\2\2\u012d\u0130")
        buf.write("\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f")
        buf.write("\u0131\3\2\2\2\u0130\u012e\3\2\2\2\u0131\u0134\7A\2\2")
        buf.write("\u0132\u0134\5j\66\2\u0133\u0128\3\2\2\2\u0133\u0132\3")
        buf.write("\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\7\66\2\2\u0136")
        buf.write("\u0137\5J&\2\u0137\u0138\7*\2\2\u0138+\3\2\2\2\u0139\u013a")
        buf.write("\7\30\2\2\u013a\u013b\7$\2\2\u013b\u013c\5J&\2\u013c\u013d")
        buf.write("\7%\2\2\u013d\u013f\7(\2\2\u013e\u0140\5B\"\2\u013f\u013e")
        buf.write("\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0141\3\2\2\2\u0141")
        buf.write("\u0143\7)\2\2\u0142\u0144\5.\30\2\u0143\u0142\3\2\2\2")
        buf.write("\u0143\u0144\3\2\2\2\u0144-\3\2\2\2\u0145\u0146\7\34\2")
        buf.write("\2\u0146\u0147\7$\2\2\u0147\u0148\5J&\2\u0148\u0149\7")
        buf.write("%\2\2\u0149\u014b\7(\2\2\u014a\u014c\5B\"\2\u014b\u014a")
        buf.write("\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014d\3\2\2\2\u014d")
        buf.write("\u014f\7)\2\2\u014e\u0150\5.\30\2\u014f\u014e\3\2\2\2")
        buf.write("\u014f\u0150\3\2\2\2\u0150/\3\2\2\2\u0151\u0152\7\17\2")
        buf.write("\2\u0152\u0153\5\62\32\2\u0153\u0154\7*\2\2\u0154\61\3")
        buf.write("\2\2\2\u0155\u0156\7$\2\2\u0156\u0157\7A\2\2\u0157\u0158")
        buf.write("\7!\2\2\u0158\u0159\5\64\33\2\u0159\u015a\7,\2\2\u015a")
        buf.write("\u015d\5\64\33\2\u015b\u015c\7\37\2\2\u015c\u015e\5\64")
        buf.write("\33\2\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015f")
        buf.write("\3\2\2\2\u015f\u0160\7%\2\2\u0160\63\3\2\2\2\u0161\u0163")
        buf.write("\7.\2\2\u0162\u0161\3\2\2\2\u0162\u0163\3\2\2\2\u0163")
        buf.write("\u0164\3\2\2\2\u0164\u0165\7\3\2\2\u0165\65\3\2\2\2\u0166")
        buf.write("\u0167\7\16\2\2\u0167\u0168\7*\2\2\u0168\67\3\2\2\2\u0169")
        buf.write("\u016a\7\23\2\2\u016a\u016b\7*\2\2\u016b9\3\2\2\2\u016c")
        buf.write("\u0170\7\"\2\2\u016d\u016f\5J&\2\u016e\u016d\3\2\2\2\u016f")
        buf.write("\u0172\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2")
        buf.write("\u0171\u0173\3\2\2\2\u0172\u0170\3\2\2\2\u0173\u0174\7")
        buf.write("*\2\2\u0174;\3\2\2\2\u0175\u0176\t\3\2\2\u0176=\3\2\2")
        buf.write("\2\u0177\u017a\5t;\2\u0178\u017a\5x=\2\u0179\u0177\3\2")
        buf.write("\2\2\u0179\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c")
        buf.write("\7*\2\2\u017c?\3\2\2\2\u017d\u017e\5J&\2\u017e\u017f\7")
        buf.write("+\2\2\u017f\u0181\3\2\2\2\u0180\u017d\3\2\2\2\u0181\u0184")
        buf.write("\3\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183")
        buf.write("\u0185\3\2\2\2\u0184\u0182\3\2\2\2\u0185\u0186\5J&\2\u0186")
        buf.write("A\3\2\2\2\u0187\u0189\5\30\r\2\u0188\u0187\3\2\2\2\u0189")
        buf.write("\u018a\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u018b\3\2\2\2")
        buf.write("\u018bC\3\2\2\2\u018c\u018d\7\35\2\2\u018d\u0194\7$\2")
        buf.write("\2\u018e\u0190\5H%\2\u018f\u0191\7+\2\2\u0190\u018f\3")
        buf.write("\2\2\2\u0190\u0191\3\2\2\2\u0191\u0193\3\2\2\2\u0192\u018e")
        buf.write("\3\2\2\2\u0193\u0196\3\2\2\2\u0194\u0192\3\2\2\2\u0194")
        buf.write("\u0195\3\2\2\2\u0195\u0197\3\2\2\2\u0196\u0194\3\2\2\2")
        buf.write("\u0197\u0198\7%\2\2\u0198E\3\2\2\2\u0199\u019a\7\35\2")
        buf.write("\2\u019a\u01a1\7$\2\2\u019b\u019d\5D#\2\u019c\u019e\7")
        buf.write("+\2\2\u019d\u019c\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u01a0")
        buf.write("\3\2\2\2\u019f\u019b\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1")
        buf.write("\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a4\3\2\2\2")
        buf.write("\u01a3\u01a1\3\2\2\2\u01a4\u01a5\7%\2\2\u01a5G\3\2\2\2")
        buf.write("\u01a6\u01a8\5~@\2\u01a7\u01a9\7+\2\2\u01a8\u01a7\3\2")
        buf.write("\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ab\3\2\2\2\u01aa\u01a6")
        buf.write("\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac")
        buf.write("\u01ad\3\2\2\2\u01adI\3\2\2\2\u01ae\u01b2\5L\'\2\u01af")
        buf.write("\u01b2\5n8\2\u01b0\u01b2\5z>\2\u01b1\u01ae\3\2\2\2\u01b1")
        buf.write("\u01af\3\2\2\2\u01b1\u01b0\3\2\2\2\u01b2K\3\2\2\2\u01b3")
        buf.write("\u01b4\5N(\2\u01b4\u01b5\t\4\2\2\u01b5\u01b6\5N(\2\u01b6")
        buf.write("\u01b9\3\2\2\2\u01b7\u01b9\5N(\2\u01b8\u01b3\3\2\2\2\u01b8")
        buf.write("\u01b7\3\2\2\2\u01b9M\3\2\2\2\u01ba\u01bb\5P)\2\u01bb")
        buf.write("\u01bc\t\5\2\2\u01bc\u01bd\5P)\2\u01bd\u01c0\3\2\2\2\u01be")
        buf.write("\u01c0\5P)\2\u01bf\u01ba\3\2\2\2\u01bf\u01be\3\2\2\2\u01c0")
        buf.write("O\3\2\2\2\u01c1\u01c2\b)\1\2\u01c2\u01c3\5R*\2\u01c3\u01c9")
        buf.write("\3\2\2\2\u01c4\u01c5\f\4\2\2\u01c5\u01c6\t\6\2\2\u01c6")
        buf.write("\u01c8\5R*\2\u01c7\u01c4\3\2\2\2\u01c8\u01cb\3\2\2\2\u01c9")
        buf.write("\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01caQ\3\2\2\2\u01cb")
        buf.write("\u01c9\3\2\2\2\u01cc\u01cd\b*\1\2\u01cd\u01ce\5T+\2\u01ce")
        buf.write("\u01d4\3\2\2\2\u01cf\u01d0\f\4\2\2\u01d0\u01d1\t\7\2\2")
        buf.write("\u01d1\u01d3\5T+\2\u01d2\u01cf\3\2\2\2\u01d3\u01d6\3\2")
        buf.write("\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5S\3")
        buf.write("\2\2\2\u01d6\u01d4\3\2\2\2\u01d7\u01d8\b+\1\2\u01d8\u01d9")
        buf.write("\5V,\2\u01d9\u01df\3\2\2\2\u01da\u01db\f\4\2\2\u01db\u01dc")
        buf.write("\t\b\2\2\u01dc\u01de\5V,\2\u01dd\u01da\3\2\2\2\u01de\u01e1")
        buf.write("\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0")
        buf.write("U\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2\u01e3\7\62\2\2\u01e3")
        buf.write("\u01e6\5V,\2\u01e4\u01e6\5X-\2\u01e5\u01e2\3\2\2\2\u01e5")
        buf.write("\u01e4\3\2\2\2\u01e6W\3\2\2\2\u01e7\u01e8\7.\2\2\u01e8")
        buf.write("\u01eb\5X-\2\u01e9\u01eb\5Z.\2\u01ea\u01e7\3\2\2\2\u01ea")
        buf.write("\u01e9\3\2\2\2\u01ebY\3\2\2\2\u01ec\u01ed\5\\/\2\u01ed")
        buf.write("\u01ee\5l\67\2\u01ee\u01f1\3\2\2\2\u01ef\u01f1\5\\/\2")
        buf.write("\u01f0\u01ec\3\2\2\2\u01f0\u01ef\3\2\2\2\u01f1[\3\2\2")
        buf.write("\2\u01f2\u01f3\b/\1\2\u01f3\u01f4\5^\60\2\u01f4\u01fa")
        buf.write("\3\2\2\2\u01f5\u01f6\f\4\2\2\u01f6\u01f7\t\t\2\2\u01f7")
        buf.write("\u01f9\5^\60\2\u01f8\u01f5\3\2\2\2\u01f9\u01fc\3\2\2\2")
        buf.write("\u01fa\u01f8\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb]\3\2\2")
        buf.write("\2\u01fc\u01fa\3\2\2\2\u01fd\u01fe\7\33\2\2\u01fe\u0201")
        buf.write("\5^\60\2\u01ff\u0201\5`\61\2\u0200\u01fd\3\2\2\2\u0200")
        buf.write("\u01ff\3\2\2\2\u0201_\3\2\2\2\u0202\u020b\5~@\2\u0203")
        buf.write("\u020b\7A\2\2\u0204\u0205\7$\2\2\u0205\u0206\5L\'\2\u0206")
        buf.write("\u0207\7%\2\2\u0207\u020b\3\2\2\2\u0208\u020b\7\21\2\2")
        buf.write("\u0209\u020b\5n8\2\u020a\u0202\3\2\2\2\u020a\u0203\3\2")
        buf.write("\2\2\u020a\u0204\3\2\2\2\u020a\u0208\3\2\2\2\u020a\u0209")
        buf.write("\3\2\2\2\u020ba\3\2\2\2\u020c\u020d\t\n\2\2\u020dc\3\2")
        buf.write("\2\2\u020e\u020f\t\13\2\2\u020fe\3\2\2\2\u0210\u0211\7")
        buf.write("=\2\2\u0211g\3\2\2\2\u0212\u0213\t\5\2\2\u0213i\3\2\2")
        buf.write("\2\u0214\u0215\5J&\2\u0215\u0216\5l\67\2\u0216k\3\2\2")
        buf.write("\2\u0217\u0218\7&\2\2\u0218\u0219\5J&\2\u0219\u021b\7")
        buf.write("\'\2\2\u021a\u021c\5l\67\2\u021b\u021a\3\2\2\2\u021b\u021c")
        buf.write("\3\2\2\2\u021cm\3\2\2\2\u021d\u0222\5p9\2\u021e\u0222")
        buf.write("\5r:\2\u021f\u0222\5t;\2\u0220\u0222\5x=\2\u0221\u021d")
        buf.write("\3\2\2\2\u0221\u021e\3\2\2\2\u0221\u021f\3\2\2\2\u0221")
        buf.write("\u0220\3\2\2\2\u0222o\3\2\2\2\u0223\u0224\5<\37\2\u0224")
        buf.write("\u0225\7>\2\2\u0225\u0226\7A\2\2\u0226q\3\2\2\2\u0227")
        buf.write("\u0228\7A\2\2\u0228\u0229\7?\2\2\u0229\u022a\7A\2\2\u022a")
        buf.write("s\3\2\2\2\u022b\u022c\5<\37\2\u022c\u022d\7>\2\2\u022d")
        buf.write("\u022f\3\2\2\2\u022e\u022b\3\2\2\2\u022e\u022f\3\2\2\2")
        buf.write("\u022f\u0230\3\2\2\2\u0230\u0231\5v<\2\u0231u\3\2\2\2")
        buf.write("\u0232\u0233\7A\2\2\u0233\u0235\7$\2\2\u0234\u0236\5|")
        buf.write("?\2\u0235\u0234\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0237")
        buf.write("\3\2\2\2\u0237\u0238\7%\2\2\u0238w\3\2\2\2\u0239\u023a")
        buf.write("\7A\2\2\u023a\u023c\7?\2\2\u023b\u0239\3\2\2\2\u023b\u023c")
        buf.write("\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023e\7A\2\2\u023e")
        buf.write("\u0240\7$\2\2\u023f\u0241\5|?\2\u0240\u023f\3\2\2\2\u0240")
        buf.write("\u0241\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0243\7%\2\2")
        buf.write("\u0243y\3\2\2\2\u0244\u0245\7\33\2\2\u0245\u0246\7A\2")
        buf.write("\2\u0246\u0248\7$\2\2\u0247\u0249\5|?\2\u0248\u0247\3")
        buf.write("\2\2\2\u0248\u0249\3\2\2\2\u0249\u024a\3\2\2\2\u024a\u024b")
        buf.write("\7%\2\2\u024b{\3\2\2\2\u024c\u024e\5L\'\2\u024d\u024f")
        buf.write("\7+\2\2\u024e\u024d\3\2\2\2\u024e\u024f\3\2\2\2\u024f")
        buf.write("\u0251\3\2\2\2\u0250\u024c\3\2\2\2\u0251\u0252\3\2\2\2")
        buf.write("\u0252\u0250\3\2\2\2\u0252\u0253\3\2\2\2\u0253}\3\2\2")
        buf.write("\2\u0254\u0255\t\f\2\2\u0255\177\3\2\2\2@\u0083\u008b")
        buf.write("\u0093\u0095\u009d\u00a2\u00a7\u00ae\u00b3\u00bc\u00c5")
        buf.write("\u00cd\u00d8\u00e2\u00e7\u00ee\u00f6\u00fb\u00fd\u010a")
        buf.write("\u0110\u0120\u0128\u012e\u0133\u013f\u0143\u014b\u014f")
        buf.write("\u015d\u0162\u0170\u0179\u0182\u018a\u0190\u0194\u019d")
        buf.write("\u01a1\u01a8\u01ac\u01b1\u01b8\u01bf\u01c9\u01d4\u01df")
        buf.write("\u01e5\u01ea\u01f0\u01fa\u0200\u020a\u021b\u0221\u022e")
        buf.write("\u0235\u023b\u0240\u0248\u024e\u0252")
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
                      "BLOCK_COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_class_body = 2
    RULE_class_attr = 3
    RULE_class_method = 4
    RULE_normal_method = 5
    RULE_constructor = 6
    RULE_destructor = 7
    RULE_params_list = 8
    RULE_params = 9
    RULE_data_type = 10
    RULE_stmt = 11
    RULE_var_decl = 12
    RULE_pair_list = 13
    RULE_pair = 14
    RULE_pair_list_arr = 15
    RULE_pair_arr = 16
    RULE_array_decl_tail = 17
    RULE_object_decl = 18
    RULE_expr_tail = 19
    RULE_assign_stmt = 20
    RULE_if_stmt = 21
    RULE_else_if_body = 22
    RULE_for_in_stmt = 23
    RULE_for_in_body = 24
    RULE_for_in_expr = 25
    RULE_break_stmt = 26
    RULE_continue_stmt = 27
    RULE_return_stmt = 28
    RULE_class_name = 29
    RULE_method_invoc = 30
    RULE_expr_list = 31
    RULE_block_stmt = 32
    RULE_literal_idx_array = 33
    RULE_literal_mtd_array = 34
    RULE_array_element = 35
    RULE_all_expr = 36
    RULE_op = 37
    RULE_op1 = 38
    RULE_op2 = 39
    RULE_op3 = 40
    RULE_op4 = 41
    RULE_op5 = 42
    RULE_op6 = 43
    RULE_op7 = 44
    RULE_op8 = 45
    RULE_op9 = 46
    RULE_operands = 47
    RULE_arithmetic_ops = 48
    RULE_boolean_ops = 49
    RULE_string_ops = 50
    RULE_relational_ops = 51
    RULE_element_expr = 52
    RULE_index_ops = 53
    RULE_member_access = 54
    RULE_instance_attr = 55
    RULE_static_attr = 56
    RULE_instance_method = 57
    RULE_instance_method_tail = 58
    RULE_static_method = 59
    RULE_object_create = 60
    RULE_list_of_expr = 61
    RULE_literal = 62

    ruleNames =  [ "program", "class_decl", "class_body", "class_attr", 
                   "class_method", "normal_method", "constructor", "destructor", 
                   "params_list", "params", "data_type", "stmt", "var_decl", 
                   "pair_list", "pair", "pair_list_arr", "pair_arr", "array_decl_tail", 
                   "object_decl", "expr_tail", "assign_stmt", "if_stmt", 
                   "else_if_body", "for_in_stmt", "for_in_body", "for_in_expr", 
                   "break_stmt", "continue_stmt", "return_stmt", "class_name", 
                   "method_invoc", "expr_list", "block_stmt", "literal_idx_array", 
                   "literal_mtd_array", "array_element", "all_expr", "op", 
                   "op1", "op2", "op3", "op4", "op5", "op6", "op7", "op8", 
                   "op9", "operands", "arithmetic_ops", "boolean_ops", "string_ops", 
                   "relational_ops", "element_expr", "index_ops", "member_access", 
                   "instance_attr", "static_attr", "instance_method", "instance_method_tail", 
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
            self.state = 127 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 126
                self.class_decl()
                self.state = 129 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 131
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
            self.state = 133
            self.match(D96Parser.CLASS)
            self.state = 134
            self.class_name()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 135
                self.match(D96Parser.COLON)
                self.state = 136
                self.class_name()


            self.state = 139
            self.match(D96Parser.LP)
            self.state = 140
            self.class_body()
            self.state = 141
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
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID))) != 0):
                self.state = 145
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 143
                    self.class_attr()
                    pass
                elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID]:
                    self.state = 144
                    self.class_method()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 149
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

        def var_decl(self):
            return self.getTypedRuleContext(D96Parser.Var_declContext,0)


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
            self.state = 150
            self.var_decl()
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
        self.enterRule(localctx, 8, self.RULE_class_method)
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.normal_method()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 154
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_method" ):
                return visitor.visitNormal_method(self)
            else:
                return visitor.visitChildren(self)




    def normal_method(self):

        localctx = D96Parser.Normal_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_normal_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(D96Parser.ID)
            self.state = 158
            self.match(D96Parser.LB)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 159
                self.params_list()


            self.state = 162
            self.match(D96Parser.RB)
            self.state = 163
            self.match(D96Parser.LP)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.NULL) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 164
                self.block_stmt()


            self.state = 167
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
        self.enterRule(localctx, 12, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 170
            self.match(D96Parser.LB)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 171
                self.params_list()


            self.state = 174
            self.match(D96Parser.RB)
            self.state = 175
            self.match(D96Parser.LP)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.NULL) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 176
                self.block_stmt()


            self.state = 179
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
        self.enterRule(localctx, 14, self.RULE_destructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(D96Parser.DESTRUCTOR)
            self.state = 182
            self.match(D96Parser.LB)
            self.state = 183
            self.match(D96Parser.RB)
            self.state = 184
            self.match(D96Parser.LP)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.NULL) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 185
                self.block_stmt()


            self.state = 188
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
        self.enterRule(localctx, 16, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.params()
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 191
                self.match(D96Parser.SEMI)
                self.state = 192
                self.params()
                self.state = 197
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
        self.enterRule(localctx, 18, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(D96Parser.ID)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 199
                self.match(D96Parser.COMMA)
                self.state = 200
                self.match(D96Parser.ID)
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 206
            self.match(D96Parser.COLON)
            self.state = 207
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
        self.enterRule(localctx, 20, self.RULE_data_type)
        try:
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 211
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 212
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.SELF, D96Parser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 213
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
        self.enterRule(localctx, 22, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 216
                self.var_decl()
                pass

            elif la_ == 2:
                self.state = 217
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.state = 218
                self.if_stmt()
                pass

            elif la_ == 4:
                self.state = 219
                self.for_in_stmt()
                pass

            elif la_ == 5:
                self.state = 220
                self.break_stmt()
                pass

            elif la_ == 6:
                self.state = 221
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.state = 222
                self.return_stmt()
                pass

            elif la_ == 8:
                self.state = 223
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
        self.enterRule(localctx, 24, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 227
                self.pair_list()
                pass

            elif la_ == 2:
                self.state = 228
                self.pair_list_arr()
                pass


            self.state = 231
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
        self.enterRule(localctx, 26, self.RULE_pair_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(D96Parser.ID)
            self.state = 234
            self.pair()
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 235
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
        self.enterRule(localctx, 28, self.RULE_pair)
        self._la = 0 # Token type
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(D96Parser.COMMA)
                self.state = 239
                self.match(D96Parser.ID)
                self.state = 240
                self.pair()
                self.state = 244
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 241
                    self.all_expr()
                    self.state = 242
                    self.match(D96Parser.COMMA)


                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.match(D96Parser.COLON)
                self.state = 247
                self.data_type()
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.ASSIGN:
                    self.state = 248
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
        self.enterRule(localctx, 30, self.RULE_pair_list_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(D96Parser.ID)
            self.state = 254
            self.pair_arr()
            self.state = 255
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
        self.enterRule(localctx, 32, self.RULE_pair_arr)
        try:
            self.state = 264
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.match(D96Parser.COMMA)
                self.state = 258
                self.match(D96Parser.ID)
                self.state = 259
                self.pair_arr()
                self.state = 260
                self.array_decl_tail()
                self.state = 261
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
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
        self.enterRule(localctx, 34, self.RULE_array_decl_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(D96Parser.ARRAY)
            self.state = 267
            self.match(D96Parser.LS)
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.SELF, D96Parser.ID]:
                self.state = 268
                self.data_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 269
                self.match(D96Parser.ARRAY)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 272
            self.match(D96Parser.COMMA)

            self.state = 273
            self.match(D96Parser.LITERAL_INT)
            self.state = 274
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
        self.enterRule(localctx, 36, self.RULE_object_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(D96Parser.NEW)
            self.state = 277
            self.match(D96Parser.ID)
            self.state = 278
            self.match(D96Parser.LB)
            self.state = 279
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_tailContext(ParserRuleContext):
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
            return D96Parser.RULE_expr_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_tail" ):
                return visitor.visitExpr_tail(self)
            else:
                return visitor.visitChildren(self)




    def expr_tail(self):

        localctx = D96Parser.Expr_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 281
                    self.all_expr()
                    self.state = 282
                    self.match(D96Parser.COMMA) 
                self.state = 288
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 289
            self.all_expr()
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def element_expr(self):
            return self.getTypedRuleContext(D96Parser.Element_exprContext,0)


        def class_name(self):
            return self.getTypedRuleContext(D96Parser.Class_nameContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOT)
            else:
                return self.getToken(D96Parser.DOT, i)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 294
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 291
                    self.class_name()
                    self.state = 292
                    self.match(D96Parser.DOT)


                self.state = 300
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 296
                        self.match(D96Parser.ID)
                        self.state = 297
                        self.match(D96Parser.DOT) 
                    self.state = 302
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

                self.state = 303
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 304
                self.element_expr()
                pass


            self.state = 307
            self.match(D96Parser.ASSIGN)
            self.state = 308
            self.all_expr()
            self.state = 309
            self.match(D96Parser.SEMI)
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
        self.enterRule(localctx, 42, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(D96Parser.IF)
            self.state = 312
            self.match(D96Parser.LB)
            self.state = 313
            self.all_expr()
            self.state = 314
            self.match(D96Parser.RB)
            self.state = 315
            self.match(D96Parser.LP)
            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.NULL) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 316
                self.block_stmt()


            self.state = 319
            self.match(D96Parser.RP)
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSEIF:
                self.state = 320
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
        self.enterRule(localctx, 44, self.RULE_else_if_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(D96Parser.ELSEIF)
            self.state = 324
            self.match(D96Parser.LB)
            self.state = 325
            self.all_expr()
            self.state = 326
            self.match(D96Parser.RB)
            self.state = 327
            self.match(D96Parser.LP)
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.NULL) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 328
                self.block_stmt()


            self.state = 331
            self.match(D96Parser.RP)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSEIF:
                self.state = 332
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

        def for_in_body(self):
            return self.getTypedRuleContext(D96Parser.For_in_bodyContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_for_in_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_in_stmt" ):
                return visitor.visitFor_in_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_in_stmt(self):

        localctx = D96Parser.For_in_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_for_in_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(D96Parser.FOREACH)
            self.state = 336
            self.for_in_body()
            self.state = 337
            self.match(D96Parser.SEMI)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_in_body" ):
                return visitor.visitFor_in_body(self)
            else:
                return visitor.visitChildren(self)




    def for_in_body(self):

        localctx = D96Parser.For_in_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_for_in_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(D96Parser.LB)
            self.state = 340
            self.match(D96Parser.ID)
            self.state = 341
            self.match(D96Parser.IN)
            self.state = 342
            self.for_in_expr()
            self.state = 343
            self.match(D96Parser.DOTDOT)
            self.state = 344
            self.for_in_expr()
            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 345
                self.match(D96Parser.BY)
                self.state = 346
                self.for_in_expr()


            self.state = 349
            self.match(D96Parser.RB)
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
        self.enterRule(localctx, 50, self.RULE_for_in_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.SUBTRACT:
                self.state = 351
                self.match(D96Parser.SUBTRACT)


            self.state = 354
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
        self.enterRule(localctx, 52, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(D96Parser.BREAK)
            self.state = 357
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
        self.enterRule(localctx, 54, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(D96Parser.CONTINUE)
            self.state = 360
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
        self.enterRule(localctx, 56, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(D96Parser.RETURN)
            self.state = 366
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 363
                self.all_expr()
                self.state = 368
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 369
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
        self.enterRule(localctx, 58, self.RULE_class_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
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
        self.enterRule(localctx, 60, self.RULE_method_invoc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 373
                self.instance_method()
                pass

            elif la_ == 2:
                self.state = 374
                self.static_method()
                pass


            self.state = 377
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
        self.enterRule(localctx, 62, self.RULE_expr_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 379
                    self.all_expr()
                    self.state = 380
                    self.match(D96Parser.COMMA) 
                self.state = 386
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

            self.state = 387
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
        self.enterRule(localctx, 64, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 389
                self.stmt()
                self.state = 392 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.NULL) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0)):
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
        self.enterRule(localctx, 66, self.RULE_literal_idx_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(D96Parser.ARRAY)
            self.state = 395
            self.match(D96Parser.LB)
            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING))) != 0):
                self.state = 396
                self.array_element()
                self.state = 398
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.COMMA:
                    self.state = 397
                    self.match(D96Parser.COMMA)


                self.state = 404
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 405
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
        self.enterRule(localctx, 68, self.RULE_literal_mtd_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(D96Parser.ARRAY)
            self.state = 408
            self.match(D96Parser.LB)
            self.state = 415
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ARRAY:
                self.state = 409
                self.literal_idx_array()
                self.state = 411
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.COMMA:
                    self.state = 410
                    self.match(D96Parser.COMMA)


                self.state = 417
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 418
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
        self.enterRule(localctx, 70, self.RULE_array_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 420
                    self.literal()
                    self.state = 422
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        self.state = 421
                        self.match(D96Parser.COMMA)



                else:
                    raise NoViableAltException(self)
                self.state = 426 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
        self.enterRule(localctx, 72, self.RULE_all_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 428
                self.op()
                pass

            elif la_ == 2:
                self.state = 429
                self.member_access()
                pass

            elif la_ == 3:
                self.state = 430
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
        self.enterRule(localctx, 74, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.op1()
                self.state = 434
                _la = self._input.LA(1)
                if not(_la==D96Parser.EQUAL_STRING or _la==D96Parser.STRING_CONCAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 435
                self.op1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
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
        self.enterRule(localctx, 76, self.RULE_op1)
        self._la = 0 # Token type
        try:
            self.state = 445
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.op2(0)
                self.state = 441
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.LESS_THAN) | (1 << D96Parser.LEQ) | (1 << D96Parser.GREATER_THAN) | (1 << D96Parser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 442
                self.op2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_op2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.op3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 455
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op2)
                    self.state = 450
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 451
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 452
                    self.op3(0) 
                self.state = 457
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_op3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.op4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 466
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op3)
                    self.state = 461
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 462
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUBTRACT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 463
                    self.op4(0) 
                self.state = 468
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_op4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.op5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 477
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op4)
                    self.state = 472
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 473
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLY) | (1 << D96Parser.DIVIDE) | (1 << D96Parser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 474
                    self.op5() 
                self.state = 479
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

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
        self.enterRule(localctx, 84, self.RULE_op5)
        try:
            self.state = 483
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 480
                self.match(D96Parser.NOT)
                self.state = 481
                self.op5()
                pass
            elif token in [D96Parser.LITERAL_INT, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.SUBTRACT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
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
        self.enterRule(localctx, 86, self.RULE_op6)
        try:
            self.state = 488
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUBTRACT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.match(D96Parser.SUBTRACT)
                self.state = 486
                self.op6()
                pass
            elif token in [D96Parser.LITERAL_INT, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
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
        self.enterRule(localctx, 88, self.RULE_op7)
        try:
            self.state = 494
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 490
                self.op8(0)
                self.state = 491
                self.index_ops()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
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
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_op8, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.op9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 504
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op8)
                    self.state = 499
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 500
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.DOT or _la==D96Parser.DOUBLE_COLON):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 501
                    self.op9() 
                self.state = 506
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

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
        self.enterRule(localctx, 92, self.RULE_op9)
        try:
            self.state = 510
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 507
                self.match(D96Parser.NEW)
                self.state = 508
                self.op9()
                pass
            elif token in [D96Parser.LITERAL_INT, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.SELF, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 509
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
        self.enterRule(localctx, 94, self.RULE_operands)
        try:
            self.state = 520
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 512
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 513
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 514
                self.match(D96Parser.LB)
                self.state = 515
                self.op()
                self.state = 516
                self.match(D96Parser.RB)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 518
                self.match(D96Parser.NULL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 519
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
        self.enterRule(localctx, 96, self.RULE_arithmetic_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
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
        self.enterRule(localctx, 98, self.RULE_boolean_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
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
        self.enterRule(localctx, 100, self.RULE_string_ops)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
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
        self.enterRule(localctx, 102, self.RULE_relational_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
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
        self.enterRule(localctx, 104, self.RULE_element_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.all_expr()
            self.state = 531
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
        self.enterRule(localctx, 106, self.RULE_index_ops)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.match(D96Parser.LS)
            self.state = 534
            self.all_expr()
            self.state = 535
            self.match(D96Parser.RS)
            self.state = 537
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 536
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


        def getRuleIndex(self):
            return D96Parser.RULE_member_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_access" ):
                return visitor.visitMember_access(self)
            else:
                return visitor.visitChildren(self)




    def member_access(self):

        localctx = D96Parser.Member_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_member_access)
        try:
            self.state = 543
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 539
                self.instance_attr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 540
                self.static_attr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 541
                self.instance_method()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 542
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

        def class_name(self):
            return self.getTypedRuleContext(D96Parser.Class_nameContext,0)


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
        self.enterRule(localctx, 110, self.RULE_instance_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self.class_name()
            self.state = 546
            self.match(D96Parser.DOT)
            self.state = 547
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

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
        self.enterRule(localctx, 112, self.RULE_static_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.match(D96Parser.ID)
            self.state = 550
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 551
            self.match(D96Parser.ID)
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

        def instance_method_tail(self):
            return self.getTypedRuleContext(D96Parser.Instance_method_tailContext,0)


        def class_name(self):
            return self.getTypedRuleContext(D96Parser.Class_nameContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method" ):
                return visitor.visitInstance_method(self)
            else:
                return visitor.visitChildren(self)




    def instance_method(self):

        localctx = D96Parser.Instance_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_instance_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.state = 553
                self.class_name()
                self.state = 554
                self.match(D96Parser.DOT)


            self.state = 558
            self.instance_method_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_method_tailContext(ParserRuleContext):
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
            return D96Parser.RULE_instance_method_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method_tail" ):
                return visitor.visitInstance_method_tail(self)
            else:
                return visitor.visitChildren(self)




    def instance_method_tail(self):

        localctx = D96Parser.Instance_method_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_instance_method_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self.match(D96Parser.ID)
            self.state = 561
            self.match(D96Parser.LB)
            self.state = 563
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 562
                self.list_of_expr()


            self.state = 565
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

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
        self.enterRule(localctx, 118, self.RULE_static_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 567
                self.match(D96Parser.ID)
                self.state = 568
                self.match(D96Parser.DOUBLE_COLON)


            self.state = 571
            self.match(D96Parser.ID)
            self.state = 572
            self.match(D96Parser.LB)
            self.state = 574
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 573
                self.list_of_expr()


            self.state = 576
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
        self.enterRule(localctx, 120, self.RULE_object_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 578
            self.match(D96Parser.NEW)
            self.state = 579
            self.match(D96Parser.ID)
            self.state = 580
            self.match(D96Parser.LB)
            self.state = 582
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 581
                self.list_of_expr()


            self.state = 584
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
        self.enterRule(localctx, 122, self.RULE_list_of_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 590 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 586
                self.op()
                self.state = 588
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.COMMA:
                    self.state = 587
                    self.match(D96Parser.COMMA)


                self.state = 592 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0)):
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
        self.enterRule(localctx, 124, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
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
        self._predicates[39] = self.op2_sempred
        self._predicates[40] = self.op3_sempred
        self._predicates[41] = self.op4_sempred
        self._predicates[45] = self.op8_sempred
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
         




