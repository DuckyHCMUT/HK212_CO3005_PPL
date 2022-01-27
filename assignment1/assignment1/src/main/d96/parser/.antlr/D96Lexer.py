# Generated from d:\HCMUT\Semester 212\Principles of Programming Languages\HK212_CO3005_PPL\assignment1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2H")
        buf.write("\u024f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\3\2\3\2\5\2\u009e\n\2\3\3\3\3\3\3\3\3\3\3\5\3")
        buf.write("\u00a5\n\3\3\3\3\3\3\4\3\4\3\4\5\4\u00ac\n\4\3\4\7\4\u00af")
        buf.write("\n\4\f\4\16\4\u00b2\13\4\5\4\u00b4\n\4\3\5\3\5\3\5\3\5")
        buf.write("\5\5\u00ba\n\5\3\5\3\5\3\5\5\5\u00bf\n\5\3\5\7\5\u00c2")
        buf.write("\n\5\f\5\16\5\u00c5\13\5\5\5\u00c7\n\5\3\6\3\6\3\6\3\6")
        buf.write("\5\6\u00cd\n\6\3\6\7\6\u00d0\n\6\f\6\16\6\u00d3\13\6\5")
        buf.write("\6\u00d5\n\6\3\7\3\7\3\7\3\7\5\7\u00db\n\7\3\7\3\7\3\7")
        buf.write("\5\7\u00e0\n\7\3\7\7\7\u00e3\n\7\f\7\16\7\u00e6\13\7\5")
        buf.write("\7\u00e8\n\7\3\b\3\b\3\b\5\b\u00ed\n\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\5\b\u00f5\n\b\3\b\3\b\3\t\3\t\3\t\5\t\u00fc\n")
        buf.write("\t\3\t\7\t\u00ff\n\t\f\t\16\t\u0102\13\t\5\t\u0104\n\t")
        buf.write("\3\n\3\n\7\n\u0108\n\n\f\n\16\n\u010b\13\n\3\13\3\13\5")
        buf.write("\13\u010f\n\13\3\13\6\13\u0112\n\13\r\13\16\13\u0113\3")
        buf.write("\f\3\f\3\f\3\f\7\f\u011a\n\f\f\f\16\f\u011d\13\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!")
        buf.write("\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\38\38\38\39\39\3:\3:\3:\3;\3;\3<\3<\3")
        buf.write("<\3=\3=\3>\3>\3>\3?\3?\3?\3?\3@\3@\3@\3A\3A\3B\3B\3B\3")
        buf.write("C\3C\3D\3D\7D\u01fe\nD\fD\16D\u0201\13D\3E\3E\6E\u0205")
        buf.write("\nE\rE\16E\u0206\3F\3F\3F\3F\7F\u020d\nF\fF\16F\u0210")
        buf.write("\13F\3F\3F\3F\3F\3F\3G\6G\u0218\nG\rG\16G\u0219\3G\3G")
        buf.write("\3H\3H\3I\3I\3I\7I\u0223\nI\fI\16I\u0226\13I\3I\5I\u0229")
        buf.write("\nI\3I\3I\3J\3J\3J\7J\u0230\nJ\fJ\16J\u0233\13J\3J\3J")
        buf.write("\3J\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\5")
        buf.write("K\u0248\nK\3L\3L\3L\3M\3M\3M\3\u020e\2N\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\2\23\2\25\2\27\n\31\13\33\f\35\r\37")
        buf.write("\16!\17#\20%\21\'\22)\23+\24-\25/\26\61\27\63\30\65\31")
        buf.write("\67\329\33;\34=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[")
        buf.write(",]-_.a/c\60e\61g\62i\63k\64m\65o\66q\67s8u9w:y;{<}=\177")
        buf.write(">\u0081?\u0083@\u0085A\u0087B\u0089C\u008bD\u008dE\u008f")
        buf.write("\2\u0091F\u0093G\u0095\2\u0097\2\u0099H\3\2\21\3\2\63")
        buf.write(";\3\2\62;\4\2\63;CH\4\2\62;CH\3\2\639\3\2\629\3\2\62\63")
        buf.write("\4\2GGgg\4\2--//\5\2C\\aac|\6\2\62;C\\aac|\5\2\n\f\16")
        buf.write("\17\"\"\5\2\f\f$$^^\3\3\f\f\t\2))^^ddhhppttvv\2\u0276")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\27\3\2\2\2\2\31\3")
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
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0099\3\2\2\2\3\u009d")
        buf.write("\3\2\2\2\5\u00a4\3\2\2\2\7\u00b3\3\2\2\2\t\u00b9\3\2\2")
        buf.write("\2\13\u00c8\3\2\2\2\r\u00da\3\2\2\2\17\u00f4\3\2\2\2\21")
        buf.write("\u0103\3\2\2\2\23\u0105\3\2\2\2\25\u010c\3\2\2\2\27\u0115")
        buf.write("\3\2\2\2\31\u0121\3\2\2\2\33\u0124\3\2\2\2\35\u0128\3")
        buf.write("\2\2\2\37\u012c\3\2\2\2!\u012e\3\2\2\2#\u0134\3\2\2\2")
        buf.write("%\u013c\3\2\2\2\'\u0140\3\2\2\2)\u0145\3\2\2\2+\u0151")
        buf.write("\3\2\2\2-\u015a\3\2\2\2/\u015f\3\2\2\2\61\u0165\3\2\2")
        buf.write("\2\63\u016b\3\2\2\2\65\u0176\3\2\2\2\67\u0179\3\2\2\2")
        buf.write("9\u017f\3\2\2\2;\u0187\3\2\2\2=\u018b\3\2\2\2?\u0192\3")
        buf.write("\2\2\2A\u0198\3\2\2\2C\u019f\3\2\2\2E\u01a2\3\2\2\2G\u01a7")
        buf.write("\3\2\2\2I\u01aa\3\2\2\2K\u01b1\3\2\2\2M\u01b6\3\2\2\2")
        buf.write("O\u01b8\3\2\2\2Q\u01ba\3\2\2\2S\u01bc\3\2\2\2U\u01be\3")
        buf.write("\2\2\2W\u01c0\3\2\2\2Y\u01c2\3\2\2\2[\u01c4\3\2\2\2]\u01c6")
        buf.write("\3\2\2\2_\u01c9\3\2\2\2a\u01cb\3\2\2\2c\u01cd\3\2\2\2")
        buf.write("e\u01cf\3\2\2\2g\u01d1\3\2\2\2i\u01d3\3\2\2\2k\u01d5\3")
        buf.write("\2\2\2m\u01d8\3\2\2\2o\u01db\3\2\2\2q\u01de\3\2\2\2s\u01e0")
        buf.write("\3\2\2\2u\u01e3\3\2\2\2w\u01e5\3\2\2\2y\u01e8\3\2\2\2")
        buf.write("{\u01ea\3\2\2\2}\u01ed\3\2\2\2\177\u01f1\3\2\2\2\u0081")
        buf.write("\u01f4\3\2\2\2\u0083\u01f6\3\2\2\2\u0085\u01f9\3\2\2\2")
        buf.write("\u0087\u01fb\3\2\2\2\u0089\u0202\3\2\2\2\u008b\u0208\3")
        buf.write("\2\2\2\u008d\u0217\3\2\2\2\u008f\u021d\3\2\2\2\u0091\u021f")
        buf.write("\3\2\2\2\u0093\u022c\3\2\2\2\u0095\u0247\3\2\2\2\u0097")
        buf.write("\u0249\3\2\2\2\u0099\u024c\3\2\2\2\u009b\u009e\5-\27\2")
        buf.write("\u009c\u009e\5\67\34\2\u009d\u009b\3\2\2\2\u009d\u009c")
        buf.write("\3\2\2\2\u009e\4\3\2\2\2\u009f\u00a5\5\7\4\2\u00a0\u00a5")
        buf.write("\5\t\5\2\u00a1\u00a5\5\13\6\2\u00a2\u00a5\5\r\7\2\u00a3")
        buf.write("\u00a5\5\r\7\2\u00a4\u009f\3\2\2\2\u00a4\u00a0\3\2\2\2")
        buf.write("\u00a4\u00a1\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a3\3")
        buf.write("\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\b\3\2\2\u00a7\6")
        buf.write("\3\2\2\2\u00a8\u00b4\7\62\2\2\u00a9\u00b0\t\2\2\2\u00aa")
        buf.write("\u00ac\7a\2\2\u00ab\u00aa\3\2\2\2\u00ab\u00ac\3\2\2\2")
        buf.write("\u00ac\u00ad\3\2\2\2\u00ad\u00af\t\3\2\2\u00ae\u00ab\3")
        buf.write("\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1")
        buf.write("\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3")
        buf.write("\u00a8\3\2\2\2\u00b3\u00a9\3\2\2\2\u00b4\b\3\2\2\2\u00b5")
        buf.write("\u00b6\7\62\2\2\u00b6\u00ba\7z\2\2\u00b7\u00b8\7\62\2")
        buf.write("\2\u00b8\u00ba\7Z\2\2\u00b9\u00b5\3\2\2\2\u00b9\u00b7")
        buf.write("\3\2\2\2\u00ba\u00c6\3\2\2\2\u00bb\u00c7\7\62\2\2\u00bc")
        buf.write("\u00c3\t\4\2\2\u00bd\u00bf\7a\2\2\u00be\u00bd\3\2\2\2")
        buf.write("\u00be\u00bf\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c2\t")
        buf.write("\5\2\2\u00c1\u00be\3\2\2\2\u00c2\u00c5\3\2\2\2\u00c3\u00c1")
        buf.write("\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5")
        buf.write("\u00c3\3\2\2\2\u00c6\u00bb\3\2\2\2\u00c6\u00bc\3\2\2\2")
        buf.write("\u00c7\n\3\2\2\2\u00c8\u00d4\7\62\2\2\u00c9\u00d5\7\62")
        buf.write("\2\2\u00ca\u00d1\t\6\2\2\u00cb\u00cd\7a\2\2\u00cc\u00cb")
        buf.write("\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce")
        buf.write("\u00d0\t\7\2\2\u00cf\u00cc\3\2\2\2\u00d0\u00d3\3\2\2\2")
        buf.write("\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d5\3")
        buf.write("\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00c9\3\2\2\2\u00d4\u00ca")
        buf.write("\3\2\2\2\u00d5\f\3\2\2\2\u00d6\u00d7\7\62\2\2\u00d7\u00db")
        buf.write("\7d\2\2\u00d8\u00d9\7\62\2\2\u00d9\u00db\7D\2\2\u00da")
        buf.write("\u00d6\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00e7\3\2\2\2")
        buf.write("\u00dc\u00e8\7\62\2\2\u00dd\u00e4\7\63\2\2\u00de\u00e0")
        buf.write("\7a\2\2\u00df\u00de\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0")
        buf.write("\u00e1\3\2\2\2\u00e1\u00e3\t\b\2\2\u00e2\u00df\3\2\2\2")
        buf.write("\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3")
        buf.write("\2\2\2\u00e5\u00e8\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00dc")
        buf.write("\3\2\2\2\u00e7\u00dd\3\2\2\2\u00e8\16\3\2\2\2\u00e9\u00ea")
        buf.write("\5\21\t\2\u00ea\u00ec\5\23\n\2\u00eb\u00ed\5\25\13\2\u00ec")
        buf.write("\u00eb\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00f5\3\2\2\2")
        buf.write("\u00ee\u00ef\5\21\t\2\u00ef\u00f0\5\25\13\2\u00f0\u00f5")
        buf.write("\3\2\2\2\u00f1\u00f2\5\23\n\2\u00f2\u00f3\5\25\13\2\u00f3")
        buf.write("\u00f5\3\2\2\2\u00f4\u00e9\3\2\2\2\u00f4\u00ee\3\2\2\2")
        buf.write("\u00f4\u00f1\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\b")
        buf.write("\b\3\2\u00f7\20\3\2\2\2\u00f8\u0104\7\62\2\2\u00f9\u0100")
        buf.write("\t\2\2\2\u00fa\u00fc\7a\2\2\u00fb\u00fa\3\2\2\2\u00fb")
        buf.write("\u00fc\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00ff\t\3\2\2")
        buf.write("\u00fe\u00fb\3\2\2\2\u00ff\u0102\3\2\2\2\u0100\u00fe\3")
        buf.write("\2\2\2\u0100\u0101\3\2\2\2\u0101\u0104\3\2\2\2\u0102\u0100")
        buf.write("\3\2\2\2\u0103\u00f8\3\2\2\2\u0103\u00f9\3\2\2\2\u0104")
        buf.write("\22\3\2\2\2\u0105\u0109\5\u0081A\2\u0106\u0108\t\3\2\2")
        buf.write("\u0107\u0106\3\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3")
        buf.write("\2\2\2\u0109\u010a\3\2\2\2\u010a\24\3\2\2\2\u010b\u0109")
        buf.write("\3\2\2\2\u010c\u010e\t\t\2\2\u010d\u010f\t\n\2\2\u010e")
        buf.write("\u010d\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0111\3\2\2\2")
        buf.write("\u0110\u0112\t\3\2\2\u0111\u0110\3\2\2\2\u0112\u0113\3")
        buf.write("\2\2\2\u0113\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114\26")
        buf.write("\3\2\2\2\u0115\u011b\7$\2\2\u0116\u011a\5\u008fH\2\u0117")
        buf.write("\u011a\5\31\r\2\u0118\u011a\5\u0095K\2\u0119\u0116\3\2")
        buf.write("\2\2\u0119\u0117\3\2\2\2\u0119\u0118\3\2\2\2\u011a\u011d")
        buf.write("\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c")
        buf.write("\u011e\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u011f\7$\2\2")
        buf.write("\u011f\u0120\b\f\4\2\u0120\30\3\2\2\2\u0121\u0122\7)\2")
        buf.write("\2\u0122\u0123\7$\2\2\u0123\32\3\2\2\2\u0124\u0125\7X")
        buf.write("\2\2\u0125\u0126\7c\2\2\u0126\u0127\7n\2\2\u0127\34\3")
        buf.write("\2\2\2\u0128\u0129\7X\2\2\u0129\u012a\7c\2\2\u012a\u012b")
        buf.write("\7t\2\2\u012b\36\3\2\2\2\u012c\u012d\7&\2\2\u012d \3\2")
        buf.write("\2\2\u012e\u012f\7D\2\2\u012f\u0130\7t\2\2\u0130\u0131")
        buf.write("\7g\2\2\u0131\u0132\7c\2\2\u0132\u0133\7m\2\2\u0133\"")
        buf.write("\3\2\2\2\u0134\u0135\7H\2\2\u0135\u0136\7q\2\2\u0136\u0137")
        buf.write("\7t\2\2\u0137\u0138\7g\2\2\u0138\u0139\7c\2\2\u0139\u013a")
        buf.write("\7e\2\2\u013a\u013b\7j\2\2\u013b$\3\2\2\2\u013c\u013d")
        buf.write("\7K\2\2\u013d\u013e\7p\2\2\u013e\u013f\7v\2\2\u013f&\3")
        buf.write("\2\2\2\u0140\u0141\7P\2\2\u0141\u0142\7w\2\2\u0142\u0143")
        buf.write("\7n\2\2\u0143\u0144\7n\2\2\u0144(\3\2\2\2\u0145\u0146")
        buf.write("\7E\2\2\u0146\u0147\7q\2\2\u0147\u0148\7p\2\2\u0148\u0149")
        buf.write("\7u\2\2\u0149\u014a\7v\2\2\u014a\u014b\7t\2\2\u014b\u014c")
        buf.write("\7w\2\2\u014c\u014d\7e\2\2\u014d\u014e\7v\2\2\u014e\u014f")
        buf.write("\7q\2\2\u014f\u0150\7t\2\2\u0150*\3\2\2\2\u0151\u0152")
        buf.write("\7E\2\2\u0152\u0153\7q\2\2\u0153\u0154\7p\2\2\u0154\u0155")
        buf.write("\7v\2\2\u0155\u0156\7k\2\2\u0156\u0157\7p\2\2\u0157\u0158")
        buf.write("\7w\2\2\u0158\u0159\7g\2\2\u0159,\3\2\2\2\u015a\u015b")
        buf.write("\7V\2\2\u015b\u015c\7t\2\2\u015c\u015d\7w\2\2\u015d\u015e")
        buf.write("\7g\2\2\u015e.\3\2\2\2\u015f\u0160\7H\2\2\u0160\u0161")
        buf.write("\7n\2\2\u0161\u0162\7q\2\2\u0162\u0163\7c\2\2\u0163\u0164")
        buf.write("\7v\2\2\u0164\60\3\2\2\2\u0165\u0166\7E\2\2\u0166\u0167")
        buf.write("\7n\2\2\u0167\u0168\7c\2\2\u0168\u0169\7u\2\2\u0169\u016a")
        buf.write("\7u\2\2\u016a\62\3\2\2\2\u016b\u016c\7F\2\2\u016c\u016d")
        buf.write("\7g\2\2\u016d\u016e\7u\2\2\u016e\u016f\7v\2\2\u016f\u0170")
        buf.write("\7t\2\2\u0170\u0171\7w\2\2\u0171\u0172\7e\2\2\u0172\u0173")
        buf.write("\7v\2\2\u0173\u0174\7q\2\2\u0174\u0175\7t\2\2\u0175\64")
        buf.write("\3\2\2\2\u0176\u0177\7K\2\2\u0177\u0178\7h\2\2\u0178\66")
        buf.write("\3\2\2\2\u0179\u017a\7H\2\2\u017a\u017b\7c\2\2\u017b\u017c")
        buf.write("\7n\2\2\u017c\u017d\7u\2\2\u017d\u017e\7g\2\2\u017e8\3")
        buf.write("\2\2\2\u017f\u0180\7D\2\2\u0180\u0181\7q\2\2\u0181\u0182")
        buf.write("\7q\2\2\u0182\u0183\7n\2\2\u0183\u0184\7g\2\2\u0184\u0185")
        buf.write("\7c\2\2\u0185\u0186\7p\2\2\u0186:\3\2\2\2\u0187\u0188")
        buf.write("\7P\2\2\u0188\u0189\7g\2\2\u0189\u018a\7y\2\2\u018a<\3")
        buf.write("\2\2\2\u018b\u018c\7G\2\2\u018c\u018d\7n\2\2\u018d\u018e")
        buf.write("\7u\2\2\u018e\u018f\7g\2\2\u018f\u0190\7k\2\2\u0190\u0191")
        buf.write("\7h\2\2\u0191>\3\2\2\2\u0192\u0193\7C\2\2\u0193\u0194")
        buf.write("\7t\2\2\u0194\u0195\7t\2\2\u0195\u0196\7c\2\2\u0196\u0197")
        buf.write("\7{\2\2\u0197@\3\2\2\2\u0198\u0199\7U\2\2\u0199\u019a")
        buf.write("\7v\2\2\u019a\u019b\7t\2\2\u019b\u019c\7k\2\2\u019c\u019d")
        buf.write("\7p\2\2\u019d\u019e\7i\2\2\u019eB\3\2\2\2\u019f\u01a0")
        buf.write("\7D\2\2\u01a0\u01a1\7{\2\2\u01a1D\3\2\2\2\u01a2\u01a3")
        buf.write("\7G\2\2\u01a3\u01a4\7n\2\2\u01a4\u01a5\7u\2\2\u01a5\u01a6")
        buf.write("\7g\2\2\u01a6F\3\2\2\2\u01a7\u01a8\7K\2\2\u01a8\u01a9")
        buf.write("\7p\2\2\u01a9H\3\2\2\2\u01aa\u01ab\7T\2\2\u01ab\u01ac")
        buf.write("\7g\2\2\u01ac\u01ad\7v\2\2\u01ad\u01ae\7w\2\2\u01ae\u01af")
        buf.write("\7t\2\2\u01af\u01b0\7p\2\2\u01b0J\3\2\2\2\u01b1\u01b2")
        buf.write("\7U\2\2\u01b2\u01b3\7g\2\2\u01b3\u01b4\7n\2\2\u01b4\u01b5")
        buf.write("\7h\2\2\u01b5L\3\2\2\2\u01b6\u01b7\7*\2\2\u01b7N\3\2\2")
        buf.write("\2\u01b8\u01b9\7+\2\2\u01b9P\3\2\2\2\u01ba\u01bb\7]\2")
        buf.write("\2\u01bbR\3\2\2\2\u01bc\u01bd\7_\2\2\u01bdT\3\2\2\2\u01be")
        buf.write("\u01bf\7}\2\2\u01bfV\3\2\2\2\u01c0\u01c1\7\177\2\2\u01c1")
        buf.write("X\3\2\2\2\u01c2\u01c3\7=\2\2\u01c3Z\3\2\2\2\u01c4\u01c5")
        buf.write("\7.\2\2\u01c5\\\3\2\2\2\u01c6\u01c7\7\60\2\2\u01c7\u01c8")
        buf.write("\7\60\2\2\u01c8^\3\2\2\2\u01c9\u01ca\7-\2\2\u01ca`\3\2")
        buf.write("\2\2\u01cb\u01cc\7/\2\2\u01ccb\3\2\2\2\u01cd\u01ce\7,")
        buf.write("\2\2\u01ced\3\2\2\2\u01cf\u01d0\7\61\2\2\u01d0f\3\2\2")
        buf.write("\2\u01d1\u01d2\7\'\2\2\u01d2h\3\2\2\2\u01d3\u01d4\7#\2")
        buf.write("\2\u01d4j\3\2\2\2\u01d5\u01d6\7(\2\2\u01d6\u01d7\7(\2")
        buf.write("\2\u01d7l\3\2\2\2\u01d8\u01d9\7~\2\2\u01d9\u01da\7~\2")
        buf.write("\2\u01dan\3\2\2\2\u01db\u01dc\7?\2\2\u01dc\u01dd\7?\2")
        buf.write("\2\u01ddp\3\2\2\2\u01de\u01df\7?\2\2\u01dfr\3\2\2\2\u01e0")
        buf.write("\u01e1\7#\2\2\u01e1\u01e2\7?\2\2\u01e2t\3\2\2\2\u01e3")
        buf.write("\u01e4\7>\2\2\u01e4v\3\2\2\2\u01e5\u01e6\7>\2\2\u01e6")
        buf.write("\u01e7\7?\2\2\u01e7x\3\2\2\2\u01e8\u01e9\7@\2\2\u01e9")
        buf.write("z\3\2\2\2\u01ea\u01eb\7@\2\2\u01eb\u01ec\7?\2\2\u01ec")
        buf.write("|\3\2\2\2\u01ed\u01ee\7?\2\2\u01ee\u01ef\7?\2\2\u01ef")
        buf.write("\u01f0\7\60\2\2\u01f0~\3\2\2\2\u01f1\u01f2\7-\2\2\u01f2")
        buf.write("\u01f3\7\60\2\2\u01f3\u0080\3\2\2\2\u01f4\u01f5\7\60\2")
        buf.write("\2\u01f5\u0082\3\2\2\2\u01f6\u01f7\7<\2\2\u01f7\u01f8")
        buf.write("\7<\2\2\u01f8\u0084\3\2\2\2\u01f9\u01fa\7<\2\2\u01fa\u0086")
        buf.write("\3\2\2\2\u01fb\u01ff\t\13\2\2\u01fc\u01fe\t\f\2\2\u01fd")
        buf.write("\u01fc\3\2\2\2\u01fe\u0201\3\2\2\2\u01ff\u01fd\3\2\2\2")
        buf.write("\u01ff\u0200\3\2\2\2\u0200\u0088\3\2\2\2\u0201\u01ff\3")
        buf.write("\2\2\2\u0202\u0204\5\37\20\2\u0203\u0205\t\f\2\2\u0204")
        buf.write("\u0203\3\2\2\2\u0205\u0206\3\2\2\2\u0206\u0204\3\2\2\2")
        buf.write("\u0206\u0207\3\2\2\2\u0207\u008a\3\2\2\2\u0208\u0209\7")
        buf.write("%\2\2\u0209\u020a\7%\2\2\u020a\u020e\3\2\2\2\u020b\u020d")
        buf.write("\13\2\2\2\u020c\u020b\3\2\2\2\u020d\u0210\3\2\2\2\u020e")
        buf.write("\u020f\3\2\2\2\u020e\u020c\3\2\2\2\u020f\u0211\3\2\2\2")
        buf.write("\u0210\u020e\3\2\2\2\u0211\u0212\7%\2\2\u0212\u0213\7")
        buf.write("%\2\2\u0213\u0214\3\2\2\2\u0214\u0215\bF\5\2\u0215\u008c")
        buf.write("\3\2\2\2\u0216\u0218\t\r\2\2\u0217\u0216\3\2\2\2\u0218")
        buf.write("\u0219\3\2\2\2\u0219\u0217\3\2\2\2\u0219\u021a\3\2\2\2")
        buf.write("\u021a\u021b\3\2\2\2\u021b\u021c\bG\5\2\u021c\u008e\3")
        buf.write("\2\2\2\u021d\u021e\n\16\2\2\u021e\u0090\3\2\2\2\u021f")
        buf.write("\u0224\7$\2\2\u0220\u0223\5\u008fH\2\u0221\u0223\5\u0095")
        buf.write("K\2\u0222\u0220\3\2\2\2\u0222\u0221\3\2\2\2\u0223\u0226")
        buf.write("\3\2\2\2\u0224\u0222\3\2\2\2\u0224\u0225\3\2\2\2\u0225")
        buf.write("\u0228\3\2\2\2\u0226\u0224\3\2\2\2\u0227\u0229\t\17\2")
        buf.write("\2\u0228\u0227\3\2\2\2\u0229\u022a\3\2\2\2\u022a\u022b")
        buf.write("\bI\6\2\u022b\u0092\3\2\2\2\u022c\u0231\7$\2\2\u022d\u0230")
        buf.write("\5\u008fH\2\u022e\u0230\5\u0095K\2\u022f\u022d\3\2\2\2")
        buf.write("\u022f\u022e\3\2\2\2\u0230\u0233\3\2\2\2\u0231\u022f\3")
        buf.write("\2\2\2\u0231\u0232\3\2\2\2\u0232\u0234\3\2\2\2\u0233\u0231")
        buf.write("\3\2\2\2\u0234\u0235\5\u0097L\2\u0235\u0236\bJ\7\2\u0236")
        buf.write("\u0094\3\2\2\2\u0237\u0238\7^\2\2\u0238\u0248\7d\2\2\u0239")
        buf.write("\u023a\7^\2\2\u023a\u0248\7h\2\2\u023b\u023c\7^\2\2\u023c")
        buf.write("\u0248\7t\2\2\u023d\u023e\7^\2\2\u023e\u0248\7p\2\2\u023f")
        buf.write("\u0240\7^\2\2\u0240\u0248\7v\2\2\u0241\u0242\7^\2\2\u0242")
        buf.write("\u0248\7)\2\2\u0243\u0244\7^\2\2\u0244\u0248\7^\2\2\u0245")
        buf.write("\u0246\7)\2\2\u0246\u0248\7$\2\2\u0247\u0237\3\2\2\2\u0247")
        buf.write("\u0239\3\2\2\2\u0247\u023b\3\2\2\2\u0247\u023d\3\2\2\2")
        buf.write("\u0247\u023f\3\2\2\2\u0247\u0241\3\2\2\2\u0247\u0243\3")
        buf.write("\2\2\2\u0247\u0245\3\2\2\2\u0248\u0096\3\2\2\2\u0249\u024a")
        buf.write("\7^\2\2\u024a\u024b\n\20\2\2\u024b\u0098\3\2\2\2\u024c")
        buf.write("\u024d\13\2\2\2\u024d\u024e\bM\b\2\u024e\u009a\3\2\2\2")
        buf.write("\'\2\u009d\u00a4\u00ab\u00b0\u00b3\u00b9\u00be\u00c3\u00c6")
        buf.write("\u00cc\u00d1\u00d4\u00da\u00df\u00e4\u00e7\u00ec\u00f4")
        buf.write("\u00fb\u0100\u0103\u0109\u010e\u0113\u0119\u011b\u01ff")
        buf.write("\u0206\u020e\u0219\u0222\u0224\u0228\u022f\u0231\u0247")
        buf.write("\t\3\3\2\3\b\3\3\f\4\b\2\2\3I\5\3J\6\3M\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LITERAL_BOOLEAN = 1
    LITERAL_INT = 2
    LITERAL_INT_DEC = 3
    LITERAL_INT_HEX = 4
    LITERAL_INT_OCT = 5
    LITERAL_INT_BIN = 6
    LITERAL_FLOAT = 7
    LITERAL_STRING = 8
    DOUBLE_QUOTE = 9
    VAL = 10
    VAR = 11
    STATIC = 12
    BREAK = 13
    FOREACH = 14
    INT = 15
    NULL = 16
    CONSTRUCTOR = 17
    CONTINUE = 18
    TRUE = 19
    FLOAT = 20
    CLASS = 21
    DESTRUCTOR = 22
    IF = 23
    FALSE = 24
    BOOLEAN = 25
    NEW = 26
    ELSEIF = 27
    ARRAY = 28
    STRING = 29
    BY = 30
    ELSE = 31
    IN = 32
    RETURN = 33
    SELF = 34
    LB = 35
    RB = 36
    LS = 37
    RS = 38
    LP = 39
    RP = 40
    SEMI = 41
    COMMA = 42
    DOTDOT = 43
    ADD = 44
    SUBTRACT = 45
    MULTIPLY = 46
    DIVIDE = 47
    MODULO = 48
    NOT = 49
    AND = 50
    OR = 51
    EQUAL = 52
    ASSIGN = 53
    NOT_EQUAL = 54
    LESS_THAN = 55
    LEQ = 56
    GREATER_THAN = 57
    GEQ = 58
    EQUAL_STRING = 59
    STRING_CONCAT = 60
    DOT = 61
    DOUBLE_COLON = 62
    COLON = 63
    ID = 64
    DOLLAR_ID = 65
    BLOCK_COMMENT = 66
    WS = 67
    UNCLOSE_STRING = 68
    ILLEGAL_ESCAPE = 69
    ERROR_CHAR = 70

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
            "LITERAL_BOOLEAN", "LITERAL_INT", "LITERAL_INT_DEC", "LITERAL_INT_HEX", 
            "LITERAL_INT_OCT", "LITERAL_INT_BIN", "LITERAL_FLOAT", "LITERAL_STRING", 
            "DOUBLE_QUOTE", "VAL", "VAR", "STATIC", "BREAK", "FOREACH", 
            "INT", "NULL", "CONSTRUCTOR", "CONTINUE", "TRUE", "FLOAT", "CLASS", 
            "DESTRUCTOR", "IF", "FALSE", "BOOLEAN", "NEW", "ELSEIF", "ARRAY", 
            "STRING", "BY", "ELSE", "IN", "RETURN", "SELF", "LB", "RB", 
            "LS", "RS", "LP", "RP", "SEMI", "COMMA", "DOTDOT", "ADD", "SUBTRACT", 
            "MULTIPLY", "DIVIDE", "MODULO", "NOT", "AND", "OR", "EQUAL", 
            "ASSIGN", "NOT_EQUAL", "LESS_THAN", "LEQ", "GREATER_THAN", "GEQ", 
            "EQUAL_STRING", "STRING_CONCAT", "DOT", "DOUBLE_COLON", "COLON", 
            "ID", "DOLLAR_ID", "BLOCK_COMMENT", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "LITERAL_BOOLEAN", "LITERAL_INT", "LITERAL_INT_DEC", "LITERAL_INT_HEX", 
                  "LITERAL_INT_OCT", "LITERAL_INT_BIN", "LITERAL_FLOAT", 
                  "FLOAT_INT", "FLOAT_DECIMAL", "FLOAT_EXP", "LITERAL_STRING", 
                  "DOUBLE_QUOTE", "VAL", "VAR", "STATIC", "BREAK", "FOREACH", 
                  "INT", "NULL", "CONSTRUCTOR", "CONTINUE", "TRUE", "FLOAT", 
                  "CLASS", "DESTRUCTOR", "IF", "FALSE", "BOOLEAN", "NEW", 
                  "ELSEIF", "ARRAY", "STRING", "BY", "ELSE", "IN", "RETURN", 
                  "SELF", "LB", "RB", "LS", "RS", "LP", "RP", "SEMI", "COMMA", 
                  "DOTDOT", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", "MODULO", 
                  "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", "LESS_THAN", 
                  "LEQ", "GREATER_THAN", "GEQ", "EQUAL_STRING", "STRING_CONCAT", 
                  "DOT", "DOUBLE_COLON", "COLON", "ID", "DOLLAR_ID", "BLOCK_COMMENT", 
                  "WS", "STRING_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ESC_SEQUENCE", "ESC_ILLEGAL", "ERROR_CHAR" ]

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
            actions[6] = self.LITERAL_FLOAT_action 
            actions[10] = self.LITERAL_STRING_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            actions[75] = self.ERROR_CHAR_action 
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
            	
     


