# Generated from d:\HCMUT\Semester 212\Principles of Programming Languages\HK212_CO3005_PPL\assignment1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u0240\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\2\3\2\3\2\3\2\3\2\5\2\u009e\n\2\3\2\3\2\3\2\5\2\u00a3")
        buf.write("\n\2\3\3\3\3\3\3\5\3\u00a8\n\3\3\3\7\3\u00ab\n\3\f\3\16")
        buf.write("\3\u00ae\13\3\5\3\u00b0\n\3\3\3\3\3\3\4\3\4\3\4\3\4\5")
        buf.write("\4\u00b8\n\4\3\4\3\4\3\4\5\4\u00bd\n\4\3\4\7\4\u00c0\n")
        buf.write("\4\f\4\16\4\u00c3\13\4\5\4\u00c5\n\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\5\5\u00cd\n\5\3\5\7\5\u00d0\n\5\f\5\16\5\u00d3")
        buf.write("\13\5\5\5\u00d5\n\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6\u00dd")
        buf.write("\n\6\3\6\3\6\3\6\7\6\u00e2\n\6\f\6\16\6\u00e5\13\6\5\6")
        buf.write("\u00e7\n\6\3\7\3\7\3\7\5\7\u00ec\n\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\5\7\u00f4\n\7\3\7\3\7\3\b\3\b\3\b\5\b\u00fb\n\b")
        buf.write("\3\b\7\b\u00fe\n\b\f\b\16\b\u0101\13\b\5\b\u0103\n\b\3")
        buf.write("\t\3\t\7\t\u0107\n\t\f\t\16\t\u010a\13\t\3\n\3\n\5\n\u010e")
        buf.write("\n\n\3\n\3\n\7\n\u0112\n\n\f\n\16\n\u0115\13\n\3\13\3")
        buf.write("\13\7\13\u0119\n\13\f\13\16\13\u011c\13\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3")
        buf.write("*\3*\3+\3+\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3")
        buf.write("\61\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\67\3\67\38\38\38\39\39\3:\3:\3:\3;\3")
        buf.write(";\3<\3<\3<\3=\3=\3=\3=\3>\3>\3>\3?\3?\3@\3@\3@\3A\3A\3")
        buf.write("B\5B\u01f7\nB\3B\3B\7B\u01fb\nB\fB\16B\u01fe\13B\3C\3")
        buf.write("C\7C\u0202\nC\fC\16C\u0205\13C\3D\6D\u0208\nD\rD\16D\u0209")
        buf.write("\3D\3D\3E\3E\3E\3E\7E\u0212\nE\fE\16E\u0215\13E\3E\3E")
        buf.write("\3E\3E\3E\3F\3F\3F\3G\3G\7G\u0221\nG\fG\16G\u0224\13G")
        buf.write("\3G\5G\u0227\nG\3G\3G\3H\3H\7H\u022d\nH\fH\16H\u0230\13")
        buf.write("H\3H\3H\3H\3I\3I\5I\u0237\nI\3J\3J\3J\3K\3K\3K\5K\u023f")
        buf.write("\nK\3\u0213\2L\3\3\5\4\7\5\t\6\13\7\r\b\17\2\21\2\23\2")
        buf.write("\25\t\27\n\31\13\33\f\35\r\37\16!\17#\20%\21\'\22)\23")
        buf.write("+\24-\25/\26\61\27\63\30\65\31\67\329\33;\34=\35?\36A")
        buf.write("\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62i\63")
        buf.write("k\64m\65o\66q\67s8u9w:y;{<}=\177>\u0081?\u0083@\u0085")
        buf.write("\2\u0087A\u0089B\u008bC\u008dD\u008fE\u0091\2\u0093\2")
        buf.write("\u0095\2\3\2\22\3\2\63;\3\2\62;\4\2\63;CH\4\2\62;CH\3")
        buf.write("\2\639\3\2\629\3\2\62\63\4\2GGgg\4\2--//\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\5\2\n\f\16\17\"\"\7\3\n\f\16\17$$))^^\7")
        buf.write("\2\n\f\16\17$$))^^\n\2$$))^^ddhhppttvv\3\2^^\2\u025e\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\3\u00a2")
        buf.write("\3\2\2\2\5\u00af\3\2\2\2\7\u00b7\3\2\2\2\t\u00c8\3\2\2")
        buf.write("\2\13\u00dc\3\2\2\2\r\u00f3\3\2\2\2\17\u0102\3\2\2\2\21")
        buf.write("\u0104\3\2\2\2\23\u010b\3\2\2\2\25\u0116\3\2\2\2\27\u0120")
        buf.write("\3\2\2\2\31\u0123\3\2\2\2\33\u0127\3\2\2\2\35\u012b\3")
        buf.write("\2\2\2\37\u012d\3\2\2\2!\u0133\3\2\2\2#\u013b\3\2\2\2")
        buf.write("%\u013f\3\2\2\2\'\u0144\3\2\2\2)\u0150\3\2\2\2+\u0159")
        buf.write("\3\2\2\2-\u015e\3\2\2\2/\u0164\3\2\2\2\61\u016a\3\2\2")
        buf.write("\2\63\u0175\3\2\2\2\65\u0178\3\2\2\2\67\u017e\3\2\2\2")
        buf.write("9\u0186\3\2\2\2;\u018a\3\2\2\2=\u0191\3\2\2\2?\u0197\3")
        buf.write("\2\2\2A\u019e\3\2\2\2C\u01a1\3\2\2\2E\u01a6\3\2\2\2G\u01a9")
        buf.write("\3\2\2\2I\u01b0\3\2\2\2K\u01b2\3\2\2\2M\u01b4\3\2\2\2")
        buf.write("O\u01b6\3\2\2\2Q\u01b8\3\2\2\2S\u01ba\3\2\2\2U\u01bc\3")
        buf.write("\2\2\2W\u01be\3\2\2\2Y\u01c0\3\2\2\2[\u01c3\3\2\2\2]\u01c5")
        buf.write("\3\2\2\2_\u01c7\3\2\2\2a\u01c9\3\2\2\2c\u01cb\3\2\2\2")
        buf.write("e\u01cd\3\2\2\2g\u01cf\3\2\2\2i\u01d2\3\2\2\2k\u01d5\3")
        buf.write("\2\2\2m\u01d8\3\2\2\2o\u01da\3\2\2\2q\u01dd\3\2\2\2s\u01df")
        buf.write("\3\2\2\2u\u01e2\3\2\2\2w\u01e4\3\2\2\2y\u01e7\3\2\2\2")
        buf.write("{\u01eb\3\2\2\2}\u01ee\3\2\2\2\177\u01f0\3\2\2\2\u0081")
        buf.write("\u01f3\3\2\2\2\u0083\u01f6\3\2\2\2\u0085\u01ff\3\2\2\2")
        buf.write("\u0087\u0207\3\2\2\2\u0089\u020d\3\2\2\2\u008b\u021b\3")
        buf.write("\2\2\2\u008d\u021e\3\2\2\2\u008f\u022a\3\2\2\2\u0091\u0236")
        buf.write("\3\2\2\2\u0093\u0238\3\2\2\2\u0095\u023e\3\2\2\2\u0097")
        buf.write("\u009e\5\5\3\2\u0098\u009e\5\7\4\2\u0099\u009e\5\t\5\2")
        buf.write("\u009a\u009e\5\13\6\2\u009b\u009e\5\13\6\2\u009c\u009e")
        buf.write("\5\r\7\2\u009d\u0097\3\2\2\2\u009d\u0098\3\2\2\2\u009d")
        buf.write("\u0099\3\2\2\2\u009d\u009a\3\2\2\2\u009d\u009b\3\2\2\2")
        buf.write("\u009d\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\b")
        buf.write("\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u00a3\5\25\13\2\u00a2")
        buf.write("\u009d\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\4\3\2\2\2\u00a4")
        buf.write("\u00b0\7\62\2\2\u00a5\u00ac\t\2\2\2\u00a6\u00a8\7a\2\2")
        buf.write("\u00a7\u00a6\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a9\3")
        buf.write("\2\2\2\u00a9\u00ab\t\3\2\2\u00aa\u00a7\3\2\2\2\u00ab\u00ae")
        buf.write("\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad")
        buf.write("\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00a4\3\2\2\2")
        buf.write("\u00af\u00a5\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\b")
        buf.write("\3\3\2\u00b2\6\3\2\2\2\u00b3\u00b4\7\62\2\2\u00b4\u00b8")
        buf.write("\7z\2\2\u00b5\u00b6\7\62\2\2\u00b6\u00b8\7Z\2\2\u00b7")
        buf.write("\u00b3\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00c4\3\2\2\2")
        buf.write("\u00b9\u00c5\7\62\2\2\u00ba\u00c1\t\4\2\2\u00bb\u00bd")
        buf.write("\7a\2\2\u00bc\u00bb\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write("\u00be\3\2\2\2\u00be\u00c0\t\5\2\2\u00bf\u00bc\3\2\2\2")
        buf.write("\u00c0\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3")
        buf.write("\2\2\2\u00c2\u00c5\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00b9")
        buf.write("\3\2\2\2\u00c4\u00ba\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6")
        buf.write("\u00c7\b\4\4\2\u00c7\b\3\2\2\2\u00c8\u00d4\7\62\2\2\u00c9")
        buf.write("\u00d5\7\62\2\2\u00ca\u00d1\t\6\2\2\u00cb\u00cd\7a\2\2")
        buf.write("\u00cc\u00cb\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce\3")
        buf.write("\2\2\2\u00ce\u00d0\t\7\2\2\u00cf\u00cc\3\2\2\2\u00d0\u00d3")
        buf.write("\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2")
        buf.write("\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00c9\3\2\2\2")
        buf.write("\u00d4\u00ca\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d7\b")
        buf.write("\5\5\2\u00d7\n\3\2\2\2\u00d8\u00d9\7\62\2\2\u00d9\u00dd")
        buf.write("\7d\2\2\u00da\u00db\7\62\2\2\u00db\u00dd\7D\2\2\u00dc")
        buf.write("\u00d8\3\2\2\2\u00dc\u00da\3\2\2\2\u00dd\u00e6\3\2\2\2")
        buf.write("\u00de\u00e7\7\62\2\2\u00df\u00e3\7\63\2\2\u00e0\u00e2")
        buf.write("\t\b\2\2\u00e1\u00e0\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3")
        buf.write("\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e7\3\2\2\2")
        buf.write("\u00e5\u00e3\3\2\2\2\u00e6\u00de\3\2\2\2\u00e6\u00df\3")
        buf.write("\2\2\2\u00e7\f\3\2\2\2\u00e8\u00e9\5\17\b\2\u00e9\u00eb")
        buf.write("\5\21\t\2\u00ea\u00ec\5\23\n\2\u00eb\u00ea\3\2\2\2\u00eb")
        buf.write("\u00ec\3\2\2\2\u00ec\u00f4\3\2\2\2\u00ed\u00ee\5\17\b")
        buf.write("\2\u00ee\u00ef\5\23\n\2\u00ef\u00f4\3\2\2\2\u00f0\u00f1")
        buf.write("\5\21\t\2\u00f1\u00f2\5\23\n\2\u00f2\u00f4\3\2\2\2\u00f3")
        buf.write("\u00e8\3\2\2\2\u00f3\u00ed\3\2\2\2\u00f3\u00f0\3\2\2\2")
        buf.write("\u00f4\u00f5\3\2\2\2\u00f5\u00f6\b\7\6\2\u00f6\16\3\2")
        buf.write("\2\2\u00f7\u0103\7\62\2\2\u00f8\u00ff\t\2\2\2\u00f9\u00fb")
        buf.write("\7a\2\2\u00fa\u00f9\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb")
        buf.write("\u00fc\3\2\2\2\u00fc\u00fe\t\3\2\2\u00fd\u00fa\3\2\2\2")
        buf.write("\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3")
        buf.write("\2\2\2\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0102\u00f7")
        buf.write("\3\2\2\2\u0102\u00f8\3\2\2\2\u0103\20\3\2\2\2\u0104\u0108")
        buf.write("\5}?\2\u0105\u0107\t\3\2\2\u0106\u0105\3\2\2\2\u0107\u010a")
        buf.write("\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109")
        buf.write("\22\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u010d\t\t\2\2\u010c")
        buf.write("\u010e\t\n\2\2\u010d\u010c\3\2\2\2\u010d\u010e\3\2\2\2")
        buf.write("\u010e\u010f\3\2\2\2\u010f\u0113\t\2\2\2\u0110\u0112\t")
        buf.write("\3\2\2\u0111\u0110\3\2\2\2\u0112\u0115\3\2\2\2\u0113\u0111")
        buf.write("\3\2\2\2\u0113\u0114\3\2\2\2\u0114\24\3\2\2\2\u0115\u0113")
        buf.write("\3\2\2\2\u0116\u011a\7$\2\2\u0117\u0119\5\u0091I\2\u0118")
        buf.write("\u0117\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2")
        buf.write("\u011a\u011b\3\2\2\2\u011b\u011d\3\2\2\2\u011c\u011a\3")
        buf.write("\2\2\2\u011d\u011e\7$\2\2\u011e\u011f\b\13\7\2\u011f\26")
        buf.write("\3\2\2\2\u0120\u0121\7)\2\2\u0121\u0122\7$\2\2\u0122\30")
        buf.write("\3\2\2\2\u0123\u0124\7X\2\2\u0124\u0125\7c\2\2\u0125\u0126")
        buf.write("\7n\2\2\u0126\32\3\2\2\2\u0127\u0128\7X\2\2\u0128\u0129")
        buf.write("\7c\2\2\u0129\u012a\7t\2\2\u012a\34\3\2\2\2\u012b\u012c")
        buf.write("\7&\2\2\u012c\36\3\2\2\2\u012d\u012e\7D\2\2\u012e\u012f")
        buf.write("\7t\2\2\u012f\u0130\7g\2\2\u0130\u0131\7c\2\2\u0131\u0132")
        buf.write("\7m\2\2\u0132 \3\2\2\2\u0133\u0134\7H\2\2\u0134\u0135")
        buf.write("\7q\2\2\u0135\u0136\7t\2\2\u0136\u0137\7g\2\2\u0137\u0138")
        buf.write("\7c\2\2\u0138\u0139\7e\2\2\u0139\u013a\7j\2\2\u013a\"")
        buf.write("\3\2\2\2\u013b\u013c\7K\2\2\u013c\u013d\7p\2\2\u013d\u013e")
        buf.write("\7v\2\2\u013e$\3\2\2\2\u013f\u0140\7P\2\2\u0140\u0141")
        buf.write("\7w\2\2\u0141\u0142\7n\2\2\u0142\u0143\7n\2\2\u0143&\3")
        buf.write("\2\2\2\u0144\u0145\7E\2\2\u0145\u0146\7q\2\2\u0146\u0147")
        buf.write("\7p\2\2\u0147\u0148\7u\2\2\u0148\u0149\7v\2\2\u0149\u014a")
        buf.write("\7t\2\2\u014a\u014b\7w\2\2\u014b\u014c\7e\2\2\u014c\u014d")
        buf.write("\7v\2\2\u014d\u014e\7q\2\2\u014e\u014f\7t\2\2\u014f(\3")
        buf.write("\2\2\2\u0150\u0151\7E\2\2\u0151\u0152\7q\2\2\u0152\u0153")
        buf.write("\7p\2\2\u0153\u0154\7v\2\2\u0154\u0155\7k\2\2\u0155\u0156")
        buf.write("\7p\2\2\u0156\u0157\7w\2\2\u0157\u0158\7g\2\2\u0158*\3")
        buf.write("\2\2\2\u0159\u015a\7V\2\2\u015a\u015b\7t\2\2\u015b\u015c")
        buf.write("\7w\2\2\u015c\u015d\7g\2\2\u015d,\3\2\2\2\u015e\u015f")
        buf.write("\7H\2\2\u015f\u0160\7n\2\2\u0160\u0161\7q\2\2\u0161\u0162")
        buf.write("\7c\2\2\u0162\u0163\7v\2\2\u0163.\3\2\2\2\u0164\u0165")
        buf.write("\7E\2\2\u0165\u0166\7n\2\2\u0166\u0167\7c\2\2\u0167\u0168")
        buf.write("\7u\2\2\u0168\u0169\7u\2\2\u0169\60\3\2\2\2\u016a\u016b")
        buf.write("\7F\2\2\u016b\u016c\7g\2\2\u016c\u016d\7u\2\2\u016d\u016e")
        buf.write("\7v\2\2\u016e\u016f\7t\2\2\u016f\u0170\7w\2\2\u0170\u0171")
        buf.write("\7e\2\2\u0171\u0172\7v\2\2\u0172\u0173\7q\2\2\u0173\u0174")
        buf.write("\7t\2\2\u0174\62\3\2\2\2\u0175\u0176\7K\2\2\u0176\u0177")
        buf.write("\7h\2\2\u0177\64\3\2\2\2\u0178\u0179\7H\2\2\u0179\u017a")
        buf.write("\7c\2\2\u017a\u017b\7n\2\2\u017b\u017c\7u\2\2\u017c\u017d")
        buf.write("\7g\2\2\u017d\66\3\2\2\2\u017e\u017f\7D\2\2\u017f\u0180")
        buf.write("\7q\2\2\u0180\u0181\7q\2\2\u0181\u0182\7n\2\2\u0182\u0183")
        buf.write("\7g\2\2\u0183\u0184\7c\2\2\u0184\u0185\7p\2\2\u01858\3")
        buf.write("\2\2\2\u0186\u0187\7P\2\2\u0187\u0188\7g\2\2\u0188\u0189")
        buf.write("\7y\2\2\u0189:\3\2\2\2\u018a\u018b\7G\2\2\u018b\u018c")
        buf.write("\7n\2\2\u018c\u018d\7u\2\2\u018d\u018e\7g\2\2\u018e\u018f")
        buf.write("\7k\2\2\u018f\u0190\7h\2\2\u0190<\3\2\2\2\u0191\u0192")
        buf.write("\7C\2\2\u0192\u0193\7t\2\2\u0193\u0194\7t\2\2\u0194\u0195")
        buf.write("\7c\2\2\u0195\u0196\7{\2\2\u0196>\3\2\2\2\u0197\u0198")
        buf.write("\7U\2\2\u0198\u0199\7v\2\2\u0199\u019a\7t\2\2\u019a\u019b")
        buf.write("\7k\2\2\u019b\u019c\7p\2\2\u019c\u019d\7i\2\2\u019d@\3")
        buf.write("\2\2\2\u019e\u019f\7D\2\2\u019f\u01a0\7{\2\2\u01a0B\3")
        buf.write("\2\2\2\u01a1\u01a2\7G\2\2\u01a2\u01a3\7n\2\2\u01a3\u01a4")
        buf.write("\7u\2\2\u01a4\u01a5\7g\2\2\u01a5D\3\2\2\2\u01a6\u01a7")
        buf.write("\7K\2\2\u01a7\u01a8\7p\2\2\u01a8F\3\2\2\2\u01a9\u01aa")
        buf.write("\7T\2\2\u01aa\u01ab\7g\2\2\u01ab\u01ac\7v\2\2\u01ac\u01ad")
        buf.write("\7w\2\2\u01ad\u01ae\7t\2\2\u01ae\u01af\7p\2\2\u01afH\3")
        buf.write("\2\2\2\u01b0\u01b1\7*\2\2\u01b1J\3\2\2\2\u01b2\u01b3\7")
        buf.write("+\2\2\u01b3L\3\2\2\2\u01b4\u01b5\7]\2\2\u01b5N\3\2\2\2")
        buf.write("\u01b6\u01b7\7_\2\2\u01b7P\3\2\2\2\u01b8\u01b9\7}\2\2")
        buf.write("\u01b9R\3\2\2\2\u01ba\u01bb\7\177\2\2\u01bbT\3\2\2\2\u01bc")
        buf.write("\u01bd\7=\2\2\u01bdV\3\2\2\2\u01be\u01bf\7.\2\2\u01bf")
        buf.write("X\3\2\2\2\u01c0\u01c1\7\60\2\2\u01c1\u01c2\7\60\2\2\u01c2")
        buf.write("Z\3\2\2\2\u01c3\u01c4\7-\2\2\u01c4\\\3\2\2\2\u01c5\u01c6")
        buf.write("\7/\2\2\u01c6^\3\2\2\2\u01c7\u01c8\7,\2\2\u01c8`\3\2\2")
        buf.write("\2\u01c9\u01ca\7\61\2\2\u01cab\3\2\2\2\u01cb\u01cc\7\'")
        buf.write("\2\2\u01ccd\3\2\2\2\u01cd\u01ce\7#\2\2\u01cef\3\2\2\2")
        buf.write("\u01cf\u01d0\7(\2\2\u01d0\u01d1\7(\2\2\u01d1h\3\2\2\2")
        buf.write("\u01d2\u01d3\7~\2\2\u01d3\u01d4\7~\2\2\u01d4j\3\2\2\2")
        buf.write("\u01d5\u01d6\7?\2\2\u01d6\u01d7\7?\2\2\u01d7l\3\2\2\2")
        buf.write("\u01d8\u01d9\7?\2\2\u01d9n\3\2\2\2\u01da\u01db\7#\2\2")
        buf.write("\u01db\u01dc\7?\2\2\u01dcp\3\2\2\2\u01dd\u01de\7>\2\2")
        buf.write("\u01der\3\2\2\2\u01df\u01e0\7>\2\2\u01e0\u01e1\7?\2\2")
        buf.write("\u01e1t\3\2\2\2\u01e2\u01e3\7@\2\2\u01e3v\3\2\2\2\u01e4")
        buf.write("\u01e5\7@\2\2\u01e5\u01e6\7?\2\2\u01e6x\3\2\2\2\u01e7")
        buf.write("\u01e8\7?\2\2\u01e8\u01e9\7?\2\2\u01e9\u01ea\7\60\2\2")
        buf.write("\u01eaz\3\2\2\2\u01eb\u01ec\7-\2\2\u01ec\u01ed\7\60\2")
        buf.write("\2\u01ed|\3\2\2\2\u01ee\u01ef\7\60\2\2\u01ef~\3\2\2\2")
        buf.write("\u01f0\u01f1\7<\2\2\u01f1\u01f2\7<\2\2\u01f2\u0080\3\2")
        buf.write("\2\2\u01f3\u01f4\7<\2\2\u01f4\u0082\3\2\2\2\u01f5\u01f7")
        buf.write("\5\35\17\2\u01f6\u01f5\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7")
        buf.write("\u01f8\3\2\2\2\u01f8\u01fc\t\13\2\2\u01f9\u01fb\t\f\2")
        buf.write("\2\u01fa\u01f9\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa")
        buf.write("\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u0084\3\2\2\2\u01fe")
        buf.write("\u01fc\3\2\2\2\u01ff\u0203\t\3\2\2\u0200\u0202\t\2\2\2")
        buf.write("\u0201\u0200\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201\3")
        buf.write("\2\2\2\u0203\u0204\3\2\2\2\u0204\u0086\3\2\2\2\u0205\u0203")
        buf.write("\3\2\2\2\u0206\u0208\t\r\2\2\u0207\u0206\3\2\2\2\u0208")
        buf.write("\u0209\3\2\2\2\u0209\u0207\3\2\2\2\u0209\u020a\3\2\2\2")
        buf.write("\u020a\u020b\3\2\2\2\u020b\u020c\bD\b\2\u020c\u0088\3")
        buf.write("\2\2\2\u020d\u020e\7%\2\2\u020e\u020f\7%\2\2\u020f\u0213")
        buf.write("\3\2\2\2\u0210\u0212\13\2\2\2\u0211\u0210\3\2\2\2\u0212")
        buf.write("\u0215\3\2\2\2\u0213\u0214\3\2\2\2\u0213\u0211\3\2\2\2")
        buf.write("\u0214\u0216\3\2\2\2\u0215\u0213\3\2\2\2\u0216\u0217\7")
        buf.write("%\2\2\u0217\u0218\7%\2\2\u0218\u0219\3\2\2\2\u0219\u021a")
        buf.write("\bE\b\2\u021a\u008a\3\2\2\2\u021b\u021c\13\2\2\2\u021c")
        buf.write("\u021d\bF\t\2\u021d\u008c\3\2\2\2\u021e\u0222\7$\2\2\u021f")
        buf.write("\u0221\5\u0091I\2\u0220\u021f\3\2\2\2\u0221\u0224\3\2")
        buf.write("\2\2\u0222\u0220\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0226")
        buf.write("\3\2\2\2\u0224\u0222\3\2\2\2\u0225\u0227\t\16\2\2\u0226")
        buf.write("\u0225\3\2\2\2\u0227\u0228\3\2\2\2\u0228\u0229\bG\n\2")
        buf.write("\u0229\u008e\3\2\2\2\u022a\u022e\7$\2\2\u022b\u022d\5")
        buf.write("\u0091I\2\u022c\u022b\3\2\2\2\u022d\u0230\3\2\2\2\u022e")
        buf.write("\u022c\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u0231\3\2\2\2")
        buf.write("\u0230\u022e\3\2\2\2\u0231\u0232\5\u0095K\2\u0232\u0233")
        buf.write("\bH\13\2\u0233\u0090\3\2\2\2\u0234\u0237\n\17\2\2\u0235")
        buf.write("\u0237\5\u0093J\2\u0236\u0234\3\2\2\2\u0236\u0235\3\2")
        buf.write("\2\2\u0237\u0092\3\2\2\2\u0238\u0239\7^\2\2\u0239\u023a")
        buf.write("\t\20\2\2\u023a\u0094\3\2\2\2\u023b\u023c\7^\2\2\u023c")
        buf.write("\u023f\n\20\2\2\u023d\u023f\n\21\2\2\u023e\u023b\3\2\2")
        buf.write("\2\u023e\u023d\3\2\2\2\u023f\u0096\3\2\2\2%\2\u009d\u00a2")
        buf.write("\u00a7\u00ac\u00af\u00b7\u00bc\u00c1\u00c4\u00cc\u00d1")
        buf.write("\u00d4\u00dc\u00e3\u00e6\u00eb\u00f3\u00fa\u00ff\u0102")
        buf.write("\u0108\u010d\u0113\u011a\u01f6\u01fc\u0203\u0209\u0213")
        buf.write("\u0222\u0226\u022e\u0236\u023e\f\3\2\2\3\3\3\3\4\4\3\5")
        buf.write("\5\3\7\6\3\13\7\b\2\2\3F\b\3G\t\3H\n")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LITERAL = 1
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
    DOUBLE_SEMI = 60
    COLON = 61
    ID = 62
    WS = 63
    BLOCK_COMMENT = 64
    ERROR_CHAR = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Val'", "'Var'", "'$'", "'Break'", "'Foreach'", "'Int'", "'Null'", 
            "'Constructor'", "'Continue'", "'True'", "'Float'", "'Class'", 
            "'Destructor'", "'If'", "'False'", "'Boolean'", "'New'", "'Elseif'", 
            "'Array'", "'String'", "'By'", "'Else'", "'In'", "'Return'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", "','", "'..'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'='", "'!='", "'<'", "'<='", "'>'", "'>='", "'==.'", "'+.'", 
            "'.'", "'::'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "LITERAL", "LITERAL_INT_DEC", "LITERAL_INT_HEX", "LITERAL_INT_OCT", 
            "LITERAL_INT_BIN", "LITERAL_FLOAT", "LITERAL_STRING", "DOUBLE_QUOTE", 
            "VAL", "VAR", "STATIC", "BREAK", "FOREACH", "INT", "NULL", "CONSTRUCTOR", 
            "CONTINUE", "TRUE", "FLOAT", "CLASS", "DESTRUCTOR", "IF", "FALSE", 
            "BOOLEAN", "NEW", "ELSEIF", "ARRAY", "STRING", "BY", "ELSE", 
            "IN", "RETURN", "LB", "RB", "LS", "RS", "LP", "RP", "SEMI", 
            "COMMA", "DOTDOT", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", 
            "MODULO", "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", 
            "LESS_THAN", "LEQ", "GREATER_THAN", "GEQ", "EQUAL_STRING", "STRING_CONCAT", 
            "DOT", "DOUBLE_SEMI", "COLON", "ID", "WS", "BLOCK_COMMENT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "LITERAL", "LITERAL_INT_DEC", "LITERAL_INT_HEX", "LITERAL_INT_OCT", 
                  "LITERAL_INT_BIN", "LITERAL_FLOAT", "FLOAT_INT", "FLOAT_DECIMAL", 
                  "FLOAT_EXP", "LITERAL_STRING", "DOUBLE_QUOTE", "VAL", 
                  "VAR", "STATIC", "BREAK", "FOREACH", "INT", "NULL", "CONSTRUCTOR", 
                  "CONTINUE", "TRUE", "FLOAT", "CLASS", "DESTRUCTOR", "IF", 
                  "FALSE", "BOOLEAN", "NEW", "ELSEIF", "ARRAY", "STRING", 
                  "BY", "ELSE", "IN", "RETURN", "LB", "RB", "LS", "RS", 
                  "LP", "RP", "SEMI", "COMMA", "DOTDOT", "ADD", "SUBTRACT", 
                  "MULTIPLY", "DIVIDE", "MODULO", "NOT", "AND", "OR", "EQUAL", 
                  "ASSIGN", "NOT_EQUAL", "LESS_THAN", "LEQ", "GREATER_THAN", 
                  "GEQ", "EQUAL_STRING", "STRING_CONCAT", "DOT", "DOUBLE_SEMI", 
                  "COLON", "ID", "INTLIT", "WS", "BLOCK_COMMENT", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "STRING_CHAR", "ESC_SEQUENCE", 
                  "ESC_ILLEGAL" ]

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
            actions[0] = self.LITERAL_action 
            actions[1] = self.LITERAL_INT_DEC_action 
            actions[2] = self.LITERAL_INT_HEX_action 
            actions[3] = self.LITERAL_INT_OCT_action 
            actions[5] = self.LITERAL_FLOAT_action 
            actions[9] = self.LITERAL_STRING_action 
            actions[68] = self.ERROR_CHAR_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def LITERAL_action(self, localctx:RuleContext , actionIndex:int):
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
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

            		y = str(self.text)
            		possible_char = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
            		if y[-1] in possible_char:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

