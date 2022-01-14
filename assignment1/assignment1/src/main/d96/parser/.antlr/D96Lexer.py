# Generated from d:\HCMUT\Semester 212\Principles of Programming Languages\HK212_CO3005_PPL\assignment1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *
id = 1953097



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2H")
        buf.write("\u01e7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\6\b\u00a7\n\b\r\b\16\b\u00a8\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\7\t\u00b1\n\t\f\t\16\t\u00b4\13\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\n\6\n\u00bc\n\n\r\n\16\n\u00bd\3\13\6\13")
        buf.write("\u00c1\n\13\r\13\16\13\u00c2\3\f\3\f\3\f\3\f\7\f\u00c9")
        buf.write("\n\f\f\f\16\f\u00cc\13\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3")
        buf.write("(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3-\3.\3.\3/\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38")
        buf.write("\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\6=\u0196\n=\r=\16=\u0197")
        buf.write("\3=\3=\3>\3>\3>\3>\5>\u01a0\n>\3>\6>\u01a3\n>\r>\16>\u01a4")
        buf.write("\3>\3>\3?\3?\3?\3@\3@\3@\3@\5@\u01b0\n@\3@\6@\u01b3\n")
        buf.write("@\r@\16@\u01b4\3A\3A\3A\7A\u01ba\nA\fA\16A\u01bd\13A\3")
        buf.write("A\3A\3B\3B\3B\3B\3B\3B\3B\3B\3B\3C\3C\3C\3C\3C\3C\3C\3")
        buf.write("C\3C\5C\u01d3\nC\7C\u01d5\nC\fC\16C\u01d8\13C\3C\3C\3")
        buf.write("D\3D\3D\3E\3E\3E\3F\3F\3F\3G\3G\3G\3\u00b2\2H\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}")
        buf.write("@\177A\u0081B\u0083C\u0085D\u0087E\u0089F\u008bG\u008d")
        buf.write("H\3\2\n\5\2\n\f\16\17\"\"\5\2C\\aac|\3\2\62;\3\2\63;\4")
        buf.write("\2\62;aa\5\2\63;CHaa\3\2\62\63\3\2$$\2\u01f4\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2")
        buf.write("\u008b\3\2\2\2\2\u008d\3\2\2\2\3\u008f\3\2\2\2\5\u0094")
        buf.write("\3\2\2\2\7\u0096\3\2\2\2\t\u0098\3\2\2\2\13\u009c\3\2")
        buf.write("\2\2\r\u00a0\3\2\2\2\17\u00a6\3\2\2\2\21\u00ac\3\2\2\2")
        buf.write("\23\u00bb\3\2\2\2\25\u00c0\3\2\2\2\27\u00c4\3\2\2\2\31")
        buf.write("\u00cd\3\2\2\2\33\u00d3\3\2\2\2\35\u00db\3\2\2\2\37\u00df")
        buf.write("\3\2\2\2!\u00e4\3\2\2\2#\u00f0\3\2\2\2%\u00f9\3\2\2\2")
        buf.write("\'\u00fe\3\2\2\2)\u0104\3\2\2\2+\u010a\3\2\2\2-\u0115")
        buf.write("\3\2\2\2/\u0118\3\2\2\2\61\u011e\3\2\2\2\63\u0126\3\2")
        buf.write("\2\2\65\u012a\3\2\2\2\67\u012e\3\2\2\29\u0135\3\2\2\2")
        buf.write(";\u013b\3\2\2\2=\u0142\3\2\2\2?\u0146\3\2\2\2A\u0149\3")
        buf.write("\2\2\2C\u014e\3\2\2\2E\u0151\3\2\2\2G\u0158\3\2\2\2I\u015a")
        buf.write("\3\2\2\2K\u015c\3\2\2\2M\u015e\3\2\2\2O\u0160\3\2\2\2")
        buf.write("Q\u0162\3\2\2\2S\u0165\3\2\2\2U\u0168\3\2\2\2W\u016b\3")
        buf.write("\2\2\2Y\u016d\3\2\2\2[\u0170\3\2\2\2]\u0172\3\2\2\2_\u0175")
        buf.write("\3\2\2\2a\u0177\3\2\2\2c\u017a\3\2\2\2e\u017e\3\2\2\2")
        buf.write("g\u0180\3\2\2\2i\u0183\3\2\2\2k\u0185\3\2\2\2m\u0187\3")
        buf.write("\2\2\2o\u0189\3\2\2\2q\u018b\3\2\2\2s\u018d\3\2\2\2u\u018f")
        buf.write("\3\2\2\2w\u0191\3\2\2\2y\u0193\3\2\2\2{\u019f\3\2\2\2")
        buf.write("}\u01a8\3\2\2\2\177\u01af\3\2\2\2\u0081\u01b6\3\2\2\2")
        buf.write("\u0083\u01c0\3\2\2\2\u0085\u01c9\3\2\2\2\u0087\u01db\3")
        buf.write("\2\2\2\u0089\u01de\3\2\2\2\u008b\u01e1\3\2\2\2\u008d\u01e4")
        buf.write("\3\2\2\2\u008f\u0090\7o\2\2\u0090\u0091\7c\2\2\u0091\u0092")
        buf.write("\7k\2\2\u0092\u0093\7p\2\2\u0093\4\3\2\2\2\u0094\u0095")
        buf.write("\7<\2\2\u0095\6\3\2\2\2\u0096\u0097\7&\2\2\u0097\b\3\2")
        buf.write("\2\2\u0098\u0099\7y\2\2\u0099\u009a\7v\2\2\u009a\u009b")
        buf.write("\7h\2\2\u009b\n\3\2\2\2\u009c\u009d\7k\2\2\u009d\u009e")
        buf.write("\7p\2\2\u009e\u009f\7v\2\2\u009f\f\3\2\2\2\u00a0\u00a1")
        buf.write("\7x\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3\7k\2\2\u00a3\u00a4")
        buf.write("\7f\2\2\u00a4\16\3\2\2\2\u00a5\u00a7\t\2\2\2\u00a6\u00a5")
        buf.write("\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8")
        buf.write("\u00a9\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\b\b\2\2")
        buf.write("\u00ab\20\3\2\2\2\u00ac\u00ad\7%\2\2\u00ad\u00ae\7%\2")
        buf.write("\2\u00ae\u00b2\3\2\2\2\u00af\u00b1\13\2\2\2\u00b0\u00af")
        buf.write("\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b2")
        buf.write("\u00b0\3\2\2\2\u00b3\u00b5\3\2\2\2\u00b4\u00b2\3\2\2\2")
        buf.write("\u00b5\u00b6\7%\2\2\u00b6\u00b7\7%\2\2\u00b7\u00b8\3\2")
        buf.write("\2\2\u00b8\u00b9\b\t\2\2\u00b9\22\3\2\2\2\u00ba\u00bc")
        buf.write("\t\3\2\2\u00bb\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write("\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\24\3\2\2\2\u00bf")
        buf.write("\u00c1\t\4\2\2\u00c0\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2")
        buf.write("\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\26\3\2")
        buf.write("\2\2\u00c4\u00ca\5\23\n\2\u00c5\u00c6\5\23\n\2\u00c6\u00c7")
        buf.write("\t\4\2\2\u00c7\u00c9\3\2\2\2\u00c8\u00c5\3\2\2\2\u00c9")
        buf.write("\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2")
        buf.write("\u00cb\30\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00ce\7D\2")
        buf.write("\2\u00ce\u00cf\7t\2\2\u00cf\u00d0\7g\2\2\u00d0\u00d1\7")
        buf.write("c\2\2\u00d1\u00d2\7m\2\2\u00d2\32\3\2\2\2\u00d3\u00d4")
        buf.write("\7H\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6\7t\2\2\u00d6\u00d7")
        buf.write("\7g\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9\7e\2\2\u00d9\u00da")
        buf.write("\7j\2\2\u00da\34\3\2\2\2\u00db\u00dc\7K\2\2\u00dc\u00dd")
        buf.write("\7p\2\2\u00dd\u00de\7v\2\2\u00de\36\3\2\2\2\u00df\u00e0")
        buf.write("\7P\2\2\u00e0\u00e1\7w\2\2\u00e1\u00e2\7n\2\2\u00e2\u00e3")
        buf.write("\7n\2\2\u00e3 \3\2\2\2\u00e4\u00e5\7E\2\2\u00e5\u00e6")
        buf.write("\7q\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8\7u\2\2\u00e8\u00e9")
        buf.write("\7v\2\2\u00e9\u00ea\7t\2\2\u00ea\u00eb\7w\2\2\u00eb\u00ec")
        buf.write("\7e\2\2\u00ec\u00ed\7v\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef")
        buf.write("\7t\2\2\u00ef\"\3\2\2\2\u00f0\u00f1\7E\2\2\u00f1\u00f2")
        buf.write("\7q\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4\7v\2\2\u00f4\u00f5")
        buf.write("\7k\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7\7w\2\2\u00f7\u00f8")
        buf.write("\7g\2\2\u00f8$\3\2\2\2\u00f9\u00fa\7V\2\2\u00fa\u00fb")
        buf.write("\7t\2\2\u00fb\u00fc\7w\2\2\u00fc\u00fd\7g\2\2\u00fd&\3")
        buf.write("\2\2\2\u00fe\u00ff\7H\2\2\u00ff\u0100\7n\2\2\u0100\u0101")
        buf.write("\7q\2\2\u0101\u0102\7c\2\2\u0102\u0103\7v\2\2\u0103(\3")
        buf.write("\2\2\2\u0104\u0105\7E\2\2\u0105\u0106\7n\2\2\u0106\u0107")
        buf.write("\7c\2\2\u0107\u0108\7u\2\2\u0108\u0109\7u\2\2\u0109*\3")
        buf.write("\2\2\2\u010a\u010b\7F\2\2\u010b\u010c\7g\2\2\u010c\u010d")
        buf.write("\7u\2\2\u010d\u010e\7v\2\2\u010e\u010f\7t\2\2\u010f\u0110")
        buf.write("\7w\2\2\u0110\u0111\7e\2\2\u0111\u0112\7v\2\2\u0112\u0113")
        buf.write("\7q\2\2\u0113\u0114\7t\2\2\u0114,\3\2\2\2\u0115\u0116")
        buf.write("\7K\2\2\u0116\u0117\7h\2\2\u0117.\3\2\2\2\u0118\u0119")
        buf.write("\7H\2\2\u0119\u011a\7c\2\2\u011a\u011b\7n\2\2\u011b\u011c")
        buf.write("\7u\2\2\u011c\u011d\7g\2\2\u011d\60\3\2\2\2\u011e\u011f")
        buf.write("\7D\2\2\u011f\u0120\7q\2\2\u0120\u0121\7q\2\2\u0121\u0122")
        buf.write("\7n\2\2\u0122\u0123\7g\2\2\u0123\u0124\7c\2\2\u0124\u0125")
        buf.write("\7p\2\2\u0125\62\3\2\2\2\u0126\u0127\7X\2\2\u0127\u0128")
        buf.write("\7c\2\2\u0128\u0129\7n\2\2\u0129\64\3\2\2\2\u012a\u012b")
        buf.write("\7P\2\2\u012b\u012c\7g\2\2\u012c\u012d\7y\2\2\u012d\66")
        buf.write("\3\2\2\2\u012e\u012f\7G\2\2\u012f\u0130\7n\2\2\u0130\u0131")
        buf.write("\7u\2\2\u0131\u0132\7g\2\2\u0132\u0133\7k\2\2\u0133\u0134")
        buf.write("\7h\2\2\u01348\3\2\2\2\u0135\u0136\7C\2\2\u0136\u0137")
        buf.write("\7t\2\2\u0137\u0138\7t\2\2\u0138\u0139\7c\2\2\u0139\u013a")
        buf.write("\7{\2\2\u013a:\3\2\2\2\u013b\u013c\7U\2\2\u013c\u013d")
        buf.write("\7v\2\2\u013d\u013e\7t\2\2\u013e\u013f\7k\2\2\u013f\u0140")
        buf.write("\7p\2\2\u0140\u0141\7i\2\2\u0141<\3\2\2\2\u0142\u0143")
        buf.write("\7X\2\2\u0143\u0144\7c\2\2\u0144\u0145\7t\2\2\u0145>\3")
        buf.write("\2\2\2\u0146\u0147\7D\2\2\u0147\u0148\7{\2\2\u0148@\3")
        buf.write("\2\2\2\u0149\u014a\7G\2\2\u014a\u014b\7n\2\2\u014b\u014c")
        buf.write("\7u\2\2\u014c\u014d\7g\2\2\u014dB\3\2\2\2\u014e\u014f")
        buf.write("\7K\2\2\u014f\u0150\7p\2\2\u0150D\3\2\2\2\u0151\u0152")
        buf.write("\7T\2\2\u0152\u0153\7g\2\2\u0153\u0154\7v\2\2\u0154\u0155")
        buf.write("\7w\2\2\u0155\u0156\7t\2\2\u0156\u0157\7p\2\2\u0157F\3")
        buf.write("\2\2\2\u0158\u0159\7-\2\2\u0159H\3\2\2\2\u015a\u015b\7")
        buf.write("/\2\2\u015bJ\3\2\2\2\u015c\u015d\7\61\2\2\u015dL\3\2\2")
        buf.write("\2\u015e\u015f\7\'\2\2\u015fN\3\2\2\2\u0160\u0161\7#\2")
        buf.write("\2\u0161P\3\2\2\2\u0162\u0163\7(\2\2\u0163\u0164\7(\2")
        buf.write("\2\u0164R\3\2\2\2\u0165\u0166\7~\2\2\u0166\u0167\7~\2")
        buf.write("\2\u0167T\3\2\2\2\u0168\u0169\7?\2\2\u0169\u016a\7?\2")
        buf.write("\2\u016aV\3\2\2\2\u016b\u016c\7?\2\2\u016cX\3\2\2\2\u016d")
        buf.write("\u016e\7#\2\2\u016e\u016f\7?\2\2\u016fZ\3\2\2\2\u0170")
        buf.write("\u0171\7>\2\2\u0171\\\3\2\2\2\u0172\u0173\7>\2\2\u0173")
        buf.write("\u0174\7?\2\2\u0174^\3\2\2\2\u0175\u0176\7@\2\2\u0176")
        buf.write("`\3\2\2\2\u0177\u0178\7@\2\2\u0178\u0179\7?\2\2\u0179")
        buf.write("b\3\2\2\2\u017a\u017b\7?\2\2\u017b\u017c\7?\2\2\u017c")
        buf.write("\u017d\7\60\2\2\u017dd\3\2\2\2\u017e\u017f\7\60\2\2\u017f")
        buf.write("f\3\2\2\2\u0180\u0181\7<\2\2\u0181\u0182\7<\2\2\u0182")
        buf.write("h\3\2\2\2\u0183\u0184\7*\2\2\u0184j\3\2\2\2\u0185\u0186")
        buf.write("\7+\2\2\u0186l\3\2\2\2\u0187\u0188\7]\2\2\u0188n\3\2\2")
        buf.write("\2\u0189\u018a\7_\2\2\u018ap\3\2\2\2\u018b\u018c\7}\2")
        buf.write("\2\u018cr\3\2\2\2\u018d\u018e\7\177\2\2\u018et\3\2\2\2")
        buf.write("\u018f\u0190\7=\2\2\u0190v\3\2\2\2\u0191\u0192\7.\2\2")
        buf.write("\u0192x\3\2\2\2\u0193\u0195\t\5\2\2\u0194\u0196\t\6\2")
        buf.write("\2\u0195\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0195")
        buf.write("\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0199\3\2\2\2\u0199")
        buf.write("\u019a\b=\3\2\u019az\3\2\2\2\u019b\u019c\7\62\2\2\u019c")
        buf.write("\u01a0\7z\2\2\u019d\u019e\7\62\2\2\u019e\u01a0\7Z\2\2")
        buf.write("\u019f\u019b\3\2\2\2\u019f\u019d\3\2\2\2\u01a0\u01a2\3")
        buf.write("\2\2\2\u01a1\u01a3\t\7\2\2\u01a2\u01a1\3\2\2\2\u01a3\u01a4")
        buf.write("\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5")
        buf.write("\u01a6\3\2\2\2\u01a6\u01a7\b>\4\2\u01a7|\3\2\2\2\u01a8")
        buf.write("\u01a9\7\62\2\2\u01a9\u01aa\5y=\2\u01aa~\3\2\2\2\u01ab")
        buf.write("\u01ac\7\62\2\2\u01ac\u01b0\7d\2\2\u01ad\u01ae\7\62\2")
        buf.write("\2\u01ae\u01b0\7D\2\2\u01af\u01ab\3\2\2\2\u01af\u01ad")
        buf.write("\3\2\2\2\u01b0\u01b2\3\2\2\2\u01b1\u01b3\t\b\2\2\u01b2")
        buf.write("\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b2\3\2\2\2")
        buf.write("\u01b4\u01b5\3\2\2\2\u01b5\u0080\3\2\2\2\u01b6\u01bb\t")
        buf.write("\t\2\2\u01b7\u01ba\5\23\n\2\u01b8\u01ba\5\25\13\2\u01b9")
        buf.write("\u01b7\3\2\2\2\u01b9\u01b8\3\2\2\2\u01ba\u01bd\3\2\2\2")
        buf.write("\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01be\3")
        buf.write("\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u01bf\t\t\2\2\u01bf\u0082")
        buf.write("\3\2\2\2\u01c0\u01c1\7C\2\2\u01c1\u01c2\7t\2\2\u01c2\u01c3")
        buf.write("\7t\2\2\u01c3\u01c4\7c\2\2\u01c4\u01c5\7{\2\2\u01c5\u01c6")
        buf.write("\3\2\2\2\u01c6\u01c7\5i\65\2\u01c7\u01c8\5k\66\2\u01c8")
        buf.write("\u0084\3\2\2\2\u01c9\u01ca\7C\2\2\u01ca\u01cb\7t\2\2\u01cb")
        buf.write("\u01cc\7t\2\2\u01cc\u01cd\7c\2\2\u01cd\u01ce\7{\2\2\u01ce")
        buf.write("\u01cf\3\2\2\2\u01cf\u01d6\5i\65\2\u01d0\u01d2\5\u0083")
        buf.write("B\2\u01d1\u01d3\5w<\2\u01d2\u01d1\3\2\2\2\u01d2\u01d3")
        buf.write("\3\2\2\2\u01d3\u01d5\3\2\2\2\u01d4\u01d0\3\2\2\2\u01d5")
        buf.write("\u01d8\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2")
        buf.write("\u01d7\u01d9\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9\u01da\5")
        buf.write("k\66\2\u01da\u0086\3\2\2\2\u01db\u01dc\7)\2\2\u01dc\u01dd")
        buf.write("\7$\2\2\u01dd\u0088\3\2\2\2\u01de\u01df\13\2\2\2\u01df")
        buf.write("\u01e0\bE\5\2\u01e0\u008a\3\2\2\2\u01e1\u01e2\13\2\2\2")
        buf.write("\u01e2\u01e3\bF\6\2\u01e3\u008c\3\2\2\2\u01e4\u01e5\13")
        buf.write("\2\2\2\u01e5\u01e6\bG\7\2\u01e6\u008e\3\2\2\2\21\2\u00a8")
        buf.write("\u00b2\u00bd\u00c2\u00ca\u0197\u019f\u01a4\u01af\u01b4")
        buf.write("\u01b9\u01bb\u01d2\u01d6\b\b\2\2\3=\2\3>\3\3E\4\3F\5\3")
        buf.write("G\6")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    INTTYPE = 5
    VOIDTYPE = 6
    WS = 7
    BLOCK_COMMENT = 8
    ALPHABET = 9
    INTLIT = 10
    ID = 11
    BREAK = 12
    FOREACH = 13
    INT = 14
    NULL = 15
    CONSTRUCTOR = 16
    CONTINUE = 17
    TRUE = 18
    FLOAT = 19
    CLASS = 20
    DESTRUCTOR = 21
    IF = 22
    FALSE = 23
    BOOLEAN = 24
    VAL = 25
    NEW = 26
    ELSEIF = 27
    ARRAY = 28
    STRING = 29
    VAR = 30
    BY = 31
    ELSE = 32
    IN = 33
    RETURN = 34
    ADD = 35
    SUBTRACT = 36
    MULTIPLY = 37
    MODULO = 38
    NOT = 39
    AND = 40
    OR = 41
    EQUAL = 42
    ASSIGN = 43
    NOT_EQUAL = 44
    LESS_THAN = 45
    LEQ = 46
    GREATER_THAN = 47
    GEQ = 48
    EQUAL_WHAT = 49
    DOT = 50
    SUPER_CLASS = 51
    LB = 52
    RB = 53
    LS = 54
    RS = 55
    LP = 56
    RP = 57
    SEMI = 58
    COMMA = 59
    LITERAL_INT_DEC = 60
    LITERAL_INT_HEX = 61
    LITERAL_INT_OCT = 62
    LITERAL_INT_BIN = 63
    LITERAL_STRING = 64
    LITERAL_IDX_ARRAY = 65
    LITERAL_MTD_ARRAY = 66
    DOUBLE_QUOTE = 67
    ERROR_CHAR = 68
    UNCLOSE_STRING = 69
    ILLEGAL_ESCAPE = 70

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "':'", "'$'", "'wtf'", "'int'", "'void'", "'Break'", 
            "'Foreach'", "'Int'", "'Null'", "'Constructor'", "'Continue'", 
            "'True'", "'Float'", "'Class'", "'Destructor'", "'If'", "'False'", 
            "'Boolean'", "'Val'", "'New'", "'Elseif'", "'Array'", "'String'", 
            "'Var'", "'By'", "'Else'", "'In'", "'Return'", "'+'", "'-'", 
            "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'==.'", "'.'", "'::'", "'('", 
            "')'", "'['", "']'", "'{'", "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "WS", "BLOCK_COMMENT", "ALPHABET", "INTLIT", 
            "ID", "BREAK", "FOREACH", "INT", "NULL", "CONSTRUCTOR", "CONTINUE", 
            "TRUE", "FLOAT", "CLASS", "DESTRUCTOR", "IF", "FALSE", "BOOLEAN", 
            "VAL", "NEW", "ELSEIF", "ARRAY", "STRING", "VAR", "BY", "ELSE", 
            "IN", "RETURN", "ADD", "SUBTRACT", "MULTIPLY", "MODULO", "NOT", 
            "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", "LESS_THAN", "LEQ", 
            "GREATER_THAN", "GEQ", "EQUAL_WHAT", "DOT", "SUPER_CLASS", "LB", 
            "RB", "LS", "RS", "LP", "RP", "SEMI", "COMMA", "LITERAL_INT_DEC", 
            "LITERAL_INT_HEX", "LITERAL_INT_OCT", "LITERAL_INT_BIN", "LITERAL_STRING", 
            "LITERAL_IDX_ARRAY", "LITERAL_MTD_ARRAY", "DOUBLE_QUOTE", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "INTTYPE", "VOIDTYPE", 
                  "WS", "BLOCK_COMMENT", "ALPHABET", "INTLIT", "ID", "BREAK", 
                  "FOREACH", "INT", "NULL", "CONSTRUCTOR", "CONTINUE", "TRUE", 
                  "FLOAT", "CLASS", "DESTRUCTOR", "IF", "FALSE", "BOOLEAN", 
                  "VAL", "NEW", "ELSEIF", "ARRAY", "STRING", "VAR", "BY", 
                  "ELSE", "IN", "RETURN", "ADD", "SUBTRACT", "MULTIPLY", 
                  "MODULO", "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", 
                  "LESS_THAN", "LEQ", "GREATER_THAN", "GEQ", "EQUAL_WHAT", 
                  "DOT", "SUPER_CLASS", "LB", "RB", "LS", "RS", "LP", "RP", 
                  "SEMI", "COMMA", "LITERAL_INT_DEC", "LITERAL_INT_HEX", 
                  "LITERAL_INT_OCT", "LITERAL_INT_BIN", "LITERAL_STRING", 
                  "LITERAL_IDX_ARRAY", "LITERAL_MTD_ARRAY", "DOUBLE_QUOTE", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[59] = self.LITERAL_INT_DEC_action 
            actions[60] = self.LITERAL_INT_HEX_action 
            actions[67] = self.ERROR_CHAR_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def LITERAL_INT_DEC_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def LITERAL_INT_HEX_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     


