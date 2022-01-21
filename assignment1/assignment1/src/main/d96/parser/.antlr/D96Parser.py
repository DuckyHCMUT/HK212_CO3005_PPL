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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u0234\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\3\2\6\2|\n\2\r\2\16\2}\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\5\3\u0086\n\3\3\3\3\3\3\3\3\3\3\4\3\4\7\4\u008e")
        buf.write("\n\4\f\4\16\4\u0091\13\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\5\6\u009c\n\6\3\7\5\7\u009f\n\7\3\7\3\7\3\7\5\7")
        buf.write("\u00a4\n\7\3\7\3\7\3\7\5\7\u00a9\n\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\5\b\u00b0\n\b\3\b\3\b\3\b\5\b\u00b5\n\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\5\t\u00bf\n\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\7\n\u00c6\n\n\f\n\16\n\u00c9\13\n\3\13\3\13\3\13\7\13")
        buf.write("\u00ce\n\13\f\13\16\13\u00d1\13\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\5\16\u00e6\n\16\3\17\3\17\3\17\5\17")
        buf.write("\u00eb\n\17\3\20\3\20\7\20\u00ef\n\20\f\20\16\20\u00f2")
        buf.write("\13\20\3\20\3\20\3\20\3\20\3\20\5\20\u00f9\n\20\3\20\3")
        buf.write("\20\3\21\3\21\7\21\u00ff\n\21\f\21\16\21\u0102\13\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\7\23\u0111\n\23\f\23\16\23\u0114\13\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\7\24\u011b\n\24\f\24\16\24\u011e")
        buf.write("\13\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\27\3\27\5\27\u0130\n\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u013b\n")
        buf.write("\31\3\31\3\31\3\32\3\32\3\32\3\32\5\32\u0143\n\32\3\32")
        buf.write("\3\32\7\32\u0147\n\32\f\32\16\32\u014a\13\32\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u0158\n\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3")
        buf.write("\37\3\37\3 \3 \5 \u0166\n \3 \3 \3!\3!\3!\5!\u016d\n!")
        buf.write("\3!\3!\3!\5!\u0172\n!\3!\3!\3!\3\"\3\"\3\"\7\"\u017a\n")
        buf.write("\"\f\"\16\"\u017d\13\"\3\"\3\"\3#\6#\u0182\n#\r#\16#\u0183")
        buf.write("\3$\3$\3$\3$\5$\u018a\n$\7$\u018c\n$\f$\16$\u018f\13$")
        buf.write("\3$\3$\3%\3%\3%\3%\5%\u0197\n%\7%\u0199\n%\f%\16%\u019c")
        buf.write("\13%\3%\3%\3&\3&\5&\u01a2\n&\6&\u01a4\n&\r&\16&\u01a5")
        buf.write("\3\'\3\'\3\'\3\'\3\'\5\'\u01ad\n\'\3(\3(\3(\3(\3(\5(\u01b4")
        buf.write("\n(\3)\3)\3)\3)\3)\3)\7)\u01bc\n)\f)\16)\u01bf\13)\3*")
        buf.write("\3*\3*\3*\3*\3*\7*\u01c7\n*\f*\16*\u01ca\13*\3+\3+\3+")
        buf.write("\3+\3+\3+\7+\u01d2\n+\f+\16+\u01d5\13+\3,\3,\3,\5,\u01da")
        buf.write("\n,\3-\3-\3-\5-\u01df\n-\3.\3.\3.\3.\5.\u01e5\n.\3/\3")
        buf.write("/\3/\3/\3/\3/\7/\u01ed\n/\f/\16/\u01f0\13/\3\60\3\60\3")
        buf.write("\60\5\60\u01f5\n\60\3\61\3\61\3\61\3\61\3\61\3\61\5\61")
        buf.write("\u01fd\n\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3")
        buf.write("\66\3\66\3\66\3\67\3\67\3\67\3\67\5\67\u020e\n\67\38\3")
        buf.write("8\38\38\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3")
        buf.write(";\3;\3;\3<\3<\3<\3<\3<\3<\3=\3=\5=\u022e\n=\6=\u0230\n")
        buf.write("=\r=\16=\u0231\3=\2\6PRT\\>\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bdfhjlnprtvx\2\f\3\2\13\f\6\2\20\20\25\25\32\32\36\36")
        buf.write("\3\2=>\3\2;<\4\2\64\64\66:\3\2\62\63\3\2,-\3\2.\60\3\2")
        buf.write(",\60\4\2\61\63;;\2\u0232\2{\3\2\2\2\4\u0081\3\2\2\2\6")
        buf.write("\u008f\3\2\2\2\b\u0092\3\2\2\2\n\u009b\3\2\2\2\f\u009e")
        buf.write("\3\2\2\2\16\u00ac\3\2\2\2\20\u00b9\3\2\2\2\22\u00c2\3")
        buf.write("\2\2\2\24\u00ca\3\2\2\2\26\u00d5\3\2\2\2\30\u00d7\3\2")
        buf.write("\2\2\32\u00e5\3\2\2\2\34\u00e7\3\2\2\2\36\u00f0\3\2\2")
        buf.write("\2 \u0100\3\2\2\2\"\u0108\3\2\2\2$\u0112\3\2\2\2&\u011c")
        buf.write("\3\2\2\2(\u0121\3\2\2\2*\u0128\3\2\2\2,\u012f\3\2\2\2")
        buf.write(".\u0131\3\2\2\2\60\u0134\3\2\2\2\62\u0148\3\2\2\2\64\u014b")
        buf.write("\3\2\2\2\66\u014f\3\2\2\28\u015b\3\2\2\2:\u015d\3\2\2")
        buf.write("\2<\u0160\3\2\2\2>\u0163\3\2\2\2@\u0169\3\2\2\2B\u017b")
        buf.write("\3\2\2\2D\u0181\3\2\2\2F\u0185\3\2\2\2H\u0192\3\2\2\2")
        buf.write("J\u01a3\3\2\2\2L\u01ac\3\2\2\2N\u01b3\3\2\2\2P\u01b5\3")
        buf.write("\2\2\2R\u01c0\3\2\2\2T\u01cb\3\2\2\2V\u01d9\3\2\2\2X\u01de")
        buf.write("\3\2\2\2Z\u01e4\3\2\2\2\\\u01e6\3\2\2\2^\u01f4\3\2\2\2")
        buf.write("`\u01fc\3\2\2\2b\u01fe\3\2\2\2d\u0200\3\2\2\2f\u0202\3")
        buf.write("\2\2\2h\u0204\3\2\2\2j\u0206\3\2\2\2l\u0209\3\2\2\2n\u020f")
        buf.write("\3\2\2\2p\u0213\3\2\2\2r\u0217\3\2\2\2t\u021e\3\2\2\2")
        buf.write("v\u0225\3\2\2\2x\u022f\3\2\2\2z|\5\4\3\2{z\3\2\2\2|}\3")
        buf.write("\2\2\2}{\3\2\2\2}~\3\2\2\2~\177\3\2\2\2\177\u0080\7\2")
        buf.write("\2\3\u0080\3\3\2\2\2\u0081\u0082\7\26\2\2\u0082\u0085")
        buf.write("\7@\2\2\u0083\u0084\7?\2\2\u0084\u0086\7@\2\2\u0085\u0083")
        buf.write("\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087\3\2\2\2\u0087")
        buf.write("\u0088\7\'\2\2\u0088\u0089\5\6\4\2\u0089\u008a\7(\2\2")
        buf.write("\u008a\5\3\2\2\2\u008b\u008e\5\b\5\2\u008c\u008e\5\n\6")
        buf.write("\2\u008d\u008b\3\2\2\2\u008d\u008c\3\2\2\2\u008e\u0091")
        buf.write("\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090")
        buf.write("\7\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0093\t\2\2\2\u0093")
        buf.write("\u0094\7@\2\2\u0094\u0095\7?\2\2\u0095\u0096\5\26\f\2")
        buf.write("\u0096\u0097\7)\2\2\u0097\t\3\2\2\2\u0098\u009c\5\f\7")
        buf.write("\2\u0099\u009c\5\16\b\2\u009a\u009c\5\20\t\2\u009b\u0098")
        buf.write("\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009a\3\2\2\2\u009c")
        buf.write("\13\3\2\2\2\u009d\u009f\7\r\2\2\u009e\u009d\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\7@\2\2")
        buf.write("\u00a1\u00a3\7#\2\2\u00a2\u00a4\5\22\n\2\u00a3\u00a2\3")
        buf.write("\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6")
        buf.write("\7$\2\2\u00a6\u00a8\7\'\2\2\u00a7\u00a9\5D#\2\u00a8\u00a7")
        buf.write("\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa")
        buf.write("\u00ab\7(\2\2\u00ab\r\3\2\2\2\u00ac\u00ad\7\22\2\2\u00ad")
        buf.write("\u00af\7#\2\2\u00ae\u00b0\5\22\n\2\u00af\u00ae\3\2\2\2")
        buf.write("\u00af\u00b0\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\7")
        buf.write("$\2\2\u00b2\u00b4\7\'\2\2\u00b3\u00b5\5D#\2\u00b4\u00b3")
        buf.write("\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6")
        buf.write("\u00b7\7(\2\2\u00b7\u00b8\b\b\1\2\u00b8\17\3\2\2\2\u00b9")
        buf.write("\u00ba\7\27\2\2\u00ba\u00bb\7#\2\2\u00bb\u00bc\7$\2\2")
        buf.write("\u00bc\u00be\7\'\2\2\u00bd\u00bf\5D#\2\u00be\u00bd\3\2")
        buf.write("\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1")
        buf.write("\7(\2\2\u00c1\21\3\2\2\2\u00c2\u00c7\5\24\13\2\u00c3\u00c4")
        buf.write("\7)\2\2\u00c4\u00c6\5\24\13\2\u00c5\u00c3\3\2\2\2\u00c6")
        buf.write("\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2")
        buf.write("\u00c8\23\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00cf\7@\2")
        buf.write("\2\u00cb\u00cc\7*\2\2\u00cc\u00ce\7@\2\2\u00cd\u00cb\3")
        buf.write("\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0")
        buf.write("\3\2\2\2\u00d0\u00d2\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d2")
        buf.write("\u00d3\7?\2\2\u00d3\u00d4\5\26\f\2\u00d4\25\3\2\2\2\u00d5")
        buf.write("\u00d6\t\3\2\2\u00d6\27\3\2\2\2\u00d7\u00d8\7@\2\2\u00d8")
        buf.write("\31\3\2\2\2\u00d9\u00e6\5\34\17\2\u00da\u00e6\5*\26\2")
        buf.write("\u00db\u00e6\5.\30\2\u00dc\u00e6\5\64\33\2\u00dd\u00e6")
        buf.write("\5:\36\2\u00de\u00e6\5<\37\2\u00df\u00e6\5> \2\u00e0\u00e6")
        buf.write("\5@!\2\u00e1\u00e2\7\'\2\2\u00e2\u00e3\5D#\2\u00e3\u00e4")
        buf.write("\7(\2\2\u00e4\u00e6\3\2\2\2\u00e5\u00d9\3\2\2\2\u00e5")
        buf.write("\u00da\3\2\2\2\u00e5\u00db\3\2\2\2\u00e5\u00dc\3\2\2\2")
        buf.write("\u00e5\u00dd\3\2\2\2\u00e5\u00de\3\2\2\2\u00e5\u00df\3")
        buf.write("\2\2\2\u00e5\u00e0\3\2\2\2\u00e5\u00e1\3\2\2\2\u00e6\33")
        buf.write("\3\2\2\2\u00e7\u00ea\t\2\2\2\u00e8\u00eb\5\36\20\2\u00e9")
        buf.write("\u00eb\5 \21\2\u00ea\u00e8\3\2\2\2\u00ea\u00e9\3\2\2\2")
        buf.write("\u00eb\35\3\2\2\2\u00ec\u00ed\7@\2\2\u00ed\u00ef\7*\2")
        buf.write("\2\u00ee\u00ec\3\2\2\2\u00ef\u00f2\3\2\2\2\u00f0\u00ee")
        buf.write("\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f3\3\2\2\2\u00f2")
        buf.write("\u00f0\3\2\2\2\u00f3\u00f4\7@\2\2\u00f4\u00f5\7?\2\2\u00f5")
        buf.write("\u00f6\5\26\f\2\u00f6\u00f8\7\65\2\2\u00f7\u00f9\5$\23")
        buf.write("\2\u00f8\u00f7\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fa")
        buf.write("\3\2\2\2\u00fa\u00fb\7)\2\2\u00fb\37\3\2\2\2\u00fc\u00fd")
        buf.write("\7@\2\2\u00fd\u00ff\7*\2\2\u00fe\u00fc\3\2\2\2\u00ff\u0102")
        buf.write("\3\2\2\2\u0100\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101")
        buf.write("\u0103\3\2\2\2\u0102\u0100\3\2\2\2\u0103\u0104\7@\2\2")
        buf.write("\u0104\u0105\7?\2\2\u0105\u0106\5&\24\2\u0106\u0107\7")
        buf.write(")\2\2\u0107!\3\2\2\2\u0108\u0109\7\33\2\2\u0109\u010a")
        buf.write("\7@\2\2\u010a\u010b\7#\2\2\u010b\u010c\7$\2\2\u010c#\3")
        buf.write("\2\2\2\u010d\u010e\5L\'\2\u010e\u010f\7*\2\2\u010f\u0111")
        buf.write("\3\2\2\2\u0110\u010d\3\2\2\2\u0111\u0114\3\2\2\2\u0112")
        buf.write("\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0115\3\2\2\2")
        buf.write("\u0114\u0112\3\2\2\2\u0115\u0116\5L\'\2\u0116%\3\2\2\2")
        buf.write("\u0117\u0118\5(\25\2\u0118\u0119\7*\2\2\u0119\u011b\3")
        buf.write("\2\2\2\u011a\u0117\3\2\2\2\u011b\u011e\3\2\2\2\u011c\u011a")
        buf.write("\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011f\3\2\2\2\u011e")
        buf.write("\u011c\3\2\2\2\u011f\u0120\5(\25\2\u0120\'\3\2\2\2\u0121")
        buf.write("\u0122\7\35\2\2\u0122\u0123\7%\2\2\u0123\u0124\5\26\f")
        buf.write("\2\u0124\u0125\7*\2\2\u0125\u0126\7\4\2\2\u0126\u0127")
        buf.write("\7&\2\2\u0127)\3\2\2\2\u0128\u0129\5,\27\2\u0129\u012a")
        buf.write("\7\65\2\2\u012a\u012b\5L\'\2\u012b\u012c\7)\2\2\u012c")
        buf.write("+\3\2\2\2\u012d\u0130\5j\66\2\u012e\u0130\7@\2\2\u012f")
        buf.write("\u012d\3\2\2\2\u012f\u012e\3\2\2\2\u0130-\3\2\2\2\u0131")
        buf.write("\u0132\5\60\31\2\u0132\u0133\7)\2\2\u0133/\3\2\2\2\u0134")
        buf.write("\u0135\7\30\2\2\u0135\u0136\5L\'\2\u0136\u0137\5\62\32")
        buf.write("\2\u0137\u0138\7 \2\2\u0138\u013a\7\'\2\2\u0139\u013b")
        buf.write("\5D#\2\u013a\u0139\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013c")
        buf.write("\3\2\2\2\u013c\u013d\7(\2\2\u013d\61\3\2\2\2\u013e\u013f")
        buf.write("\7\34\2\2\u013f\u0140\5L\'\2\u0140\u0142\7\'\2\2\u0141")
        buf.write("\u0143\5D#\2\u0142\u0141\3\2\2\2\u0142\u0143\3\2\2\2\u0143")
        buf.write("\u0144\3\2\2\2\u0144\u0145\7(\2\2\u0145\u0147\3\2\2\2")
        buf.write("\u0146\u013e\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0146\3")
        buf.write("\2\2\2\u0148\u0149\3\2\2\2\u0149\63\3\2\2\2\u014a\u0148")
        buf.write("\3\2\2\2\u014b\u014c\7\17\2\2\u014c\u014d\5\66\34\2\u014d")
        buf.write("\u014e\7)\2\2\u014e\65\3\2\2\2\u014f\u0150\7#\2\2\u0150")
        buf.write("\u0151\7@\2\2\u0151\u0152\7!\2\2\u0152\u0153\58\35\2\u0153")
        buf.write("\u0154\7+\2\2\u0154\u0157\58\35\2\u0155\u0156\7\37\2\2")
        buf.write("\u0156\u0158\58\35\2\u0157\u0155\3\2\2\2\u0157\u0158\3")
        buf.write("\2\2\2\u0158\u0159\3\2\2\2\u0159\u015a\7$\2\2\u015a\67")
        buf.write("\3\2\2\2\u015b\u015c\7\4\2\2\u015c9\3\2\2\2\u015d\u015e")
        buf.write("\7\16\2\2\u015e\u015f\7)\2\2\u015f;\3\2\2\2\u0160\u0161")
        buf.write("\7\23\2\2\u0161\u0162\7)\2\2\u0162=\3\2\2\2\u0163\u0165")
        buf.write("\7\"\2\2\u0164\u0166\5L\'\2\u0165\u0164\3\2\2\2\u0165")
        buf.write("\u0166\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0168\7)\2\2")
        buf.write("\u0168?\3\2\2\2\u0169\u016a\7@\2\2\u016a\u016c\t\4\2\2")
        buf.write("\u016b\u016d\7\r\2\2\u016c\u016b\3\2\2\2\u016c\u016d\3")
        buf.write("\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f\7@\2\2\u016f\u0171")
        buf.write("\7#\2\2\u0170\u0172\5B\"\2\u0171\u0170\3\2\2\2\u0171\u0172")
        buf.write("\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0174\7$\2\2\u0174")
        buf.write("\u0175\7)\2\2\u0175A\3\2\2\2\u0176\u0177\5L\'\2\u0177")
        buf.write("\u0178\7*\2\2\u0178\u017a\3\2\2\2\u0179\u0176\3\2\2\2")
        buf.write("\u017a\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3")
        buf.write("\2\2\2\u017c\u017e\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u017f")
        buf.write("\5L\'\2\u017fC\3\2\2\2\u0180\u0182\5\32\16\2\u0181\u0180")
        buf.write("\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0181\3\2\2\2\u0183")
        buf.write("\u0184\3\2\2\2\u0184E\3\2\2\2\u0185\u0186\7\35\2\2\u0186")
        buf.write("\u018d\7#\2\2\u0187\u0189\5J&\2\u0188\u018a\7*\2\2\u0189")
        buf.write("\u0188\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018c\3\2\2\2")
        buf.write("\u018b\u0187\3\2\2\2\u018c\u018f\3\2\2\2\u018d\u018b\3")
        buf.write("\2\2\2\u018d\u018e\3\2\2\2\u018e\u0190\3\2\2\2\u018f\u018d")
        buf.write("\3\2\2\2\u0190\u0191\7$\2\2\u0191G\3\2\2\2\u0192\u0193")
        buf.write("\7\35\2\2\u0193\u019a\7#\2\2\u0194\u0196\5F$\2\u0195\u0197")
        buf.write("\7*\2\2\u0196\u0195\3\2\2\2\u0196\u0197\3\2\2\2\u0197")
        buf.write("\u0199\3\2\2\2\u0198\u0194\3\2\2\2\u0199\u019c\3\2\2\2")
        buf.write("\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019d\3")
        buf.write("\2\2\2\u019c\u019a\3\2\2\2\u019d\u019e\7$\2\2\u019eI\3")
        buf.write("\2\2\2\u019f\u01a1\7\3\2\2\u01a0\u01a2\7*\2\2\u01a1\u01a0")
        buf.write("\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a4\3\2\2\2\u01a3")
        buf.write("\u019f\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a3\3\2\2\2")
        buf.write("\u01a5\u01a6\3\2\2\2\u01a6K\3\2\2\2\u01a7\u01a8\5N(\2")
        buf.write("\u01a8\u01a9\t\5\2\2\u01a9\u01aa\5N(\2\u01aa\u01ad\3\2")
        buf.write("\2\2\u01ab\u01ad\5N(\2\u01ac\u01a7\3\2\2\2\u01ac\u01ab")
        buf.write("\3\2\2\2\u01adM\3\2\2\2\u01ae\u01af\5P)\2\u01af\u01b0")
        buf.write("\t\6\2\2\u01b0\u01b1\5P)\2\u01b1\u01b4\3\2\2\2\u01b2\u01b4")
        buf.write("\5P)\2\u01b3\u01ae\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4O")
        buf.write("\3\2\2\2\u01b5\u01b6\b)\1\2\u01b6\u01b7\5R*\2\u01b7\u01bd")
        buf.write("\3\2\2\2\u01b8\u01b9\f\4\2\2\u01b9\u01ba\t\7\2\2\u01ba")
        buf.write("\u01bc\5R*\2\u01bb\u01b8\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01beQ\3\2\2\2\u01bf")
        buf.write("\u01bd\3\2\2\2\u01c0\u01c1\b*\1\2\u01c1\u01c2\5T+\2\u01c2")
        buf.write("\u01c8\3\2\2\2\u01c3\u01c4\f\4\2\2\u01c4\u01c5\t\b\2\2")
        buf.write("\u01c5\u01c7\5T+\2\u01c6\u01c3\3\2\2\2\u01c7\u01ca\3\2")
        buf.write("\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9S\3")
        buf.write("\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01cc\b+\1\2\u01cc\u01cd")
        buf.write("\5V,\2\u01cd\u01d3\3\2\2\2\u01ce\u01cf\f\4\2\2\u01cf\u01d0")
        buf.write("\t\t\2\2\u01d0\u01d2\5V,\2\u01d1\u01ce\3\2\2\2\u01d2\u01d5")
        buf.write("\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4")
        buf.write("U\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6\u01d7\7\61\2\2\u01d7")
        buf.write("\u01da\5V,\2\u01d8\u01da\5X-\2\u01d9\u01d6\3\2\2\2\u01d9")
        buf.write("\u01d8\3\2\2\2\u01daW\3\2\2\2\u01db\u01dc\7-\2\2\u01dc")
        buf.write("\u01df\5X-\2\u01dd\u01df\5Z.\2\u01de\u01db\3\2\2\2\u01de")
        buf.write("\u01dd\3\2\2\2\u01dfY\3\2\2\2\u01e0\u01e1\5\\/\2\u01e1")
        buf.write("\u01e2\5l\67\2\u01e2\u01e5\3\2\2\2\u01e3\u01e5\5\\/\2")
        buf.write("\u01e4\u01e0\3\2\2\2\u01e4\u01e3\3\2\2\2\u01e5[\3\2\2")
        buf.write("\2\u01e6\u01e7\b/\1\2\u01e7\u01e8\5^\60\2\u01e8\u01ee")
        buf.write("\3\2\2\2\u01e9\u01ea\f\4\2\2\u01ea\u01eb\t\4\2\2\u01eb")
        buf.write("\u01ed\5^\60\2\u01ec\u01e9\3\2\2\2\u01ed\u01f0\3\2\2\2")
        buf.write("\u01ee\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef]\3\2\2")
        buf.write("\2\u01f0\u01ee\3\2\2\2\u01f1\u01f2\7\33\2\2\u01f2\u01f5")
        buf.write("\5^\60\2\u01f3\u01f5\5`\61\2\u01f4\u01f1\3\2\2\2\u01f4")
        buf.write("\u01f3\3\2\2\2\u01f5_\3\2\2\2\u01f6\u01fd\7\3\2\2\u01f7")
        buf.write("\u01fd\7@\2\2\u01f8\u01f9\7#\2\2\u01f9\u01fa\5L\'\2\u01fa")
        buf.write("\u01fb\7$\2\2\u01fb\u01fd\3\2\2\2\u01fc\u01f6\3\2\2\2")
        buf.write("\u01fc\u01f7\3\2\2\2\u01fc\u01f8\3\2\2\2\u01fda\3\2\2")
        buf.write("\2\u01fe\u01ff\t\n\2\2\u01ffc\3\2\2\2\u0200\u0201\t\13")
        buf.write("\2\2\u0201e\3\2\2\2\u0202\u0203\7<\2\2\u0203g\3\2\2\2")
        buf.write("\u0204\u0205\t\6\2\2\u0205i\3\2\2\2\u0206\u0207\5L\'\2")
        buf.write("\u0207\u0208\5l\67\2\u0208k\3\2\2\2\u0209\u020a\7%\2\2")
        buf.write("\u020a\u020b\5L\'\2\u020b\u020d\7&\2\2\u020c\u020e\5l")
        buf.write("\67\2\u020d\u020c\3\2\2\2\u020d\u020e\3\2\2\2\u020em\3")
        buf.write("\2\2\2\u020f\u0210\5L\'\2\u0210\u0211\7=\2\2\u0211\u0212")
        buf.write("\7@\2\2\u0212o\3\2\2\2\u0213\u0214\7@\2\2\u0214\u0215")
        buf.write("\7>\2\2\u0215\u0216\7@\2\2\u0216q\3\2\2\2\u0217\u0218")
        buf.write("\5L\'\2\u0218\u0219\7=\2\2\u0219\u021a\7@\2\2\u021a\u021b")
        buf.write("\7#\2\2\u021b\u021c\5x=\2\u021c\u021d\7$\2\2\u021ds\3")
        buf.write("\2\2\2\u021e\u021f\7@\2\2\u021f\u0220\7>\2\2\u0220\u0221")
        buf.write("\7@\2\2\u0221\u0222\7#\2\2\u0222\u0223\5x=\2\u0223\u0224")
        buf.write("\7$\2\2\u0224u\3\2\2\2\u0225\u0226\7\33\2\2\u0226\u0227")
        buf.write("\7@\2\2\u0227\u0228\7#\2\2\u0228\u0229\5x=\2\u0229\u022a")
        buf.write("\7$\2\2\u022aw\3\2\2\2\u022b\u022d\5L\'\2\u022c\u022e")
        buf.write("\7*\2\2\u022d\u022c\3\2\2\2\u022d\u022e\3\2\2\2\u022e")
        buf.write("\u0230\3\2\2\2\u022f\u022b\3\2\2\2\u0230\u0231\3\2\2\2")
        buf.write("\u0231\u022f\3\2\2\2\u0231\u0232\3\2\2\2\u0232y\3\2\2")
        buf.write("\2\64}\u0085\u008d\u008f\u009b\u009e\u00a3\u00a8\u00af")
        buf.write("\u00b4\u00be\u00c7\u00cf\u00e5\u00ea\u00f0\u00f8\u0100")
        buf.write("\u0112\u011c\u012f\u013a\u0142\u0148\u0157\u0165\u016c")
        buf.write("\u0171\u017b\u0183\u0189\u018d\u0196\u019a\u01a1\u01a5")
        buf.write("\u01ac\u01b3\u01bd\u01c8\u01d3\u01d9\u01de\u01e4\u01ee")
        buf.write("\u01f4\u01fc\u020d\u022d\u0231")
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
                     "'By'", "'Else'", "'In'", "'Return'", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "';'", "','", "'..'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'==.'", "'+.'", "'.'", "'::'", "':'" ]

    symbolicNames = [ "<INVALID>", "LITERAL", "LITERAL_INT_DEC", "LITERAL_INT_HEX", 
                      "LITERAL_INT_OCT", "LITERAL_INT_BIN", "LITERAL_FLOAT", 
                      "LITERAL_STRING", "DOUBLE_QUOTE", "VAL", "VAR", "STATIC", 
                      "BREAK", "FOREACH", "INT", "NULL", "CONSTRUCTOR", 
                      "CONTINUE", "TRUE", "FLOAT", "CLASS", "DESTRUCTOR", 
                      "IF", "FALSE", "BOOLEAN", "NEW", "ELSEIF", "ARRAY", 
                      "STRING", "BY", "ELSE", "IN", "RETURN", "LB", "RB", 
                      "LS", "RS", "LP", "RP", "SEMI", "COMMA", "DOTDOT", 
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
    RULE_normal_method = 5
    RULE_constructor = 6
    RULE_destructor = 7
    RULE_params_list = 8
    RULE_params = 9
    RULE_data_type = 10
    RULE_class_types = 11
    RULE_stmt = 12
    RULE_var_decl = 13
    RULE_decl_tail = 14
    RULE_array_decl_tail = 15
    RULE_object_decl = 16
    RULE_expr_tail = 17
    RULE_array_type = 18
    RULE_array_type_tail = 19
    RULE_assign_stmt = 20
    RULE_assign_lhs = 21
    RULE_if_stmt = 22
    RULE_if_body = 23
    RULE_else_if_body = 24
    RULE_for_in_stmt = 25
    RULE_for_in_body = 26
    RULE_for_in_expr = 27
    RULE_break_stmt = 28
    RULE_continue_stmt = 29
    RULE_return_stmt = 30
    RULE_method_invoc = 31
    RULE_expr_list = 32
    RULE_block_stmt = 33
    RULE_literal_idx_array = 34
    RULE_literal_mtd_array = 35
    RULE_array_element = 36
    RULE_expr = 37
    RULE_expr1 = 38
    RULE_expr2 = 39
    RULE_expr3 = 40
    RULE_expr4 = 41
    RULE_expr5 = 42
    RULE_expr6 = 43
    RULE_expr7 = 44
    RULE_expr8 = 45
    RULE_expr9 = 46
    RULE_operands = 47
    RULE_arithmetic_ops = 48
    RULE_boolean_ops = 49
    RULE_string_ops = 50
    RULE_relational_ops = 51
    RULE_element_expr = 52
    RULE_index_ops = 53
    RULE_instance_attr = 54
    RULE_static_attr = 55
    RULE_instance_method = 56
    RULE_static_method = 57
    RULE_object_create = 58
    RULE_list_of_expr = 59

    ruleNames =  [ "program", "class_decl", "class_body", "class_attr", 
                   "class_method", "normal_method", "constructor", "destructor", 
                   "params_list", "params", "data_type", "class_types", 
                   "stmt", "var_decl", "decl_tail", "array_decl_tail", "object_decl", 
                   "expr_tail", "array_type", "array_type_tail", "assign_stmt", 
                   "assign_lhs", "if_stmt", "if_body", "else_if_body", "for_in_stmt", 
                   "for_in_body", "for_in_expr", "break_stmt", "continue_stmt", 
                   "return_stmt", "method_invoc", "expr_list", "block_stmt", 
                   "literal_idx_array", "literal_mtd_array", "array_element", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "expr8", "expr9", "operands", "arithmetic_ops", 
                   "boolean_ops", "string_ops", "relational_ops", "element_expr", 
                   "index_ops", "instance_attr", "static_attr", "instance_method", 
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
    DOUBLE_SEMI=60
    COLON=61
    ID=62
    WS=63
    BLOCK_COMMENT=64
    ERROR_CHAR=65
    UNCLOSE_STRING=66
    ILLEGAL_ESCAPE=67

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
            self.state = 121 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 120
                self.class_decl()
                self.state = 123 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 125
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
            self.state = 127
            self.match(D96Parser.CLASS)
            self.state = 128
            self.match(D96Parser.ID)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 129
                self.match(D96Parser.COLON)
                self.state = 130
                self.match(D96Parser.ID)


            self.state = 133
            self.match(D96Parser.LP)
            self.state = 134
            self.class_body()
            self.state = 135
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
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.STATIC) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID))) != 0):
                self.state = 139
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 137
                    self.class_attr()
                    pass
                elif token in [D96Parser.STATIC, D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID]:
                    self.state = 138
                    self.class_method()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 143
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

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

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

        def getRuleIndex(self):
            return D96Parser.RULE_class_attr




    def class_attr(self):

        localctx = D96Parser.Class_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_attr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 145
            self.match(D96Parser.ID)
            self.state = 146
            self.match(D96Parser.COLON)
            self.state = 147
            self.data_type()
            self.state = 148
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
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.STATIC, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.normal_method()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 152
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

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def params_list(self):
            return self.getTypedRuleContext(D96Parser.Params_listContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_normal_method




    def normal_method(self):

        localctx = D96Parser.Normal_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_normal_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.STATIC:
                self.state = 155
                self.match(D96Parser.STATIC)


            self.state = 158
            self.match(D96Parser.ID)
            self.state = 159
            self.match(D96Parser.LB)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 160
                self.params_list()


            self.state = 163
            self.match(D96Parser.RB)
            self.state = 164
            self.match(D96Parser.LP)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 165
                self.block_stmt()


            self.state = 168
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
        self.enterRule(localctx, 12, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 171
            self.match(D96Parser.LB)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 172
                self.params_list()


            self.state = 175
            self.match(D96Parser.RB)
            self.state = 176
            self.match(D96Parser.LP)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 177
                self.block_stmt()


            self.state = 180
            self.match(D96Parser.RP)
            print("text")
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
        self.enterRule(localctx, 14, self.RULE_destructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(D96Parser.DESTRUCTOR)
            self.state = 184
            self.match(D96Parser.LB)
            self.state = 185
            self.match(D96Parser.RB)
            self.state = 186
            self.match(D96Parser.LP)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 187
                self.block_stmt()


            self.state = 190
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
        self.enterRule(localctx, 16, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.params()
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 193
                self.match(D96Parser.SEMI)
                self.state = 194
                self.params()
                self.state = 199
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
        self.enterRule(localctx, 18, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(D96Parser.ID)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 201
                self.match(D96Parser.COMMA)
                self.state = 202
                self.match(D96Parser.ID)
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 208
            self.match(D96Parser.COLON)
            self.state = 209
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

        def getRuleIndex(self):
            return D96Parser.RULE_data_type




    def data_type(self):

        localctx = D96Parser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
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


    class Class_typesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_types




    def class_types(self):

        localctx = D96Parser.Class_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_class_types)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(D96Parser.ID)
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


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 215
                self.var_decl()
                pass

            elif la_ == 2:
                self.state = 216
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.state = 217
                self.if_stmt()
                pass

            elif la_ == 4:
                self.state = 218
                self.for_in_stmt()
                pass

            elif la_ == 5:
                self.state = 219
                self.break_stmt()
                pass

            elif la_ == 6:
                self.state = 220
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.state = 221
                self.return_stmt()
                pass

            elif la_ == 8:
                self.state = 222
                self.method_invoc()
                pass

            elif la_ == 9:
                self.state = 223
                self.match(D96Parser.LP)
                self.state = 224
                self.block_stmt()
                self.state = 225
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Decl_tailContext,0)


        def array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Array_decl_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_decl




    def var_decl(self):

        localctx = D96Parser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 230
                self.decl_tail()
                pass

            elif la_ == 2:
                self.state = 231
                self.array_decl_tail()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_tailContext(ParserRuleContext):

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

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def expr_tail(self):
            return self.getTypedRuleContext(D96Parser.Expr_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_decl_tail




    def decl_tail(self):

        localctx = D96Parser.Decl_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_decl_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 234
                    self.match(D96Parser.ID)
                    self.state = 235
                    self.match(D96Parser.COMMA) 
                self.state = 240
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 241
            self.match(D96Parser.ID)
            self.state = 242
            self.match(D96Parser.COLON)

            self.state = 243
            self.data_type()
            self.state = 244
            self.match(D96Parser.ASSIGN)
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 245
                self.expr_tail()


            self.state = 248
            self.match(D96Parser.SEMI)
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_array_decl_tail




    def array_decl_tail(self):

        localctx = D96Parser.Array_decl_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_array_decl_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 250
                    self.match(D96Parser.ID)
                    self.state = 251
                    self.match(D96Parser.COMMA) 
                self.state = 256
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 257
            self.match(D96Parser.ID)
            self.state = 258
            self.match(D96Parser.COLON)

            self.state = 259
            self.array_type()
            self.state = 260
            self.match(D96Parser.SEMI)
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
        self.enterRule(localctx, 32, self.RULE_object_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(D96Parser.NEW)
            self.state = 263
            self.match(D96Parser.ID)
            self.state = 264
            self.match(D96Parser.LB)
            self.state = 265
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_tail




    def expr_tail(self):

        localctx = D96Parser.Expr_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 267
                    self.expr()
                    self.state = 268
                    self.match(D96Parser.COMMA) 
                self.state = 274
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

            self.state = 275
            self.expr()
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
        self.enterRule(localctx, 36, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 277
                    self.array_type_tail()
                    self.state = 278
                    self.match(D96Parser.COMMA) 
                self.state = 284
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 285
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
        self.enterRule(localctx, 38, self.RULE_array_type_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(D96Parser.ARRAY)
            self.state = 288
            self.match(D96Parser.LS)
            self.state = 289
            self.data_type()
            self.state = 290
            self.match(D96Parser.COMMA)
            self.state = 291
            self.match(D96Parser.LITERAL_INT_DEC)
            self.state = 292
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

        def assign_lhs(self):
            return self.getTypedRuleContext(D96Parser.Assign_lhsContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.assign_lhs()
            self.state = 295
            self.match(D96Parser.ASSIGN)
            self.state = 296
            self.expr()
            self.state = 297
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

        def element_expr(self):
            return self.getTypedRuleContext(D96Parser.Element_exprContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_lhs




    def assign_lhs(self):

        localctx = D96Parser.Assign_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assign_lhs)
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.element_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.match(D96Parser.ID)
                pass


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
        self.enterRule(localctx, 44, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.if_body()
            self.state = 304
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

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


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
        self.enterRule(localctx, 46, self.RULE_if_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(D96Parser.IF)
            self.state = 307
            self.expr()
            self.state = 308
            self.else_if_body()
            self.state = 309
            self.match(D96Parser.ELSE)
            self.state = 310
            self.match(D96Parser.LP)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 311
                self.block_stmt()


            self.state = 314
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


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
        self.enterRule(localctx, 48, self.RULE_else_if_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 316
                self.match(D96Parser.ELSEIF)
                self.state = 317
                self.expr()
                self.state = 318
                self.match(D96Parser.LP)
                self.state = 320
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                    self.state = 319
                    self.block_stmt()


                self.state = 322
                self.match(D96Parser.RP)
                self.state = 328
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
        self.enterRule(localctx, 50, self.RULE_for_in_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(D96Parser.FOREACH)
            self.state = 330
            self.for_in_body()
            self.state = 331
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
        self.enterRule(localctx, 52, self.RULE_for_in_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(D96Parser.LB)
            self.state = 334
            self.match(D96Parser.ID)
            self.state = 335
            self.match(D96Parser.IN)
            self.state = 336
            self.for_in_expr()
            self.state = 337
            self.match(D96Parser.DOTDOT)
            self.state = 338
            self.for_in_expr()
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 339
                self.match(D96Parser.BY)
                self.state = 340
                self.for_in_expr()


            self.state = 343
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
        self.enterRule(localctx, 54, self.RULE_for_in_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
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
        self.enterRule(localctx, 56, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(D96Parser.BREAK)
            self.state = 348
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
        self.enterRule(localctx, 58, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(D96Parser.CONTINUE)
            self.state = 351
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

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_stmt




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(D96Parser.RETURN)
            self.state = 355
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 354
                self.expr()


            self.state = 357
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
        self.enterRule(localctx, 62, self.RULE_method_invoc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(D96Parser.ID)
            self.state = 360
            _la = self._input.LA(1)
            if not(_la==D96Parser.DOT or _la==D96Parser.DOUBLE_SEMI):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.STATIC:
                self.state = 361
                self.match(D96Parser.STATIC)


            self.state = 364
            self.match(D96Parser.ID)
            self.state = 365
            self.match(D96Parser.LB)
            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0):
                self.state = 366
                self.expr_list()


            self.state = 369
            self.match(D96Parser.RB)
            self.state = 370
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_list




    def expr_list(self):

        localctx = D96Parser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 372
                    self.expr()
                    self.state = 373
                    self.match(D96Parser.COMMA) 
                self.state = 379
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

            self.state = 380
            self.expr()
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
        self.enterRule(localctx, 66, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 382
                self.stmt()
                self.state = 385 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.BREAK) | (1 << D96Parser.FOREACH) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0)):
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
        self.enterRule(localctx, 68, self.RULE_literal_idx_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(D96Parser.ARRAY)
            self.state = 388
            self.match(D96Parser.LB)
            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.LITERAL:
                self.state = 389
                self.array_element()
                self.state = 391
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.COMMA:
                    self.state = 390
                    self.match(D96Parser.COMMA)


                self.state = 397
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 398
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
        self.enterRule(localctx, 70, self.RULE_literal_mtd_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(D96Parser.ARRAY)
            self.state = 401
            self.match(D96Parser.LB)
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ARRAY:
                self.state = 402
                self.literal_idx_array()
                self.state = 404
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.COMMA:
                    self.state = 403
                    self.match(D96Parser.COMMA)


                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 411
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
        self.enterRule(localctx, 72, self.RULE_array_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 413
                    self.match(D96Parser.LITERAL)
                    self.state = 415
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        self.state = 414
                        self.match(D96Parser.COMMA)



                else:
                    raise NoViableAltException(self)
                self.state = 419 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr1Context,i)


        def STRING_CONCAT(self):
            return self.getToken(D96Parser.STRING_CONCAT, 0)

        def EQUAL_STRING(self):
            return self.getToken(D96Parser.EQUAL_STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.expr1()
                self.state = 422
                _la = self._input.LA(1)
                if not(_la==D96Parser.EQUAL_STRING or _la==D96Parser.STRING_CONCAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 423
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr2Context,i)


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
            return D96Parser.RULE_expr1




    def expr1(self):

        localctx = D96Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.expr2(0)
                self.state = 429
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.LESS_THAN) | (1 << D96Parser.LEQ) | (1 << D96Parser.GREATER_THAN) | (1 << D96Parser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 430
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(D96Parser.Expr2Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 443
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 438
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 439
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 440
                    self.expr3(0) 
                self.state = 445
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUBTRACT(self):
            return self.getToken(D96Parser.SUBTRACT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 454
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 449
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 450
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUBTRACT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 451
                    self.expr4(0) 
                self.state = 456
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def MULTIPLY(self):
            return self.getToken(D96Parser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(D96Parser.DIVIDE, 0)

        def MODULO(self):
            return self.getToken(D96Parser.MODULO, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 465
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 460
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 461
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLY) | (1 << D96Parser.DIVIDE) | (1 << D96Parser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 462
                    self.expr5() 
                self.state = 467
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr5




    def expr5(self):

        localctx = D96Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr5)
        try:
            self.state = 471
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 468
                self.match(D96Parser.NOT)
                self.state = 469
                self.expr5()
                pass
            elif token in [D96Parser.LITERAL, D96Parser.NEW, D96Parser.LB, D96Parser.SUBTRACT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.expr6()
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


    class Expr6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBTRACT(self):
            return self.getToken(D96Parser.SUBTRACT, 0)

        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr6




    def expr6(self):

        localctx = D96Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr6)
        try:
            self.state = 476
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUBTRACT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.match(D96Parser.SUBTRACT)
                self.state = 474
                self.expr6()
                pass
            elif token in [D96Parser.LITERAL, D96Parser.NEW, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 475
                self.expr7()
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


    class Expr7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def index_ops(self):
            return self.getTypedRuleContext(D96Parser.Index_opsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr7




    def expr7(self):

        localctx = D96Parser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expr7)
        try:
            self.state = 482
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.expr8(0)
                self.state = 479
                self.index_ops()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 481
                self.expr8(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def DOUBLE_SEMI(self):
            return self.getToken(D96Parser.DOUBLE_SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr8



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expr8, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 492
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 487
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 488
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.DOT or _la==D96Parser.DOUBLE_SEMI):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 489
                    self.expr9() 
                self.state = 494
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def operands(self):
            return self.getTypedRuleContext(D96Parser.OperandsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr9




    def expr9(self):

        localctx = D96Parser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr9)
        try:
            self.state = 498
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.match(D96Parser.NEW)
                self.state = 496
                self.expr9()
                pass
            elif token in [D96Parser.LITERAL, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 497
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

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operands




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_operands)
        try:
            self.state = 506
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 500
                self.match(D96Parser.LITERAL)
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 501
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 502
                self.match(D96Parser.LB)
                self.state = 503
                self.expr()
                self.state = 504
                self.match(D96Parser.RB)
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
        self.enterRule(localctx, 96, self.RULE_arithmetic_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
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
        self.enterRule(localctx, 98, self.RULE_boolean_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
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
        self.enterRule(localctx, 100, self.RULE_string_ops)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
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
        self.enterRule(localctx, 102, self.RULE_relational_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
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

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def index_ops(self):
            return self.getTypedRuleContext(D96Parser.Index_opsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_element_expr




    def element_expr(self):

        localctx = D96Parser.Element_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_element_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.expr()
            self.state = 517
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

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def index_ops(self):
            return self.getTypedRuleContext(D96Parser.Index_opsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_ops




    def index_ops(self):

        localctx = D96Parser.Index_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_index_ops)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.match(D96Parser.LS)
            self.state = 520
            self.expr()
            self.state = 521
            self.match(D96Parser.RS)
            self.state = 523
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 522
                self.index_ops()


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

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_attr




    def instance_attr(self):

        localctx = D96Parser.Instance_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_instance_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            self.expr()
            self.state = 526
            self.match(D96Parser.DOT)
            self.state = 527
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
        self.enterRule(localctx, 110, self.RULE_static_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self.match(D96Parser.ID)
            self.state = 530
            self.match(D96Parser.DOUBLE_SEMI)
            self.state = 531
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

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_of_expr(self):
            return self.getTypedRuleContext(D96Parser.List_of_exprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_method




    def instance_method(self):

        localctx = D96Parser.Instance_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_instance_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.expr()
            self.state = 534
            self.match(D96Parser.DOT)
            self.state = 535
            self.match(D96Parser.ID)
            self.state = 536
            self.match(D96Parser.LB)
            self.state = 537
            self.list_of_expr()
            self.state = 538
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

        def list_of_expr(self):
            return self.getTypedRuleContext(D96Parser.List_of_exprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_method




    def static_method(self):

        localctx = D96Parser.Static_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_static_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.match(D96Parser.ID)
            self.state = 541
            self.match(D96Parser.DOUBLE_SEMI)
            self.state = 542
            self.match(D96Parser.ID)
            self.state = 543
            self.match(D96Parser.LB)
            self.state = 544
            self.list_of_expr()
            self.state = 545
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

        def list_of_expr(self):
            return self.getTypedRuleContext(D96Parser.List_of_exprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_object_create




    def object_create(self):

        localctx = D96Parser.Object_createContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_object_create)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.match(D96Parser.NEW)
            self.state = 548
            self.match(D96Parser.ID)
            self.state = 549
            self.match(D96Parser.LB)
            self.state = 550
            self.list_of_expr()
            self.state = 551
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_list_of_expr




    def list_of_expr(self):

        localctx = D96Parser.List_of_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_list_of_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 553
                self.expr()
                self.state = 555
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.COMMA:
                    self.state = 554
                    self.match(D96Parser.COMMA)


                self.state = 559 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT) | (1 << D96Parser.ID))) != 0)):
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
        self._predicates[39] = self.expr2_sempred
        self._predicates[40] = self.expr3_sempred
        self._predicates[41] = self.expr4_sempred
        self._predicates[45] = self.expr8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




