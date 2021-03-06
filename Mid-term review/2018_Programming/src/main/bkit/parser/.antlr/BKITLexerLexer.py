# Generated from d:\HCMUT\Semester 212\Principles of Programming Languages\1_Lexer_Exercise\bkit\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("T\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\6\5/\n\5\r\5\16\5\60\3\5\7\5\64")
        buf.write("\n\5\f\5\16\5\67\13\5\3\6\6\6:\n\6\r\6\16\6;\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\6\fI\n\f\r\f\16\f")
        buf.write("J\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\2\2\20\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\3\2\5\3\2c|\3\2\62;\5\2\13\f\17\17\"\"\2W\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\3\37\3\2\2\2\5$\3\2\2\2\7(\3\2\2\2\t.\3\2")
        buf.write("\2\2\139\3\2\2\2\r=\3\2\2\2\17?\3\2\2\2\21A\3\2\2\2\23")
        buf.write("C\3\2\2\2\25E\3\2\2\2\27H\3\2\2\2\31N\3\2\2\2\33P\3\2")
        buf.write("\2\2\35R\3\2\2\2\37 \7o\2\2 !\7c\2\2!\"\7k\2\2\"#\7p\2")
        buf.write("\2#\4\3\2\2\2$%\7k\2\2%&\7p\2\2&\'\7v\2\2\'\6\3\2\2\2")
        buf.write("()\7x\2\2)*\7q\2\2*+\7k\2\2+,\7f\2\2,\b\3\2\2\2-/\t\2")
        buf.write("\2\2.-\3\2\2\2/\60\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61")
        buf.write("\65\3\2\2\2\62\64\5\13\6\2\63\62\3\2\2\2\64\67\3\2\2\2")
        buf.write("\65\63\3\2\2\2\65\66\3\2\2\2\66\n\3\2\2\2\67\65\3\2\2")
        buf.write("\28:\t\3\2\298\3\2\2\2:;\3\2\2\2;9\3\2\2\2;<\3\2\2\2<")
        buf.write("\f\3\2\2\2=>\7*\2\2>\16\3\2\2\2?@\7+\2\2@\20\3\2\2\2A")
        buf.write("B\7}\2\2B\22\3\2\2\2CD\7\177\2\2D\24\3\2\2\2EF\7=\2\2")
        buf.write("F\26\3\2\2\2GI\t\4\2\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2J")
        buf.write("K\3\2\2\2KL\3\2\2\2LM\b\f\2\2M\30\3\2\2\2NO\13\2\2\2O")
        buf.write("\32\3\2\2\2PQ\13\2\2\2Q\34\3\2\2\2RS\13\2\2\2S\36\3\2")
        buf.write("\2\2\7\2\60\65;J\3\b\2\2")
        return buf.getvalue()


class BKITLexerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    ID = 4
    INTLIT = 5
    LB = 6
    RB = 7
    LP = 8
    RP = 9
    SEMI = 10
    WS = 11
    ERROR_CHAR = 12
    UNCLOSE_STRING = 13
    ILLEGAL_ESCAPE = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "LB", "RB", "LP", "RP", 
            "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "LB", "RB", 
                  "LP", "RP", "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


