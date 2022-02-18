# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3I")
        buf.write("\u02fe\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\6\2\u0094\n\2\r\2")
        buf.write("\16\2\u0095\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u009e\n\3\3\3")
        buf.write("\3\3\7\3\u00a2\n\3\f\3\16\3\u00a5\13\3\3\3\3\3\3\4\3\4")
        buf.write("\5\4\u00ab\n\4\3\5\3\5\3\5\3\5\5\5\u00b1\n\5\3\6\3\6\3")
        buf.write("\6\3\6\7\6\u00b7\n\6\f\6\16\6\u00ba\13\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\5\b\u00d0\n\b\3\t\3\t\3\t\3\t\7\t\u00d6\n")
        buf.write("\t\f\t\16\t\u00d9\13\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\5\13\u00ef\n\13\3\f\3\f\3\f\3\f\5\f\u00f5\n\f\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16\5\16\u0100\n\16")
        buf.write("\3\17\3\17\3\17\5\17\u0105\n\17\3\17\3\17\3\17\5\17\u010a")
        buf.write("\n\17\3\17\3\17\3\20\3\20\3\20\5\20\u0111\n\20\3\20\3")
        buf.write("\20\3\20\5\20\u0116\n\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\5\21\u011f\n\21\3\21\3\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\5\22\u012d\n\22\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u0133\n\23\3\24\3\24\3\24\3\24\7\24\u0139")
        buf.write("\n\24\f\24\16\24\u013c\13\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\5\26\u0152\n\26\3\27\3\27\3\27\3")
        buf.write("\27\7\27\u0158\n\27\f\27\16\27\u015b\13\27\3\27\3\27\3")
        buf.write("\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0171\n\31\3")
        buf.write("\32\3\32\3\32\3\32\5\32\u0177\n\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\5\33\u017f\n\33\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\35\3\35\5\35\u0188\n\35\3\36\3\36\3\36\7\36\u018d\n\36")
        buf.write("\f\36\16\36\u0190\13\36\3\37\3\37\3\37\7\37\u0195\n\37")
        buf.write("\f\37\16\37\u0198\13\37\3\37\3\37\3\37\5\37\u019d\n\37")
        buf.write("\3 \3 \3!\3!\3!\3!\3!\3!\5!\u01a7\n!\3!\3!\5!\u01ab\n")
        buf.write("!\3!\5!\u01ae\n!\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u01b6\n\"")
        buf.write("\3\"\3\"\5\"\u01ba\n\"\3#\3#\3#\5#\u01bf\n#\3#\3#\3$\3")
        buf.write("$\3$\3$\3$\3$\5$\u01c9\n$\3$\3$\3%\3%\3%\3%\3%\3%\3%\5")
        buf.write("%\u01d4\n%\3&\3&\3\'\3\'\3\'\3\'\5\'\u01dc\n\'\3\'\3\'")
        buf.write("\3\'\3\'\5\'\u01e2\n\'\7\'\u01e4\n\'\f\'\16\'\u01e7\13")
        buf.write("\'\3(\3(\3(\3)\3)\3)\3*\3*\7*\u01f1\n*\f*\16*\u01f4\13")
        buf.write("*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\5-\u0204\n")
        buf.write("-\3-\3-\3.\6.\u0209\n.\r.\16.\u020a\3/\3/\3/\3/\3/\3/")
        buf.write("\5/\u0213\n/\3/\3/\3/\3/\5/\u0219\n/\3/\3/\7/\u021d\n")
        buf.write("/\f/\16/\u0220\13/\3\60\3\60\3\60\7\60\u0225\n\60\f\60")
        buf.write("\16\60\u0228\13\60\3\60\3\60\3\61\3\61\3\61\5\61\u022f")
        buf.write("\n\61\3\61\3\61\3\62\3\62\5\62\u0235\n\62\3\63\3\63\3")
        buf.write("\63\3\63\3\63\5\63\u023c\n\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\5\64\u0243\n\64\3\65\3\65\3\65\3\65\3\65\3\65\7\65\u024b")
        buf.write("\n\65\f\65\16\65\u024e\13\65\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\7\66\u0256\n\66\f\66\16\66\u0259\13\66\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\7\67\u0261\n\67\f\67\16\67\u0264")
        buf.write("\13\67\38\38\38\58\u0269\n8\39\39\39\59\u026e\n9\3:\3")
        buf.write(":\3:\3:\3:\3:\5:\u0276\n:\3:\3:\3:\3:\3:\7:\u027d\n:\f")
        buf.write(":\16:\u0280\13:\3;\3;\3;\3;\3;\3;\3;\5;\u0289\n;\7;\u028b")
        buf.write("\n;\f;\16;\u028e\13;\3<\3<\3<\3<\5<\u0294\n<\3<\5<\u0297")
        buf.write("\n<\3=\3=\3=\3=\5=\u029d\n=\3=\3=\3=\5=\u02a2\n=\3>\3")
        buf.write(">\3>\3>\3>\3>\3>\3>\3>\5>\u02ad\n>\3?\3?\3@\3@\3@\3@\3")
        buf.write("@\3@\3@\3@\3@\3@\7@\u02bb\n@\f@\16@\u02be\13@\3A\3A\3")
        buf.write("A\3A\5A\u02c4\nA\3B\3B\3B\5B\u02c9\nB\3B\3B\3C\3C\3C\3")
        buf.write("C\5C\u02d1\nC\3C\3C\3D\3D\3D\7D\u02d8\nD\fD\16D\u02db")
        buf.write("\13D\3E\3E\3F\3F\5F\u02e1\nF\3G\3G\3G\5G\u02e6\nG\3G\3")
        buf.write("G\3H\3H\3H\3H\3H\7H\u02ef\nH\fH\16H\u02f2\13H\3H\3H\3")
        buf.write("I\3I\3I\7I\u02f9\nI\fI\16I\u02fc\13I\3I\2\nL\\hjlrt~J")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\u0086\u0088\u008a\u008c\u008e\u0090\2\f\3\2\r\16")
        buf.write("\3\2CD\b\2\22\22\27\27\34\34  %%CC\4\2%%CC\3\2>?\4\2\67")
        buf.write("\679=\3\2\65\66\3\2/\60\3\2\61\63\4\2\3\5\n\13\2\u0313")
        buf.write("\2\u0093\3\2\2\2\4\u0099\3\2\2\2\6\u00aa\3\2\2\2\b\u00b0")
        buf.write("\3\2\2\2\n\u00b2\3\2\2\2\f\u00bf\3\2\2\2\16\u00cf\3\2")
        buf.write("\2\2\20\u00d1\3\2\2\2\22\u00de\3\2\2\2\24\u00ee\3\2\2")
        buf.write("\2\26\u00f0\3\2\2\2\30\u00fa\3\2\2\2\32\u00ff\3\2\2\2")
        buf.write("\34\u0101\3\2\2\2\36\u010d\3\2\2\2 \u0119\3\2\2\2\"\u012c")
        buf.write("\3\2\2\2$\u0132\3\2\2\2&\u0134\3\2\2\2(\u0141\3\2\2\2")
        buf.write("*\u0151\3\2\2\2,\u0153\3\2\2\2.\u0160\3\2\2\2\60\u0170")
        buf.write("\3\2\2\2\62\u0172\3\2\2\2\64\u017e\3\2\2\2\66\u0180\3")
        buf.write("\2\2\28\u0185\3\2\2\2:\u0189\3\2\2\2<\u0191\3\2\2\2>\u019e")
        buf.write("\3\2\2\2@\u01a0\3\2\2\2B\u01af\3\2\2\2D\u01bb\3\2\2\2")
        buf.write("F\u01c2\3\2\2\2H\u01cc\3\2\2\2J\u01d5\3\2\2\2L\u01db\3")
        buf.write("\2\2\2N\u01e8\3\2\2\2P\u01eb\3\2\2\2R\u01ee\3\2\2\2T\u01f7")
        buf.write("\3\2\2\2V\u01fc\3\2\2\2X\u0201\3\2\2\2Z\u0208\3\2\2\2")
        buf.write("\\\u0212\3\2\2\2^\u0226\3\2\2\2`\u022b\3\2\2\2b\u0234")
        buf.write("\3\2\2\2d\u023b\3\2\2\2f\u0242\3\2\2\2h\u0244\3\2\2\2")
        buf.write("j\u024f\3\2\2\2l\u025a\3\2\2\2n\u0268\3\2\2\2p\u026d\3")
        buf.write("\2\2\2r\u0275\3\2\2\2t\u0281\3\2\2\2v\u0296\3\2\2\2x\u02a1")
        buf.write("\3\2\2\2z\u02ac\3\2\2\2|\u02ae\3\2\2\2~\u02b0\3\2\2\2")
        buf.write("\u0080\u02bf\3\2\2\2\u0082\u02c5\3\2\2\2\u0084\u02cc\3")
        buf.write("\2\2\2\u0086\u02d4\3\2\2\2\u0088\u02dc\3\2\2\2\u008a\u02e0")
        buf.write("\3\2\2\2\u008c\u02e2\3\2\2\2\u008e\u02e9\3\2\2\2\u0090")
        buf.write("\u02f5\3\2\2\2\u0092\u0094\5\4\3\2\u0093\u0092\3\2\2\2")
        buf.write("\u0094\u0095\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3")
        buf.write("\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098\7\2\2\3\u0098\3")
        buf.write("\3\2\2\2\u0099\u009a\7\30\2\2\u009a\u009d\7C\2\2\u009b")
        buf.write("\u009c\7B\2\2\u009c\u009e\7C\2\2\u009d\u009b\3\2\2\2\u009d")
        buf.write("\u009e\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a3\7*\2\2")
        buf.write("\u00a0\u00a2\5\6\4\2\u00a1\u00a0\3\2\2\2\u00a2\u00a5\3")
        buf.write("\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a6")
        buf.write("\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a7\7+\2\2\u00a7")
        buf.write("\5\3\2\2\2\u00a8\u00ab\5\b\5\2\u00a9\u00ab\5\32\16\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\7\3\2\2\2\u00ac")
        buf.write("\u00b1\5\n\6\2\u00ad\u00b1\5\f\7\2\u00ae\u00b1\5\20\t")
        buf.write("\2\u00af\u00b1\5\22\n\2\u00b0\u00ac\3\2\2\2\u00b0\u00ad")
        buf.write("\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00af\3\2\2\2\u00b1")
        buf.write("\t\3\2\2\2\u00b2\u00b3\t\2\2\2\u00b3\u00b8\5\30\r\2\u00b4")
        buf.write("\u00b5\7-\2\2\u00b5\u00b7\5\30\r\2\u00b6\u00b4\3\2\2\2")
        buf.write("\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9\3")
        buf.write("\2\2\2\u00b9\u00bb\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb\u00bc")
        buf.write("\7B\2\2\u00bc\u00bd\5> \2\u00bd\u00be\7,\2\2\u00be\13")
        buf.write("\3\2\2\2\u00bf\u00c0\t\2\2\2\u00c0\u00c1\5\30\r\2\u00c1")
        buf.write("\u00c2\5\16\b\2\u00c2\u00c3\5b\62\2\u00c3\u00c4\7,\2\2")
        buf.write("\u00c4\r\3\2\2\2\u00c5\u00c6\7-\2\2\u00c6\u00c7\5\30\r")
        buf.write("\2\u00c7\u00c8\5\16\b\2\u00c8\u00c9\5b\62\2\u00c9\u00ca")
        buf.write("\7-\2\2\u00ca\u00d0\3\2\2\2\u00cb\u00cc\7B\2\2\u00cc\u00cd")
        buf.write("\5> \2\u00cd\u00ce\78\2\2\u00ce\u00d0\3\2\2\2\u00cf\u00c5")
        buf.write("\3\2\2\2\u00cf\u00cb\3\2\2\2\u00d0\17\3\2\2\2\u00d1\u00d2")
        buf.write("\t\2\2\2\u00d2\u00d7\5\30\r\2\u00d3\u00d4\7-\2\2\u00d4")
        buf.write("\u00d6\5\30\r\2\u00d5\u00d3\3\2\2\2\u00d6\u00d9\3\2\2")
        buf.write("\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00da")
        buf.write("\3\2\2\2\u00d9\u00d7\3\2\2\2\u00da\u00db\7B\2\2\u00db")
        buf.write("\u00dc\5\26\f\2\u00dc\u00dd\7,\2\2\u00dd\21\3\2\2\2\u00de")
        buf.write("\u00df\t\2\2\2\u00df\u00e0\5\30\r\2\u00e0\u00e1\5\24\13")
        buf.write("\2\u00e1\u00e2\5\64\33\2\u00e2\u00e3\7,\2\2\u00e3\23\3")
        buf.write("\2\2\2\u00e4\u00e5\7-\2\2\u00e5\u00e6\5\30\r\2\u00e6\u00e7")
        buf.write("\5\24\13\2\u00e7\u00e8\5\64\33\2\u00e8\u00e9\7-\2\2\u00e9")
        buf.write("\u00ef\3\2\2\2\u00ea\u00eb\7B\2\2\u00eb\u00ec\5\26\f\2")
        buf.write("\u00ec\u00ed\78\2\2\u00ed\u00ef\3\2\2\2\u00ee\u00e4\3")
        buf.write("\2\2\2\u00ee\u00ea\3\2\2\2\u00ef\25\3\2\2\2\u00f0\u00f1")
        buf.write("\7\37\2\2\u00f1\u00f4\7(\2\2\u00f2\u00f5\5> \2\u00f3\u00f5")
        buf.write("\5\26\f\2\u00f4\u00f2\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5")
        buf.write("\u00f6\3\2\2\2\u00f6\u00f7\7-\2\2\u00f7\u00f8\7\4\2\2")
        buf.write("\u00f8\u00f9\7)\2\2\u00f9\27\3\2\2\2\u00fa\u00fb\t\3\2")
        buf.write("\2\u00fb\31\3\2\2\2\u00fc\u0100\5\34\17\2\u00fd\u0100")
        buf.write("\5\36\20\2\u00fe\u0100\5 \21\2\u00ff\u00fc\3\2\2\2\u00ff")
        buf.write("\u00fd\3\2\2\2\u00ff\u00fe\3\2\2\2\u0100\33\3\2\2\2\u0101")
        buf.write("\u0102\5\30\r\2\u0102\u0104\7&\2\2\u0103\u0105\5:\36\2")
        buf.write("\u0104\u0103\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0106\3")
        buf.write("\2\2\2\u0106\u0107\7\'\2\2\u0107\u0109\7*\2\2\u0108\u010a")
        buf.write("\5Z.\2\u0109\u0108\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010b")
        buf.write("\3\2\2\2\u010b\u010c\7+\2\2\u010c\35\3\2\2\2\u010d\u010e")
        buf.write("\7\24\2\2\u010e\u0110\7&\2\2\u010f\u0111\5:\36\2\u0110")
        buf.write("\u010f\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0112\3\2\2\2")
        buf.write("\u0112\u0113\7\'\2\2\u0113\u0115\7*\2\2\u0114\u0116\5")
        buf.write("Z.\2\u0115\u0114\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0117")
        buf.write("\3\2\2\2\u0117\u0118\7+\2\2\u0118\37\3\2\2\2\u0119\u011a")
        buf.write("\7\31\2\2\u011a\u011b\7&\2\2\u011b\u011c\7\'\2\2\u011c")
        buf.write("\u011e\7*\2\2\u011d\u011f\5Z.\2\u011e\u011d\3\2\2\2\u011e")
        buf.write("\u011f\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0121\7+\2\2")
        buf.write("\u0121!\3\2\2\2\u0122\u012d\5$\23\2\u0123\u012d\5\66\34")
        buf.write("\2\u0124\u012d\5@!\2\u0125\u012d\5F$\2\u0126\u012d\5N")
        buf.write("(\2\u0127\u012d\5P)\2\u0128\u012d\5R*\2\u0129\u012d\5")
        buf.write("T+\2\u012a\u012d\5V,\2\u012b\u012d\5X-\2\u012c\u0122\3")
        buf.write("\2\2\2\u012c\u0123\3\2\2\2\u012c\u0124\3\2\2\2\u012c\u0125")
        buf.write("\3\2\2\2\u012c\u0126\3\2\2\2\u012c\u0127\3\2\2\2\u012c")
        buf.write("\u0128\3\2\2\2\u012c\u0129\3\2\2\2\u012c\u012a\3\2\2\2")
        buf.write("\u012c\u012b\3\2\2\2\u012d#\3\2\2\2\u012e\u0133\5&\24")
        buf.write("\2\u012f\u0133\5(\25\2\u0130\u0133\5,\27\2\u0131\u0133")
        buf.write("\5.\30\2\u0132\u012e\3\2\2\2\u0132\u012f\3\2\2\2\u0132")
        buf.write("\u0130\3\2\2\2\u0132\u0131\3\2\2\2\u0133%\3\2\2\2\u0134")
        buf.write("\u0135\t\2\2\2\u0135\u013a\7C\2\2\u0136\u0137\7-\2\2\u0137")
        buf.write("\u0139\7C\2\2\u0138\u0136\3\2\2\2\u0139\u013c\3\2\2\2")
        buf.write("\u013a\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013d\3")
        buf.write("\2\2\2\u013c\u013a\3\2\2\2\u013d\u013e\7B\2\2\u013e\u013f")
        buf.write("\5> \2\u013f\u0140\7,\2\2\u0140\'\3\2\2\2\u0141\u0142")
        buf.write("\t\2\2\2\u0142\u0143\7C\2\2\u0143\u0144\5*\26\2\u0144")
        buf.write("\u0145\5b\62\2\u0145\u0146\7,\2\2\u0146)\3\2\2\2\u0147")
        buf.write("\u0148\7-\2\2\u0148\u0149\7C\2\2\u0149\u014a\5*\26\2\u014a")
        buf.write("\u014b\5b\62\2\u014b\u014c\7-\2\2\u014c\u0152\3\2\2\2")
        buf.write("\u014d\u014e\7B\2\2\u014e\u014f\5> \2\u014f\u0150\78\2")
        buf.write("\2\u0150\u0152\3\2\2\2\u0151\u0147\3\2\2\2\u0151\u014d")
        buf.write("\3\2\2\2\u0152+\3\2\2\2\u0153\u0154\t\2\2\2\u0154\u0159")
        buf.write("\7C\2\2\u0155\u0156\7-\2\2\u0156\u0158\7C\2\2\u0157\u0155")
        buf.write("\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157\3\2\2\2\u0159")
        buf.write("\u015a\3\2\2\2\u015a\u015c\3\2\2\2\u015b\u0159\3\2\2\2")
        buf.write("\u015c\u015d\7B\2\2\u015d\u015e\5\62\32\2\u015e\u015f")
        buf.write("\7,\2\2\u015f-\3\2\2\2\u0160\u0161\t\2\2\2\u0161\u0162")
        buf.write("\7C\2\2\u0162\u0163\5\60\31\2\u0163\u0164\5\64\33\2\u0164")
        buf.write("\u0165\7,\2\2\u0165/\3\2\2\2\u0166\u0167\7-\2\2\u0167")
        buf.write("\u0168\7C\2\2\u0168\u0169\5\60\31\2\u0169\u016a\5\64\33")
        buf.write("\2\u016a\u016b\7-\2\2\u016b\u0171\3\2\2\2\u016c\u016d")
        buf.write("\7B\2\2\u016d\u016e\5\62\32\2\u016e\u016f\78\2\2\u016f")
        buf.write("\u0171\3\2\2\2\u0170\u0166\3\2\2\2\u0170\u016c\3\2\2\2")
        buf.write("\u0171\61\3\2\2\2\u0172\u0173\7\37\2\2\u0173\u0176\7(")
        buf.write("\2\2\u0174\u0177\5> \2\u0175\u0177\5\62\32\2\u0176\u0174")
        buf.write("\3\2\2\2\u0176\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178")
        buf.write("\u0179\7-\2\2\u0179\u017a\7\4\2\2\u017a\u017b\7)\2\2\u017b")
        buf.write("\63\3\2\2\2\u017c\u017f\5\u008aF\2\u017d\u017f\5\u0084")
        buf.write("C\2\u017e\u017c\3\2\2\2\u017e\u017d\3\2\2\2\u017f\65\3")
        buf.write("\2\2\2\u0180\u0181\58\35\2\u0181\u0182\78\2\2\u0182\u0183")
        buf.write("\5b\62\2\u0183\u0184\7,\2\2\u0184\67\3\2\2\2\u0185\u0187")
        buf.write("\5L\'\2\u0186\u0188\5|?\2\u0187\u0186\3\2\2\2\u0187\u0188")
        buf.write("\3\2\2\2\u01889\3\2\2\2\u0189\u018e\5<\37\2\u018a\u018b")
        buf.write("\7,\2\2\u018b\u018d\5<\37\2\u018c\u018a\3\2\2\2\u018d")
        buf.write("\u0190\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2")
        buf.write("\u018f;\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0196\7C\2\2")
        buf.write("\u0192\u0193\7-\2\2\u0193\u0195\7C\2\2\u0194\u0192\3\2")
        buf.write("\2\2\u0195\u0198\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197")
        buf.write("\3\2\2\2\u0197\u0199\3\2\2\2\u0198\u0196\3\2\2\2\u0199")
        buf.write("\u019c\7B\2\2\u019a\u019d\5> \2\u019b\u019d\5\62\32\2")
        buf.write("\u019c\u019a\3\2\2\2\u019c\u019b\3\2\2\2\u019d=\3\2\2")
        buf.write("\2\u019e\u019f\t\4\2\2\u019f?\3\2\2\2\u01a0\u01a1\7\32")
        buf.write("\2\2\u01a1\u01a2\7&\2\2\u01a2\u01a3\5b\62\2\u01a3\u01a4")
        buf.write("\7\'\2\2\u01a4\u01a6\7*\2\2\u01a5\u01a7\5Z.\2\u01a6\u01a5")
        buf.write("\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8")
        buf.write("\u01aa\7+\2\2\u01a9\u01ab\5B\"\2\u01aa\u01a9\3\2\2\2\u01aa")
        buf.write("\u01ab\3\2\2\2\u01ab\u01ad\3\2\2\2\u01ac\u01ae\5D#\2\u01ad")
        buf.write("\u01ac\3\2\2\2\u01ad\u01ae\3\2\2\2\u01aeA\3\2\2\2\u01af")
        buf.write("\u01b0\7\36\2\2\u01b0\u01b1\7&\2\2\u01b1\u01b2\5b\62\2")
        buf.write("\u01b2\u01b3\7\'\2\2\u01b3\u01b5\7*\2\2\u01b4\u01b6\5")
        buf.write("Z.\2\u01b5\u01b4\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b7")
        buf.write("\3\2\2\2\u01b7\u01b9\7+\2\2\u01b8\u01ba\5B\"\2\u01b9\u01b8")
        buf.write("\3\2\2\2\u01b9\u01ba\3\2\2\2\u01baC\3\2\2\2\u01bb\u01bc")
        buf.write("\7\"\2\2\u01bc\u01be\7*\2\2\u01bd\u01bf\5Z.\2\u01be\u01bd")
        buf.write("\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0")
        buf.write("\u01c1\7+\2\2\u01c1E\3\2\2\2\u01c2\u01c3\7\21\2\2\u01c3")
        buf.write("\u01c4\7&\2\2\u01c4\u01c5\5H%\2\u01c5\u01c6\7\'\2\2\u01c6")
        buf.write("\u01c8\7*\2\2\u01c7\u01c9\5Z.\2\u01c8\u01c7\3\2\2\2\u01c8")
        buf.write("\u01c9\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb\7+\2\2")
        buf.write("\u01cbG\3\2\2\2\u01cc\u01cd\5L\'\2\u01cd\u01ce\7#\2\2")
        buf.write("\u01ce\u01cf\5J&\2\u01cf\u01d0\7.\2\2\u01d0\u01d3\5J&")
        buf.write("\2\u01d1\u01d2\7!\2\2\u01d2\u01d4\5J&\2\u01d3\u01d1\3")
        buf.write("\2\2\2\u01d3\u01d4\3\2\2\2\u01d4I\3\2\2\2\u01d5\u01d6")
        buf.write("\5b\62\2\u01d6K\3\2\2\2\u01d7\u01d8\b\'\1\2\u01d8\u01dc")
        buf.write("\5\u0080A\2\u01d9\u01dc\7%\2\2\u01da\u01dc\7C\2\2\u01db")
        buf.write("\u01d7\3\2\2\2\u01db\u01d9\3\2\2\2\u01db\u01da\3\2\2\2")
        buf.write("\u01dc\u01e5\3\2\2\2\u01dd\u01de\f\6\2\2\u01de\u01e1\7")
        buf.write("@\2\2\u01df\u01e2\7C\2\2\u01e0\u01e2\5`\61\2\u01e1\u01df")
        buf.write("\3\2\2\2\u01e1\u01e0\3\2\2\2\u01e2\u01e4\3\2\2\2\u01e3")
        buf.write("\u01dd\3\2\2\2\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2")
        buf.write("\u01e5\u01e6\3\2\2\2\u01e6M\3\2\2\2\u01e7\u01e5\3\2\2")
        buf.write("\2\u01e8\u01e9\7\20\2\2\u01e9\u01ea\7,\2\2\u01eaO\3\2")
        buf.write("\2\2\u01eb\u01ec\7\25\2\2\u01ec\u01ed\7,\2\2\u01edQ\3")
        buf.write("\2\2\2\u01ee\u01f2\7$\2\2\u01ef\u01f1\5b\62\2\u01f0\u01ef")
        buf.write("\3\2\2\2\u01f1\u01f4\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2")
        buf.write("\u01f3\3\2\2\2\u01f3\u01f5\3\2\2\2\u01f4\u01f2\3\2\2\2")
        buf.write("\u01f5\u01f6\7,\2\2\u01f6S\3\2\2\2\u01f7\u01f8\5\\/\2")
        buf.write("\u01f8\u01f9\7@\2\2\u01f9\u01fa\5`\61\2\u01fa\u01fb\7")
        buf.write(",\2\2\u01fbU\3\2\2\2\u01fc\u01fd\t\5\2\2\u01fd\u01fe\7")
        buf.write("A\2\2\u01fe\u01ff\5\u0082B\2\u01ff\u0200\7,\2\2\u0200")
        buf.write("W\3\2\2\2\u0201\u0203\7*\2\2\u0202\u0204\5Z.\2\u0203\u0202")
        buf.write("\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0205\3\2\2\2\u0205")
        buf.write("\u0206\7+\2\2\u0206Y\3\2\2\2\u0207\u0209\5\"\22\2\u0208")
        buf.write("\u0207\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u0208\3\2\2\2")
        buf.write("\u020a\u020b\3\2\2\2\u020b[\3\2\2\2\u020c\u020d\b/\1\2")
        buf.write("\u020d\u020e\7\35\2\2\u020e\u0213\5`\61\2\u020f\u0213")
        buf.write("\5\u0080A\2\u0210\u0213\7%\2\2\u0211\u0213\7C\2\2\u0212")
        buf.write("\u020c\3\2\2\2\u0212\u020f\3\2\2\2\u0212\u0210\3\2\2\2")
        buf.write("\u0212\u0211\3\2\2\2\u0213\u021e\3\2\2\2\u0214\u0215\f")
        buf.write("\b\2\2\u0215\u0218\7@\2\2\u0216\u0219\7C\2\2\u0217\u0219")
        buf.write("\5`\61\2\u0218\u0216\3\2\2\2\u0218\u0217\3\2\2\2\u0219")
        buf.write("\u021d\3\2\2\2\u021a\u021b\f\6\2\2\u021b\u021d\5|?\2\u021c")
        buf.write("\u0214\3\2\2\2\u021c\u021a\3\2\2\2\u021d\u0220\3\2\2\2")
        buf.write("\u021e\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f]\3\2\2")
        buf.write("\2\u0220\u021e\3\2\2\2\u0221\u0222\5b\62\2\u0222\u0223")
        buf.write("\7-\2\2\u0223\u0225\3\2\2\2\u0224\u0221\3\2\2\2\u0225")
        buf.write("\u0228\3\2\2\2\u0226\u0224\3\2\2\2\u0226\u0227\3\2\2\2")
        buf.write("\u0227\u0229\3\2\2\2\u0228\u0226\3\2\2\2\u0229\u022a\5")
        buf.write("b\62\2\u022a_\3\2\2\2\u022b\u022c\7C\2\2\u022c\u022e\7")
        buf.write("&\2\2\u022d\u022f\5\u0086D\2\u022e\u022d\3\2\2\2\u022e")
        buf.write("\u022f\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u0231\7\'\2\2")
        buf.write("\u0231a\3\2\2\2\u0232\u0235\5d\63\2\u0233\u0235\5\u0084")
        buf.write("C\2\u0234\u0232\3\2\2\2\u0234\u0233\3\2\2\2\u0235c\3\2")
        buf.write("\2\2\u0236\u0237\5f\64\2\u0237\u0238\t\6\2\2\u0238\u0239")
        buf.write("\5f\64\2\u0239\u023c\3\2\2\2\u023a\u023c\5f\64\2\u023b")
        buf.write("\u0236\3\2\2\2\u023b\u023a\3\2\2\2\u023ce\3\2\2\2\u023d")
        buf.write("\u023e\5h\65\2\u023e\u023f\t\7\2\2\u023f\u0240\5h\65\2")
        buf.write("\u0240\u0243\3\2\2\2\u0241\u0243\5h\65\2\u0242\u023d\3")
        buf.write("\2\2\2\u0242\u0241\3\2\2\2\u0243g\3\2\2\2\u0244\u0245")
        buf.write("\b\65\1\2\u0245\u0246\5j\66\2\u0246\u024c\3\2\2\2\u0247")
        buf.write("\u0248\f\4\2\2\u0248\u0249\t\b\2\2\u0249\u024b\5j\66\2")
        buf.write("\u024a\u0247\3\2\2\2\u024b\u024e\3\2\2\2\u024c\u024a\3")
        buf.write("\2\2\2\u024c\u024d\3\2\2\2\u024di\3\2\2\2\u024e\u024c")
        buf.write("\3\2\2\2\u024f\u0250\b\66\1\2\u0250\u0251\5l\67\2\u0251")
        buf.write("\u0257\3\2\2\2\u0252\u0253\f\4\2\2\u0253\u0254\t\t\2\2")
        buf.write("\u0254\u0256\5l\67\2\u0255\u0252\3\2\2\2\u0256\u0259\3")
        buf.write("\2\2\2\u0257\u0255\3\2\2\2\u0257\u0258\3\2\2\2\u0258k")
        buf.write("\3\2\2\2\u0259\u0257\3\2\2\2\u025a\u025b\b\67\1\2\u025b")
        buf.write("\u025c\5n8\2\u025c\u0262\3\2\2\2\u025d\u025e\f\4\2\2\u025e")
        buf.write("\u025f\t\n\2\2\u025f\u0261\5n8\2\u0260\u025d\3\2\2\2\u0261")
        buf.write("\u0264\3\2\2\2\u0262\u0260\3\2\2\2\u0262\u0263\3\2\2\2")
        buf.write("\u0263m\3\2\2\2\u0264\u0262\3\2\2\2\u0265\u0266\7\64\2")
        buf.write("\2\u0266\u0269\5n8\2\u0267\u0269\5p9\2\u0268\u0265\3\2")
        buf.write("\2\2\u0268\u0267\3\2\2\2\u0269o\3\2\2\2\u026a\u026b\7")
        buf.write("\60\2\2\u026b\u026e\5p9\2\u026c\u026e\5r:\2\u026d\u026a")
        buf.write("\3\2\2\2\u026d\u026c\3\2\2\2\u026eq\3\2\2\2\u026f\u0270")
        buf.write("\b:\1\2\u0270\u0271\7(\2\2\u0271\u0272\5t;\2\u0272\u0273")
        buf.write("\7)\2\2\u0273\u0276\3\2\2\2\u0274\u0276\5t;\2\u0275\u026f")
        buf.write("\3\2\2\2\u0275\u0274\3\2\2\2\u0276\u027e\3\2\2\2\u0277")
        buf.write("\u0278\f\5\2\2\u0278\u0279\7(\2\2\u0279\u027a\5t;\2\u027a")
        buf.write("\u027b\7)\2\2\u027b\u027d\3\2\2\2\u027c\u0277\3\2\2\2")
        buf.write("\u027d\u0280\3\2\2\2\u027e\u027c\3\2\2\2\u027e\u027f\3")
        buf.write("\2\2\2\u027fs\3\2\2\2\u0280\u027e\3\2\2\2\u0281\u0282")
        buf.write("\b;\1\2\u0282\u0283\5v<\2\u0283\u028c\3\2\2\2\u0284\u0285")
        buf.write("\f\4\2\2\u0285\u0288\7@\2\2\u0286\u0289\7C\2\2\u0287\u0289")
        buf.write("\5`\61\2\u0288\u0286\3\2\2\2\u0288\u0287\3\2\2\2\u0289")
        buf.write("\u028b\3\2\2\2\u028a\u0284\3\2\2\2\u028b\u028e\3\2\2\2")
        buf.write("\u028c\u028a\3\2\2\2\u028c\u028d\3\2\2\2\u028du\3\2\2")
        buf.write("\2\u028e\u028c\3\2\2\2\u028f\u0290\t\5\2\2\u0290\u0293")
        buf.write("\7A\2\2\u0291\u0294\5\u0082B\2\u0292\u0294\7D\2\2\u0293")
        buf.write("\u0291\3\2\2\2\u0293\u0292\3\2\2\2\u0294\u0297\3\2\2\2")
        buf.write("\u0295\u0297\5x=\2\u0296\u028f\3\2\2\2\u0296\u0295\3\2")
        buf.write("\2\2\u0297w\3\2\2\2\u0298\u0299\7\35\2\2\u0299\u029a\5")
        buf.write("z>\2\u029a\u029c\7&\2\2\u029b\u029d\5\u0086D\2\u029c\u029b")
        buf.write("\3\2\2\2\u029c\u029d\3\2\2\2\u029d\u029e\3\2\2\2\u029e")
        buf.write("\u029f\7\'\2\2\u029f\u02a2\3\2\2\2\u02a0\u02a2\5z>\2\u02a1")
        buf.write("\u0298\3\2\2\2\u02a1\u02a0\3\2\2\2\u02a2y\3\2\2\2\u02a3")
        buf.write("\u02ad\5\u0088E\2\u02a4\u02ad\7%\2\2\u02a5\u02ad\7C\2")
        buf.write("\2\u02a6\u02a7\7&\2\2\u02a7\u02a8\5d\63\2\u02a8\u02a9")
        buf.write("\7\'\2\2\u02a9\u02ad\3\2\2\2\u02aa\u02ad\7\23\2\2\u02ab")
        buf.write("\u02ad\5\u008aF\2\u02ac\u02a3\3\2\2\2\u02ac\u02a4\3\2")
        buf.write("\2\2\u02ac\u02a5\3\2\2\2\u02ac\u02a6\3\2\2\2\u02ac\u02aa")
        buf.write("\3\2\2\2\u02ac\u02ab\3\2\2\2\u02ad{\3\2\2\2\u02ae\u02af")
        buf.write("\5~@\2\u02af}\3\2\2\2\u02b0\u02b1\b@\1\2\u02b1\u02b2\7")
        buf.write("(\2\2\u02b2\u02b3\5b\62\2\u02b3\u02b4\7)\2\2\u02b4\u02bc")
        buf.write("\3\2\2\2\u02b5\u02b6\f\4\2\2\u02b6\u02b7\7(\2\2\u02b7")
        buf.write("\u02b8\5b\62\2\u02b8\u02b9\7)\2\2\u02b9\u02bb\3\2\2\2")
        buf.write("\u02ba\u02b5\3\2\2\2\u02bb\u02be\3\2\2\2\u02bc\u02ba\3")
        buf.write("\2\2\2\u02bc\u02bd\3\2\2\2\u02bd\177\3\2\2\2\u02be\u02bc")
        buf.write("\3\2\2\2\u02bf\u02c0\t\5\2\2\u02c0\u02c3\7A\2\2\u02c1")
        buf.write("\u02c4\7D\2\2\u02c2\u02c4\5\u0082B\2\u02c3\u02c1\3\2\2")
        buf.write("\2\u02c3\u02c2\3\2\2\2\u02c4\u0081\3\2\2\2\u02c5\u02c6")
        buf.write("\7D\2\2\u02c6\u02c8\7&\2\2\u02c7\u02c9\5\u0086D\2\u02c8")
        buf.write("\u02c7\3\2\2\2\u02c8\u02c9\3\2\2\2\u02c9\u02ca\3\2\2\2")
        buf.write("\u02ca\u02cb\7\'\2\2\u02cb\u0083\3\2\2\2\u02cc\u02cd\7")
        buf.write("\35\2\2\u02cd\u02ce\7C\2\2\u02ce\u02d0\7&\2\2\u02cf\u02d1")
        buf.write("\5\u0086D\2\u02d0\u02cf\3\2\2\2\u02d0\u02d1\3\2\2\2\u02d1")
        buf.write("\u02d2\3\2\2\2\u02d2\u02d3\7\'\2\2\u02d3\u0085\3\2\2\2")
        buf.write("\u02d4\u02d9\5d\63\2\u02d5\u02d6\7-\2\2\u02d6\u02d8\5")
        buf.write("d\63\2\u02d7\u02d5\3\2\2\2\u02d8\u02db\3\2\2\2\u02d9\u02d7")
        buf.write("\3\2\2\2\u02d9\u02da\3\2\2\2\u02da\u0087\3\2\2\2\u02db")
        buf.write("\u02d9\3\2\2\2\u02dc\u02dd\t\13\2\2\u02dd\u0089\3\2\2")
        buf.write("\2\u02de\u02e1\5\u008cG\2\u02df\u02e1\5\u008eH\2\u02e0")
        buf.write("\u02de\3\2\2\2\u02e0\u02df\3\2\2\2\u02e1\u008b\3\2\2\2")
        buf.write("\u02e2\u02e3\7\37\2\2\u02e3\u02e5\7&\2\2\u02e4\u02e6\5")
        buf.write("\u0090I\2\u02e5\u02e4\3\2\2\2\u02e5\u02e6\3\2\2\2\u02e6")
        buf.write("\u02e7\3\2\2\2\u02e7\u02e8\7\'\2\2\u02e8\u008d\3\2\2\2")
        buf.write("\u02e9\u02ea\7\37\2\2\u02ea\u02eb\7&\2\2\u02eb\u02f0\5")
        buf.write("\u008cG\2\u02ec\u02ed\7-\2\2\u02ed\u02ef\5\u008cG\2\u02ee")
        buf.write("\u02ec\3\2\2\2\u02ef\u02f2\3\2\2\2\u02f0\u02ee\3\2\2\2")
        buf.write("\u02f0\u02f1\3\2\2\2\u02f1\u02f3\3\2\2\2\u02f2\u02f0\3")
        buf.write("\2\2\2\u02f3\u02f4\7\'\2\2\u02f4\u008f\3\2\2\2\u02f5\u02fa")
        buf.write("\5b\62\2\u02f6\u02f7\7-\2\2\u02f7\u02f9\5b\62\2\u02f8")
        buf.write("\u02f6\3\2\2\2\u02f9\u02fc\3\2\2\2\u02fa\u02f8\3\2\2\2")
        buf.write("\u02fa\u02fb\3\2\2\2\u02fb\u0091\3\2\2\2\u02fc\u02fa\3")
        buf.write("\2\2\2L\u0095\u009d\u00a3\u00aa\u00b0\u00b8\u00cf\u00d7")
        buf.write("\u00ee\u00f4\u00ff\u0104\u0109\u0110\u0115\u011e\u012c")
        buf.write("\u0132\u013a\u0151\u0159\u0170\u0176\u017e\u0187\u018e")
        buf.write("\u0196\u019c\u01a6\u01aa\u01ad\u01b5\u01b9\u01be\u01c8")
        buf.write("\u01d3\u01db\u01e1\u01e5\u01f2\u0203\u020a\u0212\u0218")
        buf.write("\u021c\u021e\u0226\u022e\u0234\u023b\u0242\u024c\u0257")
        buf.write("\u0262\u0268\u026d\u0275\u027e\u0288\u028c\u0293\u0296")
        buf.write("\u029c\u02a1\u02ac\u02bc\u02c3\u02c8\u02d0\u02d9\u02e0")
        buf.write("\u02e5\u02f0\u02fa")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'Val'", "'Var'", 
                     "'$'", "'Break'", "'Foreach'", "'Int'", "'Null'", "'Constructor'", 
                     "'Continue'", "'True'", "'Float'", "'Class'", "'Destructor'", 
                     "'If'", "'False'", "'Boolean'", "'New'", "'Elseif'", 
                     "'Array'", "'String'", "'By'", "'Else'", "'In'", "'Return'", 
                     "'Self'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "';'", "','", "'..'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'==.'", "'+.'", "'.'", "'::'", 
                     "':'" ]

    symbolicNames = [ "<INVALID>", "LITERAL_BOOLEAN", "LITERAL_INT", "LITERAL_ZERO", 
                      "LITERAL_INT_DEC", "LITERAL_INT_HEX", "LITERAL_INT_OCT", 
                      "LITERAL_INT_BIN", "LITERAL_FLOAT", "LITERAL_STRING", 
                      "DOUBLE_QUOTE", "VAL", "VAR", "STATIC", "BREAK", "FOREACH", 
                      "INT", "NULL", "CONSTRUCTOR", "CONTINUE", "TRUE", 
                      "FLOAT", "CLASS", "DESTRUCTOR", "IF", "FALSE", "BOOLEAN", 
                      "NEW", "ELSEIF", "ARRAY", "STRING", "BY", "ELSE", 
                      "IN", "RETURN", "SELF", "LB", "RB", "LS", "RS", "LP", 
                      "RP", "SEMI", "COMMA", "DOTDOT", "ADD", "SUBTRACT", 
                      "MULTIPLY", "DIVIDE", "MODULO", "NOT", "AND", "OR", 
                      "EQUAL", "ASSIGN", "NOT_EQUAL", "LESS_THAN", "LEQ", 
                      "GREATER_THAN", "GEQ", "EQUAL_STRING", "STRING_CONCAT", 
                      "DOT", "DOUBLE_COLON", "COLON", "ID", "DOLLAR_ID", 
                      "BLOCK_COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_class_body = 2
    RULE_class_attr = 3
    RULE_attr_no_value = 4
    RULE_attr_with_value = 5
    RULE_attr_pair = 6
    RULE_attr_array_no_value = 7
    RULE_attr_array_with_value = 8
    RULE_attr_array_pair = 9
    RULE_attr_array_decl_tail = 10
    RULE_any_id = 11
    RULE_class_method = 12
    RULE_normal_method = 13
    RULE_constructor = 14
    RULE_destructor = 15
    RULE_stmt = 16
    RULE_var_decl = 17
    RULE_var_no_value = 18
    RULE_var_with_value = 19
    RULE_var_pair = 20
    RULE_var_array_no_value = 21
    RULE_var_array_with_value = 22
    RULE_var_array_pair = 23
    RULE_var_array_decl_tail = 24
    RULE_array_rhs = 25
    RULE_assign_stmt = 26
    RULE_assign_lhs = 27
    RULE_params_list = 28
    RULE_params = 29
    RULE_data_type = 30
    RULE_if_stmt = 31
    RULE_else_if_body = 32
    RULE_else_body = 33
    RULE_for_in_stmt = 34
    RULE_for_in_body = 35
    RULE_for_in_expr = 36
    RULE_scalar_variable = 37
    RULE_break_stmt = 38
    RULE_continue_stmt = 39
    RULE_return_stmt = 40
    RULE_method_invoc = 41
    RULE_static_method_invoc = 42
    RULE_block_stmt_stmt = 43
    RULE_block_stmt = 44
    RULE_method_invoc_literal = 45
    RULE_expr_list = 46
    RULE_funcall = 47
    RULE_all_expr = 48
    RULE_op = 49
    RULE_op1 = 50
    RULE_op2 = 51
    RULE_op3 = 52
    RULE_op4 = 53
    RULE_op5 = 54
    RULE_op6 = 55
    RULE_op7 = 56
    RULE_op8 = 57
    RULE_op9 = 58
    RULE_op10 = 59
    RULE_operands = 60
    RULE_element_expr = 61
    RULE_index_ops = 62
    RULE_static_member_access = 63
    RULE_static_method = 64
    RULE_object_create = 65
    RULE_list_of_expr = 66
    RULE_literal = 67
    RULE_literal_array = 68
    RULE_literal_idx_array = 69
    RULE_literal_mtd_array = 70
    RULE_array_element = 71

    ruleNames =  [ "program", "class_decl", "class_body", "class_attr", 
                   "attr_no_value", "attr_with_value", "attr_pair", "attr_array_no_value", 
                   "attr_array_with_value", "attr_array_pair", "attr_array_decl_tail", 
                   "any_id", "class_method", "normal_method", "constructor", 
                   "destructor", "stmt", "var_decl", "var_no_value", "var_with_value", 
                   "var_pair", "var_array_no_value", "var_array_with_value", 
                   "var_array_pair", "var_array_decl_tail", "array_rhs", 
                   "assign_stmt", "assign_lhs", "params_list", "params", 
                   "data_type", "if_stmt", "else_if_body", "else_body", 
                   "for_in_stmt", "for_in_body", "for_in_expr", "scalar_variable", 
                   "break_stmt", "continue_stmt", "return_stmt", "method_invoc", 
                   "static_method_invoc", "block_stmt_stmt", "block_stmt", 
                   "method_invoc_literal", "expr_list", "funcall", "all_expr", 
                   "op", "op1", "op2", "op3", "op4", "op5", "op6", "op7", 
                   "op8", "op9", "op10", "operands", "element_expr", "index_ops", 
                   "static_member_access", "static_method", "object_create", 
                   "list_of_expr", "literal", "literal_array", "literal_idx_array", 
                   "literal_mtd_array", "array_element" ]

    EOF = Token.EOF
    LITERAL_BOOLEAN=1
    LITERAL_INT=2
    LITERAL_ZERO=3
    LITERAL_INT_DEC=4
    LITERAL_INT_HEX=5
    LITERAL_INT_OCT=6
    LITERAL_INT_BIN=7
    LITERAL_FLOAT=8
    LITERAL_STRING=9
    DOUBLE_QUOTE=10
    VAL=11
    VAR=12
    STATIC=13
    BREAK=14
    FOREACH=15
    INT=16
    NULL=17
    CONSTRUCTOR=18
    CONTINUE=19
    TRUE=20
    FLOAT=21
    CLASS=22
    DESTRUCTOR=23
    IF=24
    FALSE=25
    BOOLEAN=26
    NEW=27
    ELSEIF=28
    ARRAY=29
    STRING=30
    BY=31
    ELSE=32
    IN=33
    RETURN=34
    SELF=35
    LB=36
    RB=37
    LS=38
    RS=39
    LP=40
    RP=41
    SEMI=42
    COMMA=43
    DOTDOT=44
    ADD=45
    SUBTRACT=46
    MULTIPLY=47
    DIVIDE=48
    MODULO=49
    NOT=50
    AND=51
    OR=52
    EQUAL=53
    ASSIGN=54
    NOT_EQUAL=55
    LESS_THAN=56
    LEQ=57
    GREATER_THAN=58
    GEQ=59
    EQUAL_STRING=60
    STRING_CONCAT=61
    DOT=62
    DOUBLE_COLON=63
    COLON=64
    ID=65
    DOLLAR_ID=66
    BLOCK_COMMENT=67
    WS=68
    UNCLOSE_STRING=69
    ILLEGAL_ESCAPE=70
    ERROR_CHAR=71

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 144
                self.class_decl()
                self.state = 147 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 149
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def class_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_bodyContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_bodyContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = D96Parser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(D96Parser.CLASS)
            self.state = 152
            self.match(D96Parser.ID)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 153
                self.match(D96Parser.COLON)
                self.state = 154
                self.match(D96Parser.ID)


            self.state = 157
            self.match(D96Parser.LP)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.CONSTRUCTOR - 11)) | (1 << (D96Parser.DESTRUCTOR - 11)) | (1 << (D96Parser.ID - 11)) | (1 << (D96Parser.DOLLAR_ID - 11)))) != 0):
                self.state = 158
                self.class_body()
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 164
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_attr(self):
            return self.getTypedRuleContext(D96Parser.Class_attrContext,0)


        def class_method(self):
            return self.getTypedRuleContext(D96Parser.Class_methodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body" ):
                return visitor.visitClass_body(self)
            else:
                return visitor.visitChildren(self)




    def class_body(self):

        localctx = D96Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_body)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.class_attr()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.class_method()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_attrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_no_value(self):
            return self.getTypedRuleContext(D96Parser.Attr_no_valueContext,0)


        def attr_with_value(self):
            return self.getTypedRuleContext(D96Parser.Attr_with_valueContext,0)


        def attr_array_no_value(self):
            return self.getTypedRuleContext(D96Parser.Attr_array_no_valueContext,0)


        def attr_array_with_value(self):
            return self.getTypedRuleContext(D96Parser.Attr_array_with_valueContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_attr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_attr" ):
                return visitor.visitClass_attr(self)
            else:
                return visitor.visitChildren(self)




    def class_attr(self):

        localctx = D96Parser.Class_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_attr)
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.attr_no_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.attr_with_value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 172
                self.attr_array_no_value()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 173
                self.attr_array_with_value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_no_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def any_id(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Any_idContext)
            else:
                return self.getTypedRuleContext(D96Parser.Any_idContext,i)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_no_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_no_value" ):
                return visitor.visitAttr_no_value(self)
            else:
                return visitor.visitChildren(self)




    def attr_no_value(self):

        localctx = D96Parser.Attr_no_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attr_no_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 177
            self.any_id()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 178
                self.match(D96Parser.COMMA)
                self.state = 179
                self.any_id()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 185
            self.match(D96Parser.COLON)
            self.state = 186
            self.data_type()
            self.state = 187
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_with_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def any_id(self):
            return self.getTypedRuleContext(D96Parser.Any_idContext,0)


        def attr_pair(self):
            return self.getTypedRuleContext(D96Parser.Attr_pairContext,0)


        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_with_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_with_value" ):
                return visitor.visitAttr_with_value(self)
            else:
                return visitor.visitChildren(self)




    def attr_with_value(self):

        localctx = D96Parser.Attr_with_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attr_with_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 190
            self.any_id()
            self.state = 191
            self.attr_pair()
            self.state = 192
            self.all_expr()
            self.state = 193
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_pairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def any_id(self):
            return self.getTypedRuleContext(D96Parser.Any_idContext,0)


        def attr_pair(self):
            return self.getTypedRuleContext(D96Parser.Attr_pairContext,0)


        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_pair

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_pair" ):
                return visitor.visitAttr_pair(self)
            else:
                return visitor.visitChildren(self)




    def attr_pair(self):

        localctx = D96Parser.Attr_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attr_pair)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.match(D96Parser.COMMA)
                self.state = 196
                self.any_id()
                self.state = 197
                self.attr_pair()
                self.state = 198
                self.all_expr()
                self.state = 199
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.match(D96Parser.COLON)
                self.state = 202
                self.data_type()
                self.state = 203
                self.match(D96Parser.ASSIGN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_array_no_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def any_id(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Any_idContext)
            else:
                return self.getTypedRuleContext(D96Parser.Any_idContext,i)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def attr_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Attr_array_decl_tailContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_array_no_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_array_no_value" ):
                return visitor.visitAttr_array_no_value(self)
            else:
                return visitor.visitChildren(self)




    def attr_array_no_value(self):

        localctx = D96Parser.Attr_array_no_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attr_array_no_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 208
            self.any_id()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 209
                self.match(D96Parser.COMMA)
                self.state = 210
                self.any_id()
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 216
            self.match(D96Parser.COLON)
            self.state = 217
            self.attr_array_decl_tail()
            self.state = 218
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_array_with_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def any_id(self):
            return self.getTypedRuleContext(D96Parser.Any_idContext,0)


        def attr_array_pair(self):
            return self.getTypedRuleContext(D96Parser.Attr_array_pairContext,0)


        def array_rhs(self):
            return self.getTypedRuleContext(D96Parser.Array_rhsContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_array_with_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_array_with_value" ):
                return visitor.visitAttr_array_with_value(self)
            else:
                return visitor.visitChildren(self)




    def attr_array_with_value(self):

        localctx = D96Parser.Attr_array_with_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attr_array_with_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 221
            self.any_id()
            self.state = 222
            self.attr_array_pair()
            self.state = 223
            self.array_rhs()
            self.state = 224
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_array_pairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def any_id(self):
            return self.getTypedRuleContext(D96Parser.Any_idContext,0)


        def attr_array_pair(self):
            return self.getTypedRuleContext(D96Parser.Attr_array_pairContext,0)


        def array_rhs(self):
            return self.getTypedRuleContext(D96Parser.Array_rhsContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def attr_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Attr_array_decl_tailContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_array_pair

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_array_pair" ):
                return visitor.visitAttr_array_pair(self)
            else:
                return visitor.visitChildren(self)




    def attr_array_pair(self):

        localctx = D96Parser.Attr_array_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attr_array_pair)
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(D96Parser.COMMA)
                self.state = 227
                self.any_id()
                self.state = 228
                self.attr_array_pair()
                self.state = 229
                self.array_rhs()
                self.state = 230
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.match(D96Parser.COLON)
                self.state = 233
                self.attr_array_decl_tail()
                self.state = 234
                self.match(D96Parser.ASSIGN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_array_decl_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def LITERAL_INT(self):
            return self.getToken(D96Parser.LITERAL_INT, 0)

        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def attr_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Attr_array_decl_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attr_array_decl_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_array_decl_tail" ):
                return visitor.visitAttr_array_decl_tail(self)
            else:
                return visitor.visitChildren(self)




    def attr_array_decl_tail(self):

        localctx = D96Parser.Attr_array_decl_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attr_array_decl_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(D96Parser.ARRAY)
            self.state = 239
            self.match(D96Parser.LS)
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.SELF, D96Parser.ID]:
                self.state = 240
                self.data_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 241
                self.attr_array_decl_tail()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 244
            self.match(D96Parser.COMMA)
            self.state = 245
            self.match(D96Parser.LITERAL_INT)
            self.state = 246
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Any_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_any_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAny_id" ):
                return visitor.visitAny_id(self)
            else:
                return visitor.visitChildren(self)




    def any_id(self):

        localctx = D96Parser.Any_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_any_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normal_method(self):
            return self.getTypedRuleContext(D96Parser.Normal_methodContext,0)


        def constructor(self):
            return self.getTypedRuleContext(D96Parser.ConstructorContext,0)


        def destructor(self):
            return self.getTypedRuleContext(D96Parser.DestructorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_method" ):
                return visitor.visitClass_method(self)
            else:
                return visitor.visitChildren(self)




    def class_method(self):

        localctx = D96Parser.Class_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_class_method)
        try:
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.normal_method()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.destructor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def any_id(self):
            return self.getTypedRuleContext(D96Parser.Any_idContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def params_list(self):
            return self.getTypedRuleContext(D96Parser.Params_listContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_normal_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_method" ):
                return visitor.visitNormal_method(self)
            else:
                return visitor.visitChildren(self)




    def normal_method(self):

        localctx = D96Parser.Normal_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_normal_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.any_id()
            self.state = 256
            self.match(D96Parser.LB)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 257
                self.params_list()


            self.state = 260
            self.match(D96Parser.RB)
            self.state = 261
            self.match(D96Parser.LP)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 262
                self.block_stmt()


            self.state = 265
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def params_list(self):
            return self.getTypedRuleContext(D96Parser.Params_listContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 268
            self.match(D96Parser.LB)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 269
                self.params_list()


            self.state = 272
            self.match(D96Parser.RB)
            self.state = 273
            self.match(D96Parser.LP)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 274
                self.block_stmt()


            self.state = 277
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor" ):
                return visitor.visitDestructor(self)
            else:
                return visitor.visitChildren(self)




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_destructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(D96Parser.DESTRUCTOR)
            self.state = 280
            self.match(D96Parser.LB)
            self.state = 281
            self.match(D96Parser.RB)
            self.state = 282
            self.match(D96Parser.LP)
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 283
                self.block_stmt()


            self.state = 286
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(D96Parser.Var_declContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(D96Parser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(D96Parser.If_stmtContext,0)


        def for_in_stmt(self):
            return self.getTypedRuleContext(D96Parser.For_in_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(D96Parser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(D96Parser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(D96Parser.Return_stmtContext,0)


        def method_invoc(self):
            return self.getTypedRuleContext(D96Parser.Method_invocContext,0)


        def static_method_invoc(self):
            return self.getTypedRuleContext(D96Parser.Static_method_invocContext,0)


        def block_stmt_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmt_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_stmt)
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 290
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 291
                self.for_in_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 292
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 293
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 294
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 295
                self.method_invoc()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 296
                self.static_method_invoc()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 297
                self.block_stmt_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_no_value(self):
            return self.getTypedRuleContext(D96Parser.Var_no_valueContext,0)


        def var_with_value(self):
            return self.getTypedRuleContext(D96Parser.Var_with_valueContext,0)


        def var_array_no_value(self):
            return self.getTypedRuleContext(D96Parser.Var_array_no_valueContext,0)


        def var_array_with_value(self):
            return self.getTypedRuleContext(D96Parser.Var_array_with_valueContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = D96Parser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_var_decl)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.var_no_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.var_with_value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 302
                self.var_array_no_value()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 303
                self.var_array_with_value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_no_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_var_no_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_no_value" ):
                return visitor.visitVar_no_value(self)
            else:
                return visitor.visitChildren(self)




    def var_no_value(self):

        localctx = D96Parser.Var_no_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_var_no_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 307
            self.match(D96Parser.ID)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 308
                self.match(D96Parser.COMMA)
                self.state = 309
                self.match(D96Parser.ID)
                self.state = 314
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 315
            self.match(D96Parser.COLON)
            self.state = 316
            self.data_type()
            self.state = 317
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_with_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def var_pair(self):
            return self.getTypedRuleContext(D96Parser.Var_pairContext,0)


        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_with_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_with_value" ):
                return visitor.visitVar_with_value(self)
            else:
                return visitor.visitChildren(self)




    def var_with_value(self):

        localctx = D96Parser.Var_with_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_with_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 320
            self.match(D96Parser.ID)
            self.state = 321
            self.var_pair()
            self.state = 322
            self.all_expr()
            self.state = 323
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_pairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def var_pair(self):
            return self.getTypedRuleContext(D96Parser.Var_pairContext,0)


        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_pair

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_pair" ):
                return visitor.visitVar_pair(self)
            else:
                return visitor.visitChildren(self)




    def var_pair(self):

        localctx = D96Parser.Var_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_var_pair)
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.match(D96Parser.COMMA)
                self.state = 326
                self.match(D96Parser.ID)
                self.state = 327
                self.var_pair()
                self.state = 328
                self.all_expr()
                self.state = 329
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.match(D96Parser.COLON)
                self.state = 332
                self.data_type()
                self.state = 333
                self.match(D96Parser.ASSIGN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_array_no_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def var_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Var_array_decl_tailContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_var_array_no_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_array_no_value" ):
                return visitor.visitVar_array_no_value(self)
            else:
                return visitor.visitChildren(self)




    def var_array_no_value(self):

        localctx = D96Parser.Var_array_no_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_var_array_no_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 338
            self.match(D96Parser.ID)
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 339
                self.match(D96Parser.COMMA)
                self.state = 340
                self.match(D96Parser.ID)
                self.state = 345
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 346
            self.match(D96Parser.COLON)
            self.state = 347
            self.var_array_decl_tail()
            self.state = 348
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_array_with_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def var_array_pair(self):
            return self.getTypedRuleContext(D96Parser.Var_array_pairContext,0)


        def array_rhs(self):
            return self.getTypedRuleContext(D96Parser.Array_rhsContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_array_with_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_array_with_value" ):
                return visitor.visitVar_array_with_value(self)
            else:
                return visitor.visitChildren(self)




    def var_array_with_value(self):

        localctx = D96Parser.Var_array_with_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_var_array_with_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 351
            self.match(D96Parser.ID)
            self.state = 352
            self.var_array_pair()
            self.state = 353
            self.array_rhs()
            self.state = 354
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_array_pairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def var_array_pair(self):
            return self.getTypedRuleContext(D96Parser.Var_array_pairContext,0)


        def array_rhs(self):
            return self.getTypedRuleContext(D96Parser.Array_rhsContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def var_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Var_array_decl_tailContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_array_pair

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_array_pair" ):
                return visitor.visitVar_array_pair(self)
            else:
                return visitor.visitChildren(self)




    def var_array_pair(self):

        localctx = D96Parser.Var_array_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_var_array_pair)
        try:
            self.state = 366
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.match(D96Parser.COMMA)
                self.state = 357
                self.match(D96Parser.ID)
                self.state = 358
                self.var_array_pair()
                self.state = 359
                self.array_rhs()
                self.state = 360
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.match(D96Parser.COLON)
                self.state = 363
                self.var_array_decl_tail()
                self.state = 364
                self.match(D96Parser.ASSIGN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_array_decl_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def LITERAL_INT(self):
            return self.getToken(D96Parser.LITERAL_INT, 0)

        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def var_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Var_array_decl_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_array_decl_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_array_decl_tail" ):
                return visitor.visitVar_array_decl_tail(self)
            else:
                return visitor.visitChildren(self)




    def var_array_decl_tail(self):

        localctx = D96Parser.Var_array_decl_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_var_array_decl_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(D96Parser.ARRAY)
            self.state = 369
            self.match(D96Parser.LS)
            self.state = 372
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.SELF, D96Parser.ID]:
                self.state = 370
                self.data_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 371
                self.var_array_decl_tail()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 374
            self.match(D96Parser.COMMA)
            self.state = 375
            self.match(D96Parser.LITERAL_INT)
            self.state = 376
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_rhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_array(self):
            return self.getTypedRuleContext(D96Parser.Literal_arrayContext,0)


        def object_create(self):
            return self.getTypedRuleContext(D96Parser.Object_createContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_rhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_rhs" ):
                return visitor.visitArray_rhs(self)
            else:
                return visitor.visitChildren(self)




    def array_rhs(self):

        localctx = D96Parser.Array_rhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_array_rhs)
        try:
            self.state = 380
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.literal_array()
                pass
            elif token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.object_create()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs(self):
            return self.getTypedRuleContext(D96Parser.Assign_lhsContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.assign_lhs()
            self.state = 383
            self.match(D96Parser.ASSIGN)
            self.state = 384
            self.all_expr()
            self.state = 385
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_variable(self):
            return self.getTypedRuleContext(D96Parser.Scalar_variableContext,0)


        def element_expr(self):
            return self.getTypedRuleContext(D96Parser.Element_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_lhs" ):
                return visitor.visitAssign_lhs(self)
            else:
                return visitor.visitChildren(self)




    def assign_lhs(self):

        localctx = D96Parser.Assign_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_assign_lhs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.scalar_variable(0)
            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.LS:
                self.state = 388
                self.element_expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ParamsContext)
            else:
                return self.getTypedRuleContext(D96Parser.ParamsContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI)
            else:
                return self.getToken(D96Parser.SEMI, i)

        def getRuleIndex(self):
            return D96Parser.RULE_params_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_list" ):
                return visitor.visitParams_list(self)
            else:
                return visitor.visitChildren(self)




    def params_list(self):

        localctx = D96Parser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.params()
            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 392
                self.match(D96Parser.SEMI)
                self.state = 393
                self.params()
                self.state = 398
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def var_array_decl_tail(self):
            return self.getTypedRuleContext(D96Parser.Var_array_decl_tailContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = D96Parser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(D96Parser.ID)

            self.state = 404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 400
                self.match(D96Parser.COMMA)
                self.state = 401
                self.match(D96Parser.ID)
                self.state = 406
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 407
            self.match(D96Parser.COLON)
            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.SELF, D96Parser.ID]:
                self.state = 408
                self.data_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 409
                self.var_array_decl_tail()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = D96Parser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            _la = self._input.LA(1)
            if not(((((_la - 16)) & ~0x3f) == 0 and ((1 << (_la - 16)) & ((1 << (D96Parser.INT - 16)) | (1 << (D96Parser.FLOAT - 16)) | (1 << (D96Parser.BOOLEAN - 16)) | (1 << (D96Parser.STRING - 16)) | (1 << (D96Parser.SELF - 16)) | (1 << (D96Parser.ID - 16)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def else_if_body(self):
            return self.getTypedRuleContext(D96Parser.Else_if_bodyContext,0)


        def else_body(self):
            return self.getTypedRuleContext(D96Parser.Else_bodyContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(D96Parser.IF)
            self.state = 415
            self.match(D96Parser.LB)
            self.state = 416
            self.all_expr()
            self.state = 417
            self.match(D96Parser.RB)
            self.state = 418
            self.match(D96Parser.LP)
            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 419
                self.block_stmt()


            self.state = 422
            self.match(D96Parser.RP)
            self.state = 424
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSEIF:
                self.state = 423
                self.else_if_body()


            self.state = 427
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 426
                self.else_body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def else_if_body(self):
            return self.getTypedRuleContext(D96Parser.Else_if_bodyContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_if_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_body" ):
                return visitor.visitElse_if_body(self)
            else:
                return visitor.visitChildren(self)




    def else_if_body(self):

        localctx = D96Parser.Else_if_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_else_if_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(D96Parser.ELSEIF)
            self.state = 430
            self.match(D96Parser.LB)
            self.state = 431
            self.all_expr()
            self.state = 432
            self.match(D96Parser.RB)
            self.state = 433
            self.match(D96Parser.LP)
            self.state = 435
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 434
                self.block_stmt()


            self.state = 437
            self.match(D96Parser.RP)
            self.state = 439
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSEIF:
                self.state = 438
                self.else_if_body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_body" ):
                return visitor.visitElse_body(self)
            else:
                return visitor.visitChildren(self)




    def else_body(self):

        localctx = D96Parser.Else_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_else_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(D96Parser.ELSE)
            self.state = 442
            self.match(D96Parser.LP)
            self.state = 444
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 443
                self.block_stmt()


            self.state = 446
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_in_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def for_in_body(self):
            return self.getTypedRuleContext(D96Parser.For_in_bodyContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_for_in_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_in_stmt" ):
                return visitor.visitFor_in_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_in_stmt(self):

        localctx = D96Parser.For_in_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_for_in_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(D96Parser.FOREACH)
            self.state = 449
            self.match(D96Parser.LB)
            self.state = 450
            self.for_in_body()
            self.state = 451
            self.match(D96Parser.RB)
            self.state = 452
            self.match(D96Parser.LP)
            self.state = 454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 453
                self.block_stmt()


            self.state = 456
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_in_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_variable(self):
            return self.getTypedRuleContext(D96Parser.Scalar_variableContext,0)


        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def for_in_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.For_in_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.For_in_exprContext,i)


        def DOTDOT(self):
            return self.getToken(D96Parser.DOTDOT, 0)

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_for_in_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_in_body" ):
                return visitor.visitFor_in_body(self)
            else:
                return visitor.visitChildren(self)




    def for_in_body(self):

        localctx = D96Parser.For_in_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_for_in_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.scalar_variable(0)
            self.state = 459
            self.match(D96Parser.IN)
            self.state = 460
            self.for_in_expr()
            self.state = 461
            self.match(D96Parser.DOTDOT)
            self.state = 462
            self.for_in_expr()
            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 463
                self.match(D96Parser.BY)
                self.state = 464
                self.for_in_expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_in_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_for_in_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_in_expr" ):
                return visitor.visitFor_in_expr(self)
            else:
                return visitor.visitChildren(self)




    def for_in_expr(self):

        localctx = D96Parser.For_in_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_for_in_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.all_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def static_member_access(self):
            return self.getTypedRuleContext(D96Parser.Static_member_accessContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def scalar_variable(self):
            return self.getTypedRuleContext(D96Parser.Scalar_variableContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_scalar_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_variable" ):
                return visitor.visitScalar_variable(self)
            else:
                return visitor.visitChildren(self)



    def scalar_variable(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Scalar_variableContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_scalar_variable, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 470
                self.static_member_access()
                pass

            elif la_ == 2:
                self.state = 471
                self.match(D96Parser.SELF)
                pass

            elif la_ == 3:
                self.state = 472
                self.match(D96Parser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 483
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Scalar_variableContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_scalar_variable)
                    self.state = 475
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 476
                    self.match(D96Parser.DOT)
                    self.state = 479
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        self.state = 477
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 478
                        self.funcall()
                        pass

             
                self.state = 485
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(D96Parser.BREAK)
            self.state = 487
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = D96Parser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.match(D96Parser.CONTINUE)
            self.state = 490
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def all_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.All_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.All_exprContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(D96Parser.RETURN)
            self.state = 496
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_ZERO) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.LS) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.ID:
                self.state = 493
                self.all_expr()
                self.state = 498
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 499
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_invoc_literal(self):
            return self.getTypedRuleContext(D96Parser.Method_invoc_literalContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_invoc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invoc" ):
                return visitor.visitMethod_invoc(self)
            else:
                return visitor.visitChildren(self)




    def method_invoc(self):

        localctx = D96Parser.Method_invocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_method_invoc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.method_invoc_literal(0)
            self.state = 502
            self.match(D96Parser.DOT)
            self.state = 503
            self.funcall()
            self.state = 504
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_method_invocContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def static_method(self):
            return self.getTypedRuleContext(D96Parser.Static_methodContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_method_invoc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method_invoc" ):
                return visitor.visitStatic_method_invoc(self)
            else:
                return visitor.visitChildren(self)




    def static_method_invoc(self):

        localctx = D96Parser.Static_method_invocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_static_method_invoc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            _la = self._input.LA(1)
            if not(_la==D96Parser.SELF or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 507
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 508
            self.static_method()
            self.state = 509
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmt_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt_stmt" ):
                return visitor.visitBlock_stmt_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt_stmt(self):

        localctx = D96Parser.Block_stmt_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_block_stmt_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.match(D96Parser.LP)
            self.state = 513
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0):
                self.state = 512
                self.block_stmt()


            self.state = 515
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.StmtContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 517
                self.stmt()
                self.state = 520 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (D96Parser.VAL - 11)) | (1 << (D96Parser.VAR - 11)) | (1 << (D96Parser.BREAK - 11)) | (1 << (D96Parser.FOREACH - 11)) | (1 << (D96Parser.CONTINUE - 11)) | (1 << (D96Parser.IF - 11)) | (1 << (D96Parser.NEW - 11)) | (1 << (D96Parser.RETURN - 11)) | (1 << (D96Parser.SELF - 11)) | (1 << (D96Parser.LP - 11)) | (1 << (D96Parser.ID - 11)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invoc_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def static_member_access(self):
            return self.getTypedRuleContext(D96Parser.Static_member_accessContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def method_invoc_literal(self):
            return self.getTypedRuleContext(D96Parser.Method_invoc_literalContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def element_expr(self):
            return self.getTypedRuleContext(D96Parser.Element_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invoc_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invoc_literal" ):
                return visitor.visitMethod_invoc_literal(self)
            else:
                return visitor.visitChildren(self)



    def method_invoc_literal(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Method_invoc_literalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_method_invoc_literal, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 523
                self.match(D96Parser.NEW)
                self.state = 524
                self.funcall()
                pass

            elif la_ == 2:
                self.state = 525
                self.static_member_access()
                pass

            elif la_ == 3:
                self.state = 526
                self.match(D96Parser.SELF)
                pass

            elif la_ == 4:
                self.state = 527
                self.match(D96Parser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 540
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 538
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Method_invoc_literalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_method_invoc_literal)
                        self.state = 530
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 531
                        self.match(D96Parser.DOT)
                        self.state = 534
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                        if la_ == 1:
                            self.state = 532
                            self.match(D96Parser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 533
                            self.funcall()
                            pass


                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Method_invoc_literalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_method_invoc_literal)
                        self.state = 536
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 537
                        self.element_expr()
                        pass

             
                self.state = 542
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.All_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.All_exprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = D96Parser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 543
                    self.all_expr()
                    self.state = 544
                    self.match(D96Parser.COMMA) 
                self.state = 550
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

            self.state = 551
            self.all_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_of_expr(self):
            return self.getTypedRuleContext(D96Parser.List_of_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = D96Parser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.match(D96Parser.ID)
            self.state = 554
            self.match(D96Parser.LB)
            self.state = 556
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_ZERO) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.LS) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.ID:
                self.state = 555
                self.list_of_expr()


            self.state = 558
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op(self):
            return self.getTypedRuleContext(D96Parser.OpContext,0)


        def object_create(self):
            return self.getTypedRuleContext(D96Parser.Object_createContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_all_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_expr" ):
                return visitor.visitAll_expr(self)
            else:
                return visitor.visitChildren(self)




    def all_expr(self):

        localctx = D96Parser.All_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_all_expr)
        try:
            self.state = 562
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 560
                self.op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 561
                self.object_create()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Op1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Op1Context,i)


        def STRING_CONCAT(self):
            return self.getToken(D96Parser.STRING_CONCAT, 0)

        def EQUAL_STRING(self):
            return self.getToken(D96Parser.EQUAL_STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)




    def op(self):

        localctx = D96Parser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.state = 569
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 564
                self.op1()
                self.state = 565
                _la = self._input.LA(1)
                if not(_la==D96Parser.EQUAL_STRING or _la==D96Parser.STRING_CONCAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 566
                self.op1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 568
                self.op1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Op2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Op2Context,i)


        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(D96Parser.NOT_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(D96Parser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(D96Parser.GREATER_THAN, 0)

        def LEQ(self):
            return self.getToken(D96Parser.LEQ, 0)

        def GEQ(self):
            return self.getToken(D96Parser.GEQ, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_op1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp1" ):
                return visitor.visitOp1(self)
            else:
                return visitor.visitChildren(self)




    def op1(self):

        localctx = D96Parser.Op1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_op1)
        self._la = 0 # Token type
        try:
            self.state = 576
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 571
                self.op2(0)
                self.state = 572
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.LESS_THAN) | (1 << D96Parser.LEQ) | (1 << D96Parser.GREATER_THAN) | (1 << D96Parser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 573
                self.op2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 575
                self.op2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op3(self):
            return self.getTypedRuleContext(D96Parser.Op3Context,0)


        def op2(self):
            return self.getTypedRuleContext(D96Parser.Op2Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_op2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp2" ):
                return visitor.visitOp2(self)
            else:
                return visitor.visitChildren(self)



    def op2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Op2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_op2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 579
            self.op3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 586
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op2)
                    self.state = 581
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 582
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 583
                    self.op3(0) 
                self.state = 588
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Op3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op4(self):
            return self.getTypedRuleContext(D96Parser.Op4Context,0)


        def op3(self):
            return self.getTypedRuleContext(D96Parser.Op3Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUBTRACT(self):
            return self.getToken(D96Parser.SUBTRACT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_op3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp3" ):
                return visitor.visitOp3(self)
            else:
                return visitor.visitChildren(self)



    def op3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Op3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_op3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 590
            self.op4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 597
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op3)
                    self.state = 592
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 593
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUBTRACT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 594
                    self.op4(0) 
                self.state = 599
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Op4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op5(self):
            return self.getTypedRuleContext(D96Parser.Op5Context,0)


        def op4(self):
            return self.getTypedRuleContext(D96Parser.Op4Context,0)


        def MULTIPLY(self):
            return self.getToken(D96Parser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(D96Parser.DIVIDE, 0)

        def MODULO(self):
            return self.getToken(D96Parser.MODULO, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_op4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp4" ):
                return visitor.visitOp4(self)
            else:
                return visitor.visitChildren(self)



    def op4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Op4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_op4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 601
            self.op5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 608
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,53,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op4)
                    self.state = 603
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 604
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLY) | (1 << D96Parser.DIVIDE) | (1 << D96Parser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 605
                    self.op5() 
                self.state = 610
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Op5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def op5(self):
            return self.getTypedRuleContext(D96Parser.Op5Context,0)


        def op6(self):
            return self.getTypedRuleContext(D96Parser.Op6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_op5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp5" ):
                return visitor.visitOp5(self)
            else:
                return visitor.visitChildren(self)




    def op5(self):

        localctx = D96Parser.Op5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_op5)
        try:
            self.state = 614
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 611
                self.match(D96Parser.NOT)
                self.state = 612
                self.op5()
                pass
            elif token in [D96Parser.LITERAL_BOOLEAN, D96Parser.LITERAL_INT, D96Parser.LITERAL_ZERO, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.LS, D96Parser.SUBTRACT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 613
                self.op6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBTRACT(self):
            return self.getToken(D96Parser.SUBTRACT, 0)

        def op6(self):
            return self.getTypedRuleContext(D96Parser.Op6Context,0)


        def op7(self):
            return self.getTypedRuleContext(D96Parser.Op7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_op6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp6" ):
                return visitor.visitOp6(self)
            else:
                return visitor.visitChildren(self)




    def op6(self):

        localctx = D96Parser.Op6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_op6)
        try:
            self.state = 619
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUBTRACT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 616
                self.match(D96Parser.SUBTRACT)
                self.state = 617
                self.op6()
                pass
            elif token in [D96Parser.LITERAL_BOOLEAN, D96Parser.LITERAL_INT, D96Parser.LITERAL_ZERO, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.LS, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 618
                self.op7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def op8(self):
            return self.getTypedRuleContext(D96Parser.Op8Context,0)


        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def op7(self):
            return self.getTypedRuleContext(D96Parser.Op7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_op7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp7" ):
                return visitor.visitOp7(self)
            else:
                return visitor.visitChildren(self)



    def op7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Op7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_op7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 627
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LS]:
                self.state = 622
                self.match(D96Parser.LS)
                self.state = 623
                self.op8(0)
                self.state = 624
                self.match(D96Parser.RS)
                pass
            elif token in [D96Parser.LITERAL_BOOLEAN, D96Parser.LITERAL_INT, D96Parser.LITERAL_ZERO, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.ID]:
                self.state = 626
                self.op8(0)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 636
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op7)
                    self.state = 629
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 630
                    self.match(D96Parser.LS)
                    self.state = 631
                    self.op8(0)
                    self.state = 632
                    self.match(D96Parser.RS) 
                self.state = 638
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Op8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op9(self):
            return self.getTypedRuleContext(D96Parser.Op9Context,0)


        def op8(self):
            return self.getTypedRuleContext(D96Parser.Op8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_op8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp8" ):
                return visitor.visitOp8(self)
            else:
                return visitor.visitChildren(self)



    def op8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Op8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 114
        self.enterRecursionRule(localctx, 114, self.RULE_op8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 640
            self.op9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 650
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Op8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_op8)
                    self.state = 642
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 643
                    self.match(D96Parser.DOT)
                    self.state = 646
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
                    if la_ == 1:
                        self.state = 644
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 645
                        self.funcall()
                        pass

             
                self.state = 652
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Op9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def static_method(self):
            return self.getTypedRuleContext(D96Parser.Static_methodContext,0)


        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def op10(self):
            return self.getTypedRuleContext(D96Parser.Op10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_op9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp9" ):
                return visitor.visitOp9(self)
            else:
                return visitor.visitChildren(self)




    def op9(self):

        localctx = D96Parser.Op9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_op9)
        self._la = 0 # Token type
        try:
            self.state = 660
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 653
                _la = self._input.LA(1)
                if not(_la==D96Parser.SELF or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 654
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 657
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                if la_ == 1:
                    self.state = 655
                    self.static_method()
                    pass

                elif la_ == 2:
                    self.state = 656
                    self.match(D96Parser.DOLLAR_ID)
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 659
                self.op10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def operands(self):
            return self.getTypedRuleContext(D96Parser.OperandsContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_of_expr(self):
            return self.getTypedRuleContext(D96Parser.List_of_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_op10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp10" ):
                return visitor.visitOp10(self)
            else:
                return visitor.visitChildren(self)




    def op10(self):

        localctx = D96Parser.Op10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_op10)
        self._la = 0 # Token type
        try:
            self.state = 671
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 662
                self.match(D96Parser.NEW)
                self.state = 663
                self.operands()
                self.state = 664
                self.match(D96Parser.LB)
                self.state = 666
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_ZERO) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.LS) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.ID:
                    self.state = 665
                    self.list_of_expr()


                self.state = 668
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.LITERAL_BOOLEAN, D96Parser.LITERAL_INT, D96Parser.LITERAL_ZERO, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING, D96Parser.NULL, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 670
                self.operands()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def op(self):
            return self.getTypedRuleContext(D96Parser.OpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def literal_array(self):
            return self.getTypedRuleContext(D96Parser.Literal_arrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_operands)
        try:
            self.state = 682
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LITERAL_BOOLEAN, D96Parser.LITERAL_INT, D96Parser.LITERAL_ZERO, D96Parser.LITERAL_FLOAT, D96Parser.LITERAL_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 673
                self.literal()
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 674
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 675
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 676
                self.match(D96Parser.LB)
                self.state = 677
                self.op()
                self.state = 678
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 680
                self.match(D96Parser.NULL)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 681
                self.literal_array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_ops(self):
            return self.getTypedRuleContext(D96Parser.Index_opsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_element_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_expr" ):
                return visitor.visitElement_expr(self)
            else:
                return visitor.visitChildren(self)




    def element_expr(self):

        localctx = D96Parser.Element_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_element_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 684
            self.index_ops(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_opsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def all_expr(self):
            return self.getTypedRuleContext(D96Parser.All_exprContext,0)


        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def index_ops(self):
            return self.getTypedRuleContext(D96Parser.Index_opsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_ops

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_ops" ):
                return visitor.visitIndex_ops(self)
            else:
                return visitor.visitChildren(self)



    def index_ops(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Index_opsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 124
        self.enterRecursionRule(localctx, 124, self.RULE_index_ops, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 687
            self.match(D96Parser.LS)
            self.state = 688
            self.all_expr()
            self.state = 689
            self.match(D96Parser.RS)
            self._ctx.stop = self._input.LT(-1)
            self.state = 698
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,65,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_opsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_ops)
                    self.state = 691
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 692
                    self.match(D96Parser.LS)
                    self.state = 693
                    self.all_expr()
                    self.state = 694
                    self.match(D96Parser.RS) 
                self.state = 700
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,65,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Static_member_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def static_method(self):
            return self.getTypedRuleContext(D96Parser.Static_methodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_member_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_member_access" ):
                return visitor.visitStatic_member_access(self)
            else:
                return visitor.visitChildren(self)




    def static_member_access(self):

        localctx = D96Parser.Static_member_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_static_member_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 701
            _la = self._input.LA(1)
            if not(_la==D96Parser.SELF or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 702
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 705
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.state = 703
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 2:
                self.state = 704
                self.static_method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_of_expr(self):
            return self.getTypedRuleContext(D96Parser.List_of_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method" ):
                return visitor.visitStatic_method(self)
            else:
                return visitor.visitChildren(self)




    def static_method(self):

        localctx = D96Parser.Static_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_static_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 707
            self.match(D96Parser.DOLLAR_ID)
            self.state = 708
            self.match(D96Parser.LB)
            self.state = 710
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_ZERO) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.LS) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.ID:
                self.state = 709
                self.list_of_expr()


            self.state = 712
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_createContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_of_expr(self):
            return self.getTypedRuleContext(D96Parser.List_of_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_object_create

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_create" ):
                return visitor.visitObject_create(self)
            else:
                return visitor.visitChildren(self)




    def object_create(self):

        localctx = D96Parser.Object_createContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_object_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 714
            self.match(D96Parser.NEW)
            self.state = 715
            self.match(D96Parser.ID)
            self.state = 716
            self.match(D96Parser.LB)
            self.state = 718
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_ZERO) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.LS) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.ID:
                self.state = 717
                self.list_of_expr()


            self.state = 720
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.OpContext)
            else:
                return self.getTypedRuleContext(D96Parser.OpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_list_of_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_expr" ):
                return visitor.visitList_of_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_of_expr(self):

        localctx = D96Parser.List_of_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_list_of_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 722
            self.op()
            self.state = 727
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 723
                self.match(D96Parser.COMMA)
                self.state = 724
                self.op()
                self.state = 729
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LITERAL_INT(self):
            return self.getToken(D96Parser.LITERAL_INT, 0)

        def LITERAL_FLOAT(self):
            return self.getToken(D96Parser.LITERAL_FLOAT, 0)

        def LITERAL_STRING(self):
            return self.getToken(D96Parser.LITERAL_STRING, 0)

        def LITERAL_BOOLEAN(self):
            return self.getToken(D96Parser.LITERAL_BOOLEAN, 0)

        def LITERAL_ZERO(self):
            return self.getToken(D96Parser.LITERAL_ZERO, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 730
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_ZERO) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_idx_array(self):
            return self.getTypedRuleContext(D96Parser.Literal_idx_arrayContext,0)


        def literal_mtd_array(self):
            return self.getTypedRuleContext(D96Parser.Literal_mtd_arrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_array" ):
                return visitor.visitLiteral_array(self)
            else:
                return visitor.visitChildren(self)




    def literal_array(self):

        localctx = D96Parser.Literal_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_literal_array)
        try:
            self.state = 734
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 732
                self.literal_idx_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 733
                self.literal_mtd_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_idx_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def array_element(self):
            return self.getTypedRuleContext(D96Parser.Array_elementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal_idx_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_idx_array" ):
                return visitor.visitLiteral_idx_array(self)
            else:
                return visitor.visitChildren(self)




    def literal_idx_array(self):

        localctx = D96Parser.Literal_idx_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_literal_idx_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 736
            self.match(D96Parser.ARRAY)
            self.state = 737
            self.match(D96Parser.LB)
            self.state = 739
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_INT) | (1 << D96Parser.LITERAL_ZERO) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_STRING) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.LB) | (1 << D96Parser.LS) | (1 << D96Parser.SUBTRACT) | (1 << D96Parser.NOT))) != 0) or _la==D96Parser.ID:
                self.state = 738
                self.array_element()


            self.state = 741
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_mtd_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def literal_idx_array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Literal_idx_arrayContext)
            else:
                return self.getTypedRuleContext(D96Parser.Literal_idx_arrayContext,i)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_literal_mtd_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_mtd_array" ):
                return visitor.visitLiteral_mtd_array(self)
            else:
                return visitor.visitChildren(self)




    def literal_mtd_array(self):

        localctx = D96Parser.Literal_mtd_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_literal_mtd_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 743
            self.match(D96Parser.ARRAY)
            self.state = 744
            self.match(D96Parser.LB)
            self.state = 745
            self.literal_idx_array()
            self.state = 750
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 746
                self.match(D96Parser.COMMA)
                self.state = 747
                self.literal_idx_array()
                self.state = 752
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 753
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.All_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.All_exprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element" ):
                return visitor.visitArray_element(self)
            else:
                return visitor.visitChildren(self)




    def array_element(self):

        localctx = D96Parser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_array_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 755
            self.all_expr()
            self.state = 760
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 756
                self.match(D96Parser.COMMA)
                self.state = 757
                self.all_expr()
                self.state = 762
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[37] = self.scalar_variable_sempred
        self._predicates[45] = self.method_invoc_literal_sempred
        self._predicates[51] = self.op2_sempred
        self._predicates[52] = self.op3_sempred
        self._predicates[53] = self.op4_sempred
        self._predicates[56] = self.op7_sempred
        self._predicates[57] = self.op8_sempred
        self._predicates[62] = self.index_ops_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def scalar_variable_sempred(self, localctx:Scalar_variableContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

    def method_invoc_literal_sempred(self, localctx:Method_invoc_literalContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

    def op2_sempred(self, localctx:Op2Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def op3_sempred(self, localctx:Op3Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def op4_sempred(self, localctx:Op4Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def op7_sempred(self, localctx:Op7Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

    def op8_sempred(self, localctx:Op8Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def index_ops_sempred(self, localctx:Index_opsContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




