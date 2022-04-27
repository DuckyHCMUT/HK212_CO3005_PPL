# Generated from d:\HCMUT\Semester 212\Principles of Programming Languages\HK212_CO3005_PPL\assignment4\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2I")
        buf.write("\u0255\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\3\2\3\2\5\2\u00a0\n\2\3\3\3\3\3\3\3\3\5")
        buf.write("\3\u00a6\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u00b9\n\4\3\5\3\5\5\5\u00bd")
        buf.write("\n\5\3\5\7\5\u00c0\n\5\f\5\16\5\u00c3\13\5\3\6\3\6\3\6")
        buf.write("\3\6\5\6\u00c9\n\6\3\6\3\6\5\6\u00cd\n\6\3\6\7\6\u00d0")
        buf.write("\n\6\f\6\16\6\u00d3\13\6\3\7\3\7\3\7\5\7\u00d8\n\7\3\7")
        buf.write("\7\7\u00db\n\7\f\7\16\7\u00de\13\7\3\b\3\b\3\b\3\b\5\b")
        buf.write("\u00e4\n\b\3\b\3\b\5\b\u00e8\n\b\3\b\7\b\u00eb\n\b\f\b")
        buf.write("\16\b\u00ee\13\b\3\t\3\t\3\t\5\t\u00f3\n\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\5\t\u00fb\n\t\3\t\3\t\3\n\3\n\3\n\5\n\u0102")
        buf.write("\n\n\3\n\7\n\u0105\n\n\f\n\16\n\u0108\13\n\5\n\u010a\n")
        buf.write("\n\3\13\3\13\7\13\u010e\n\13\f\13\16\13\u0111\13\13\3")
        buf.write("\f\3\f\5\f\u0115\n\f\3\f\6\f\u0118\n\f\r\f\16\f\u0119")
        buf.write("\3\r\3\r\3\r\3\r\7\r\u0120\n\r\f\r\16\r\u0123\13\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write(",\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3")
        buf.write("\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\3\67\38\38\38\39\39\39\3:\3:\3;\3;\3;\3<\3<\3=\3=\3=")
        buf.write("\3>\3>\3?\3?\3?\3@\3@\3@\3@\3A\3A\3A\3B\3B\3C\3C\3C\3")
        buf.write("D\3D\3E\3E\7E\u0204\nE\fE\16E\u0207\13E\3F\3F\6F\u020b")
        buf.write("\nF\rF\16F\u020c\3G\3G\3G\3G\7G\u0213\nG\fG\16G\u0216")
        buf.write("\13G\3G\3G\3G\3G\3G\3H\6H\u021e\nH\rH\16H\u021f\3H\3H")
        buf.write("\3I\3I\3J\3J\3J\7J\u0229\nJ\fJ\16J\u022c\13J\3J\5J\u022f")
        buf.write("\nJ\3J\3J\3K\3K\3K\7K\u0236\nK\fK\16K\u0239\13K\3K\3K")
        buf.write("\3K\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\5")
        buf.write("L\u024e\nL\3M\3M\3M\3N\3N\3N\3\u0214\2O\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\2\25\2\27\2\31\13\33\f\35\r\37")
        buf.write("\16!\17#\20%\21\'\22)\23+\24-\25/\26\61\27\63\30\65\31")
        buf.write("\67\329\33;\34=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[")
        buf.write(",]-_.a/c\60e\61g\62i\63k\64m\65o\66q\67s8u9w:y;{<}=\177")
        buf.write(">\u0081?\u0083@\u0085A\u0087B\u0089C\u008bD\u008dE\u008f")
        buf.write("F\u0091\2\u0093G\u0095H\u0097\2\u0099\2\u009bI\3\2\21")
        buf.write("\3\2\63;\3\2\62;\4\2\63;CH\4\2\62;CH\3\2\639\3\2\629\3")
        buf.write("\2\62\63\4\2GGgg\4\2--//\5\2C\\aac|\6\2\62;C\\aac|\5\2")
        buf.write("\n\f\16\17\"\"\5\2\f\f$$^^\3\3\f\f\t\2))^^ddhhppttvv\2")
        buf.write("\u027c\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
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
        buf.write("\2\2\u009b\3\2\2\2\3\u009f\3\2\2\2\5\u00a5\3\2\2\2\7\u00b8")
        buf.write("\3\2\2\2\t\u00ba\3\2\2\2\13\u00c8\3\2\2\2\r\u00d4\3\2")
        buf.write("\2\2\17\u00e3\3\2\2\2\21\u00fa\3\2\2\2\23\u0109\3\2\2")
        buf.write("\2\25\u010b\3\2\2\2\27\u0112\3\2\2\2\31\u011b\3\2\2\2")
        buf.write("\33\u0127\3\2\2\2\35\u012a\3\2\2\2\37\u012e\3\2\2\2!\u0132")
        buf.write("\3\2\2\2#\u0134\3\2\2\2%\u013a\3\2\2\2\'\u0142\3\2\2\2")
        buf.write(")\u0146\3\2\2\2+\u014b\3\2\2\2-\u0157\3\2\2\2/\u0160\3")
        buf.write("\2\2\2\61\u0165\3\2\2\2\63\u016b\3\2\2\2\65\u0171\3\2")
        buf.write("\2\2\67\u017c\3\2\2\29\u017f\3\2\2\2;\u0185\3\2\2\2=\u018d")
        buf.write("\3\2\2\2?\u0191\3\2\2\2A\u0198\3\2\2\2C\u019e\3\2\2\2")
        buf.write("E\u01a5\3\2\2\2G\u01a8\3\2\2\2I\u01ad\3\2\2\2K\u01b0\3")
        buf.write("\2\2\2M\u01b7\3\2\2\2O\u01bc\3\2\2\2Q\u01be\3\2\2\2S\u01c0")
        buf.write("\3\2\2\2U\u01c2\3\2\2\2W\u01c4\3\2\2\2Y\u01c6\3\2\2\2")
        buf.write("[\u01c8\3\2\2\2]\u01ca\3\2\2\2_\u01cc\3\2\2\2a\u01cf\3")
        buf.write("\2\2\2c\u01d1\3\2\2\2e\u01d3\3\2\2\2g\u01d5\3\2\2\2i\u01d7")
        buf.write("\3\2\2\2k\u01d9\3\2\2\2m\u01db\3\2\2\2o\u01de\3\2\2\2")
        buf.write("q\u01e1\3\2\2\2s\u01e4\3\2\2\2u\u01e6\3\2\2\2w\u01e9\3")
        buf.write("\2\2\2y\u01eb\3\2\2\2{\u01ee\3\2\2\2}\u01f0\3\2\2\2\177")
        buf.write("\u01f3\3\2\2\2\u0081\u01f7\3\2\2\2\u0083\u01fa\3\2\2\2")
        buf.write("\u0085\u01fc\3\2\2\2\u0087\u01ff\3\2\2\2\u0089\u0201\3")
        buf.write("\2\2\2\u008b\u0208\3\2\2\2\u008d\u020e\3\2\2\2\u008f\u021d")
        buf.write("\3\2\2\2\u0091\u0223\3\2\2\2\u0093\u0225\3\2\2\2\u0095")
        buf.write("\u0232\3\2\2\2\u0097\u024d\3\2\2\2\u0099\u024f\3\2\2\2")
        buf.write("\u009b\u0252\3\2\2\2\u009d\u00a0\5/\30\2\u009e\u00a0\5")
        buf.write("9\35\2\u009f\u009d\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\4")
        buf.write("\3\2\2\2\u00a1\u00a6\5\t\5\2\u00a2\u00a6\5\13\6\2\u00a3")
        buf.write("\u00a6\5\r\7\2\u00a4\u00a6\5\17\b\2\u00a5\u00a1\3\2\2")
        buf.write("\2\u00a5\u00a2\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a4")
        buf.write("\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a8\b\3\2\2\u00a8")
        buf.write("\6\3\2\2\2\u00a9\u00b9\7\62\2\2\u00aa\u00ab\7\62\2\2\u00ab")
        buf.write("\u00b9\7\62\2\2\u00ac\u00ad\7\62\2\2\u00ad\u00ae\7z\2")
        buf.write("\2\u00ae\u00b9\7\62\2\2\u00af\u00b0\7\62\2\2\u00b0\u00b1")
        buf.write("\7Z\2\2\u00b1\u00b9\7\62\2\2\u00b2\u00b3\7\62\2\2\u00b3")
        buf.write("\u00b4\7d\2\2\u00b4\u00b9\7\62\2\2\u00b5\u00b6\7\62\2")
        buf.write("\2\u00b6\u00b7\7D\2\2\u00b7\u00b9\7\62\2\2\u00b8\u00a9")
        buf.write("\3\2\2\2\u00b8\u00aa\3\2\2\2\u00b8\u00ac\3\2\2\2\u00b8")
        buf.write("\u00af\3\2\2\2\u00b8\u00b2\3\2\2\2\u00b8\u00b5\3\2\2\2")
        buf.write("\u00b9\b\3\2\2\2\u00ba\u00c1\t\2\2\2\u00bb\u00bd\7a\2")
        buf.write("\2\u00bc\u00bb\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00be")
        buf.write("\3\2\2\2\u00be\u00c0\t\3\2\2\u00bf\u00bc\3\2\2\2\u00c0")
        buf.write("\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2")
        buf.write("\u00c2\n\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c5\7\62")
        buf.write("\2\2\u00c5\u00c9\7z\2\2\u00c6\u00c7\7\62\2\2\u00c7\u00c9")
        buf.write("\7Z\2\2\u00c8\u00c4\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9")
        buf.write("\u00ca\3\2\2\2\u00ca\u00d1\t\4\2\2\u00cb\u00cd\7a\2\2")
        buf.write("\u00cc\u00cb\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce\3")
        buf.write("\2\2\2\u00ce\u00d0\t\5\2\2\u00cf\u00cc\3\2\2\2\u00d0\u00d3")
        buf.write("\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2")
        buf.write("\f\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00d5\7\62\2\2\u00d5")
        buf.write("\u00dc\t\6\2\2\u00d6\u00d8\7a\2\2\u00d7\u00d6\3\2\2\2")
        buf.write("\u00d7\u00d8\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00db\t")
        buf.write("\7\2\2\u00da\u00d7\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da")
        buf.write("\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\16\3\2\2\2\u00de\u00dc")
        buf.write("\3\2\2\2\u00df\u00e0\7\62\2\2\u00e0\u00e4\7d\2\2\u00e1")
        buf.write("\u00e2\7\62\2\2\u00e2\u00e4\7D\2\2\u00e3\u00df\3\2\2\2")
        buf.write("\u00e3\u00e1\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00ec\7")
        buf.write("\63\2\2\u00e6\u00e8\7a\2\2\u00e7\u00e6\3\2\2\2\u00e7\u00e8")
        buf.write("\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00eb\t\b\2\2\u00ea")
        buf.write("\u00e7\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2")
        buf.write("\u00ec\u00ed\3\2\2\2\u00ed\20\3\2\2\2\u00ee\u00ec\3\2")
        buf.write("\2\2\u00ef\u00f0\5\23\n\2\u00f0\u00f2\5\25\13\2\u00f1")
        buf.write("\u00f3\5\27\f\2\u00f2\u00f1\3\2\2\2\u00f2\u00f3\3\2\2")
        buf.write("\2\u00f3\u00fb\3\2\2\2\u00f4\u00f5\5\23\n\2\u00f5\u00f6")
        buf.write("\5\27\f\2\u00f6\u00fb\3\2\2\2\u00f7\u00f8\5\25\13\2\u00f8")
        buf.write("\u00f9\5\27\f\2\u00f9\u00fb\3\2\2\2\u00fa\u00ef\3\2\2")
        buf.write("\2\u00fa\u00f4\3\2\2\2\u00fa\u00f7\3\2\2\2\u00fb\u00fc")
        buf.write("\3\2\2\2\u00fc\u00fd\b\t\3\2\u00fd\22\3\2\2\2\u00fe\u010a")
        buf.write("\7\62\2\2\u00ff\u0106\t\2\2\2\u0100\u0102\7a\2\2\u0101")
        buf.write("\u0100\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0103\3\2\2\2")
        buf.write("\u0103\u0105\t\3\2\2\u0104\u0101\3\2\2\2\u0105\u0108\3")
        buf.write("\2\2\2\u0106\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u010a")
        buf.write("\3\2\2\2\u0108\u0106\3\2\2\2\u0109\u00fe\3\2\2\2\u0109")
        buf.write("\u00ff\3\2\2\2\u010a\24\3\2\2\2\u010b\u010f\5\u0083B\2")
        buf.write("\u010c\u010e\t\3\2\2\u010d\u010c\3\2\2\2\u010e\u0111\3")
        buf.write("\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110\26")
        buf.write("\3\2\2\2\u0111\u010f\3\2\2\2\u0112\u0114\t\t\2\2\u0113")
        buf.write("\u0115\t\n\2\2\u0114\u0113\3\2\2\2\u0114\u0115\3\2\2\2")
        buf.write("\u0115\u0117\3\2\2\2\u0116\u0118\t\3\2\2\u0117\u0116\3")
        buf.write("\2\2\2\u0118\u0119\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u011a")
        buf.write("\3\2\2\2\u011a\30\3\2\2\2\u011b\u0121\7$\2\2\u011c\u0120")
        buf.write("\5\u0091I\2\u011d\u0120\5\33\16\2\u011e\u0120\5\u0097")
        buf.write("L\2\u011f\u011c\3\2\2\2\u011f\u011d\3\2\2\2\u011f\u011e")
        buf.write("\3\2\2\2\u0120\u0123\3\2\2\2\u0121\u011f\3\2\2\2\u0121")
        buf.write("\u0122\3\2\2\2\u0122\u0124\3\2\2\2\u0123\u0121\3\2\2\2")
        buf.write("\u0124\u0125\7$\2\2\u0125\u0126\b\r\4\2\u0126\32\3\2\2")
        buf.write("\2\u0127\u0128\7)\2\2\u0128\u0129\7$\2\2\u0129\34\3\2")
        buf.write("\2\2\u012a\u012b\7X\2\2\u012b\u012c\7c\2\2\u012c\u012d")
        buf.write("\7n\2\2\u012d\36\3\2\2\2\u012e\u012f\7X\2\2\u012f\u0130")
        buf.write("\7c\2\2\u0130\u0131\7t\2\2\u0131 \3\2\2\2\u0132\u0133")
        buf.write("\7&\2\2\u0133\"\3\2\2\2\u0134\u0135\7D\2\2\u0135\u0136")
        buf.write("\7t\2\2\u0136\u0137\7g\2\2\u0137\u0138\7c\2\2\u0138\u0139")
        buf.write("\7m\2\2\u0139$\3\2\2\2\u013a\u013b\7H\2\2\u013b\u013c")
        buf.write("\7q\2\2\u013c\u013d\7t\2\2\u013d\u013e\7g\2\2\u013e\u013f")
        buf.write("\7c\2\2\u013f\u0140\7e\2\2\u0140\u0141\7j\2\2\u0141&\3")
        buf.write("\2\2\2\u0142\u0143\7K\2\2\u0143\u0144\7p\2\2\u0144\u0145")
        buf.write("\7v\2\2\u0145(\3\2\2\2\u0146\u0147\7P\2\2\u0147\u0148")
        buf.write("\7w\2\2\u0148\u0149\7n\2\2\u0149\u014a\7n\2\2\u014a*\3")
        buf.write("\2\2\2\u014b\u014c\7E\2\2\u014c\u014d\7q\2\2\u014d\u014e")
        buf.write("\7p\2\2\u014e\u014f\7u\2\2\u014f\u0150\7v\2\2\u0150\u0151")
        buf.write("\7t\2\2\u0151\u0152\7w\2\2\u0152\u0153\7e\2\2\u0153\u0154")
        buf.write("\7v\2\2\u0154\u0155\7q\2\2\u0155\u0156\7t\2\2\u0156,\3")
        buf.write("\2\2\2\u0157\u0158\7E\2\2\u0158\u0159\7q\2\2\u0159\u015a")
        buf.write("\7p\2\2\u015a\u015b\7v\2\2\u015b\u015c\7k\2\2\u015c\u015d")
        buf.write("\7p\2\2\u015d\u015e\7w\2\2\u015e\u015f\7g\2\2\u015f.\3")
        buf.write("\2\2\2\u0160\u0161\7V\2\2\u0161\u0162\7t\2\2\u0162\u0163")
        buf.write("\7w\2\2\u0163\u0164\7g\2\2\u0164\60\3\2\2\2\u0165\u0166")
        buf.write("\7H\2\2\u0166\u0167\7n\2\2\u0167\u0168\7q\2\2\u0168\u0169")
        buf.write("\7c\2\2\u0169\u016a\7v\2\2\u016a\62\3\2\2\2\u016b\u016c")
        buf.write("\7E\2\2\u016c\u016d\7n\2\2\u016d\u016e\7c\2\2\u016e\u016f")
        buf.write("\7u\2\2\u016f\u0170\7u\2\2\u0170\64\3\2\2\2\u0171\u0172")
        buf.write("\7F\2\2\u0172\u0173\7g\2\2\u0173\u0174\7u\2\2\u0174\u0175")
        buf.write("\7v\2\2\u0175\u0176\7t\2\2\u0176\u0177\7w\2\2\u0177\u0178")
        buf.write("\7e\2\2\u0178\u0179\7v\2\2\u0179\u017a\7q\2\2\u017a\u017b")
        buf.write("\7t\2\2\u017b\66\3\2\2\2\u017c\u017d\7K\2\2\u017d\u017e")
        buf.write("\7h\2\2\u017e8\3\2\2\2\u017f\u0180\7H\2\2\u0180\u0181")
        buf.write("\7c\2\2\u0181\u0182\7n\2\2\u0182\u0183\7u\2\2\u0183\u0184")
        buf.write("\7g\2\2\u0184:\3\2\2\2\u0185\u0186\7D\2\2\u0186\u0187")
        buf.write("\7q\2\2\u0187\u0188\7q\2\2\u0188\u0189\7n\2\2\u0189\u018a")
        buf.write("\7g\2\2\u018a\u018b\7c\2\2\u018b\u018c\7p\2\2\u018c<\3")
        buf.write("\2\2\2\u018d\u018e\7P\2\2\u018e\u018f\7g\2\2\u018f\u0190")
        buf.write("\7y\2\2\u0190>\3\2\2\2\u0191\u0192\7G\2\2\u0192\u0193")
        buf.write("\7n\2\2\u0193\u0194\7u\2\2\u0194\u0195\7g\2\2\u0195\u0196")
        buf.write("\7k\2\2\u0196\u0197\7h\2\2\u0197@\3\2\2\2\u0198\u0199")
        buf.write("\7C\2\2\u0199\u019a\7t\2\2\u019a\u019b\7t\2\2\u019b\u019c")
        buf.write("\7c\2\2\u019c\u019d\7{\2\2\u019dB\3\2\2\2\u019e\u019f")
        buf.write("\7U\2\2\u019f\u01a0\7v\2\2\u01a0\u01a1\7t\2\2\u01a1\u01a2")
        buf.write("\7k\2\2\u01a2\u01a3\7p\2\2\u01a3\u01a4\7i\2\2\u01a4D\3")
        buf.write("\2\2\2\u01a5\u01a6\7D\2\2\u01a6\u01a7\7{\2\2\u01a7F\3")
        buf.write("\2\2\2\u01a8\u01a9\7G\2\2\u01a9\u01aa\7n\2\2\u01aa\u01ab")
        buf.write("\7u\2\2\u01ab\u01ac\7g\2\2\u01acH\3\2\2\2\u01ad\u01ae")
        buf.write("\7K\2\2\u01ae\u01af\7p\2\2\u01afJ\3\2\2\2\u01b0\u01b1")
        buf.write("\7T\2\2\u01b1\u01b2\7g\2\2\u01b2\u01b3\7v\2\2\u01b3\u01b4")
        buf.write("\7w\2\2\u01b4\u01b5\7t\2\2\u01b5\u01b6\7p\2\2\u01b6L\3")
        buf.write("\2\2\2\u01b7\u01b8\7U\2\2\u01b8\u01b9\7g\2\2\u01b9\u01ba")
        buf.write("\7n\2\2\u01ba\u01bb\7h\2\2\u01bbN\3\2\2\2\u01bc\u01bd")
        buf.write("\7*\2\2\u01bdP\3\2\2\2\u01be\u01bf\7+\2\2\u01bfR\3\2\2")
        buf.write("\2\u01c0\u01c1\7]\2\2\u01c1T\3\2\2\2\u01c2\u01c3\7_\2")
        buf.write("\2\u01c3V\3\2\2\2\u01c4\u01c5\7}\2\2\u01c5X\3\2\2\2\u01c6")
        buf.write("\u01c7\7\177\2\2\u01c7Z\3\2\2\2\u01c8\u01c9\7=\2\2\u01c9")
        buf.write("\\\3\2\2\2\u01ca\u01cb\7.\2\2\u01cb^\3\2\2\2\u01cc\u01cd")
        buf.write("\7\60\2\2\u01cd\u01ce\7\60\2\2\u01ce`\3\2\2\2\u01cf\u01d0")
        buf.write("\7-\2\2\u01d0b\3\2\2\2\u01d1\u01d2\7/\2\2\u01d2d\3\2\2")
        buf.write("\2\u01d3\u01d4\7,\2\2\u01d4f\3\2\2\2\u01d5\u01d6\7\61")
        buf.write("\2\2\u01d6h\3\2\2\2\u01d7\u01d8\7\'\2\2\u01d8j\3\2\2\2")
        buf.write("\u01d9\u01da\7#\2\2\u01dal\3\2\2\2\u01db\u01dc\7(\2\2")
        buf.write("\u01dc\u01dd\7(\2\2\u01ddn\3\2\2\2\u01de\u01df\7~\2\2")
        buf.write("\u01df\u01e0\7~\2\2\u01e0p\3\2\2\2\u01e1\u01e2\7?\2\2")
        buf.write("\u01e2\u01e3\7?\2\2\u01e3r\3\2\2\2\u01e4\u01e5\7?\2\2")
        buf.write("\u01e5t\3\2\2\2\u01e6\u01e7\7#\2\2\u01e7\u01e8\7?\2\2")
        buf.write("\u01e8v\3\2\2\2\u01e9\u01ea\7>\2\2\u01eax\3\2\2\2\u01eb")
        buf.write("\u01ec\7>\2\2\u01ec\u01ed\7?\2\2\u01edz\3\2\2\2\u01ee")
        buf.write("\u01ef\7@\2\2\u01ef|\3\2\2\2\u01f0\u01f1\7@\2\2\u01f1")
        buf.write("\u01f2\7?\2\2\u01f2~\3\2\2\2\u01f3\u01f4\7?\2\2\u01f4")
        buf.write("\u01f5\7?\2\2\u01f5\u01f6\7\60\2\2\u01f6\u0080\3\2\2\2")
        buf.write("\u01f7\u01f8\7-\2\2\u01f8\u01f9\7\60\2\2\u01f9\u0082\3")
        buf.write("\2\2\2\u01fa\u01fb\7\60\2\2\u01fb\u0084\3\2\2\2\u01fc")
        buf.write("\u01fd\7<\2\2\u01fd\u01fe\7<\2\2\u01fe\u0086\3\2\2\2\u01ff")
        buf.write("\u0200\7<\2\2\u0200\u0088\3\2\2\2\u0201\u0205\t\13\2\2")
        buf.write("\u0202\u0204\t\f\2\2\u0203\u0202\3\2\2\2\u0204\u0207\3")
        buf.write("\2\2\2\u0205\u0203\3\2\2\2\u0205\u0206\3\2\2\2\u0206\u008a")
        buf.write("\3\2\2\2\u0207\u0205\3\2\2\2\u0208\u020a\5!\21\2\u0209")
        buf.write("\u020b\t\f\2\2\u020a\u0209\3\2\2\2\u020b\u020c\3\2\2\2")
        buf.write("\u020c\u020a\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u008c\3")
        buf.write("\2\2\2\u020e\u020f\7%\2\2\u020f\u0210\7%\2\2\u0210\u0214")
        buf.write("\3\2\2\2\u0211\u0213\13\2\2\2\u0212\u0211\3\2\2\2\u0213")
        buf.write("\u0216\3\2\2\2\u0214\u0215\3\2\2\2\u0214\u0212\3\2\2\2")
        buf.write("\u0215\u0217\3\2\2\2\u0216\u0214\3\2\2\2\u0217\u0218\7")
        buf.write("%\2\2\u0218\u0219\7%\2\2\u0219\u021a\3\2\2\2\u021a\u021b")
        buf.write("\bG\5\2\u021b\u008e\3\2\2\2\u021c\u021e\t\r\2\2\u021d")
        buf.write("\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u021d\3\2\2\2")
        buf.write("\u021f\u0220\3\2\2\2\u0220\u0221\3\2\2\2\u0221\u0222\b")
        buf.write("H\5\2\u0222\u0090\3\2\2\2\u0223\u0224\n\16\2\2\u0224\u0092")
        buf.write("\3\2\2\2\u0225\u022a\7$\2\2\u0226\u0229\5\u0091I\2\u0227")
        buf.write("\u0229\5\u0097L\2\u0228\u0226\3\2\2\2\u0228\u0227\3\2")
        buf.write("\2\2\u0229\u022c\3\2\2\2\u022a\u0228\3\2\2\2\u022a\u022b")
        buf.write("\3\2\2\2\u022b\u022e\3\2\2\2\u022c\u022a\3\2\2\2\u022d")
        buf.write("\u022f\t\17\2\2\u022e\u022d\3\2\2\2\u022f\u0230\3\2\2")
        buf.write("\2\u0230\u0231\bJ\6\2\u0231\u0094\3\2\2\2\u0232\u0237")
        buf.write("\7$\2\2\u0233\u0236\5\u0091I\2\u0234\u0236\5\u0097L\2")
        buf.write("\u0235\u0233\3\2\2\2\u0235\u0234\3\2\2\2\u0236\u0239\3")
        buf.write("\2\2\2\u0237\u0235\3\2\2\2\u0237\u0238\3\2\2\2\u0238\u023a")
        buf.write("\3\2\2\2\u0239\u0237\3\2\2\2\u023a\u023b\5\u0099M\2\u023b")
        buf.write("\u023c\bK\7\2\u023c\u0096\3\2\2\2\u023d\u023e\7^\2\2\u023e")
        buf.write("\u024e\7d\2\2\u023f\u0240\7^\2\2\u0240\u024e\7h\2\2\u0241")
        buf.write("\u0242\7^\2\2\u0242\u024e\7t\2\2\u0243\u0244\7^\2\2\u0244")
        buf.write("\u024e\7p\2\2\u0245\u0246\7^\2\2\u0246\u024e\7v\2\2\u0247")
        buf.write("\u0248\7^\2\2\u0248\u024e\7)\2\2\u0249\u024a\7^\2\2\u024a")
        buf.write("\u024e\7^\2\2\u024b\u024c\7)\2\2\u024c\u024e\7$\2\2\u024d")
        buf.write("\u023d\3\2\2\2\u024d\u023f\3\2\2\2\u024d\u0241\3\2\2\2")
        buf.write("\u024d\u0243\3\2\2\2\u024d\u0245\3\2\2\2\u024d\u0247\3")
        buf.write("\2\2\2\u024d\u0249\3\2\2\2\u024d\u024b\3\2\2\2\u024e\u0098")
        buf.write("\3\2\2\2\u024f\u0250\7^\2\2\u0250\u0251\n\20\2\2\u0251")
        buf.write("\u009a\3\2\2\2\u0252\u0253\13\2\2\2\u0253\u0254\bN\b\2")
        buf.write("\u0254\u009c\3\2\2\2$\2\u009f\u00a5\u00b8\u00bc\u00c1")
        buf.write("\u00c8\u00cc\u00d1\u00d7\u00dc\u00e3\u00e7\u00ec\u00f2")
        buf.write("\u00fa\u0101\u0106\u0109\u010f\u0114\u0119\u011f\u0121")
        buf.write("\u0205\u020c\u0214\u021f\u0228\u022a\u022e\u0235\u0237")
        buf.write("\u024d\t\3\3\2\3\t\3\3\r\4\b\2\2\3J\5\3K\6\3N\7")
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
        self.checkVersion("4.8")
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
            	
     


