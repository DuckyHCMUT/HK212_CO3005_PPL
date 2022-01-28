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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2I")
        buf.write("\u0256\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\3\2\3\2\5\2\u00a0\n\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\5\3\u00a7\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u00ba\n\4\3\5\3\5\5")
        buf.write("\5\u00be\n\5\3\5\7\5\u00c1\n\5\f\5\16\5\u00c4\13\5\3\6")
        buf.write("\3\6\3\6\3\6\5\6\u00ca\n\6\3\6\3\6\5\6\u00ce\n\6\3\6\7")
        buf.write("\6\u00d1\n\6\f\6\16\6\u00d4\13\6\3\7\3\7\3\7\5\7\u00d9")
        buf.write("\n\7\3\7\7\7\u00dc\n\7\f\7\16\7\u00df\13\7\3\b\3\b\3\b")
        buf.write("\3\b\5\b\u00e5\n\b\3\b\3\b\5\b\u00e9\n\b\3\b\7\b\u00ec")
        buf.write("\n\b\f\b\16\b\u00ef\13\b\3\t\3\t\3\t\5\t\u00f4\n\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\5\t\u00fc\n\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\5\n\u0103\n\n\3\n\7\n\u0106\n\n\f\n\16\n\u0109\13\n\5")
        buf.write("\n\u010b\n\n\3\13\3\13\7\13\u010f\n\13\f\13\16\13\u0112")
        buf.write("\13\13\3\f\3\f\5\f\u0116\n\f\3\f\6\f\u0119\n\f\r\f\16")
        buf.write("\f\u011a\3\r\3\r\3\r\3\r\7\r\u0121\n\r\f\r\16\r\u0124")
        buf.write("\13\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3&\3&")
        buf.write("\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*")
        buf.write("\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\3\67\38\38\38\39\39\39\3:\3:\3;\3;\3;\3<\3<\3=\3")
        buf.write("=\3=\3>\3>\3?\3?\3?\3@\3@\3@\3@\3A\3A\3A\3B\3B\3C\3C\3")
        buf.write("C\3D\3D\3E\3E\7E\u0205\nE\fE\16E\u0208\13E\3F\3F\6F\u020c")
        buf.write("\nF\rF\16F\u020d\3G\3G\3G\3G\7G\u0214\nG\fG\16G\u0217")
        buf.write("\13G\3G\3G\3G\3G\3G\3H\6H\u021f\nH\rH\16H\u0220\3H\3H")
        buf.write("\3I\3I\3J\3J\3J\7J\u022a\nJ\fJ\16J\u022d\13J\3J\5J\u0230")
        buf.write("\nJ\3J\3J\3K\3K\3K\7K\u0237\nK\fK\16K\u023a\13K\3K\3K")
        buf.write("\3K\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\5")
        buf.write("L\u024f\nL\3M\3M\3M\3N\3N\3N\3\u0215\2O\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\2\25\2\27\2\31\13\33\f\35\r\37")
        buf.write("\16!\17#\20%\21\'\22)\23+\24-\25/\26\61\27\63\30\65\31")
        buf.write("\67\329\33;\34=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[")
        buf.write(",]-_.a/c\60e\61g\62i\63k\64m\65o\66q\67s8u9w:y;{<}=\177")
        buf.write(">\u0081?\u0083@\u0085A\u0087B\u0089C\u008bD\u008dE\u008f")
        buf.write("F\u0091\2\u0093G\u0095H\u0097\2\u0099\2\u009bI\3\2\21")
        buf.write("\3\2\63;\3\2\62;\4\2\63;CH\4\2\62;CH\3\2\639\3\2\629\3")
        buf.write("\2\62\63\4\2GGgg\4\2--//\5\2C\\aac|\6\2\62;C\\aac|\5\2")
        buf.write("\n\f\16\17\"\"\5\2\f\f$$^^\3\3\f\f\t\2))^^ddhhppttvv\2")
        buf.write("\u027e\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\3\u009f\3\2\2\2\5\u00a6\3\2\2\2\7\u00b9")
        buf.write("\3\2\2\2\t\u00bb\3\2\2\2\13\u00c9\3\2\2\2\r\u00d5\3\2")
        buf.write("\2\2\17\u00e4\3\2\2\2\21\u00fb\3\2\2\2\23\u010a\3\2\2")
        buf.write("\2\25\u010c\3\2\2\2\27\u0113\3\2\2\2\31\u011c\3\2\2\2")
        buf.write("\33\u0128\3\2\2\2\35\u012b\3\2\2\2\37\u012f\3\2\2\2!\u0133")
        buf.write("\3\2\2\2#\u0135\3\2\2\2%\u013b\3\2\2\2\'\u0143\3\2\2\2")
        buf.write(")\u0147\3\2\2\2+\u014c\3\2\2\2-\u0158\3\2\2\2/\u0161\3")
        buf.write("\2\2\2\61\u0166\3\2\2\2\63\u016c\3\2\2\2\65\u0172\3\2")
        buf.write("\2\2\67\u017d\3\2\2\29\u0180\3\2\2\2;\u0186\3\2\2\2=\u018e")
        buf.write("\3\2\2\2?\u0192\3\2\2\2A\u0199\3\2\2\2C\u019f\3\2\2\2")
        buf.write("E\u01a6\3\2\2\2G\u01a9\3\2\2\2I\u01ae\3\2\2\2K\u01b1\3")
        buf.write("\2\2\2M\u01b8\3\2\2\2O\u01bd\3\2\2\2Q\u01bf\3\2\2\2S\u01c1")
        buf.write("\3\2\2\2U\u01c3\3\2\2\2W\u01c5\3\2\2\2Y\u01c7\3\2\2\2")
        buf.write("[\u01c9\3\2\2\2]\u01cb\3\2\2\2_\u01cd\3\2\2\2a\u01d0\3")
        buf.write("\2\2\2c\u01d2\3\2\2\2e\u01d4\3\2\2\2g\u01d6\3\2\2\2i\u01d8")
        buf.write("\3\2\2\2k\u01da\3\2\2\2m\u01dc\3\2\2\2o\u01df\3\2\2\2")
        buf.write("q\u01e2\3\2\2\2s\u01e5\3\2\2\2u\u01e7\3\2\2\2w\u01ea\3")
        buf.write("\2\2\2y\u01ec\3\2\2\2{\u01ef\3\2\2\2}\u01f1\3\2\2\2\177")
        buf.write("\u01f4\3\2\2\2\u0081\u01f8\3\2\2\2\u0083\u01fb\3\2\2\2")
        buf.write("\u0085\u01fd\3\2\2\2\u0087\u0200\3\2\2\2\u0089\u0202\3")
        buf.write("\2\2\2\u008b\u0209\3\2\2\2\u008d\u020f\3\2\2\2\u008f\u021e")
        buf.write("\3\2\2\2\u0091\u0224\3\2\2\2\u0093\u0226\3\2\2\2\u0095")
        buf.write("\u0233\3\2\2\2\u0097\u024e\3\2\2\2\u0099\u0250\3\2\2\2")
        buf.write("\u009b\u0253\3\2\2\2\u009d\u00a0\5/\30\2\u009e\u00a0\5")
        buf.write("9\35\2\u009f\u009d\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\4")
        buf.write("\3\2\2\2\u00a1\u00a7\5\t\5\2\u00a2\u00a7\5\13\6\2\u00a3")
        buf.write("\u00a7\5\r\7\2\u00a4\u00a7\5\17\b\2\u00a5\u00a7\5\17\b")
        buf.write("\2\u00a6\u00a1\3\2\2\2\u00a6\u00a2\3\2\2\2\u00a6\u00a3")
        buf.write("\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7")
        buf.write("\u00a8\3\2\2\2\u00a8\u00a9\b\3\2\2\u00a9\6\3\2\2\2\u00aa")
        buf.write("\u00ba\7\62\2\2\u00ab\u00ac\7\62\2\2\u00ac\u00ba\7\62")
        buf.write("\2\2\u00ad\u00ae\7\62\2\2\u00ae\u00af\7z\2\2\u00af\u00ba")
        buf.write("\7\62\2\2\u00b0\u00b1\7\62\2\2\u00b1\u00b2\7Z\2\2\u00b2")
        buf.write("\u00ba\7\62\2\2\u00b3\u00b4\7\62\2\2\u00b4\u00b5\7d\2")
        buf.write("\2\u00b5\u00ba\7\62\2\2\u00b6\u00b7\7\62\2\2\u00b7\u00b8")
        buf.write("\7D\2\2\u00b8\u00ba\7\62\2\2\u00b9\u00aa\3\2\2\2\u00b9")
        buf.write("\u00ab\3\2\2\2\u00b9\u00ad\3\2\2\2\u00b9\u00b0\3\2\2\2")
        buf.write("\u00b9\u00b3\3\2\2\2\u00b9\u00b6\3\2\2\2\u00ba\b\3\2\2")
        buf.write("\2\u00bb\u00c2\t\2\2\2\u00bc\u00be\7a\2\2\u00bd\u00bc")
        buf.write("\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf")
        buf.write("\u00c1\t\3\2\2\u00c0\u00bd\3\2\2\2\u00c1\u00c4\3\2\2\2")
        buf.write("\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\n\3\2\2")
        buf.write("\2\u00c4\u00c2\3\2\2\2\u00c5\u00c6\7\62\2\2\u00c6\u00ca")
        buf.write("\7z\2\2\u00c7\u00c8\7\62\2\2\u00c8\u00ca\7Z\2\2\u00c9")
        buf.write("\u00c5\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00cb\3\2\2\2")
        buf.write("\u00cb\u00d2\t\4\2\2\u00cc\u00ce\7a\2\2\u00cd\u00cc\3")
        buf.write("\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d1")
        buf.write("\t\5\2\2\u00d0\u00cd\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\f\3\2\2\2\u00d4")
        buf.write("\u00d2\3\2\2\2\u00d5\u00d6\7\62\2\2\u00d6\u00dd\t\6\2")
        buf.write("\2\u00d7\u00d9\7a\2\2\u00d8\u00d7\3\2\2\2\u00d8\u00d9")
        buf.write("\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00dc\t\7\2\2\u00db")
        buf.write("\u00d8\3\2\2\2\u00dc\u00df\3\2\2\2\u00dd\u00db\3\2\2\2")
        buf.write("\u00dd\u00de\3\2\2\2\u00de\16\3\2\2\2\u00df\u00dd\3\2")
        buf.write("\2\2\u00e0\u00e1\7\62\2\2\u00e1\u00e5\7d\2\2\u00e2\u00e3")
        buf.write("\7\62\2\2\u00e3\u00e5\7D\2\2\u00e4\u00e0\3\2\2\2\u00e4")
        buf.write("\u00e2\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00ed\7\63\2")
        buf.write("\2\u00e7\u00e9\7a\2\2\u00e8\u00e7\3\2\2\2\u00e8\u00e9")
        buf.write("\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00ec\t\b\2\2\u00eb")
        buf.write("\u00e8\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2")
        buf.write("\u00ed\u00ee\3\2\2\2\u00ee\20\3\2\2\2\u00ef\u00ed\3\2")
        buf.write("\2\2\u00f0\u00f1\5\23\n\2\u00f1\u00f3\5\25\13\2\u00f2")
        buf.write("\u00f4\5\27\f\2\u00f3\u00f2\3\2\2\2\u00f3\u00f4\3\2\2")
        buf.write("\2\u00f4\u00fc\3\2\2\2\u00f5\u00f6\5\23\n\2\u00f6\u00f7")
        buf.write("\5\27\f\2\u00f7\u00fc\3\2\2\2\u00f8\u00f9\5\25\13\2\u00f9")
        buf.write("\u00fa\5\27\f\2\u00fa\u00fc\3\2\2\2\u00fb\u00f0\3\2\2")
        buf.write("\2\u00fb\u00f5\3\2\2\2\u00fb\u00f8\3\2\2\2\u00fc\u00fd")
        buf.write("\3\2\2\2\u00fd\u00fe\b\t\3\2\u00fe\22\3\2\2\2\u00ff\u010b")
        buf.write("\7\62\2\2\u0100\u0107\t\2\2\2\u0101\u0103\7a\2\2\u0102")
        buf.write("\u0101\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0104\3\2\2\2")
        buf.write("\u0104\u0106\t\3\2\2\u0105\u0102\3\2\2\2\u0106\u0109\3")
        buf.write("\2\2\2\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u010b")
        buf.write("\3\2\2\2\u0109\u0107\3\2\2\2\u010a\u00ff\3\2\2\2\u010a")
        buf.write("\u0100\3\2\2\2\u010b\24\3\2\2\2\u010c\u0110\5\u0083B\2")
        buf.write("\u010d\u010f\t\3\2\2\u010e\u010d\3\2\2\2\u010f\u0112\3")
        buf.write("\2\2\2\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\26")
        buf.write("\3\2\2\2\u0112\u0110\3\2\2\2\u0113\u0115\t\t\2\2\u0114")
        buf.write("\u0116\t\n\2\2\u0115\u0114\3\2\2\2\u0115\u0116\3\2\2\2")
        buf.write("\u0116\u0118\3\2\2\2\u0117\u0119\t\3\2\2\u0118\u0117\3")
        buf.write("\2\2\2\u0119\u011a\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u011b")
        buf.write("\3\2\2\2\u011b\30\3\2\2\2\u011c\u0122\7$\2\2\u011d\u0121")
        buf.write("\5\u0091I\2\u011e\u0121\5\33\16\2\u011f\u0121\5\u0097")
        buf.write("L\2\u0120\u011d\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u011f")
        buf.write("\3\2\2\2\u0121\u0124\3\2\2\2\u0122\u0120\3\2\2\2\u0122")
        buf.write("\u0123\3\2\2\2\u0123\u0125\3\2\2\2\u0124\u0122\3\2\2\2")
        buf.write("\u0125\u0126\7$\2\2\u0126\u0127\b\r\4\2\u0127\32\3\2\2")
        buf.write("\2\u0128\u0129\7)\2\2\u0129\u012a\7$\2\2\u012a\34\3\2")
        buf.write("\2\2\u012b\u012c\7X\2\2\u012c\u012d\7c\2\2\u012d\u012e")
        buf.write("\7n\2\2\u012e\36\3\2\2\2\u012f\u0130\7X\2\2\u0130\u0131")
        buf.write("\7c\2\2\u0131\u0132\7t\2\2\u0132 \3\2\2\2\u0133\u0134")
        buf.write("\7&\2\2\u0134\"\3\2\2\2\u0135\u0136\7D\2\2\u0136\u0137")
        buf.write("\7t\2\2\u0137\u0138\7g\2\2\u0138\u0139\7c\2\2\u0139\u013a")
        buf.write("\7m\2\2\u013a$\3\2\2\2\u013b\u013c\7H\2\2\u013c\u013d")
        buf.write("\7q\2\2\u013d\u013e\7t\2\2\u013e\u013f\7g\2\2\u013f\u0140")
        buf.write("\7c\2\2\u0140\u0141\7e\2\2\u0141\u0142\7j\2\2\u0142&\3")
        buf.write("\2\2\2\u0143\u0144\7K\2\2\u0144\u0145\7p\2\2\u0145\u0146")
        buf.write("\7v\2\2\u0146(\3\2\2\2\u0147\u0148\7P\2\2\u0148\u0149")
        buf.write("\7w\2\2\u0149\u014a\7n\2\2\u014a\u014b\7n\2\2\u014b*\3")
        buf.write("\2\2\2\u014c\u014d\7E\2\2\u014d\u014e\7q\2\2\u014e\u014f")
        buf.write("\7p\2\2\u014f\u0150\7u\2\2\u0150\u0151\7v\2\2\u0151\u0152")
        buf.write("\7t\2\2\u0152\u0153\7w\2\2\u0153\u0154\7e\2\2\u0154\u0155")
        buf.write("\7v\2\2\u0155\u0156\7q\2\2\u0156\u0157\7t\2\2\u0157,\3")
        buf.write("\2\2\2\u0158\u0159\7E\2\2\u0159\u015a\7q\2\2\u015a\u015b")
        buf.write("\7p\2\2\u015b\u015c\7v\2\2\u015c\u015d\7k\2\2\u015d\u015e")
        buf.write("\7p\2\2\u015e\u015f\7w\2\2\u015f\u0160\7g\2\2\u0160.\3")
        buf.write("\2\2\2\u0161\u0162\7V\2\2\u0162\u0163\7t\2\2\u0163\u0164")
        buf.write("\7w\2\2\u0164\u0165\7g\2\2\u0165\60\3\2\2\2\u0166\u0167")
        buf.write("\7H\2\2\u0167\u0168\7n\2\2\u0168\u0169\7q\2\2\u0169\u016a")
        buf.write("\7c\2\2\u016a\u016b\7v\2\2\u016b\62\3\2\2\2\u016c\u016d")
        buf.write("\7E\2\2\u016d\u016e\7n\2\2\u016e\u016f\7c\2\2\u016f\u0170")
        buf.write("\7u\2\2\u0170\u0171\7u\2\2\u0171\64\3\2\2\2\u0172\u0173")
        buf.write("\7F\2\2\u0173\u0174\7g\2\2\u0174\u0175\7u\2\2\u0175\u0176")
        buf.write("\7v\2\2\u0176\u0177\7t\2\2\u0177\u0178\7w\2\2\u0178\u0179")
        buf.write("\7e\2\2\u0179\u017a\7v\2\2\u017a\u017b\7q\2\2\u017b\u017c")
        buf.write("\7t\2\2\u017c\66\3\2\2\2\u017d\u017e\7K\2\2\u017e\u017f")
        buf.write("\7h\2\2\u017f8\3\2\2\2\u0180\u0181\7H\2\2\u0181\u0182")
        buf.write("\7c\2\2\u0182\u0183\7n\2\2\u0183\u0184\7u\2\2\u0184\u0185")
        buf.write("\7g\2\2\u0185:\3\2\2\2\u0186\u0187\7D\2\2\u0187\u0188")
        buf.write("\7q\2\2\u0188\u0189\7q\2\2\u0189\u018a\7n\2\2\u018a\u018b")
        buf.write("\7g\2\2\u018b\u018c\7c\2\2\u018c\u018d\7p\2\2\u018d<\3")
        buf.write("\2\2\2\u018e\u018f\7P\2\2\u018f\u0190\7g\2\2\u0190\u0191")
        buf.write("\7y\2\2\u0191>\3\2\2\2\u0192\u0193\7G\2\2\u0193\u0194")
        buf.write("\7n\2\2\u0194\u0195\7u\2\2\u0195\u0196\7g\2\2\u0196\u0197")
        buf.write("\7k\2\2\u0197\u0198\7h\2\2\u0198@\3\2\2\2\u0199\u019a")
        buf.write("\7C\2\2\u019a\u019b\7t\2\2\u019b\u019c\7t\2\2\u019c\u019d")
        buf.write("\7c\2\2\u019d\u019e\7{\2\2\u019eB\3\2\2\2\u019f\u01a0")
        buf.write("\7U\2\2\u01a0\u01a1\7v\2\2\u01a1\u01a2\7t\2\2\u01a2\u01a3")
        buf.write("\7k\2\2\u01a3\u01a4\7p\2\2\u01a4\u01a5\7i\2\2\u01a5D\3")
        buf.write("\2\2\2\u01a6\u01a7\7D\2\2\u01a7\u01a8\7{\2\2\u01a8F\3")
        buf.write("\2\2\2\u01a9\u01aa\7G\2\2\u01aa\u01ab\7n\2\2\u01ab\u01ac")
        buf.write("\7u\2\2\u01ac\u01ad\7g\2\2\u01adH\3\2\2\2\u01ae\u01af")
        buf.write("\7K\2\2\u01af\u01b0\7p\2\2\u01b0J\3\2\2\2\u01b1\u01b2")
        buf.write("\7T\2\2\u01b2\u01b3\7g\2\2\u01b3\u01b4\7v\2\2\u01b4\u01b5")
        buf.write("\7w\2\2\u01b5\u01b6\7t\2\2\u01b6\u01b7\7p\2\2\u01b7L\3")
        buf.write("\2\2\2\u01b8\u01b9\7U\2\2\u01b9\u01ba\7g\2\2\u01ba\u01bb")
        buf.write("\7n\2\2\u01bb\u01bc\7h\2\2\u01bcN\3\2\2\2\u01bd\u01be")
        buf.write("\7*\2\2\u01beP\3\2\2\2\u01bf\u01c0\7+\2\2\u01c0R\3\2\2")
        buf.write("\2\u01c1\u01c2\7]\2\2\u01c2T\3\2\2\2\u01c3\u01c4\7_\2")
        buf.write("\2\u01c4V\3\2\2\2\u01c5\u01c6\7}\2\2\u01c6X\3\2\2\2\u01c7")
        buf.write("\u01c8\7\177\2\2\u01c8Z\3\2\2\2\u01c9\u01ca\7=\2\2\u01ca")
        buf.write("\\\3\2\2\2\u01cb\u01cc\7.\2\2\u01cc^\3\2\2\2\u01cd\u01ce")
        buf.write("\7\60\2\2\u01ce\u01cf\7\60\2\2\u01cf`\3\2\2\2\u01d0\u01d1")
        buf.write("\7-\2\2\u01d1b\3\2\2\2\u01d2\u01d3\7/\2\2\u01d3d\3\2\2")
        buf.write("\2\u01d4\u01d5\7,\2\2\u01d5f\3\2\2\2\u01d6\u01d7\7\61")
        buf.write("\2\2\u01d7h\3\2\2\2\u01d8\u01d9\7\'\2\2\u01d9j\3\2\2\2")
        buf.write("\u01da\u01db\7#\2\2\u01dbl\3\2\2\2\u01dc\u01dd\7(\2\2")
        buf.write("\u01dd\u01de\7(\2\2\u01den\3\2\2\2\u01df\u01e0\7~\2\2")
        buf.write("\u01e0\u01e1\7~\2\2\u01e1p\3\2\2\2\u01e2\u01e3\7?\2\2")
        buf.write("\u01e3\u01e4\7?\2\2\u01e4r\3\2\2\2\u01e5\u01e6\7?\2\2")
        buf.write("\u01e6t\3\2\2\2\u01e7\u01e8\7#\2\2\u01e8\u01e9\7?\2\2")
        buf.write("\u01e9v\3\2\2\2\u01ea\u01eb\7>\2\2\u01ebx\3\2\2\2\u01ec")
        buf.write("\u01ed\7>\2\2\u01ed\u01ee\7?\2\2\u01eez\3\2\2\2\u01ef")
        buf.write("\u01f0\7@\2\2\u01f0|\3\2\2\2\u01f1\u01f2\7@\2\2\u01f2")
        buf.write("\u01f3\7?\2\2\u01f3~\3\2\2\2\u01f4\u01f5\7?\2\2\u01f5")
        buf.write("\u01f6\7?\2\2\u01f6\u01f7\7\60\2\2\u01f7\u0080\3\2\2\2")
        buf.write("\u01f8\u01f9\7-\2\2\u01f9\u01fa\7\60\2\2\u01fa\u0082\3")
        buf.write("\2\2\2\u01fb\u01fc\7\60\2\2\u01fc\u0084\3\2\2\2\u01fd")
        buf.write("\u01fe\7<\2\2\u01fe\u01ff\7<\2\2\u01ff\u0086\3\2\2\2\u0200")
        buf.write("\u0201\7<\2\2\u0201\u0088\3\2\2\2\u0202\u0206\t\13\2\2")
        buf.write("\u0203\u0205\t\f\2\2\u0204\u0203\3\2\2\2\u0205\u0208\3")
        buf.write("\2\2\2\u0206\u0204\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u008a")
        buf.write("\3\2\2\2\u0208\u0206\3\2\2\2\u0209\u020b\5!\21\2\u020a")
        buf.write("\u020c\t\f\2\2\u020b\u020a\3\2\2\2\u020c\u020d\3\2\2\2")
        buf.write("\u020d\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u008c\3")
        buf.write("\2\2\2\u020f\u0210\7%\2\2\u0210\u0211\7%\2\2\u0211\u0215")
        buf.write("\3\2\2\2\u0212\u0214\13\2\2\2\u0213\u0212\3\2\2\2\u0214")
        buf.write("\u0217\3\2\2\2\u0215\u0216\3\2\2\2\u0215\u0213\3\2\2\2")
        buf.write("\u0216\u0218\3\2\2\2\u0217\u0215\3\2\2\2\u0218\u0219\7")
        buf.write("%\2\2\u0219\u021a\7%\2\2\u021a\u021b\3\2\2\2\u021b\u021c")
        buf.write("\bG\5\2\u021c\u008e\3\2\2\2\u021d\u021f\t\r\2\2\u021e")
        buf.write("\u021d\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u021e\3\2\2\2")
        buf.write("\u0220\u0221\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u0223\b")
        buf.write("H\5\2\u0223\u0090\3\2\2\2\u0224\u0225\n\16\2\2\u0225\u0092")
        buf.write("\3\2\2\2\u0226\u022b\7$\2\2\u0227\u022a\5\u0091I\2\u0228")
        buf.write("\u022a\5\u0097L\2\u0229\u0227\3\2\2\2\u0229\u0228\3\2")
        buf.write("\2\2\u022a\u022d\3\2\2\2\u022b\u0229\3\2\2\2\u022b\u022c")
        buf.write("\3\2\2\2\u022c\u022f\3\2\2\2\u022d\u022b\3\2\2\2\u022e")
        buf.write("\u0230\t\17\2\2\u022f\u022e\3\2\2\2\u0230\u0231\3\2\2")
        buf.write("\2\u0231\u0232\bJ\6\2\u0232\u0094\3\2\2\2\u0233\u0238")
        buf.write("\7$\2\2\u0234\u0237\5\u0091I\2\u0235\u0237\5\u0097L\2")
        buf.write("\u0236\u0234\3\2\2\2\u0236\u0235\3\2\2\2\u0237\u023a\3")
        buf.write("\2\2\2\u0238\u0236\3\2\2\2\u0238\u0239\3\2\2\2\u0239\u023b")
        buf.write("\3\2\2\2\u023a\u0238\3\2\2\2\u023b\u023c\5\u0099M\2\u023c")
        buf.write("\u023d\bK\7\2\u023d\u0096\3\2\2\2\u023e\u023f\7^\2\2\u023f")
        buf.write("\u024f\7d\2\2\u0240\u0241\7^\2\2\u0241\u024f\7h\2\2\u0242")
        buf.write("\u0243\7^\2\2\u0243\u024f\7t\2\2\u0244\u0245\7^\2\2\u0245")
        buf.write("\u024f\7p\2\2\u0246\u0247\7^\2\2\u0247\u024f\7v\2\2\u0248")
        buf.write("\u0249\7^\2\2\u0249\u024f\7)\2\2\u024a\u024b\7^\2\2\u024b")
        buf.write("\u024f\7^\2\2\u024c\u024d\7)\2\2\u024d\u024f\7$\2\2\u024e")
        buf.write("\u023e\3\2\2\2\u024e\u0240\3\2\2\2\u024e\u0242\3\2\2\2")
        buf.write("\u024e\u0244\3\2\2\2\u024e\u0246\3\2\2\2\u024e\u0248\3")
        buf.write("\2\2\2\u024e\u024a\3\2\2\2\u024e\u024c\3\2\2\2\u024f\u0098")
        buf.write("\3\2\2\2\u0250\u0251\7^\2\2\u0251\u0252\n\20\2\2\u0252")
        buf.write("\u009a\3\2\2\2\u0253\u0254\13\2\2\2\u0254\u0255\bN\b\2")
        buf.write("\u0255\u009c\3\2\2\2$\2\u009f\u00a6\u00b9\u00bd\u00c2")
        buf.write("\u00c9\u00cd\u00d2\u00d8\u00dd\u00e4\u00e8\u00ed\u00f3")
        buf.write("\u00fb\u0102\u0107\u010a\u0110\u0115\u011a\u0120\u0122")
        buf.write("\u0206\u020d\u0215\u0220\u0229\u022b\u022f\u0236\u0238")
        buf.write("\u024e\t\3\3\2\3\t\3\3\r\4\b\2\2\3J\5\3K\6\3N\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LITERAL_BOOLEAN = 1
    LITERAL_INT = 2
    LITERAL_ZERO = 3
    LITERAL_INT_DEC = 4
    LITERAL_INT_HEX = 5
    LITERAL_INT_OCT = 6
    LITERAL_INT_BIN = 7
    LITERAL_FLOAT = 8
    LITERAL_STRING = 9
    DOUBLE_QUOTE = 10
    VAL = 11
    VAR = 12
    STATIC = 13
    BREAK = 14
    FOREACH = 15
    INT = 16
    NULL = 17
    CONSTRUCTOR = 18
    CONTINUE = 19
    TRUE = 20
    FLOAT = 21
    CLASS = 22
    DESTRUCTOR = 23
    IF = 24
    FALSE = 25
    BOOLEAN = 26
    NEW = 27
    ELSEIF = 28
    ARRAY = 29
    STRING = 30
    BY = 31
    ELSE = 32
    IN = 33
    RETURN = 34
    SELF = 35
    LB = 36
    RB = 37
    LS = 38
    RS = 39
    LP = 40
    RP = 41
    SEMI = 42
    COMMA = 43
    DOTDOT = 44
    ADD = 45
    SUBTRACT = 46
    MULTIPLY = 47
    DIVIDE = 48
    MODULO = 49
    NOT = 50
    AND = 51
    OR = 52
    EQUAL = 53
    ASSIGN = 54
    NOT_EQUAL = 55
    LESS_THAN = 56
    LEQ = 57
    GREATER_THAN = 58
    GEQ = 59
    EQUAL_STRING = 60
    STRING_CONCAT = 61
    DOT = 62
    DOUBLE_COLON = 63
    COLON = 64
    ID = 65
    DOLLAR_ID = 66
    BLOCK_COMMENT = 67
    WS = 68
    UNCLOSE_STRING = 69
    ILLEGAL_ESCAPE = 70
    ERROR_CHAR = 71

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
            "LITERAL_BOOLEAN", "LITERAL_INT", "LITERAL_ZERO", "LITERAL_INT_DEC", 
            "LITERAL_INT_HEX", "LITERAL_INT_OCT", "LITERAL_INT_BIN", "LITERAL_FLOAT", 
            "LITERAL_STRING", "DOUBLE_QUOTE", "VAL", "VAR", "STATIC", "BREAK", 
            "FOREACH", "INT", "NULL", "CONSTRUCTOR", "CONTINUE", "TRUE", 
            "FLOAT", "CLASS", "DESTRUCTOR", "IF", "FALSE", "BOOLEAN", "NEW", 
            "ELSEIF", "ARRAY", "STRING", "BY", "ELSE", "IN", "RETURN", "SELF", 
            "LB", "RB", "LS", "RS", "LP", "RP", "SEMI", "COMMA", "DOTDOT", 
            "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", "MODULO", "NOT", "AND", 
            "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", "LESS_THAN", "LEQ", "GREATER_THAN", 
            "GEQ", "EQUAL_STRING", "STRING_CONCAT", "DOT", "DOUBLE_COLON", 
            "COLON", "ID", "DOLLAR_ID", "BLOCK_COMMENT", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "LITERAL_BOOLEAN", "LITERAL_INT", "LITERAL_ZERO", "LITERAL_INT_DEC", 
                  "LITERAL_INT_HEX", "LITERAL_INT_OCT", "LITERAL_INT_BIN", 
                  "LITERAL_FLOAT", "FLOAT_INT", "FLOAT_DECIMAL", "FLOAT_EXP", 
                  "LITERAL_STRING", "DOUBLE_QUOTE", "VAL", "VAR", "STATIC", 
                  "BREAK", "FOREACH", "INT", "NULL", "CONSTRUCTOR", "CONTINUE", 
                  "TRUE", "FLOAT", "CLASS", "DESTRUCTOR", "IF", "FALSE", 
                  "BOOLEAN", "NEW", "ELSEIF", "ARRAY", "STRING", "BY", "ELSE", 
                  "IN", "RETURN", "SELF", "LB", "RB", "LS", "RS", "LP", 
                  "RP", "SEMI", "COMMA", "DOTDOT", "ADD", "SUBTRACT", "MULTIPLY", 
                  "DIVIDE", "MODULO", "NOT", "AND", "OR", "EQUAL", "ASSIGN", 
                  "NOT_EQUAL", "LESS_THAN", "LEQ", "GREATER_THAN", "GEQ", 
                  "EQUAL_STRING", "STRING_CONCAT", "DOT", "DOUBLE_COLON", 
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
            actions[1] = self.LITERAL_INT_action 
            actions[7] = self.LITERAL_FLOAT_action 
            actions[11] = self.LITERAL_STRING_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
            actions[76] = self.ERROR_CHAR_action 
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
            	esc = ['\n']
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
            	
     


