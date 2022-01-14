# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *
id = 1953097



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2H")
        buf.write("\u01e6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\t\3\t\3\t\3\n\6\n\u00bc\n\n\r\n\16\n\u00bd\3\13\3\13")
        buf.write("\3\13\3\13\7\13\u00c4\n\13\f\13\16\13\u00c7\13\13\3\f")
        buf.write("\6\f\u00ca\n\f\r\f\16\f\u00cb\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3\"")
        buf.write("\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3")
        buf.write("\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3-\3.")
        buf.write("\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3")
        buf.write("\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\6=\u0196\n=")
        buf.write("\r=\16=\u0197\3=\3=\3>\3>\3>\3>\5>\u01a0\n>\3>\6>\u01a3")
        buf.write("\n>\r>\16>\u01a4\3>\3>\3?\3?\3?\3@\3@\3@\3@\5@\u01b0\n")
        buf.write("@\3@\6@\u01b3\n@\r@\16@\u01b4\3A\3A\7A\u01b9\nA\fA\16")
        buf.write("A\u01bc\13A\3A\3A\3B\3B\3B\3B\3B\3B\3B\3B\3B\3C\3C\3C")
        buf.write("\3C\3C\3C\3C\3C\3C\5C\u01d2\nC\7C\u01d4\nC\fC\16C\u01d7")
        buf.write("\13C\3C\3C\3D\3D\3D\3E\3E\3E\3F\3F\3F\3G\3G\3G\3\u00b2")
        buf.write("\2H\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F")
        buf.write("\u008bG\u008dH\3\2\13\5\2\n\f\16\17\"\"\5\2C\\aac|\3\2")
        buf.write("\62;\3\2\63;\4\2\62;aa\5\2\63;CHaa\3\2\62\63\3\2$$\5\2")
        buf.write("\62;C\\c|\2\u01f2\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\3\u008f\3\2\2\2\5\u0094\3\2\2\2\7\u0096\3\2\2\2\t\u0098")
        buf.write("\3\2\2\2\13\u009c\3\2\2\2\r\u00a0\3\2\2\2\17\u00a6\3\2")
        buf.write("\2\2\21\u00ac\3\2\2\2\23\u00bb\3\2\2\2\25\u00bf\3\2\2")
        buf.write("\2\27\u00c9\3\2\2\2\31\u00cd\3\2\2\2\33\u00d3\3\2\2\2")
        buf.write("\35\u00db\3\2\2\2\37\u00df\3\2\2\2!\u00e4\3\2\2\2#\u00f0")
        buf.write("\3\2\2\2%\u00f9\3\2\2\2\'\u00fe\3\2\2\2)\u0104\3\2\2\2")
        buf.write("+\u010a\3\2\2\2-\u0115\3\2\2\2/\u0118\3\2\2\2\61\u011e")
        buf.write("\3\2\2\2\63\u0126\3\2\2\2\65\u012a\3\2\2\2\67\u012e\3")
        buf.write("\2\2\29\u0135\3\2\2\2;\u013b\3\2\2\2=\u0142\3\2\2\2?\u0146")
        buf.write("\3\2\2\2A\u0149\3\2\2\2C\u014e\3\2\2\2E\u0151\3\2\2\2")
        buf.write("G\u0158\3\2\2\2I\u015a\3\2\2\2K\u015c\3\2\2\2M\u015e\3")
        buf.write("\2\2\2O\u0160\3\2\2\2Q\u0162\3\2\2\2S\u0165\3\2\2\2U\u0168")
        buf.write("\3\2\2\2W\u016b\3\2\2\2Y\u016d\3\2\2\2[\u0170\3\2\2\2")
        buf.write("]\u0172\3\2\2\2_\u0175\3\2\2\2a\u0177\3\2\2\2c\u017a\3")
        buf.write("\2\2\2e\u017e\3\2\2\2g\u0180\3\2\2\2i\u0183\3\2\2\2k\u0185")
        buf.write("\3\2\2\2m\u0187\3\2\2\2o\u0189\3\2\2\2q\u018b\3\2\2\2")
        buf.write("s\u018d\3\2\2\2u\u018f\3\2\2\2w\u0191\3\2\2\2y\u0193\3")
        buf.write("\2\2\2{\u019f\3\2\2\2}\u01a8\3\2\2\2\177\u01af\3\2\2\2")
        buf.write("\u0081\u01b6\3\2\2\2\u0083\u01bf\3\2\2\2\u0085\u01c8\3")
        buf.write("\2\2\2\u0087\u01da\3\2\2\2\u0089\u01dd\3\2\2\2\u008b\u01e0")
        buf.write("\3\2\2\2\u008d\u01e3\3\2\2\2\u008f\u0090\7o\2\2\u0090")
        buf.write("\u0091\7c\2\2\u0091\u0092\7k\2\2\u0092\u0093\7p\2\2\u0093")
        buf.write("\4\3\2\2\2\u0094\u0095\7<\2\2\u0095\6\3\2\2\2\u0096\u0097")
        buf.write("\7&\2\2\u0097\b\3\2\2\2\u0098\u0099\7y\2\2\u0099\u009a")
        buf.write("\7v\2\2\u009a\u009b\7h\2\2\u009b\n\3\2\2\2\u009c\u009d")
        buf.write("\7k\2\2\u009d\u009e\7p\2\2\u009e\u009f\7v\2\2\u009f\f")
        buf.write("\3\2\2\2\u00a0\u00a1\7x\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3")
        buf.write("\7k\2\2\u00a3\u00a4\7f\2\2\u00a4\16\3\2\2\2\u00a5\u00a7")
        buf.write("\t\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8")
        buf.write("\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\3\2\2\2")
        buf.write("\u00aa\u00ab\b\b\2\2\u00ab\20\3\2\2\2\u00ac\u00ad\7%\2")
        buf.write("\2\u00ad\u00ae\7%\2\2\u00ae\u00b2\3\2\2\2\u00af\u00b1")
        buf.write("\13\2\2\2\u00b0\u00af\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2")
        buf.write("\u00b3\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00b5\3\2\2\2")
        buf.write("\u00b4\u00b2\3\2\2\2\u00b5\u00b6\7%\2\2\u00b6\u00b7\7")
        buf.write("%\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\b\t\2\2\u00b9\22")
        buf.write("\3\2\2\2\u00ba\u00bc\t\3\2\2\u00bb\u00ba\3\2\2\2\u00bc")
        buf.write("\u00bd\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2")
        buf.write("\u00be\24\3\2\2\2\u00bf\u00c5\5\23\n\2\u00c0\u00c1\5\23")
        buf.write("\n\2\u00c1\u00c2\t\4\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00c0")
        buf.write("\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5")
        buf.write("\u00c6\3\2\2\2\u00c6\26\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8")
        buf.write("\u00ca\t\4\2\2\u00c9\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2")
        buf.write("\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\30\3\2")
        buf.write("\2\2\u00cd\u00ce\7D\2\2\u00ce\u00cf\7t\2\2\u00cf\u00d0")
        buf.write("\7g\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2\7m\2\2\u00d2\32")
        buf.write("\3\2\2\2\u00d3\u00d4\7H\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6")
        buf.write("\7t\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9")
        buf.write("\7e\2\2\u00d9\u00da\7j\2\2\u00da\34\3\2\2\2\u00db\u00dc")
        buf.write("\7K\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de\7v\2\2\u00de\36")
        buf.write("\3\2\2\2\u00df\u00e0\7P\2\2\u00e0\u00e1\7w\2\2\u00e1\u00e2")
        buf.write("\7n\2\2\u00e2\u00e3\7n\2\2\u00e3 \3\2\2\2\u00e4\u00e5")
        buf.write("\7E\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8")
        buf.write("\7u\2\2\u00e8\u00e9\7v\2\2\u00e9\u00ea\7t\2\2\u00ea\u00eb")
        buf.write("\7w\2\2\u00eb\u00ec\7e\2\2\u00ec\u00ed\7v\2\2\u00ed\u00ee")
        buf.write("\7q\2\2\u00ee\u00ef\7t\2\2\u00ef\"\3\2\2\2\u00f0\u00f1")
        buf.write("\7E\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4")
        buf.write("\7v\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7")
        buf.write("\7w\2\2\u00f7\u00f8\7g\2\2\u00f8$\3\2\2\2\u00f9\u00fa")
        buf.write("\7V\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc\7w\2\2\u00fc\u00fd")
        buf.write("\7g\2\2\u00fd&\3\2\2\2\u00fe\u00ff\7H\2\2\u00ff\u0100")
        buf.write("\7n\2\2\u0100\u0101\7q\2\2\u0101\u0102\7c\2\2\u0102\u0103")
        buf.write("\7v\2\2\u0103(\3\2\2\2\u0104\u0105\7E\2\2\u0105\u0106")
        buf.write("\7n\2\2\u0106\u0107\7c\2\2\u0107\u0108\7u\2\2\u0108\u0109")
        buf.write("\7u\2\2\u0109*\3\2\2\2\u010a\u010b\7F\2\2\u010b\u010c")
        buf.write("\7g\2\2\u010c\u010d\7u\2\2\u010d\u010e\7v\2\2\u010e\u010f")
        buf.write("\7t\2\2\u010f\u0110\7w\2\2\u0110\u0111\7e\2\2\u0111\u0112")
        buf.write("\7v\2\2\u0112\u0113\7q\2\2\u0113\u0114\7t\2\2\u0114,\3")
        buf.write("\2\2\2\u0115\u0116\7K\2\2\u0116\u0117\7h\2\2\u0117.\3")
        buf.write("\2\2\2\u0118\u0119\7H\2\2\u0119\u011a\7c\2\2\u011a\u011b")
        buf.write("\7n\2\2\u011b\u011c\7u\2\2\u011c\u011d\7g\2\2\u011d\60")
        buf.write("\3\2\2\2\u011e\u011f\7D\2\2\u011f\u0120\7q\2\2\u0120\u0121")
        buf.write("\7q\2\2\u0121\u0122\7n\2\2\u0122\u0123\7g\2\2\u0123\u0124")
        buf.write("\7c\2\2\u0124\u0125\7p\2\2\u0125\62\3\2\2\2\u0126\u0127")
        buf.write("\7X\2\2\u0127\u0128\7c\2\2\u0128\u0129\7n\2\2\u0129\64")
        buf.write("\3\2\2\2\u012a\u012b\7P\2\2\u012b\u012c\7g\2\2\u012c\u012d")
        buf.write("\7y\2\2\u012d\66\3\2\2\2\u012e\u012f\7G\2\2\u012f\u0130")
        buf.write("\7n\2\2\u0130\u0131\7u\2\2\u0131\u0132\7g\2\2\u0132\u0133")
        buf.write("\7k\2\2\u0133\u0134\7h\2\2\u01348\3\2\2\2\u0135\u0136")
        buf.write("\7C\2\2\u0136\u0137\7t\2\2\u0137\u0138\7t\2\2\u0138\u0139")
        buf.write("\7c\2\2\u0139\u013a\7{\2\2\u013a:\3\2\2\2\u013b\u013c")
        buf.write("\7U\2\2\u013c\u013d\7v\2\2\u013d\u013e\7t\2\2\u013e\u013f")
        buf.write("\7k\2\2\u013f\u0140\7p\2\2\u0140\u0141\7i\2\2\u0141<\3")
        buf.write("\2\2\2\u0142\u0143\7X\2\2\u0143\u0144\7c\2\2\u0144\u0145")
        buf.write("\7t\2\2\u0145>\3\2\2\2\u0146\u0147\7D\2\2\u0147\u0148")
        buf.write("\7{\2\2\u0148@\3\2\2\2\u0149\u014a\7G\2\2\u014a\u014b")
        buf.write("\7n\2\2\u014b\u014c\7u\2\2\u014c\u014d\7g\2\2\u014dB\3")
        buf.write("\2\2\2\u014e\u014f\7K\2\2\u014f\u0150\7p\2\2\u0150D\3")
        buf.write("\2\2\2\u0151\u0152\7T\2\2\u0152\u0153\7g\2\2\u0153\u0154")
        buf.write("\7v\2\2\u0154\u0155\7w\2\2\u0155\u0156\7t\2\2\u0156\u0157")
        buf.write("\7p\2\2\u0157F\3\2\2\2\u0158\u0159\7-\2\2\u0159H\3\2\2")
        buf.write("\2\u015a\u015b\7/\2\2\u015bJ\3\2\2\2\u015c\u015d\7\61")
        buf.write("\2\2\u015dL\3\2\2\2\u015e\u015f\7\'\2\2\u015fN\3\2\2\2")
        buf.write("\u0160\u0161\7#\2\2\u0161P\3\2\2\2\u0162\u0163\7(\2\2")
        buf.write("\u0163\u0164\7(\2\2\u0164R\3\2\2\2\u0165\u0166\7~\2\2")
        buf.write("\u0166\u0167\7~\2\2\u0167T\3\2\2\2\u0168\u0169\7?\2\2")
        buf.write("\u0169\u016a\7?\2\2\u016aV\3\2\2\2\u016b\u016c\7?\2\2")
        buf.write("\u016cX\3\2\2\2\u016d\u016e\7#\2\2\u016e\u016f\7?\2\2")
        buf.write("\u016fZ\3\2\2\2\u0170\u0171\7>\2\2\u0171\\\3\2\2\2\u0172")
        buf.write("\u0173\7>\2\2\u0173\u0174\7?\2\2\u0174^\3\2\2\2\u0175")
        buf.write("\u0176\7@\2\2\u0176`\3\2\2\2\u0177\u0178\7@\2\2\u0178")
        buf.write("\u0179\7?\2\2\u0179b\3\2\2\2\u017a\u017b\7?\2\2\u017b")
        buf.write("\u017c\7?\2\2\u017c\u017d\7\60\2\2\u017dd\3\2\2\2\u017e")
        buf.write("\u017f\7\60\2\2\u017ff\3\2\2\2\u0180\u0181\7<\2\2\u0181")
        buf.write("\u0182\7<\2\2\u0182h\3\2\2\2\u0183\u0184\7*\2\2\u0184")
        buf.write("j\3\2\2\2\u0185\u0186\7+\2\2\u0186l\3\2\2\2\u0187\u0188")
        buf.write("\7]\2\2\u0188n\3\2\2\2\u0189\u018a\7_\2\2\u018ap\3\2\2")
        buf.write("\2\u018b\u018c\7}\2\2\u018cr\3\2\2\2\u018d\u018e\7\177")
        buf.write("\2\2\u018et\3\2\2\2\u018f\u0190\7=\2\2\u0190v\3\2\2\2")
        buf.write("\u0191\u0192\7.\2\2\u0192x\3\2\2\2\u0193\u0195\t\5\2\2")
        buf.write("\u0194\u0196\t\6\2\2\u0195\u0194\3\2\2\2\u0196\u0197\3")
        buf.write("\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0199")
        buf.write("\3\2\2\2\u0199\u019a\b=\3\2\u019az\3\2\2\2\u019b\u019c")
        buf.write("\7\62\2\2\u019c\u01a0\7z\2\2\u019d\u019e\7\62\2\2\u019e")
        buf.write("\u01a0\7Z\2\2\u019f\u019b\3\2\2\2\u019f\u019d\3\2\2\2")
        buf.write("\u01a0\u01a2\3\2\2\2\u01a1\u01a3\t\7\2\2\u01a2\u01a1\3")
        buf.write("\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5")
        buf.write("\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a7\b>\4\2\u01a7")
        buf.write("|\3\2\2\2\u01a8\u01a9\7\62\2\2\u01a9\u01aa\5y=\2\u01aa")
        buf.write("~\3\2\2\2\u01ab\u01ac\7\62\2\2\u01ac\u01b0\7d\2\2\u01ad")
        buf.write("\u01ae\7\62\2\2\u01ae\u01b0\7D\2\2\u01af\u01ab\3\2\2\2")
        buf.write("\u01af\u01ad\3\2\2\2\u01b0\u01b2\3\2\2\2\u01b1\u01b3\t")
        buf.write("\b\2\2\u01b2\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b2")
        buf.write("\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u0080\3\2\2\2\u01b6")
        buf.write("\u01ba\t\t\2\2\u01b7\u01b9\t\n\2\2\u01b8\u01b7\3\2\2\2")
        buf.write("\u01b9\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3")
        buf.write("\2\2\2\u01bb\u01bd\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01be")
        buf.write("\t\t\2\2\u01be\u0082\3\2\2\2\u01bf\u01c0\7C\2\2\u01c0")
        buf.write("\u01c1\7t\2\2\u01c1\u01c2\7t\2\2\u01c2\u01c3\7c\2\2\u01c3")
        buf.write("\u01c4\7{\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c6\5i\65\2")
        buf.write("\u01c6\u01c7\5k\66\2\u01c7\u0084\3\2\2\2\u01c8\u01c9\7")
        buf.write("C\2\2\u01c9\u01ca\7t\2\2\u01ca\u01cb\7t\2\2\u01cb\u01cc")
        buf.write("\7c\2\2\u01cc\u01cd\7{\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01d5")
        buf.write("\5i\65\2\u01cf\u01d1\5\u0083B\2\u01d0\u01d2\5w<\2\u01d1")
        buf.write("\u01d0\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d4\3\2\2\2")
        buf.write("\u01d3\u01cf\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3\3")
        buf.write("\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d8\3\2\2\2\u01d7\u01d5")
        buf.write("\3\2\2\2\u01d8\u01d9\5k\66\2\u01d9\u0086\3\2\2\2\u01da")
        buf.write("\u01db\7)\2\2\u01db\u01dc\7$\2\2\u01dc\u0088\3\2\2\2\u01dd")
        buf.write("\u01de\13\2\2\2\u01de\u01df\bE\5\2\u01df\u008a\3\2\2\2")
        buf.write("\u01e0\u01e1\13\2\2\2\u01e1\u01e2\bF\6\2\u01e2\u008c\3")
        buf.write("\2\2\2\u01e3\u01e4\13\2\2\2\u01e4\u01e5\bG\7\2\u01e5\u008e")
        buf.write("\3\2\2\2\20\2\u00a8\u00b2\u00bd\u00c5\u00cb\u0197\u019f")
        buf.write("\u01a4\u01af\u01b4\u01ba\u01d1\u01d5\b\b\2\2\3=\2\3>\3")
        buf.write("\3E\4\3F\5\3G\6")
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
    ID = 10
    INTLIT = 11
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
            "INTTYPE", "VOIDTYPE", "WS", "BLOCK_COMMENT", "ALPHABET", "ID", 
            "INTLIT", "BREAK", "FOREACH", "INT", "NULL", "CONSTRUCTOR", 
            "CONTINUE", "TRUE", "FLOAT", "CLASS", "DESTRUCTOR", "IF", "FALSE", 
            "BOOLEAN", "VAL", "NEW", "ELSEIF", "ARRAY", "STRING", "VAR", 
            "BY", "ELSE", "IN", "RETURN", "ADD", "SUBTRACT", "MULTIPLY", 
            "MODULO", "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", 
            "LESS_THAN", "LEQ", "GREATER_THAN", "GEQ", "EQUAL_WHAT", "DOT", 
            "SUPER_CLASS", "LB", "RB", "LS", "RS", "LP", "RP", "SEMI", "COMMA", 
            "LITERAL_INT_DEC", "LITERAL_INT_HEX", "LITERAL_INT_OCT", "LITERAL_INT_BIN", 
            "LITERAL_STRING", "LITERAL_IDX_ARRAY", "LITERAL_MTD_ARRAY", 
            "DOUBLE_QUOTE", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "INTTYPE", "VOIDTYPE", 
                  "WS", "BLOCK_COMMENT", "ALPHABET", "ID", "INTLIT", "BREAK", 
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
        self.checkVersion("4.9.3")
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
     


