# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u0249\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\2\3\2\3\2\5\2\u009f\n\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\5\3\u00a6\n\3\3\3\7\3\u00a9\n\3\f\3\16\3\u00ac\13\3")
        buf.write("\5\3\u00ae\n\3\3\4\3\4\3\4\3\4\5\4\u00b4\n\4\3\4\3\4\3")
        buf.write("\4\5\4\u00b9\n\4\3\4\7\4\u00bc\n\4\f\4\16\4\u00bf\13\4")
        buf.write("\5\4\u00c1\n\4\3\5\3\5\3\5\3\5\5\5\u00c7\n\5\3\5\7\5\u00ca")
        buf.write("\n\5\f\5\16\5\u00cd\13\5\5\5\u00cf\n\5\3\6\3\6\3\6\3\6")
        buf.write("\5\6\u00d5\n\6\3\6\3\6\3\6\5\6\u00da\n\6\3\6\7\6\u00dd")
        buf.write("\n\6\f\6\16\6\u00e0\13\6\5\6\u00e2\n\6\3\7\3\7\3\7\5\7")
        buf.write("\u00e7\n\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00ef\n\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\5\b\u00f6\n\b\3\b\7\b\u00f9\n\b\f\b\16")
        buf.write("\b\u00fc\13\b\5\b\u00fe\n\b\3\t\3\t\7\t\u0102\n\t\f\t")
        buf.write("\16\t\u0105\13\t\3\n\3\n\5\n\u0109\n\n\3\n\6\n\u010c\n")
        buf.write("\n\r\n\16\n\u010d\3\13\3\13\3\13\3\13\7\13\u0114\n\13")
        buf.write("\f\13\16\13\u0117\13\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("%\3%\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write(",\3,\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\38\38\39\39\39\3:\3:\3;\3;\3;\3<\3<\3=\3=\3")
        buf.write("=\3>\3>\3>\3>\3?\3?\3?\3@\3@\3A\3A\3A\3B\3B\3C\3C\7C\u01f8")
        buf.write("\nC\fC\16C\u01fb\13C\3D\3D\6D\u01ff\nD\rD\16D\u0200\3")
        buf.write("E\3E\3E\3E\7E\u0207\nE\fE\16E\u020a\13E\3E\3E\3E\3E\3")
        buf.write("E\3F\6F\u0212\nF\rF\16F\u0213\3F\3F\3G\3G\3H\3H\3H\7H")
        buf.write("\u021d\nH\fH\16H\u0220\13H\3H\5H\u0223\nH\3H\3H\3I\3I")
        buf.write("\3I\7I\u022a\nI\fI\16I\u022d\13I\3I\3I\3I\3J\3J\3J\3J")
        buf.write("\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\5J\u0242\nJ\3K\3")
        buf.write("K\3K\3L\3L\3L\3\u0208\2M\3\3\5\4\7\5\t\6\13\7\r\b\17\2")
        buf.write("\21\2\23\2\25\t\27\n\31\13\33\f\35\r\37\16!\17#\20%\21")
        buf.write("\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67\329\33;\34")
        buf.write("=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61")
        buf.write("g\62i\63k\64m\65o\66q\67s8u9w:y;{<}=\177>\u0081?\u0083")
        buf.write("@\u0085A\u0087B\u0089C\u008bD\u008d\2\u008fE\u0091F\u0093")
        buf.write("\2\u0095\2\u0097G\3\2\21\3\2\63;\3\2\62;\4\2\63;CH\4\2")
        buf.write("\62;CH\3\2\639\3\2\629\3\2\62\63\4\2GGgg\4\2--//\5\2C")
        buf.write("\\aac|\6\2\62;C\\aac|\5\2\n\f\16\17\"\"\5\2\f\f$$^^\3")
        buf.write("\3\f\f\t\2))^^ddhhppttvv\2\u026f\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2")
        buf.write("\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3")
        buf.write("\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2")
        buf.write("\2\u008b\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\3\u009e\3\2\2\2\5\u00ad\3\2\2\2\7\u00b3\3\2\2")
        buf.write("\2\t\u00c2\3\2\2\2\13\u00d4\3\2\2\2\r\u00ee\3\2\2\2\17")
        buf.write("\u00fd\3\2\2\2\21\u00ff\3\2\2\2\23\u0106\3\2\2\2\25\u010f")
        buf.write("\3\2\2\2\27\u011b\3\2\2\2\31\u011e\3\2\2\2\33\u0122\3")
        buf.write("\2\2\2\35\u0126\3\2\2\2\37\u0128\3\2\2\2!\u012e\3\2\2")
        buf.write("\2#\u0136\3\2\2\2%\u013a\3\2\2\2\'\u013f\3\2\2\2)\u014b")
        buf.write("\3\2\2\2+\u0154\3\2\2\2-\u0159\3\2\2\2/\u015f\3\2\2\2")
        buf.write("\61\u0165\3\2\2\2\63\u0170\3\2\2\2\65\u0173\3\2\2\2\67")
        buf.write("\u0179\3\2\2\29\u0181\3\2\2\2;\u0185\3\2\2\2=\u018c\3")
        buf.write("\2\2\2?\u0192\3\2\2\2A\u0199\3\2\2\2C\u019c\3\2\2\2E\u01a1")
        buf.write("\3\2\2\2G\u01a4\3\2\2\2I\u01ab\3\2\2\2K\u01b0\3\2\2\2")
        buf.write("M\u01b2\3\2\2\2O\u01b4\3\2\2\2Q\u01b6\3\2\2\2S\u01b8\3")
        buf.write("\2\2\2U\u01ba\3\2\2\2W\u01bc\3\2\2\2Y\u01be\3\2\2\2[\u01c0")
        buf.write("\3\2\2\2]\u01c3\3\2\2\2_\u01c5\3\2\2\2a\u01c7\3\2\2\2")
        buf.write("c\u01c9\3\2\2\2e\u01cb\3\2\2\2g\u01cd\3\2\2\2i\u01cf\3")
        buf.write("\2\2\2k\u01d2\3\2\2\2m\u01d5\3\2\2\2o\u01d8\3\2\2\2q\u01da")
        buf.write("\3\2\2\2s\u01dd\3\2\2\2u\u01df\3\2\2\2w\u01e2\3\2\2\2")
        buf.write("y\u01e4\3\2\2\2{\u01e7\3\2\2\2}\u01eb\3\2\2\2\177\u01ee")
        buf.write("\3\2\2\2\u0081\u01f0\3\2\2\2\u0083\u01f3\3\2\2\2\u0085")
        buf.write("\u01f5\3\2\2\2\u0087\u01fc\3\2\2\2\u0089\u0202\3\2\2\2")
        buf.write("\u008b\u0211\3\2\2\2\u008d\u0217\3\2\2\2\u008f\u0219\3")
        buf.write("\2\2\2\u0091\u0226\3\2\2\2\u0093\u0241\3\2\2\2\u0095\u0243")
        buf.write("\3\2\2\2\u0097\u0246\3\2\2\2\u0099\u009f\5\5\3\2\u009a")
        buf.write("\u009f\5\7\4\2\u009b\u009f\5\t\5\2\u009c\u009f\5\13\6")
        buf.write("\2\u009d\u009f\5\13\6\2\u009e\u0099\3\2\2\2\u009e\u009a")
        buf.write("\3\2\2\2\u009e\u009b\3\2\2\2\u009e\u009c\3\2\2\2\u009e")
        buf.write("\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\b\2\2\2")
        buf.write("\u00a1\4\3\2\2\2\u00a2\u00ae\7\62\2\2\u00a3\u00aa\t\2")
        buf.write("\2\2\u00a4\u00a6\7a\2\2\u00a5\u00a4\3\2\2\2\u00a5\u00a6")
        buf.write("\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a9\t\3\2\2\u00a8")
        buf.write("\u00a5\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa\u00a8\3\2\2\2")
        buf.write("\u00aa\u00ab\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3")
        buf.write("\2\2\2\u00ad\u00a2\3\2\2\2\u00ad\u00a3\3\2\2\2\u00ae\6")
        buf.write("\3\2\2\2\u00af\u00b0\7\62\2\2\u00b0\u00b4\7z\2\2\u00b1")
        buf.write("\u00b2\7\62\2\2\u00b2\u00b4\7Z\2\2\u00b3\u00af\3\2\2\2")
        buf.write("\u00b3\u00b1\3\2\2\2\u00b4\u00c0\3\2\2\2\u00b5\u00c1\7")
        buf.write("\62\2\2\u00b6\u00bd\t\4\2\2\u00b7\u00b9\7a\2\2\u00b8\u00b7")
        buf.write("\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba")
        buf.write("\u00bc\t\5\2\2\u00bb\u00b8\3\2\2\2\u00bc\u00bf\3\2\2\2")
        buf.write("\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c1\3")
        buf.write("\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\u00b5\3\2\2\2\u00c0\u00b6")
        buf.write("\3\2\2\2\u00c1\b\3\2\2\2\u00c2\u00ce\7\62\2\2\u00c3\u00cf")
        buf.write("\7\62\2\2\u00c4\u00cb\t\6\2\2\u00c5\u00c7\7a\2\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\3\2\2\2")
        buf.write("\u00c8\u00ca\t\7\2\2\u00c9\u00c6\3\2\2\2\u00ca\u00cd\3")
        buf.write("\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cf")
        buf.write("\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce\u00c3\3\2\2\2\u00ce")
        buf.write("\u00c4\3\2\2\2\u00cf\n\3\2\2\2\u00d0\u00d1\7\62\2\2\u00d1")
        buf.write("\u00d5\7d\2\2\u00d2\u00d3\7\62\2\2\u00d3\u00d5\7D\2\2")
        buf.write("\u00d4\u00d0\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00e1\3")
        buf.write("\2\2\2\u00d6\u00e2\7\62\2\2\u00d7\u00de\7\63\2\2\u00d8")
        buf.write("\u00da\7a\2\2\u00d9\u00d8\3\2\2\2\u00d9\u00da\3\2\2\2")
        buf.write("\u00da\u00db\3\2\2\2\u00db\u00dd\t\b\2\2\u00dc\u00d9\3")
        buf.write("\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00df")
        buf.write("\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1")
        buf.write("\u00d6\3\2\2\2\u00e1\u00d7\3\2\2\2\u00e2\f\3\2\2\2\u00e3")
        buf.write("\u00e4\5\17\b\2\u00e4\u00e6\5\21\t\2\u00e5\u00e7\5\23")
        buf.write("\n\2\u00e6\u00e5\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00ef")
        buf.write("\3\2\2\2\u00e8\u00e9\5\17\b\2\u00e9\u00ea\5\23\n\2\u00ea")
        buf.write("\u00ef\3\2\2\2\u00eb\u00ec\5\21\t\2\u00ec\u00ed\5\23\n")
        buf.write("\2\u00ed\u00ef\3\2\2\2\u00ee\u00e3\3\2\2\2\u00ee\u00e8")
        buf.write("\3\2\2\2\u00ee\u00eb\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0")
        buf.write("\u00f1\b\7\3\2\u00f1\16\3\2\2\2\u00f2\u00fe\7\62\2\2\u00f3")
        buf.write("\u00fa\t\2\2\2\u00f4\u00f6\7a\2\2\u00f5\u00f4\3\2\2\2")
        buf.write("\u00f5\u00f6\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f9\t")
        buf.write("\3\2\2\u00f8\u00f5\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fd\u00f2\3\2\2\2\u00fd\u00f3\3\2\2\2")
        buf.write("\u00fe\20\3\2\2\2\u00ff\u0103\5\177@\2\u0100\u0102\t\3")
        buf.write("\2\2\u0101\u0100\3\2\2\2\u0102\u0105\3\2\2\2\u0103\u0101")
        buf.write("\3\2\2\2\u0103\u0104\3\2\2\2\u0104\22\3\2\2\2\u0105\u0103")
        buf.write("\3\2\2\2\u0106\u0108\t\t\2\2\u0107\u0109\t\n\2\2\u0108")
        buf.write("\u0107\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010b\3\2\2\2")
        buf.write("\u010a\u010c\t\3\2\2\u010b\u010a\3\2\2\2\u010c\u010d\3")
        buf.write("\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e\24")
        buf.write("\3\2\2\2\u010f\u0115\7$\2\2\u0110\u0114\5\u008dG\2\u0111")
        buf.write("\u0114\5\27\f\2\u0112\u0114\5\u0093J\2\u0113\u0110\3\2")
        buf.write("\2\2\u0113\u0111\3\2\2\2\u0113\u0112\3\2\2\2\u0114\u0117")
        buf.write("\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116")
        buf.write("\u0118\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u0119\7$\2\2")
        buf.write("\u0119\u011a\b\13\4\2\u011a\26\3\2\2\2\u011b\u011c\7)")
        buf.write("\2\2\u011c\u011d\7$\2\2\u011d\30\3\2\2\2\u011e\u011f\7")
        buf.write("X\2\2\u011f\u0120\7c\2\2\u0120\u0121\7n\2\2\u0121\32\3")
        buf.write("\2\2\2\u0122\u0123\7X\2\2\u0123\u0124\7c\2\2\u0124\u0125")
        buf.write("\7t\2\2\u0125\34\3\2\2\2\u0126\u0127\7&\2\2\u0127\36\3")
        buf.write("\2\2\2\u0128\u0129\7D\2\2\u0129\u012a\7t\2\2\u012a\u012b")
        buf.write("\7g\2\2\u012b\u012c\7c\2\2\u012c\u012d\7m\2\2\u012d \3")
        buf.write("\2\2\2\u012e\u012f\7H\2\2\u012f\u0130\7q\2\2\u0130\u0131")
        buf.write("\7t\2\2\u0131\u0132\7g\2\2\u0132\u0133\7c\2\2\u0133\u0134")
        buf.write("\7e\2\2\u0134\u0135\7j\2\2\u0135\"\3\2\2\2\u0136\u0137")
        buf.write("\7K\2\2\u0137\u0138\7p\2\2\u0138\u0139\7v\2\2\u0139$\3")
        buf.write("\2\2\2\u013a\u013b\7P\2\2\u013b\u013c\7w\2\2\u013c\u013d")
        buf.write("\7n\2\2\u013d\u013e\7n\2\2\u013e&\3\2\2\2\u013f\u0140")
        buf.write("\7E\2\2\u0140\u0141\7q\2\2\u0141\u0142\7p\2\2\u0142\u0143")
        buf.write("\7u\2\2\u0143\u0144\7v\2\2\u0144\u0145\7t\2\2\u0145\u0146")
        buf.write("\7w\2\2\u0146\u0147\7e\2\2\u0147\u0148\7v\2\2\u0148\u0149")
        buf.write("\7q\2\2\u0149\u014a\7t\2\2\u014a(\3\2\2\2\u014b\u014c")
        buf.write("\7E\2\2\u014c\u014d\7q\2\2\u014d\u014e\7p\2\2\u014e\u014f")
        buf.write("\7v\2\2\u014f\u0150\7k\2\2\u0150\u0151\7p\2\2\u0151\u0152")
        buf.write("\7w\2\2\u0152\u0153\7g\2\2\u0153*\3\2\2\2\u0154\u0155")
        buf.write("\7V\2\2\u0155\u0156\7t\2\2\u0156\u0157\7w\2\2\u0157\u0158")
        buf.write("\7g\2\2\u0158,\3\2\2\2\u0159\u015a\7H\2\2\u015a\u015b")
        buf.write("\7n\2\2\u015b\u015c\7q\2\2\u015c\u015d\7c\2\2\u015d\u015e")
        buf.write("\7v\2\2\u015e.\3\2\2\2\u015f\u0160\7E\2\2\u0160\u0161")
        buf.write("\7n\2\2\u0161\u0162\7c\2\2\u0162\u0163\7u\2\2\u0163\u0164")
        buf.write("\7u\2\2\u0164\60\3\2\2\2\u0165\u0166\7F\2\2\u0166\u0167")
        buf.write("\7g\2\2\u0167\u0168\7u\2\2\u0168\u0169\7v\2\2\u0169\u016a")
        buf.write("\7t\2\2\u016a\u016b\7w\2\2\u016b\u016c\7e\2\2\u016c\u016d")
        buf.write("\7v\2\2\u016d\u016e\7q\2\2\u016e\u016f\7t\2\2\u016f\62")
        buf.write("\3\2\2\2\u0170\u0171\7K\2\2\u0171\u0172\7h\2\2\u0172\64")
        buf.write("\3\2\2\2\u0173\u0174\7H\2\2\u0174\u0175\7c\2\2\u0175\u0176")
        buf.write("\7n\2\2\u0176\u0177\7u\2\2\u0177\u0178\7g\2\2\u0178\66")
        buf.write("\3\2\2\2\u0179\u017a\7D\2\2\u017a\u017b\7q\2\2\u017b\u017c")
        buf.write("\7q\2\2\u017c\u017d\7n\2\2\u017d\u017e\7g\2\2\u017e\u017f")
        buf.write("\7c\2\2\u017f\u0180\7p\2\2\u01808\3\2\2\2\u0181\u0182")
        buf.write("\7P\2\2\u0182\u0183\7g\2\2\u0183\u0184\7y\2\2\u0184:\3")
        buf.write("\2\2\2\u0185\u0186\7G\2\2\u0186\u0187\7n\2\2\u0187\u0188")
        buf.write("\7u\2\2\u0188\u0189\7g\2\2\u0189\u018a\7k\2\2\u018a\u018b")
        buf.write("\7h\2\2\u018b<\3\2\2\2\u018c\u018d\7C\2\2\u018d\u018e")
        buf.write("\7t\2\2\u018e\u018f\7t\2\2\u018f\u0190\7c\2\2\u0190\u0191")
        buf.write("\7{\2\2\u0191>\3\2\2\2\u0192\u0193\7U\2\2\u0193\u0194")
        buf.write("\7v\2\2\u0194\u0195\7t\2\2\u0195\u0196\7k\2\2\u0196\u0197")
        buf.write("\7p\2\2\u0197\u0198\7i\2\2\u0198@\3\2\2\2\u0199\u019a")
        buf.write("\7D\2\2\u019a\u019b\7{\2\2\u019bB\3\2\2\2\u019c\u019d")
        buf.write("\7G\2\2\u019d\u019e\7n\2\2\u019e\u019f\7u\2\2\u019f\u01a0")
        buf.write("\7g\2\2\u01a0D\3\2\2\2\u01a1\u01a2\7K\2\2\u01a2\u01a3")
        buf.write("\7p\2\2\u01a3F\3\2\2\2\u01a4\u01a5\7T\2\2\u01a5\u01a6")
        buf.write("\7g\2\2\u01a6\u01a7\7v\2\2\u01a7\u01a8\7w\2\2\u01a8\u01a9")
        buf.write("\7t\2\2\u01a9\u01aa\7p\2\2\u01aaH\3\2\2\2\u01ab\u01ac")
        buf.write("\7U\2\2\u01ac\u01ad\7g\2\2\u01ad\u01ae\7n\2\2\u01ae\u01af")
        buf.write("\7h\2\2\u01afJ\3\2\2\2\u01b0\u01b1\7*\2\2\u01b1L\3\2\2")
        buf.write("\2\u01b2\u01b3\7+\2\2\u01b3N\3\2\2\2\u01b4\u01b5\7]\2")
        buf.write("\2\u01b5P\3\2\2\2\u01b6\u01b7\7_\2\2\u01b7R\3\2\2\2\u01b8")
        buf.write("\u01b9\7}\2\2\u01b9T\3\2\2\2\u01ba\u01bb\7\177\2\2\u01bb")
        buf.write("V\3\2\2\2\u01bc\u01bd\7=\2\2\u01bdX\3\2\2\2\u01be\u01bf")
        buf.write("\7.\2\2\u01bfZ\3\2\2\2\u01c0\u01c1\7\60\2\2\u01c1\u01c2")
        buf.write("\7\60\2\2\u01c2\\\3\2\2\2\u01c3\u01c4\7-\2\2\u01c4^\3")
        buf.write("\2\2\2\u01c5\u01c6\7/\2\2\u01c6`\3\2\2\2\u01c7\u01c8\7")
        buf.write(",\2\2\u01c8b\3\2\2\2\u01c9\u01ca\7\61\2\2\u01cad\3\2\2")
        buf.write("\2\u01cb\u01cc\7\'\2\2\u01ccf\3\2\2\2\u01cd\u01ce\7#\2")
        buf.write("\2\u01ceh\3\2\2\2\u01cf\u01d0\7(\2\2\u01d0\u01d1\7(\2")
        buf.write("\2\u01d1j\3\2\2\2\u01d2\u01d3\7~\2\2\u01d3\u01d4\7~\2")
        buf.write("\2\u01d4l\3\2\2\2\u01d5\u01d6\7?\2\2\u01d6\u01d7\7?\2")
        buf.write("\2\u01d7n\3\2\2\2\u01d8\u01d9\7?\2\2\u01d9p\3\2\2\2\u01da")
        buf.write("\u01db\7#\2\2\u01db\u01dc\7?\2\2\u01dcr\3\2\2\2\u01dd")
        buf.write("\u01de\7>\2\2\u01det\3\2\2\2\u01df\u01e0\7>\2\2\u01e0")
        buf.write("\u01e1\7?\2\2\u01e1v\3\2\2\2\u01e2\u01e3\7@\2\2\u01e3")
        buf.write("x\3\2\2\2\u01e4\u01e5\7@\2\2\u01e5\u01e6\7?\2\2\u01e6")
        buf.write("z\3\2\2\2\u01e7\u01e8\7?\2\2\u01e8\u01e9\7?\2\2\u01e9")
        buf.write("\u01ea\7\60\2\2\u01ea|\3\2\2\2\u01eb\u01ec\7-\2\2\u01ec")
        buf.write("\u01ed\7\60\2\2\u01ed~\3\2\2\2\u01ee\u01ef\7\60\2\2\u01ef")
        buf.write("\u0080\3\2\2\2\u01f0\u01f1\7<\2\2\u01f1\u01f2\7<\2\2\u01f2")
        buf.write("\u0082\3\2\2\2\u01f3\u01f4\7<\2\2\u01f4\u0084\3\2\2\2")
        buf.write("\u01f5\u01f9\t\13\2\2\u01f6\u01f8\t\f\2\2\u01f7\u01f6")
        buf.write("\3\2\2\2\u01f8\u01fb\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9")
        buf.write("\u01fa\3\2\2\2\u01fa\u0086\3\2\2\2\u01fb\u01f9\3\2\2\2")
        buf.write("\u01fc\u01fe\5\35\17\2\u01fd\u01ff\t\f\2\2\u01fe\u01fd")
        buf.write("\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u01fe\3\2\2\2\u0200")
        buf.write("\u0201\3\2\2\2\u0201\u0088\3\2\2\2\u0202\u0203\7%\2\2")
        buf.write("\u0203\u0204\7%\2\2\u0204\u0208\3\2\2\2\u0205\u0207\13")
        buf.write("\2\2\2\u0206\u0205\3\2\2\2\u0207\u020a\3\2\2\2\u0208\u0209")
        buf.write("\3\2\2\2\u0208\u0206\3\2\2\2\u0209\u020b\3\2\2\2\u020a")
        buf.write("\u0208\3\2\2\2\u020b\u020c\7%\2\2\u020c\u020d\7%\2\2\u020d")
        buf.write("\u020e\3\2\2\2\u020e\u020f\bE\5\2\u020f\u008a\3\2\2\2")
        buf.write("\u0210\u0212\t\r\2\2\u0211\u0210\3\2\2\2\u0212\u0213\3")
        buf.write("\2\2\2\u0213\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0215")
        buf.write("\3\2\2\2\u0215\u0216\bF\5\2\u0216\u008c\3\2\2\2\u0217")
        buf.write("\u0218\n\16\2\2\u0218\u008e\3\2\2\2\u0219\u021e\7$\2\2")
        buf.write("\u021a\u021d\5\u008dG\2\u021b\u021d\5\u0093J\2\u021c\u021a")
        buf.write("\3\2\2\2\u021c\u021b\3\2\2\2\u021d\u0220\3\2\2\2\u021e")
        buf.write("\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u0222\3\2\2\2")
        buf.write("\u0220\u021e\3\2\2\2\u0221\u0223\t\17\2\2\u0222\u0221")
        buf.write("\3\2\2\2\u0223\u0224\3\2\2\2\u0224\u0225\bH\6\2\u0225")
        buf.write("\u0090\3\2\2\2\u0226\u022b\7$\2\2\u0227\u022a\5\u008d")
        buf.write("G\2\u0228\u022a\5\u0093J\2\u0229\u0227\3\2\2\2\u0229\u0228")
        buf.write("\3\2\2\2\u022a\u022d\3\2\2\2\u022b\u0229\3\2\2\2\u022b")
        buf.write("\u022c\3\2\2\2\u022c\u022e\3\2\2\2\u022d\u022b\3\2\2\2")
        buf.write("\u022e\u022f\5\u0095K\2\u022f\u0230\bI\7\2\u0230\u0092")
        buf.write("\3\2\2\2\u0231\u0232\7^\2\2\u0232\u0242\7d\2\2\u0233\u0234")
        buf.write("\7^\2\2\u0234\u0242\7h\2\2\u0235\u0236\7^\2\2\u0236\u0242")
        buf.write("\7t\2\2\u0237\u0238\7^\2\2\u0238\u0242\7p\2\2\u0239\u023a")
        buf.write("\7^\2\2\u023a\u0242\7v\2\2\u023b\u023c\7^\2\2\u023c\u0242")
        buf.write("\7)\2\2\u023d\u023e\7^\2\2\u023e\u0242\7^\2\2\u023f\u0240")
        buf.write("\7)\2\2\u0240\u0242\7$\2\2\u0241\u0231\3\2\2\2\u0241\u0233")
        buf.write("\3\2\2\2\u0241\u0235\3\2\2\2\u0241\u0237\3\2\2\2\u0241")
        buf.write("\u0239\3\2\2\2\u0241\u023b\3\2\2\2\u0241\u023d\3\2\2\2")
        buf.write("\u0241\u023f\3\2\2\2\u0242\u0094\3\2\2\2\u0243\u0244\7")
        buf.write("^\2\2\u0244\u0245\n\20\2\2\u0245\u0096\3\2\2\2\u0246\u0247")
        buf.write("\13\2\2\2\u0247\u0248\bL\b\2\u0248\u0098\3\2\2\2&\2\u009e")
        buf.write("\u00a5\u00aa\u00ad\u00b3\u00b8\u00bd\u00c0\u00c6\u00cb")
        buf.write("\u00ce\u00d4\u00d9\u00de\u00e1\u00e6\u00ee\u00f5\u00fa")
        buf.write("\u00fd\u0103\u0108\u010d\u0113\u0115\u01f9\u0200\u0208")
        buf.write("\u0213\u021c\u021e\u0222\u0229\u022b\u0241\t\3\2\2\3\7")
        buf.write("\3\3\13\4\b\2\2\3H\5\3I\6\3L\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LITERAL_INT = 1
    LITERAL_INT_DEC = 2
    LITERAL_INT_HEX = 3
    LITERAL_INT_OCT = 4
    LITERAL_INT_BIN = 5
    LITERAL_FLOAT = 6
    LITERAL_STRING = 7
    DOUBLE_QUOTE = 8
    VAL = 9
    VAR = 10
    STATIC = 11
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
    NEW = 25
    ELSEIF = 26
    ARRAY = 27
    STRING = 28
    BY = 29
    ELSE = 30
    IN = 31
    RETURN = 32
    SELF = 33
    LB = 34
    RB = 35
    LS = 36
    RS = 37
    LP = 38
    RP = 39
    SEMI = 40
    COMMA = 41
    DOTDOT = 42
    ADD = 43
    SUBTRACT = 44
    MULTIPLY = 45
    DIVIDE = 46
    MODULO = 47
    NOT = 48
    AND = 49
    OR = 50
    EQUAL = 51
    ASSIGN = 52
    NOT_EQUAL = 53
    LESS_THAN = 54
    LEQ = 55
    GREATER_THAN = 56
    GEQ = 57
    EQUAL_STRING = 58
    STRING_CONCAT = 59
    DOT = 60
    DOUBLE_COLON = 61
    COLON = 62
    ID = 63
    DOLLAR_ID = 64
    BLOCK_COMMENT = 65
    WS = 66
    UNCLOSE_STRING = 67
    ILLEGAL_ESCAPE = 68
    ERROR_CHAR = 69

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Val'", "'Var'", "'$'", "'Break'", "'Foreach'", "'Int'", "'Null'", 
            "'Constructor'", "'Continue'", "'True'", "'Float'", "'Class'", 
            "'Destructor'", "'If'", "'False'", "'Boolean'", "'New'", "'Elseif'", 
            "'Array'", "'String'", "'By'", "'Else'", "'In'", "'Return'", 
            "'Self'", "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", "','", 
            "'..'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'='", "'!='", "'<'", "'<='", "'>'", "'>='", "'==.'", 
            "'+.'", "'.'", "'::'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "LITERAL_INT", "LITERAL_INT_DEC", "LITERAL_INT_HEX", "LITERAL_INT_OCT", 
            "LITERAL_INT_BIN", "LITERAL_FLOAT", "LITERAL_STRING", "DOUBLE_QUOTE", 
            "VAL", "VAR", "STATIC", "BREAK", "FOREACH", "INT", "NULL", "CONSTRUCTOR", 
            "CONTINUE", "TRUE", "FLOAT", "CLASS", "DESTRUCTOR", "IF", "FALSE", 
            "BOOLEAN", "NEW", "ELSEIF", "ARRAY", "STRING", "BY", "ELSE", 
            "IN", "RETURN", "SELF", "LB", "RB", "LS", "RS", "LP", "RP", 
            "SEMI", "COMMA", "DOTDOT", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", 
            "MODULO", "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", 
            "LESS_THAN", "LEQ", "GREATER_THAN", "GEQ", "EQUAL_STRING", "STRING_CONCAT", 
            "DOT", "DOUBLE_COLON", "COLON", "ID", "DOLLAR_ID", "BLOCK_COMMENT", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "LITERAL_INT", "LITERAL_INT_DEC", "LITERAL_INT_HEX", "LITERAL_INT_OCT", 
                  "LITERAL_INT_BIN", "LITERAL_FLOAT", "FLOAT_INT", "FLOAT_DECIMAL", 
                  "FLOAT_EXP", "LITERAL_STRING", "DOUBLE_QUOTE", "VAL", 
                  "VAR", "STATIC", "BREAK", "FOREACH", "INT", "NULL", "CONSTRUCTOR", 
                  "CONTINUE", "TRUE", "FLOAT", "CLASS", "DESTRUCTOR", "IF", 
                  "FALSE", "BOOLEAN", "NEW", "ELSEIF", "ARRAY", "STRING", 
                  "BY", "ELSE", "IN", "RETURN", "SELF", "LB", "RB", "LS", 
                  "RS", "LP", "RP", "SEMI", "COMMA", "DOTDOT", "ADD", "SUBTRACT", 
                  "MULTIPLY", "DIVIDE", "MODULO", "NOT", "AND", "OR", "EQUAL", 
                  "ASSIGN", "NOT_EQUAL", "LESS_THAN", "LEQ", "GREATER_THAN", 
                  "GEQ", "EQUAL_STRING", "STRING_CONCAT", "DOT", "DOUBLE_COLON", 
                  "COLON", "ID", "DOLLAR_ID", "BLOCK_COMMENT", "WS", "STRING_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ESC_SEQUENCE", "ESC_ILLEGAL", 
                  "ERROR_CHAR" ]

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
            actions[0] = self.LITERAL_INT_action 
            actions[5] = self.LITERAL_FLOAT_action 
            actions[9] = self.LITERAL_STRING_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
            actions[74] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def LITERAL_INT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def LITERAL_FLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

    def LITERAL_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             
            		y = str(self.text)
            		self.text = y[1:-1]
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	content = str(self.text)
            	esc = ['"', '\n']
            	if content[-1] in esc:
            		raise UncloseString(content[1:-1])
            	else:
            		raise UncloseString(content[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            		raise ErrorToken(self.text)
            	
     


