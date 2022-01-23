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
        buf.write("\u023a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\5\3\6\3\6\3\6\3\6\5\6\u00d9\n\6\3\6\3\6\3\6\7\6\u00de")
        buf.write("\n\6\f\6\16\6\u00e1\13\6\5\6\u00e3\n\6\3\7\3\7\3\7\5\7")
        buf.write("\u00e8\n\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00f0\n\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\5\b\u00f7\n\b\3\b\7\b\u00fa\n\b\f\b\16")
        buf.write("\b\u00fd\13\b\5\b\u00ff\n\b\3\t\3\t\7\t\u0103\n\t\f\t")
        buf.write("\16\t\u0106\13\t\3\n\3\n\5\n\u010a\n\n\3\n\3\n\7\n\u010e")
        buf.write("\n\n\f\n\16\n\u0111\13\n\3\13\3\13\7\13\u0115\n\13\f\13")
        buf.write("\16\13\u0118\13\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3")
        buf.write("-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\38\38\39\39\39\3:\3:\3;\3;\3;\3<\3<\3=\3=\3=\3>")
        buf.write("\3>\3>\3>\3?\3?\3?\3@\3@\3A\3A\3A\3B\3B\3C\5C\u01f8\n")
        buf.write("C\3C\3C\7C\u01fc\nC\fC\16C\u01ff\13C\3D\3D\3D\3D\7D\u0205")
        buf.write("\nD\fD\16D\u0208\13D\3D\3D\3D\3D\3D\3E\6E\u0210\nE\rE")
        buf.write("\16E\u0211\3E\3E\3F\3F\7F\u0218\nF\fF\16F\u021b\13F\3")
        buf.write("F\5F\u021e\nF\3F\3F\3G\3G\7G\u0224\nG\fG\16G\u0227\13")
        buf.write("G\3G\3G\3G\3H\3H\5H\u022e\nH\3I\3I\3I\3J\3J\3J\5J\u0236")
        buf.write("\nJ\3K\3K\3K\3\u0206\2L\3\3\5\4\7\5\t\6\13\7\r\b\17\2")
        buf.write("\21\2\23\2\25\t\27\n\31\13\33\f\35\r\37\16!\17#\20%\21")
        buf.write("\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67\329\33;\34")
        buf.write("=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61")
        buf.write("g\62i\63k\64m\65o\66q\67s8u9w:y;{<}=\177>\u0081?\u0083")
        buf.write("@\u0085A\u0087B\u0089C\u008bD\u008dE\u008f\2\u0091\2\u0093")
        buf.write("\2\u0095F\3\2\22\3\2\63;\3\2\62;\4\2\63;CH\4\2\62;CH\3")
        buf.write("\2\639\3\2\629\3\2\62\63\4\2GGgg\4\2--//\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\5\2\n\f\16\17\"\"\7\3\n\f\16\17$$))^^\7")
        buf.write("\2\n\f\16\17$$))^^\n\2$$))^^ddhhppttvv\3\2^^\2\u0256\2")
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
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\3\u009c\3\2\2\2\5\u00ab\3\2\2\2\7\u00b3\3\2\2")
        buf.write("\2\t\u00c4\3\2\2\2\13\u00d8\3\2\2\2\r\u00ef\3\2\2\2\17")
        buf.write("\u00fe\3\2\2\2\21\u0100\3\2\2\2\23\u0107\3\2\2\2\25\u0112")
        buf.write("\3\2\2\2\27\u011c\3\2\2\2\31\u011f\3\2\2\2\33\u0123\3")
        buf.write("\2\2\2\35\u0127\3\2\2\2\37\u0129\3\2\2\2!\u012f\3\2\2")
        buf.write("\2#\u0137\3\2\2\2%\u013b\3\2\2\2\'\u0140\3\2\2\2)\u014c")
        buf.write("\3\2\2\2+\u0155\3\2\2\2-\u015a\3\2\2\2/\u0160\3\2\2\2")
        buf.write("\61\u0166\3\2\2\2\63\u0171\3\2\2\2\65\u0174\3\2\2\2\67")
        buf.write("\u017a\3\2\2\29\u0182\3\2\2\2;\u0186\3\2\2\2=\u018d\3")
        buf.write("\2\2\2?\u0193\3\2\2\2A\u019a\3\2\2\2C\u019d\3\2\2\2E\u01a2")
        buf.write("\3\2\2\2G\u01a5\3\2\2\2I\u01ac\3\2\2\2K\u01b1\3\2\2\2")
        buf.write("M\u01b3\3\2\2\2O\u01b5\3\2\2\2Q\u01b7\3\2\2\2S\u01b9\3")
        buf.write("\2\2\2U\u01bb\3\2\2\2W\u01bd\3\2\2\2Y\u01bf\3\2\2\2[\u01c1")
        buf.write("\3\2\2\2]\u01c4\3\2\2\2_\u01c6\3\2\2\2a\u01c8\3\2\2\2")
        buf.write("c\u01ca\3\2\2\2e\u01cc\3\2\2\2g\u01ce\3\2\2\2i\u01d0\3")
        buf.write("\2\2\2k\u01d3\3\2\2\2m\u01d6\3\2\2\2o\u01d9\3\2\2\2q\u01db")
        buf.write("\3\2\2\2s\u01de\3\2\2\2u\u01e0\3\2\2\2w\u01e3\3\2\2\2")
        buf.write("y\u01e5\3\2\2\2{\u01e8\3\2\2\2}\u01ec\3\2\2\2\177\u01ef")
        buf.write("\3\2\2\2\u0081\u01f1\3\2\2\2\u0083\u01f4\3\2\2\2\u0085")
        buf.write("\u01f7\3\2\2\2\u0087\u0200\3\2\2\2\u0089\u020f\3\2\2\2")
        buf.write("\u008b\u0215\3\2\2\2\u008d\u0221\3\2\2\2\u008f\u022d\3")
        buf.write("\2\2\2\u0091\u022f\3\2\2\2\u0093\u0235\3\2\2\2\u0095\u0237")
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
        buf.write("\u00d4\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9\u00e2\3\2\2\2")
        buf.write("\u00da\u00e3\7\62\2\2\u00db\u00df\7\63\2\2\u00dc\u00de")
        buf.write("\t\b\2\2\u00dd\u00dc\3\2\2\2\u00de\u00e1\3\2\2\2\u00df")
        buf.write("\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e3\3\2\2\2")
        buf.write("\u00e1\u00df\3\2\2\2\u00e2\u00da\3\2\2\2\u00e2\u00db\3")
        buf.write("\2\2\2\u00e3\f\3\2\2\2\u00e4\u00e5\5\17\b\2\u00e5\u00e7")
        buf.write("\5\21\t\2\u00e6\u00e8\5\23\n\2\u00e7\u00e6\3\2\2\2\u00e7")
        buf.write("\u00e8\3\2\2\2\u00e8\u00f0\3\2\2\2\u00e9\u00ea\5\17\b")
        buf.write("\2\u00ea\u00eb\5\23\n\2\u00eb\u00f0\3\2\2\2\u00ec\u00ed")
        buf.write("\5\21\t\2\u00ed\u00ee\5\23\n\2\u00ee\u00f0\3\2\2\2\u00ef")
        buf.write("\u00e4\3\2\2\2\u00ef\u00e9\3\2\2\2\u00ef\u00ec\3\2\2\2")
        buf.write("\u00f0\u00f1\3\2\2\2\u00f1\u00f2\b\7\6\2\u00f2\16\3\2")
        buf.write("\2\2\u00f3\u00ff\7\62\2\2\u00f4\u00fb\t\2\2\2\u00f5\u00f7")
        buf.write("\7a\2\2\u00f6\u00f5\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7")
        buf.write("\u00f8\3\2\2\2\u00f8\u00fa\t\3\2\2\u00f9\u00f6\3\2\2\2")
        buf.write("\u00fa\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3")
        buf.write("\2\2\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u00f3")
        buf.write("\3\2\2\2\u00fe\u00f4\3\2\2\2\u00ff\20\3\2\2\2\u0100\u0104")
        buf.write("\5\177@\2\u0101\u0103\t\3\2\2\u0102\u0101\3\2\2\2\u0103")
        buf.write("\u0106\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2")
        buf.write("\u0105\22\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0109\t\t")
        buf.write("\2\2\u0108\u010a\t\n\2\2\u0109\u0108\3\2\2\2\u0109\u010a")
        buf.write("\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010f\t\2\2\2\u010c")
        buf.write("\u010e\t\3\2\2\u010d\u010c\3\2\2\2\u010e\u0111\3\2\2\2")
        buf.write("\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110\24\3\2")
        buf.write("\2\2\u0111\u010f\3\2\2\2\u0112\u0116\7$\2\2\u0113\u0115")
        buf.write("\5\u008fH\2\u0114\u0113\3\2\2\2\u0115\u0118\3\2\2\2\u0116")
        buf.write("\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0119\3\2\2\2")
        buf.write("\u0118\u0116\3\2\2\2\u0119\u011a\7$\2\2\u011a\u011b\b")
        buf.write("\13\7\2\u011b\26\3\2\2\2\u011c\u011d\7)\2\2\u011d\u011e")
        buf.write("\7$\2\2\u011e\30\3\2\2\2\u011f\u0120\7X\2\2\u0120\u0121")
        buf.write("\7c\2\2\u0121\u0122\7n\2\2\u0122\32\3\2\2\2\u0123\u0124")
        buf.write("\7X\2\2\u0124\u0125\7c\2\2\u0125\u0126\7t\2\2\u0126\34")
        buf.write("\3\2\2\2\u0127\u0128\7&\2\2\u0128\36\3\2\2\2\u0129\u012a")
        buf.write("\7D\2\2\u012a\u012b\7t\2\2\u012b\u012c\7g\2\2\u012c\u012d")
        buf.write("\7c\2\2\u012d\u012e\7m\2\2\u012e \3\2\2\2\u012f\u0130")
        buf.write("\7H\2\2\u0130\u0131\7q\2\2\u0131\u0132\7t\2\2\u0132\u0133")
        buf.write("\7g\2\2\u0133\u0134\7c\2\2\u0134\u0135\7e\2\2\u0135\u0136")
        buf.write("\7j\2\2\u0136\"\3\2\2\2\u0137\u0138\7K\2\2\u0138\u0139")
        buf.write("\7p\2\2\u0139\u013a\7v\2\2\u013a$\3\2\2\2\u013b\u013c")
        buf.write("\7P\2\2\u013c\u013d\7w\2\2\u013d\u013e\7n\2\2\u013e\u013f")
        buf.write("\7n\2\2\u013f&\3\2\2\2\u0140\u0141\7E\2\2\u0141\u0142")
        buf.write("\7q\2\2\u0142\u0143\7p\2\2\u0143\u0144\7u\2\2\u0144\u0145")
        buf.write("\7v\2\2\u0145\u0146\7t\2\2\u0146\u0147\7w\2\2\u0147\u0148")
        buf.write("\7e\2\2\u0148\u0149\7v\2\2\u0149\u014a\7q\2\2\u014a\u014b")
        buf.write("\7t\2\2\u014b(\3\2\2\2\u014c\u014d\7E\2\2\u014d\u014e")
        buf.write("\7q\2\2\u014e\u014f\7p\2\2\u014f\u0150\7v\2\2\u0150\u0151")
        buf.write("\7k\2\2\u0151\u0152\7p\2\2\u0152\u0153\7w\2\2\u0153\u0154")
        buf.write("\7g\2\2\u0154*\3\2\2\2\u0155\u0156\7V\2\2\u0156\u0157")
        buf.write("\7t\2\2\u0157\u0158\7w\2\2\u0158\u0159\7g\2\2\u0159,\3")
        buf.write("\2\2\2\u015a\u015b\7H\2\2\u015b\u015c\7n\2\2\u015c\u015d")
        buf.write("\7q\2\2\u015d\u015e\7c\2\2\u015e\u015f\7v\2\2\u015f.\3")
        buf.write("\2\2\2\u0160\u0161\7E\2\2\u0161\u0162\7n\2\2\u0162\u0163")
        buf.write("\7c\2\2\u0163\u0164\7u\2\2\u0164\u0165\7u\2\2\u0165\60")
        buf.write("\3\2\2\2\u0166\u0167\7F\2\2\u0167\u0168\7g\2\2\u0168\u0169")
        buf.write("\7u\2\2\u0169\u016a\7v\2\2\u016a\u016b\7t\2\2\u016b\u016c")
        buf.write("\7w\2\2\u016c\u016d\7e\2\2\u016d\u016e\7v\2\2\u016e\u016f")
        buf.write("\7q\2\2\u016f\u0170\7t\2\2\u0170\62\3\2\2\2\u0171\u0172")
        buf.write("\7K\2\2\u0172\u0173\7h\2\2\u0173\64\3\2\2\2\u0174\u0175")
        buf.write("\7H\2\2\u0175\u0176\7c\2\2\u0176\u0177\7n\2\2\u0177\u0178")
        buf.write("\7u\2\2\u0178\u0179\7g\2\2\u0179\66\3\2\2\2\u017a\u017b")
        buf.write("\7D\2\2\u017b\u017c\7q\2\2\u017c\u017d\7q\2\2\u017d\u017e")
        buf.write("\7n\2\2\u017e\u017f\7g\2\2\u017f\u0180\7c\2\2\u0180\u0181")
        buf.write("\7p\2\2\u01818\3\2\2\2\u0182\u0183\7P\2\2\u0183\u0184")
        buf.write("\7g\2\2\u0184\u0185\7y\2\2\u0185:\3\2\2\2\u0186\u0187")
        buf.write("\7G\2\2\u0187\u0188\7n\2\2\u0188\u0189\7u\2\2\u0189\u018a")
        buf.write("\7g\2\2\u018a\u018b\7k\2\2\u018b\u018c\7h\2\2\u018c<\3")
        buf.write("\2\2\2\u018d\u018e\7C\2\2\u018e\u018f\7t\2\2\u018f\u0190")
        buf.write("\7t\2\2\u0190\u0191\7c\2\2\u0191\u0192\7{\2\2\u0192>\3")
        buf.write("\2\2\2\u0193\u0194\7U\2\2\u0194\u0195\7v\2\2\u0195\u0196")
        buf.write("\7t\2\2\u0196\u0197\7k\2\2\u0197\u0198\7p\2\2\u0198\u0199")
        buf.write("\7i\2\2\u0199@\3\2\2\2\u019a\u019b\7D\2\2\u019b\u019c")
        buf.write("\7{\2\2\u019cB\3\2\2\2\u019d\u019e\7G\2\2\u019e\u019f")
        buf.write("\7n\2\2\u019f\u01a0\7u\2\2\u01a0\u01a1\7g\2\2\u01a1D\3")
        buf.write("\2\2\2\u01a2\u01a3\7K\2\2\u01a3\u01a4\7p\2\2\u01a4F\3")
        buf.write("\2\2\2\u01a5\u01a6\7T\2\2\u01a6\u01a7\7g\2\2\u01a7\u01a8")
        buf.write("\7v\2\2\u01a8\u01a9\7w\2\2\u01a9\u01aa\7t\2\2\u01aa\u01ab")
        buf.write("\7p\2\2\u01abH\3\2\2\2\u01ac\u01ad\7U\2\2\u01ad\u01ae")
        buf.write("\7g\2\2\u01ae\u01af\7n\2\2\u01af\u01b0\7h\2\2\u01b0J\3")
        buf.write("\2\2\2\u01b1\u01b2\7*\2\2\u01b2L\3\2\2\2\u01b3\u01b4\7")
        buf.write("+\2\2\u01b4N\3\2\2\2\u01b5\u01b6\7]\2\2\u01b6P\3\2\2\2")
        buf.write("\u01b7\u01b8\7_\2\2\u01b8R\3\2\2\2\u01b9\u01ba\7}\2\2")
        buf.write("\u01baT\3\2\2\2\u01bb\u01bc\7\177\2\2\u01bcV\3\2\2\2\u01bd")
        buf.write("\u01be\7=\2\2\u01beX\3\2\2\2\u01bf\u01c0\7.\2\2\u01c0")
        buf.write("Z\3\2\2\2\u01c1\u01c2\7\60\2\2\u01c2\u01c3\7\60\2\2\u01c3")
        buf.write("\\\3\2\2\2\u01c4\u01c5\7-\2\2\u01c5^\3\2\2\2\u01c6\u01c7")
        buf.write("\7/\2\2\u01c7`\3\2\2\2\u01c8\u01c9\7,\2\2\u01c9b\3\2\2")
        buf.write("\2\u01ca\u01cb\7\61\2\2\u01cbd\3\2\2\2\u01cc\u01cd\7\'")
        buf.write("\2\2\u01cdf\3\2\2\2\u01ce\u01cf\7#\2\2\u01cfh\3\2\2\2")
        buf.write("\u01d0\u01d1\7(\2\2\u01d1\u01d2\7(\2\2\u01d2j\3\2\2\2")
        buf.write("\u01d3\u01d4\7~\2\2\u01d4\u01d5\7~\2\2\u01d5l\3\2\2\2")
        buf.write("\u01d6\u01d7\7?\2\2\u01d7\u01d8\7?\2\2\u01d8n\3\2\2\2")
        buf.write("\u01d9\u01da\7?\2\2\u01dap\3\2\2\2\u01db\u01dc\7#\2\2")
        buf.write("\u01dc\u01dd\7?\2\2\u01ddr\3\2\2\2\u01de\u01df\7>\2\2")
        buf.write("\u01dft\3\2\2\2\u01e0\u01e1\7>\2\2\u01e1\u01e2\7?\2\2")
        buf.write("\u01e2v\3\2\2\2\u01e3\u01e4\7@\2\2\u01e4x\3\2\2\2\u01e5")
        buf.write("\u01e6\7@\2\2\u01e6\u01e7\7?\2\2\u01e7z\3\2\2\2\u01e8")
        buf.write("\u01e9\7?\2\2\u01e9\u01ea\7?\2\2\u01ea\u01eb\7\60\2\2")
        buf.write("\u01eb|\3\2\2\2\u01ec\u01ed\7-\2\2\u01ed\u01ee\7\60\2")
        buf.write("\2\u01ee~\3\2\2\2\u01ef\u01f0\7\60\2\2\u01f0\u0080\3\2")
        buf.write("\2\2\u01f1\u01f2\7<\2\2\u01f2\u01f3\7<\2\2\u01f3\u0082")
        buf.write("\3\2\2\2\u01f4\u01f5\7<\2\2\u01f5\u0084\3\2\2\2\u01f6")
        buf.write("\u01f8\5\35\17\2\u01f7\u01f6\3\2\2\2\u01f7\u01f8\3\2\2")
        buf.write("\2\u01f8\u01f9\3\2\2\2\u01f9\u01fd\t\13\2\2\u01fa\u01fc")
        buf.write("\t\f\2\2\u01fb\u01fa\3\2\2\2\u01fc\u01ff\3\2\2\2\u01fd")
        buf.write("\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u0086\3\2\2\2")
        buf.write("\u01ff\u01fd\3\2\2\2\u0200\u0201\7%\2\2\u0201\u0202\7")
        buf.write("%\2\2\u0202\u0206\3\2\2\2\u0203\u0205\13\2\2\2\u0204\u0203")
        buf.write("\3\2\2\2\u0205\u0208\3\2\2\2\u0206\u0207\3\2\2\2\u0206")
        buf.write("\u0204\3\2\2\2\u0207\u0209\3\2\2\2\u0208\u0206\3\2\2\2")
        buf.write("\u0209\u020a\7%\2\2\u020a\u020b\7%\2\2\u020b\u020c\3\2")
        buf.write("\2\2\u020c\u020d\bD\b\2\u020d\u0088\3\2\2\2\u020e\u0210")
        buf.write("\t\r\2\2\u020f\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211")
        buf.write("\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0213\3\2\2\2")
        buf.write("\u0213\u0214\bE\b\2\u0214\u008a\3\2\2\2\u0215\u0219\7")
        buf.write("$\2\2\u0216\u0218\5\u008fH\2\u0217\u0216\3\2\2\2\u0218")
        buf.write("\u021b\3\2\2\2\u0219\u0217\3\2\2\2\u0219\u021a\3\2\2\2")
        buf.write("\u021a\u021d\3\2\2\2\u021b\u0219\3\2\2\2\u021c\u021e\t")
        buf.write("\16\2\2\u021d\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f")
        buf.write("\u0220\bF\t\2\u0220\u008c\3\2\2\2\u0221\u0225\7$\2\2\u0222")
        buf.write("\u0224\5\u008fH\2\u0223\u0222\3\2\2\2\u0224\u0227\3\2")
        buf.write("\2\2\u0225\u0223\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0228")
        buf.write("\3\2\2\2\u0227\u0225\3\2\2\2\u0228\u0229\5\u0093J\2\u0229")
        buf.write("\u022a\bG\n\2\u022a\u008e\3\2\2\2\u022b\u022e\n\17\2\2")
        buf.write("\u022c\u022e\5\u0091I\2\u022d\u022b\3\2\2\2\u022d\u022c")
        buf.write("\3\2\2\2\u022e\u0090\3\2\2\2\u022f\u0230\7^\2\2\u0230")
        buf.write("\u0231\t\20\2\2\u0231\u0092\3\2\2\2\u0232\u0233\7^\2\2")
        buf.write("\u0233\u0236\n\20\2\2\u0234\u0236\n\21\2\2\u0235\u0232")
        buf.write("\3\2\2\2\u0235\u0234\3\2\2\2\u0236\u0094\3\2\2\2\u0237")
        buf.write("\u0238\13\2\2\2\u0238\u0239\bK\13\2\u0239\u0096\3\2\2")
        buf.write("\2#\2\u009c\u00a3\u00a8\u00ab\u00b3\u00b8\u00bd\u00c0")
        buf.write("\u00c8\u00cd\u00d0\u00d8\u00df\u00e2\u00e7\u00ef\u00f6")
        buf.write("\u00fb\u00fe\u0104\u0109\u010f\u0116\u01f7\u01fd\u0206")
        buf.write("\u0211\u0219\u021d\u0225\u022d\u0235\f\3\2\2\3\3\3\3\4")
        buf.write("\4\3\5\5\3\7\6\3\13\7\b\2\2\3F\b\3G\t\3K\n")
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
    BLOCK_COMMENT = 64
    WS = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67
    ERROR_CHAR = 68

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
            "DOT", "DOUBLE_COLON", "COLON", "ID", "BLOCK_COMMENT", "WS", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
                  "COLON", "ID", "BLOCK_COMMENT", "WS", "UNCLOSE_STRING", 
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
            	
     


