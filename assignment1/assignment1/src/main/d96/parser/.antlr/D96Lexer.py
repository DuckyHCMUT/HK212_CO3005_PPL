# Generated from d:\HCMUT\Semester 212\Principles of Programming Languages\HK212_CO3005_PPL\assignment1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u0247\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u00a0\n\2\3\2\3\2\3\2\5")
        buf.write("\2\u00a5\n\2\3\3\3\3\3\3\5\3\u00aa\n\3\3\3\7\3\u00ad\n")
        buf.write("\3\f\3\16\3\u00b0\13\3\5\3\u00b2\n\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\5\4\u00ba\n\4\3\4\3\4\3\4\5\4\u00bf\n\4\3\4\7\4")
        buf.write("\u00c2\n\4\f\4\16\4\u00c5\13\4\5\4\u00c7\n\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\5\5\u00cf\n\5\3\5\7\5\u00d2\n\5\f\5\16")
        buf.write("\5\u00d5\13\5\5\5\u00d7\n\5\3\5\3\5\3\6\3\6\3\6\3\6\5")
        buf.write("\6\u00df\n\6\3\6\3\6\3\6\7\6\u00e4\n\6\f\6\16\6\u00e7")
        buf.write("\13\6\5\6\u00e9\n\6\3\7\3\7\3\7\5\7\u00ee\n\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\5\7\u00f6\n\7\3\7\3\7\3\b\3\b\3\b\5\b")
        buf.write("\u00fd\n\b\3\b\7\b\u0100\n\b\f\b\16\b\u0103\13\b\5\b\u0105")
        buf.write("\n\b\3\t\3\t\7\t\u0109\n\t\f\t\16\t\u010c\13\t\3\n\3\n")
        buf.write("\5\n\u0110\n\n\3\n\3\n\7\n\u0114\n\n\f\n\16\n\u0117\13")
        buf.write("\n\3\13\3\13\7\13\u011b\n\13\f\13\16\13\u011e\13\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#")
        buf.write("\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3\'\3")
        buf.write("\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3.\3/\3/")
        buf.write("\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\38\38\39\39\3")
        buf.write("9\3:\3:\3;\3;\3;\3<\3<\3=\3=\3=\3>\3>\3>\3>\3?\3?\3?\3")
        buf.write("@\3@\3A\3A\3A\3B\3B\3C\5C\u01fe\nC\3C\3C\7C\u0202\nC\f")
        buf.write("C\16C\u0205\13C\3D\3D\7D\u0209\nD\fD\16D\u020c\13D\3E")
        buf.write("\6E\u020f\nE\rE\16E\u0210\3E\3E\3F\3F\3F\3F\7F\u0219\n")
        buf.write("F\fF\16F\u021c\13F\3F\3F\3F\3F\3F\3G\3G\3G\3H\3H\7H\u0228")
        buf.write("\nH\fH\16H\u022b\13H\3H\5H\u022e\nH\3H\3H\3I\3I\7I\u0234")
        buf.write("\nI\fI\16I\u0237\13I\3I\3I\3I\3J\3J\5J\u023e\nJ\3K\3K")
        buf.write("\3K\3L\3L\3L\5L\u0246\nL\3\u021a\2M\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\2\21\2\23\2\25\t\27\n\31\13\33\f\35\r\37\16")
        buf.write("!\17#\20%\21\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67")
        buf.write("\329\33;\34=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-")
        buf.write("_.a/c\60e\61g\62i\63k\64m\65o\66q\67s8u9w:y;{<}=\177>")
        buf.write("\u0081?\u0083@\u0085A\u0087\2\u0089B\u008bC\u008dD\u008f")
        buf.write("E\u0091F\u0093\2\u0095\2\u0097\2\3\2\22\3\2\63;\3\2\62")
        buf.write(";\4\2\63;CH\4\2\62;CH\3\2\639\3\2\629\3\2\62\63\4\2GG")
        buf.write("gg\4\2--//\5\2C\\aac|\6\2\62;C\\aac|\5\2\n\f\16\17\"\"")
        buf.write("\7\3\n\f\16\17$$))^^\7\2\n\f\16\17$$))^^\n\2$$))^^ddh")
        buf.write("hppttvv\3\2^^\2\u0265\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2")
        buf.write("\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2")
        buf.write("\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u00a4\3\2\2\2\5\u00b1")
        buf.write("\3\2\2\2\7\u00b9\3\2\2\2\t\u00ca\3\2\2\2\13\u00de\3\2")
        buf.write("\2\2\r\u00f5\3\2\2\2\17\u0104\3\2\2\2\21\u0106\3\2\2\2")
        buf.write("\23\u010d\3\2\2\2\25\u0118\3\2\2\2\27\u0122\3\2\2\2\31")
        buf.write("\u0125\3\2\2\2\33\u0129\3\2\2\2\35\u012d\3\2\2\2\37\u012f")
        buf.write("\3\2\2\2!\u0135\3\2\2\2#\u013d\3\2\2\2%\u0141\3\2\2\2")
        buf.write("\'\u0146\3\2\2\2)\u0152\3\2\2\2+\u015b\3\2\2\2-\u0160")
        buf.write("\3\2\2\2/\u0166\3\2\2\2\61\u016c\3\2\2\2\63\u0177\3\2")
        buf.write("\2\2\65\u017a\3\2\2\2\67\u0180\3\2\2\29\u0188\3\2\2\2")
        buf.write(";\u018c\3\2\2\2=\u0193\3\2\2\2?\u0199\3\2\2\2A\u01a0\3")
        buf.write("\2\2\2C\u01a3\3\2\2\2E\u01a8\3\2\2\2G\u01ab\3\2\2\2I\u01b2")
        buf.write("\3\2\2\2K\u01b7\3\2\2\2M\u01b9\3\2\2\2O\u01bb\3\2\2\2")
        buf.write("Q\u01bd\3\2\2\2S\u01bf\3\2\2\2U\u01c1\3\2\2\2W\u01c3\3")
        buf.write("\2\2\2Y\u01c5\3\2\2\2[\u01c7\3\2\2\2]\u01ca\3\2\2\2_\u01cc")
        buf.write("\3\2\2\2a\u01ce\3\2\2\2c\u01d0\3\2\2\2e\u01d2\3\2\2\2")
        buf.write("g\u01d4\3\2\2\2i\u01d6\3\2\2\2k\u01d9\3\2\2\2m\u01dc\3")
        buf.write("\2\2\2o\u01df\3\2\2\2q\u01e1\3\2\2\2s\u01e4\3\2\2\2u\u01e6")
        buf.write("\3\2\2\2w\u01e9\3\2\2\2y\u01eb\3\2\2\2{\u01ee\3\2\2\2")
        buf.write("}\u01f2\3\2\2\2\177\u01f5\3\2\2\2\u0081\u01f7\3\2\2\2")
        buf.write("\u0083\u01fa\3\2\2\2\u0085\u01fd\3\2\2\2\u0087\u0206\3")
        buf.write("\2\2\2\u0089\u020e\3\2\2\2\u008b\u0214\3\2\2\2\u008d\u0222")
        buf.write("\3\2\2\2\u008f\u0225\3\2\2\2\u0091\u0231\3\2\2\2\u0093")
        buf.write("\u023d\3\2\2\2\u0095\u023f\3\2\2\2\u0097\u0245\3\2\2\2")
        buf.write("\u0099\u00a0\5\5\3\2\u009a\u00a0\5\7\4\2\u009b\u00a0\5")
        buf.write("\t\5\2\u009c\u00a0\5\13\6\2\u009d\u00a0\5\13\6\2\u009e")
        buf.write("\u00a0\5\r\7\2\u009f\u0099\3\2\2\2\u009f\u009a\3\2\2\2")
        buf.write("\u009f\u009b\3\2\2\2\u009f\u009c\3\2\2\2\u009f\u009d\3")
        buf.write("\2\2\2\u009f\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2")
        buf.write("\b\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a5\5\25\13\2\u00a4")
        buf.write("\u009f\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\4\3\2\2\2\u00a6")
        buf.write("\u00b2\7\62\2\2\u00a7\u00ae\t\2\2\2\u00a8\u00aa\7a\2\2")
        buf.write("\u00a9\u00a8\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\3")
        buf.write("\2\2\2\u00ab\u00ad\t\3\2\2\u00ac\u00a9\3\2\2\2\u00ad\u00b0")
        buf.write("\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af")
        buf.write("\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00a6\3\2\2\2")
        buf.write("\u00b1\u00a7\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\b")
        buf.write("\3\3\2\u00b4\6\3\2\2\2\u00b5\u00b6\7\62\2\2\u00b6\u00ba")
        buf.write("\7z\2\2\u00b7\u00b8\7\62\2\2\u00b8\u00ba\7Z\2\2\u00b9")
        buf.write("\u00b5\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00c6\3\2\2\2")
        buf.write("\u00bb\u00c7\7\62\2\2\u00bc\u00c3\t\4\2\2\u00bd\u00bf")
        buf.write("\7a\2\2\u00be\u00bd\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf")
        buf.write("\u00c0\3\2\2\2\u00c0\u00c2\t\5\2\2\u00c1\u00be\3\2\2\2")
        buf.write("\u00c2\u00c5\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3")
        buf.write("\2\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00bb")
        buf.write("\3\2\2\2\u00c6\u00bc\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8")
        buf.write("\u00c9\b\4\4\2\u00c9\b\3\2\2\2\u00ca\u00d6\7\62\2\2\u00cb")
        buf.write("\u00d7\7\62\2\2\u00cc\u00d3\t\6\2\2\u00cd\u00cf\7a\2\2")
        buf.write("\u00ce\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\3")
        buf.write("\2\2\2\u00d0\u00d2\t\7\2\2\u00d1\u00ce\3\2\2\2\u00d2\u00d5")
        buf.write("\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4")
        buf.write("\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00cb\3\2\2\2")
        buf.write("\u00d6\u00cc\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d9\b")
        buf.write("\5\5\2\u00d9\n\3\2\2\2\u00da\u00db\7\62\2\2\u00db\u00df")
        buf.write("\7d\2\2\u00dc\u00dd\7\62\2\2\u00dd\u00df\7D\2\2\u00de")
        buf.write("\u00da\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\u00e8\3\2\2\2")
        buf.write("\u00e0\u00e9\7\62\2\2\u00e1\u00e5\7\63\2\2\u00e2\u00e4")
        buf.write("\t\b\2\2\u00e3\u00e2\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5")
        buf.write("\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e9\3\2\2\2")
        buf.write("\u00e7\u00e5\3\2\2\2\u00e8\u00e0\3\2\2\2\u00e8\u00e1\3")
        buf.write("\2\2\2\u00e9\f\3\2\2\2\u00ea\u00eb\5\17\b\2\u00eb\u00ed")
        buf.write("\5\21\t\2\u00ec\u00ee\5\23\n\2\u00ed\u00ec\3\2\2\2\u00ed")
        buf.write("\u00ee\3\2\2\2\u00ee\u00f6\3\2\2\2\u00ef\u00f0\5\17\b")
        buf.write("\2\u00f0\u00f1\5\23\n\2\u00f1\u00f6\3\2\2\2\u00f2\u00f3")
        buf.write("\5\21\t\2\u00f3\u00f4\5\23\n\2\u00f4\u00f6\3\2\2\2\u00f5")
        buf.write("\u00ea\3\2\2\2\u00f5\u00ef\3\2\2\2\u00f5\u00f2\3\2\2\2")
        buf.write("\u00f6\u00f7\3\2\2\2\u00f7\u00f8\b\7\6\2\u00f8\16\3\2")
        buf.write("\2\2\u00f9\u0105\7\62\2\2\u00fa\u0101\t\2\2\2\u00fb\u00fd")
        buf.write("\7a\2\2\u00fc\u00fb\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd")
        buf.write("\u00fe\3\2\2\2\u00fe\u0100\t\3\2\2\u00ff\u00fc\3\2\2\2")
        buf.write("\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0102\3")
        buf.write("\2\2\2\u0102\u0105\3\2\2\2\u0103\u0101\3\2\2\2\u0104\u00f9")
        buf.write("\3\2\2\2\u0104\u00fa\3\2\2\2\u0105\20\3\2\2\2\u0106\u010a")
        buf.write("\5\177@\2\u0107\u0109\t\3\2\2\u0108\u0107\3\2\2\2\u0109")
        buf.write("\u010c\3\2\2\2\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2")
        buf.write("\u010b\22\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u010f\t\t")
        buf.write("\2\2\u010e\u0110\t\n\2\2\u010f\u010e\3\2\2\2\u010f\u0110")
        buf.write("\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0115\t\2\2\2\u0112")
        buf.write("\u0114\t\3\2\2\u0113\u0112\3\2\2\2\u0114\u0117\3\2\2\2")
        buf.write("\u0115\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116\24\3\2")
        buf.write("\2\2\u0117\u0115\3\2\2\2\u0118\u011c\7$\2\2\u0119\u011b")
        buf.write("\5\u0093J\2\u011a\u0119\3\2\2\2\u011b\u011e\3\2\2\2\u011c")
        buf.write("\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011f\3\2\2\2")
        buf.write("\u011e\u011c\3\2\2\2\u011f\u0120\7$\2\2\u0120\u0121\b")
        buf.write("\13\7\2\u0121\26\3\2\2\2\u0122\u0123\7)\2\2\u0123\u0124")
        buf.write("\7$\2\2\u0124\30\3\2\2\2\u0125\u0126\7X\2\2\u0126\u0127")
        buf.write("\7c\2\2\u0127\u0128\7n\2\2\u0128\32\3\2\2\2\u0129\u012a")
        buf.write("\7X\2\2\u012a\u012b\7c\2\2\u012b\u012c\7t\2\2\u012c\34")
        buf.write("\3\2\2\2\u012d\u012e\7&\2\2\u012e\36\3\2\2\2\u012f\u0130")
        buf.write("\7D\2\2\u0130\u0131\7t\2\2\u0131\u0132\7g\2\2\u0132\u0133")
        buf.write("\7c\2\2\u0133\u0134\7m\2\2\u0134 \3\2\2\2\u0135\u0136")
        buf.write("\7H\2\2\u0136\u0137\7q\2\2\u0137\u0138\7t\2\2\u0138\u0139")
        buf.write("\7g\2\2\u0139\u013a\7c\2\2\u013a\u013b\7e\2\2\u013b\u013c")
        buf.write("\7j\2\2\u013c\"\3\2\2\2\u013d\u013e\7K\2\2\u013e\u013f")
        buf.write("\7p\2\2\u013f\u0140\7v\2\2\u0140$\3\2\2\2\u0141\u0142")
        buf.write("\7P\2\2\u0142\u0143\7w\2\2\u0143\u0144\7n\2\2\u0144\u0145")
        buf.write("\7n\2\2\u0145&\3\2\2\2\u0146\u0147\7E\2\2\u0147\u0148")
        buf.write("\7q\2\2\u0148\u0149\7p\2\2\u0149\u014a\7u\2\2\u014a\u014b")
        buf.write("\7v\2\2\u014b\u014c\7t\2\2\u014c\u014d\7w\2\2\u014d\u014e")
        buf.write("\7e\2\2\u014e\u014f\7v\2\2\u014f\u0150\7q\2\2\u0150\u0151")
        buf.write("\7t\2\2\u0151(\3\2\2\2\u0152\u0153\7E\2\2\u0153\u0154")
        buf.write("\7q\2\2\u0154\u0155\7p\2\2\u0155\u0156\7v\2\2\u0156\u0157")
        buf.write("\7k\2\2\u0157\u0158\7p\2\2\u0158\u0159\7w\2\2\u0159\u015a")
        buf.write("\7g\2\2\u015a*\3\2\2\2\u015b\u015c\7V\2\2\u015c\u015d")
        buf.write("\7t\2\2\u015d\u015e\7w\2\2\u015e\u015f\7g\2\2\u015f,\3")
        buf.write("\2\2\2\u0160\u0161\7H\2\2\u0161\u0162\7n\2\2\u0162\u0163")
        buf.write("\7q\2\2\u0163\u0164\7c\2\2\u0164\u0165\7v\2\2\u0165.\3")
        buf.write("\2\2\2\u0166\u0167\7E\2\2\u0167\u0168\7n\2\2\u0168\u0169")
        buf.write("\7c\2\2\u0169\u016a\7u\2\2\u016a\u016b\7u\2\2\u016b\60")
        buf.write("\3\2\2\2\u016c\u016d\7F\2\2\u016d\u016e\7g\2\2\u016e\u016f")
        buf.write("\7u\2\2\u016f\u0170\7v\2\2\u0170\u0171\7t\2\2\u0171\u0172")
        buf.write("\7w\2\2\u0172\u0173\7e\2\2\u0173\u0174\7v\2\2\u0174\u0175")
        buf.write("\7q\2\2\u0175\u0176\7t\2\2\u0176\62\3\2\2\2\u0177\u0178")
        buf.write("\7K\2\2\u0178\u0179\7h\2\2\u0179\64\3\2\2\2\u017a\u017b")
        buf.write("\7H\2\2\u017b\u017c\7c\2\2\u017c\u017d\7n\2\2\u017d\u017e")
        buf.write("\7u\2\2\u017e\u017f\7g\2\2\u017f\66\3\2\2\2\u0180\u0181")
        buf.write("\7D\2\2\u0181\u0182\7q\2\2\u0182\u0183\7q\2\2\u0183\u0184")
        buf.write("\7n\2\2\u0184\u0185\7g\2\2\u0185\u0186\7c\2\2\u0186\u0187")
        buf.write("\7p\2\2\u01878\3\2\2\2\u0188\u0189\7P\2\2\u0189\u018a")
        buf.write("\7g\2\2\u018a\u018b\7y\2\2\u018b:\3\2\2\2\u018c\u018d")
        buf.write("\7G\2\2\u018d\u018e\7n\2\2\u018e\u018f\7u\2\2\u018f\u0190")
        buf.write("\7g\2\2\u0190\u0191\7k\2\2\u0191\u0192\7h\2\2\u0192<\3")
        buf.write("\2\2\2\u0193\u0194\7C\2\2\u0194\u0195\7t\2\2\u0195\u0196")
        buf.write("\7t\2\2\u0196\u0197\7c\2\2\u0197\u0198\7{\2\2\u0198>\3")
        buf.write("\2\2\2\u0199\u019a\7U\2\2\u019a\u019b\7v\2\2\u019b\u019c")
        buf.write("\7t\2\2\u019c\u019d\7k\2\2\u019d\u019e\7p\2\2\u019e\u019f")
        buf.write("\7i\2\2\u019f@\3\2\2\2\u01a0\u01a1\7D\2\2\u01a1\u01a2")
        buf.write("\7{\2\2\u01a2B\3\2\2\2\u01a3\u01a4\7G\2\2\u01a4\u01a5")
        buf.write("\7n\2\2\u01a5\u01a6\7u\2\2\u01a6\u01a7\7g\2\2\u01a7D\3")
        buf.write("\2\2\2\u01a8\u01a9\7K\2\2\u01a9\u01aa\7p\2\2\u01aaF\3")
        buf.write("\2\2\2\u01ab\u01ac\7T\2\2\u01ac\u01ad\7g\2\2\u01ad\u01ae")
        buf.write("\7v\2\2\u01ae\u01af\7w\2\2\u01af\u01b0\7t\2\2\u01b0\u01b1")
        buf.write("\7p\2\2\u01b1H\3\2\2\2\u01b2\u01b3\7U\2\2\u01b3\u01b4")
        buf.write("\7g\2\2\u01b4\u01b5\7n\2\2\u01b5\u01b6\7h\2\2\u01b6J\3")
        buf.write("\2\2\2\u01b7\u01b8\7*\2\2\u01b8L\3\2\2\2\u01b9\u01ba\7")
        buf.write("+\2\2\u01baN\3\2\2\2\u01bb\u01bc\7]\2\2\u01bcP\3\2\2\2")
        buf.write("\u01bd\u01be\7_\2\2\u01beR\3\2\2\2\u01bf\u01c0\7}\2\2")
        buf.write("\u01c0T\3\2\2\2\u01c1\u01c2\7\177\2\2\u01c2V\3\2\2\2\u01c3")
        buf.write("\u01c4\7=\2\2\u01c4X\3\2\2\2\u01c5\u01c6\7.\2\2\u01c6")
        buf.write("Z\3\2\2\2\u01c7\u01c8\7\60\2\2\u01c8\u01c9\7\60\2\2\u01c9")
        buf.write("\\\3\2\2\2\u01ca\u01cb\7-\2\2\u01cb^\3\2\2\2\u01cc\u01cd")
        buf.write("\7/\2\2\u01cd`\3\2\2\2\u01ce\u01cf\7,\2\2\u01cfb\3\2\2")
        buf.write("\2\u01d0\u01d1\7\61\2\2\u01d1d\3\2\2\2\u01d2\u01d3\7\'")
        buf.write("\2\2\u01d3f\3\2\2\2\u01d4\u01d5\7#\2\2\u01d5h\3\2\2\2")
        buf.write("\u01d6\u01d7\7(\2\2\u01d7\u01d8\7(\2\2\u01d8j\3\2\2\2")
        buf.write("\u01d9\u01da\7~\2\2\u01da\u01db\7~\2\2\u01dbl\3\2\2\2")
        buf.write("\u01dc\u01dd\7?\2\2\u01dd\u01de\7?\2\2\u01den\3\2\2\2")
        buf.write("\u01df\u01e0\7?\2\2\u01e0p\3\2\2\2\u01e1\u01e2\7#\2\2")
        buf.write("\u01e2\u01e3\7?\2\2\u01e3r\3\2\2\2\u01e4\u01e5\7>\2\2")
        buf.write("\u01e5t\3\2\2\2\u01e6\u01e7\7>\2\2\u01e7\u01e8\7?\2\2")
        buf.write("\u01e8v\3\2\2\2\u01e9\u01ea\7@\2\2\u01eax\3\2\2\2\u01eb")
        buf.write("\u01ec\7@\2\2\u01ec\u01ed\7?\2\2\u01edz\3\2\2\2\u01ee")
        buf.write("\u01ef\7?\2\2\u01ef\u01f0\7?\2\2\u01f0\u01f1\7\60\2\2")
        buf.write("\u01f1|\3\2\2\2\u01f2\u01f3\7-\2\2\u01f3\u01f4\7\60\2")
        buf.write("\2\u01f4~\3\2\2\2\u01f5\u01f6\7\60\2\2\u01f6\u0080\3\2")
        buf.write("\2\2\u01f7\u01f8\7<\2\2\u01f8\u01f9\7<\2\2\u01f9\u0082")
        buf.write("\3\2\2\2\u01fa\u01fb\7<\2\2\u01fb\u0084\3\2\2\2\u01fc")
        buf.write("\u01fe\5\35\17\2\u01fd\u01fc\3\2\2\2\u01fd\u01fe\3\2\2")
        buf.write("\2\u01fe\u01ff\3\2\2\2\u01ff\u0203\t\13\2\2\u0200\u0202")
        buf.write("\t\f\2\2\u0201\u0200\3\2\2\2\u0202\u0205\3\2\2\2\u0203")
        buf.write("\u0201\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0086\3\2\2\2")
        buf.write("\u0205\u0203\3\2\2\2\u0206\u020a\t\3\2\2\u0207\u0209\t")
        buf.write("\2\2\2\u0208\u0207\3\2\2\2\u0209\u020c\3\2\2\2\u020a\u0208")
        buf.write("\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u0088\3\2\2\2\u020c")
        buf.write("\u020a\3\2\2\2\u020d\u020f\t\r\2\2\u020e\u020d\3\2\2\2")
        buf.write("\u020f\u0210\3\2\2\2\u0210\u020e\3\2\2\2\u0210\u0211\3")
        buf.write("\2\2\2\u0211\u0212\3\2\2\2\u0212\u0213\bE\b\2\u0213\u008a")
        buf.write("\3\2\2\2\u0214\u0215\7%\2\2\u0215\u0216\7%\2\2\u0216\u021a")
        buf.write("\3\2\2\2\u0217\u0219\13\2\2\2\u0218\u0217\3\2\2\2\u0219")
        buf.write("\u021c\3\2\2\2\u021a\u021b\3\2\2\2\u021a\u0218\3\2\2\2")
        buf.write("\u021b\u021d\3\2\2\2\u021c\u021a\3\2\2\2\u021d\u021e\7")
        buf.write("%\2\2\u021e\u021f\7%\2\2\u021f\u0220\3\2\2\2\u0220\u0221")
        buf.write("\bF\b\2\u0221\u008c\3\2\2\2\u0222\u0223\13\2\2\2\u0223")
        buf.write("\u0224\bG\t\2\u0224\u008e\3\2\2\2\u0225\u0229\7$\2\2\u0226")
        buf.write("\u0228\5\u0093J\2\u0227\u0226\3\2\2\2\u0228\u022b\3\2")
        buf.write("\2\2\u0229\u0227\3\2\2\2\u0229\u022a\3\2\2\2\u022a\u022d")
        buf.write("\3\2\2\2\u022b\u0229\3\2\2\2\u022c\u022e\t\16\2\2\u022d")
        buf.write("\u022c\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u0230\bH\n\2")
        buf.write("\u0230\u0090\3\2\2\2\u0231\u0235\7$\2\2\u0232\u0234\5")
        buf.write("\u0093J\2\u0233\u0232\3\2\2\2\u0234\u0237\3\2\2\2\u0235")
        buf.write("\u0233\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0238\3\2\2\2")
        buf.write("\u0237\u0235\3\2\2\2\u0238\u0239\5\u0097L\2\u0239\u023a")
        buf.write("\bI\13\2\u023a\u0092\3\2\2\2\u023b\u023e\n\17\2\2\u023c")
        buf.write("\u023e\5\u0095K\2\u023d\u023b\3\2\2\2\u023d\u023c\3\2")
        buf.write("\2\2\u023e\u0094\3\2\2\2\u023f\u0240\7^\2\2\u0240\u0241")
        buf.write("\t\20\2\2\u0241\u0096\3\2\2\2\u0242\u0243\7^\2\2\u0243")
        buf.write("\u0246\n\20\2\2\u0244\u0246\n\21\2\2\u0245\u0242\3\2\2")
        buf.write("\2\u0245\u0244\3\2\2\2\u0246\u0098\3\2\2\2%\2\u009f\u00a4")
        buf.write("\u00a9\u00ae\u00b1\u00b9\u00be\u00c3\u00c6\u00ce\u00d3")
        buf.write("\u00d6\u00de\u00e5\u00e8\u00ed\u00f5\u00fc\u0101\u0104")
        buf.write("\u010a\u010f\u0115\u011c\u01fd\u0203\u020a\u0210\u021a")
        buf.write("\u0229\u022d\u0235\u023d\u0245\f\3\2\2\3\3\3\3\4\4\3\5")
        buf.write("\5\3\7\6\3\13\7\b\2\2\3G\b\3H\t\3I\n")
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
    DOUBLE_SEMI = 61
    COLON = 62
    ID = 63
    WS = 64
    BLOCK_COMMENT = 65
    ERROR_CHAR = 66
    UNCLOSE_STRING = 67
    ILLEGAL_ESCAPE = 68

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
            "LITERAL", "LITERAL_INT_DEC", "LITERAL_INT_HEX", "LITERAL_INT_OCT", 
            "LITERAL_INT_BIN", "LITERAL_FLOAT", "LITERAL_STRING", "DOUBLE_QUOTE", 
            "VAL", "VAR", "STATIC", "BREAK", "FOREACH", "INT", "NULL", "CONSTRUCTOR", 
            "CONTINUE", "TRUE", "FLOAT", "CLASS", "DESTRUCTOR", "IF", "FALSE", 
            "BOOLEAN", "NEW", "ELSEIF", "ARRAY", "STRING", "BY", "ELSE", 
            "IN", "RETURN", "SELF", "LB", "RB", "LS", "RS", "LP", "RP", 
            "SEMI", "COMMA", "DOTDOT", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", 
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
                  "BY", "ELSE", "IN", "RETURN", "SELF", "LB", "RB", "LS", 
                  "RS", "LP", "RP", "SEMI", "COMMA", "DOTDOT", "ADD", "SUBTRACT", 
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
            actions[69] = self.ERROR_CHAR_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
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
            	
     


