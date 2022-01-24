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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u023d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\3\2\3\2\3\2\5\2\u009d\n\2\3\2\3\2\3\3\3\3\3\3\5\3")
        buf.write("\u00a4\n\3\3\3\7\3\u00a7\n\3\f\3\16\3\u00aa\13\3\5\3\u00ac")
        buf.write("\n\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\u00b4\n\4\3\4\3\4\3\4")
        buf.write("\5\4\u00b9\n\4\3\4\7\4\u00bc\n\4\f\4\16\4\u00bf\13\4\5")
        buf.write("\4\u00c1\n\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\u00c9\n\5\3\5")
        buf.write("\7\5\u00cc\n\5\f\5\16\5\u00cf\13\5\5\5\u00d1\n\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\5\6\u00d9\n\6\3\6\3\6\3\6\5\6\u00de")
        buf.write("\n\6\3\6\7\6\u00e1\n\6\f\6\16\6\u00e4\13\6\5\6\u00e6\n")
        buf.write("\6\3\7\3\7\3\7\5\7\u00eb\n\7\3\7\3\7\3\7\3\7\3\7\3\7\5")
        buf.write("\7\u00f3\n\7\3\7\3\7\3\b\3\b\3\b\5\b\u00fa\n\b\3\b\7\b")
        buf.write("\u00fd\n\b\f\b\16\b\u0100\13\b\5\b\u0102\n\b\3\t\3\t\7")
        buf.write("\t\u0106\n\t\f\t\16\t\u0109\13\t\3\n\3\n\5\n\u010d\n\n")
        buf.write("\3\n\3\n\3\n\7\n\u0112\n\n\f\n\16\n\u0115\13\n\5\n\u0117")
        buf.write("\n\n\3\13\3\13\3\13\7\13\u011c\n\13\f\13\16\13\u011f\13")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3")
        buf.write("%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3")
        buf.write("-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67")
        buf.write("\38\38\38\39\39\3:\3:\3:\3;\3;\3<\3<\3<\3=\3=\3=\3=\3")
        buf.write(">\3>\3>\3?\3?\3@\3@\3@\3A\3A\3B\3B\7B\u01fe\nB\fB\16B")
        buf.write("\u0201\13B\3C\3C\6C\u0205\nC\rC\16C\u0206\3D\3D\3D\3D")
        buf.write("\7D\u020d\nD\fD\16D\u0210\13D\3D\3D\3D\3D\3D\3E\6E\u0218")
        buf.write("\nE\rE\16E\u0219\3E\3E\3F\3F\7F\u0220\nF\fF\16F\u0223")
        buf.write("\13F\3F\3F\3G\3G\7G\u0229\nG\fG\16G\u022c\13G\3G\3G\3")
        buf.write("G\3H\3H\5H\u0233\nH\3I\3I\3I\3J\3J\3J\3K\3K\3K\3\u020e")
        buf.write("\2L\3\3\5\4\7\5\t\6\13\7\r\b\17\2\21\2\23\2\25\t\27\n")
        buf.write("\31\13\33\f\35\r\37\16!\17#\20%\21\'\22)\23+\24-\25/\26")
        buf.write("\61\27\63\30\65\31\67\329\33;\34=\35?\36A\37C E!G\"I#")
        buf.write("K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62i\63k\64m\65o\66")
        buf.write("q\67s8u9w:y;{<}=\177>\u0081?\u0083@\u0085A\u0087B\u0089")
        buf.write("C\u008bD\u008dE\u008f\2\u0091\2\u0093\2\u0095F\3\2\20")
        buf.write("\3\2\63;\3\2\62;\4\2\63;CH\4\2\62;CH\3\2\639\3\2\629\3")
        buf.write("\2\62\63\4\2GGgg\4\2--//\5\2C\\aac|\6\2\62;C\\aac|\5\2")
        buf.write("\n\f\16\17\"\"\4\2$$^^\t\2))^^ddhhppttvv\2\u025b\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\3\u009c\3\2\2\2\5\u00ab\3\2\2\2\7\u00b3\3\2\2")
        buf.write("\2\t\u00c4\3\2\2\2\13\u00d8\3\2\2\2\r\u00f2\3\2\2\2\17")
        buf.write("\u0101\3\2\2\2\21\u0103\3\2\2\2\23\u010a\3\2\2\2\25\u0118")
        buf.write("\3\2\2\2\27\u0123\3\2\2\2\31\u0126\3\2\2\2\33\u012a\3")
        buf.write("\2\2\2\35\u012e\3\2\2\2\37\u0134\3\2\2\2!\u013c\3\2\2")
        buf.write("\2#\u0140\3\2\2\2%\u0145\3\2\2\2\'\u0151\3\2\2\2)\u015a")
        buf.write("\3\2\2\2+\u015f\3\2\2\2-\u0165\3\2\2\2/\u016b\3\2\2\2")
        buf.write("\61\u0176\3\2\2\2\63\u0179\3\2\2\2\65\u017f\3\2\2\2\67")
        buf.write("\u0187\3\2\2\29\u018b\3\2\2\2;\u0192\3\2\2\2=\u0198\3")
        buf.write("\2\2\2?\u019f\3\2\2\2A\u01a2\3\2\2\2C\u01a7\3\2\2\2E\u01aa")
        buf.write("\3\2\2\2G\u01b1\3\2\2\2I\u01b6\3\2\2\2K\u01b8\3\2\2\2")
        buf.write("M\u01ba\3\2\2\2O\u01bc\3\2\2\2Q\u01be\3\2\2\2S\u01c0\3")
        buf.write("\2\2\2U\u01c2\3\2\2\2W\u01c4\3\2\2\2Y\u01c6\3\2\2\2[\u01c9")
        buf.write("\3\2\2\2]\u01cb\3\2\2\2_\u01cd\3\2\2\2a\u01cf\3\2\2\2")
        buf.write("c\u01d1\3\2\2\2e\u01d3\3\2\2\2g\u01d5\3\2\2\2i\u01d8\3")
        buf.write("\2\2\2k\u01db\3\2\2\2m\u01de\3\2\2\2o\u01e0\3\2\2\2q\u01e3")
        buf.write("\3\2\2\2s\u01e5\3\2\2\2u\u01e8\3\2\2\2w\u01ea\3\2\2\2")
        buf.write("y\u01ed\3\2\2\2{\u01f1\3\2\2\2}\u01f4\3\2\2\2\177\u01f6")
        buf.write("\3\2\2\2\u0081\u01f9\3\2\2\2\u0083\u01fb\3\2\2\2\u0085")
        buf.write("\u0202\3\2\2\2\u0087\u0208\3\2\2\2\u0089\u0217\3\2\2\2")
        buf.write("\u008b\u021d\3\2\2\2\u008d\u0226\3\2\2\2\u008f\u0232\3")
        buf.write("\2\2\2\u0091\u0234\3\2\2\2\u0093\u0237\3\2\2\2\u0095\u023a")
        buf.write("\3\2\2\2\u0097\u009d\5\5\3\2\u0098\u009d\5\7\4\2\u0099")
        buf.write("\u009d\5\t\5\2\u009a\u009d\5\13\6\2\u009b\u009d\5\13\6")
        buf.write("\2\u009c\u0097\3\2\2\2\u009c\u0098\3\2\2\2\u009c\u0099")
        buf.write("\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009b\3\2\2\2\u009d")
        buf.write("\u009e\3\2\2\2\u009e\u009f\b\2\2\2\u009f\4\3\2\2\2\u00a0")
        buf.write("\u00ac\7\62\2\2\u00a1\u00a8\t\2\2\2\u00a2\u00a4\7a\2\2")
        buf.write("\u00a3\u00a2\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\3")
        buf.write("\2\2\2\u00a5\u00a7\t\3\2\2\u00a6\u00a3\3\2\2\2\u00a7\u00aa")
        buf.write("\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9")
        buf.write("\u00ac\3\2\2\2\u00aa\u00a8\3\2\2\2\u00ab\u00a0\3\2\2\2")
        buf.write("\u00ab\u00a1\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\b")
        buf.write("\3\3\2\u00ae\6\3\2\2\2\u00af\u00b0\7\62\2\2\u00b0\u00b4")
        buf.write("\7z\2\2\u00b1\u00b2\7\62\2\2\u00b2\u00b4\7Z\2\2\u00b3")
        buf.write("\u00af\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00c0\3\2\2\2")
        buf.write("\u00b5\u00c1\7\62\2\2\u00b6\u00bd\t\4\2\2\u00b7\u00b9")
        buf.write("\7a\2\2\u00b8\u00b7\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9")
        buf.write("\u00ba\3\2\2\2\u00ba\u00bc\t\5\2\2\u00bb\u00b8\3\2\2\2")
        buf.write("\u00bc\u00bf\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3")
        buf.write("\2\2\2\u00be\u00c1\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\u00b5")
        buf.write("\3\2\2\2\u00c0\u00b6\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2")
        buf.write("\u00c3\b\4\4\2\u00c3\b\3\2\2\2\u00c4\u00d0\7\62\2\2\u00c5")
        buf.write("\u00d1\7\62\2\2\u00c6\u00cd\t\6\2\2\u00c7\u00c9\7a\2\2")
        buf.write("\u00c8\u00c7\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00ca\3")
        buf.write("\2\2\2\u00ca\u00cc\t\7\2\2\u00cb\u00c8\3\2\2\2\u00cc\u00cf")
        buf.write("\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce")
        buf.write("\u00d1\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00c5\3\2\2\2")
        buf.write("\u00d0\u00c6\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\b")
        buf.write("\5\5\2\u00d3\n\3\2\2\2\u00d4\u00d5\7\62\2\2\u00d5\u00d9")
        buf.write("\7d\2\2\u00d6\u00d7\7\62\2\2\u00d7\u00d9\7D\2\2\u00d8")
        buf.write("\u00d4\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9\u00e5\3\2\2\2")
        buf.write("\u00da\u00e6\7\62\2\2\u00db\u00e2\7\63\2\2\u00dc\u00de")
        buf.write("\7a\2\2\u00dd\u00dc\3\2\2\2\u00dd\u00de\3\2\2\2\u00de")
        buf.write("\u00df\3\2\2\2\u00df\u00e1\t\b\2\2\u00e0\u00dd\3\2\2\2")
        buf.write("\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3")
        buf.write("\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00da")
        buf.write("\3\2\2\2\u00e5\u00db\3\2\2\2\u00e6\f\3\2\2\2\u00e7\u00e8")
        buf.write("\5\17\b\2\u00e8\u00ea\5\21\t\2\u00e9\u00eb\5\23\n\2\u00ea")
        buf.write("\u00e9\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00f3\3\2\2\2")
        buf.write("\u00ec\u00ed\5\17\b\2\u00ed\u00ee\5\23\n\2\u00ee\u00f3")
        buf.write("\3\2\2\2\u00ef\u00f0\5\21\t\2\u00f0\u00f1\5\23\n\2\u00f1")
        buf.write("\u00f3\3\2\2\2\u00f2\u00e7\3\2\2\2\u00f2\u00ec\3\2\2\2")
        buf.write("\u00f2\u00ef\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f5\b")
        buf.write("\7\6\2\u00f5\16\3\2\2\2\u00f6\u0102\7\62\2\2\u00f7\u00fe")
        buf.write("\t\2\2\2\u00f8\u00fa\7a\2\2\u00f9\u00f8\3\2\2\2\u00f9")
        buf.write("\u00fa\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fd\t\3\2\2")
        buf.write("\u00fc\u00f9\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3")
        buf.write("\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0102\3\2\2\2\u0100\u00fe")
        buf.write("\3\2\2\2\u0101\u00f6\3\2\2\2\u0101\u00f7\3\2\2\2\u0102")
        buf.write("\20\3\2\2\2\u0103\u0107\5}?\2\u0104\u0106\t\3\2\2\u0105")
        buf.write("\u0104\3\2\2\2\u0106\u0109\3\2\2\2\u0107\u0105\3\2\2\2")
        buf.write("\u0107\u0108\3\2\2\2\u0108\22\3\2\2\2\u0109\u0107\3\2")
        buf.write("\2\2\u010a\u010c\t\t\2\2\u010b\u010d\t\n\2\2\u010c\u010b")
        buf.write("\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u0116\3\2\2\2\u010e")
        buf.write("\u0117\7\62\2\2\u010f\u0113\t\2\2\2\u0110\u0112\t\3\2")
        buf.write("\2\u0111\u0110\3\2\2\2\u0112\u0115\3\2\2\2\u0113\u0111")
        buf.write("\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0117\3\2\2\2\u0115")
        buf.write("\u0113\3\2\2\2\u0116\u010e\3\2\2\2\u0116\u010f\3\2\2\2")
        buf.write("\u0117\24\3\2\2\2\u0118\u011d\7$\2\2\u0119\u011c\5\u008f")
        buf.write("H\2\u011a\u011c\5\27\f\2\u011b\u0119\3\2\2\2\u011b\u011a")
        buf.write("\3\2\2\2\u011c\u011f\3\2\2\2\u011d\u011b\3\2\2\2\u011d")
        buf.write("\u011e\3\2\2\2\u011e\u0120\3\2\2\2\u011f\u011d\3\2\2\2")
        buf.write("\u0120\u0121\7$\2\2\u0121\u0122\b\13\7\2\u0122\26\3\2")
        buf.write("\2\2\u0123\u0124\7)\2\2\u0124\u0125\7$\2\2\u0125\30\3")
        buf.write("\2\2\2\u0126\u0127\7X\2\2\u0127\u0128\7c\2\2\u0128\u0129")
        buf.write("\7n\2\2\u0129\32\3\2\2\2\u012a\u012b\7X\2\2\u012b\u012c")
        buf.write("\7c\2\2\u012c\u012d\7t\2\2\u012d\34\3\2\2\2\u012e\u012f")
        buf.write("\7D\2\2\u012f\u0130\7t\2\2\u0130\u0131\7g\2\2\u0131\u0132")
        buf.write("\7c\2\2\u0132\u0133\7m\2\2\u0133\36\3\2\2\2\u0134\u0135")
        buf.write("\7H\2\2\u0135\u0136\7q\2\2\u0136\u0137\7t\2\2\u0137\u0138")
        buf.write("\7g\2\2\u0138\u0139\7c\2\2\u0139\u013a\7e\2\2\u013a\u013b")
        buf.write("\7j\2\2\u013b \3\2\2\2\u013c\u013d\7K\2\2\u013d\u013e")
        buf.write("\7p\2\2\u013e\u013f\7v\2\2\u013f\"\3\2\2\2\u0140\u0141")
        buf.write("\7P\2\2\u0141\u0142\7w\2\2\u0142\u0143\7n\2\2\u0143\u0144")
        buf.write("\7n\2\2\u0144$\3\2\2\2\u0145\u0146\7E\2\2\u0146\u0147")
        buf.write("\7q\2\2\u0147\u0148\7p\2\2\u0148\u0149\7u\2\2\u0149\u014a")
        buf.write("\7v\2\2\u014a\u014b\7t\2\2\u014b\u014c\7w\2\2\u014c\u014d")
        buf.write("\7e\2\2\u014d\u014e\7v\2\2\u014e\u014f\7q\2\2\u014f\u0150")
        buf.write("\7t\2\2\u0150&\3\2\2\2\u0151\u0152\7E\2\2\u0152\u0153")
        buf.write("\7q\2\2\u0153\u0154\7p\2\2\u0154\u0155\7v\2\2\u0155\u0156")
        buf.write("\7k\2\2\u0156\u0157\7p\2\2\u0157\u0158\7w\2\2\u0158\u0159")
        buf.write("\7g\2\2\u0159(\3\2\2\2\u015a\u015b\7V\2\2\u015b\u015c")
        buf.write("\7t\2\2\u015c\u015d\7w\2\2\u015d\u015e\7g\2\2\u015e*\3")
        buf.write("\2\2\2\u015f\u0160\7H\2\2\u0160\u0161\7n\2\2\u0161\u0162")
        buf.write("\7q\2\2\u0162\u0163\7c\2\2\u0163\u0164\7v\2\2\u0164,\3")
        buf.write("\2\2\2\u0165\u0166\7E\2\2\u0166\u0167\7n\2\2\u0167\u0168")
        buf.write("\7c\2\2\u0168\u0169\7u\2\2\u0169\u016a\7u\2\2\u016a.\3")
        buf.write("\2\2\2\u016b\u016c\7F\2\2\u016c\u016d\7g\2\2\u016d\u016e")
        buf.write("\7u\2\2\u016e\u016f\7v\2\2\u016f\u0170\7t\2\2\u0170\u0171")
        buf.write("\7w\2\2\u0171\u0172\7e\2\2\u0172\u0173\7v\2\2\u0173\u0174")
        buf.write("\7q\2\2\u0174\u0175\7t\2\2\u0175\60\3\2\2\2\u0176\u0177")
        buf.write("\7K\2\2\u0177\u0178\7h\2\2\u0178\62\3\2\2\2\u0179\u017a")
        buf.write("\7H\2\2\u017a\u017b\7c\2\2\u017b\u017c\7n\2\2\u017c\u017d")
        buf.write("\7u\2\2\u017d\u017e\7g\2\2\u017e\64\3\2\2\2\u017f\u0180")
        buf.write("\7D\2\2\u0180\u0181\7q\2\2\u0181\u0182\7q\2\2\u0182\u0183")
        buf.write("\7n\2\2\u0183\u0184\7g\2\2\u0184\u0185\7c\2\2\u0185\u0186")
        buf.write("\7p\2\2\u0186\66\3\2\2\2\u0187\u0188\7P\2\2\u0188\u0189")
        buf.write("\7g\2\2\u0189\u018a\7y\2\2\u018a8\3\2\2\2\u018b\u018c")
        buf.write("\7G\2\2\u018c\u018d\7n\2\2\u018d\u018e\7u\2\2\u018e\u018f")
        buf.write("\7g\2\2\u018f\u0190\7k\2\2\u0190\u0191\7h\2\2\u0191:\3")
        buf.write("\2\2\2\u0192\u0193\7C\2\2\u0193\u0194\7t\2\2\u0194\u0195")
        buf.write("\7t\2\2\u0195\u0196\7c\2\2\u0196\u0197\7{\2\2\u0197<\3")
        buf.write("\2\2\2\u0198\u0199\7U\2\2\u0199\u019a\7v\2\2\u019a\u019b")
        buf.write("\7t\2\2\u019b\u019c\7k\2\2\u019c\u019d\7p\2\2\u019d\u019e")
        buf.write("\7i\2\2\u019e>\3\2\2\2\u019f\u01a0\7D\2\2\u01a0\u01a1")
        buf.write("\7{\2\2\u01a1@\3\2\2\2\u01a2\u01a3\7G\2\2\u01a3\u01a4")
        buf.write("\7n\2\2\u01a4\u01a5\7u\2\2\u01a5\u01a6\7g\2\2\u01a6B\3")
        buf.write("\2\2\2\u01a7\u01a8\7K\2\2\u01a8\u01a9\7p\2\2\u01a9D\3")
        buf.write("\2\2\2\u01aa\u01ab\7T\2\2\u01ab\u01ac\7g\2\2\u01ac\u01ad")
        buf.write("\7v\2\2\u01ad\u01ae\7w\2\2\u01ae\u01af\7t\2\2\u01af\u01b0")
        buf.write("\7p\2\2\u01b0F\3\2\2\2\u01b1\u01b2\7U\2\2\u01b2\u01b3")
        buf.write("\7g\2\2\u01b3\u01b4\7n\2\2\u01b4\u01b5\7h\2\2\u01b5H\3")
        buf.write("\2\2\2\u01b6\u01b7\7*\2\2\u01b7J\3\2\2\2\u01b8\u01b9\7")
        buf.write("+\2\2\u01b9L\3\2\2\2\u01ba\u01bb\7]\2\2\u01bbN\3\2\2\2")
        buf.write("\u01bc\u01bd\7_\2\2\u01bdP\3\2\2\2\u01be\u01bf\7}\2\2")
        buf.write("\u01bfR\3\2\2\2\u01c0\u01c1\7\177\2\2\u01c1T\3\2\2\2\u01c2")
        buf.write("\u01c3\7=\2\2\u01c3V\3\2\2\2\u01c4\u01c5\7.\2\2\u01c5")
        buf.write("X\3\2\2\2\u01c6\u01c7\7\60\2\2\u01c7\u01c8\7\60\2\2\u01c8")
        buf.write("Z\3\2\2\2\u01c9\u01ca\7-\2\2\u01ca\\\3\2\2\2\u01cb\u01cc")
        buf.write("\7/\2\2\u01cc^\3\2\2\2\u01cd\u01ce\7,\2\2\u01ce`\3\2\2")
        buf.write("\2\u01cf\u01d0\7\61\2\2\u01d0b\3\2\2\2\u01d1\u01d2\7\'")
        buf.write("\2\2\u01d2d\3\2\2\2\u01d3\u01d4\7#\2\2\u01d4f\3\2\2\2")
        buf.write("\u01d5\u01d6\7(\2\2\u01d6\u01d7\7(\2\2\u01d7h\3\2\2\2")
        buf.write("\u01d8\u01d9\7~\2\2\u01d9\u01da\7~\2\2\u01daj\3\2\2\2")
        buf.write("\u01db\u01dc\7?\2\2\u01dc\u01dd\7?\2\2\u01ddl\3\2\2\2")
        buf.write("\u01de\u01df\7?\2\2\u01dfn\3\2\2\2\u01e0\u01e1\7#\2\2")
        buf.write("\u01e1\u01e2\7?\2\2\u01e2p\3\2\2\2\u01e3\u01e4\7>\2\2")
        buf.write("\u01e4r\3\2\2\2\u01e5\u01e6\7>\2\2\u01e6\u01e7\7?\2\2")
        buf.write("\u01e7t\3\2\2\2\u01e8\u01e9\7@\2\2\u01e9v\3\2\2\2\u01ea")
        buf.write("\u01eb\7@\2\2\u01eb\u01ec\7?\2\2\u01ecx\3\2\2\2\u01ed")
        buf.write("\u01ee\7?\2\2\u01ee\u01ef\7?\2\2\u01ef\u01f0\7\60\2\2")
        buf.write("\u01f0z\3\2\2\2\u01f1\u01f2\7-\2\2\u01f2\u01f3\7\60\2")
        buf.write("\2\u01f3|\3\2\2\2\u01f4\u01f5\7\60\2\2\u01f5~\3\2\2\2")
        buf.write("\u01f6\u01f7\7<\2\2\u01f7\u01f8\7<\2\2\u01f8\u0080\3\2")
        buf.write("\2\2\u01f9\u01fa\7<\2\2\u01fa\u0082\3\2\2\2\u01fb\u01ff")
        buf.write("\t\13\2\2\u01fc\u01fe\t\f\2\2\u01fd\u01fc\3\2\2\2\u01fe")
        buf.write("\u0201\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2")
        buf.write("\u0200\u0084\3\2\2\2\u0201\u01ff\3\2\2\2\u0202\u0204\7")
        buf.write("&\2\2\u0203\u0205\t\f\2\2\u0204\u0203\3\2\2\2\u0205\u0206")
        buf.write("\3\2\2\2\u0206\u0204\3\2\2\2\u0206\u0207\3\2\2\2\u0207")
        buf.write("\u0086\3\2\2\2\u0208\u0209\7%\2\2\u0209\u020a\7%\2\2\u020a")
        buf.write("\u020e\3\2\2\2\u020b\u020d\13\2\2\2\u020c\u020b\3\2\2")
        buf.write("\2\u020d\u0210\3\2\2\2\u020e\u020f\3\2\2\2\u020e\u020c")
        buf.write("\3\2\2\2\u020f\u0211\3\2\2\2\u0210\u020e\3\2\2\2\u0211")
        buf.write("\u0212\7%\2\2\u0212\u0213\7%\2\2\u0213\u0214\3\2\2\2\u0214")
        buf.write("\u0215\bD\b\2\u0215\u0088\3\2\2\2\u0216\u0218\t\r\2\2")
        buf.write("\u0217\u0216\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u0217\3")
        buf.write("\2\2\2\u0219\u021a\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021c")
        buf.write("\bE\b\2\u021c\u008a\3\2\2\2\u021d\u0221\7$\2\2\u021e\u0220")
        buf.write("\5\u008fH\2\u021f\u021e\3\2\2\2\u0220\u0223\3\2\2\2\u0221")
        buf.write("\u021f\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u0224\3\2\2\2")
        buf.write("\u0223\u0221\3\2\2\2\u0224\u0225\bF\t\2\u0225\u008c\3")
        buf.write("\2\2\2\u0226\u022a\7$\2\2\u0227\u0229\5\u008fH\2\u0228")
        buf.write("\u0227\3\2\2\2\u0229\u022c\3\2\2\2\u022a\u0228\3\2\2\2")
        buf.write("\u022a\u022b\3\2\2\2\u022b\u022d\3\2\2\2\u022c\u022a\3")
        buf.write("\2\2\2\u022d\u022e\5\u0093J\2\u022e\u022f\bG\n\2\u022f")
        buf.write("\u008e\3\2\2\2\u0230\u0233\n\16\2\2\u0231\u0233\5\u0091")
        buf.write("I\2\u0232\u0230\3\2\2\2\u0232\u0231\3\2\2\2\u0233\u0090")
        buf.write("\3\2\2\2\u0234\u0235\7^\2\2\u0235\u0236\t\17\2\2\u0236")
        buf.write("\u0092\3\2\2\2\u0237\u0238\7^\2\2\u0238\u0239\n\17\2\2")
        buf.write("\u0239\u0094\3\2\2\2\u023a\u023b\13\2\2\2\u023b\u023c")
        buf.write("\bK\13\2\u023c\u0096\3\2\2\2$\2\u009c\u00a3\u00a8\u00ab")
        buf.write("\u00b3\u00b8\u00bd\u00c0\u00c8\u00cd\u00d0\u00d8\u00dd")
        buf.write("\u00e2\u00e5\u00ea\u00f2\u00f9\u00fe\u0101\u0107\u010c")
        buf.write("\u0113\u0116\u011b\u011d\u01ff\u0206\u020e\u0219\u0221")
        buf.write("\u022a\u0232\f\3\2\2\3\3\3\3\4\4\3\5\5\3\7\6\3\13\7\b")
        buf.write("\2\2\3F\b\3G\t\3K\n")
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
    BREAK = 11
    FOREACH = 12
    INT = 13
    NULL = 14
    CONSTRUCTOR = 15
    CONTINUE = 16
    TRUE = 17
    FLOAT = 18
    CLASS = 19
    DESTRUCTOR = 20
    IF = 21
    FALSE = 22
    BOOLEAN = 23
    NEW = 24
    ELSEIF = 25
    ARRAY = 26
    STRING = 27
    BY = 28
    ELSE = 29
    IN = 30
    RETURN = 31
    SELF = 32
    LB = 33
    RB = 34
    LS = 35
    RS = 36
    LP = 37
    RP = 38
    SEMI = 39
    COMMA = 40
    DOTDOT = 41
    ADD = 42
    SUBTRACT = 43
    MULTIPLY = 44
    DIVIDE = 45
    MODULO = 46
    NOT = 47
    AND = 48
    OR = 49
    EQUAL = 50
    ASSIGN = 51
    NOT_EQUAL = 52
    LESS_THAN = 53
    LEQ = 54
    GREATER_THAN = 55
    GEQ = 56
    EQUAL_STRING = 57
    STRING_CONCAT = 58
    DOT = 59
    DOUBLE_COLON = 60
    COLON = 61
    ID = 62
    DOLLAR_ID = 63
    BLOCK_COMMENT = 64
    WS = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67
    ERROR_CHAR = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Val'", "'Var'", "'Break'", "'Foreach'", "'Int'", "'Null'", 
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
            "VAL", "VAR", "BREAK", "FOREACH", "INT", "NULL", "CONSTRUCTOR", 
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
                  "VAR", "BREAK", "FOREACH", "INT", "NULL", "CONSTRUCTOR", 
                  "CONTINUE", "TRUE", "FLOAT", "CLASS", "DESTRUCTOR", "IF", 
                  "FALSE", "BOOLEAN", "NEW", "ELSEIF", "ARRAY", "STRING", 
                  "BY", "ELSE", "IN", "RETURN", "SELF", "LB", "RB", "LS", 
                  "RS", "LP", "RP", "SEMI", "COMMA", "DOTDOT", "ADD", "SUBTRACT", 
                  "MULTIPLY", "DIVIDE", "MODULO", "NOT", "AND", "OR", "EQUAL", 
                  "ASSIGN", "NOT_EQUAL", "LESS_THAN", "LEQ", "GREATER_THAN", 
                  "GEQ", "EQUAL_STRING", "STRING_CONCAT", "DOT", "DOUBLE_COLON", 
                  "COLON", "ID", "DOLLAR_ID", "BLOCK_COMMENT", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "STRING_CHAR", "ESC_SEQUENCE", "ESC_ILLEGAL", 
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
            actions[1] = self.LITERAL_INT_DEC_action 
            actions[2] = self.LITERAL_INT_HEX_action 
            actions[3] = self.LITERAL_INT_OCT_action 
            actions[5] = self.LITERAL_FLOAT_action 
            actions[9] = self.LITERAL_STRING_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
            actions[73] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def LITERAL_INT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def LITERAL_INT_DEC_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

    def LITERAL_INT_HEX_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.replace('_','')
     

    def LITERAL_INT_OCT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text.replace('_','')
     

    def LITERAL_FLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text.replace('_','')
     

    def LITERAL_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
             
            		y = str(self.text)
            		self.text = y[1:-1]
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

            		y = str(self.text)
            		possible_char = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
            		if y[-1] in possible_char:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:

            		raise ErrorToken(self.text)
            	
     


