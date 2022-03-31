# Generated from d:\HCMUT\Semester 212\Principles of Programming Languages\Mid-term review\Mid term VNese\Coding\2019_Theory\AST\src\main\mp\parser\MP.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("@\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\7\7/\n\7\f\7\16\7\62\13\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\6\n9\n\n\r\n\16\n:\3\n\3\n\3\13\3\13\2\2\f")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\3\2\5\3")
        buf.write("\2c|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2A\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\3\27\3\2\2\2\5\36\3\2\2\2\7\"\3\2\2\2\t(\3\2\2")
        buf.write("\2\13*\3\2\2\2\r,\3\2\2\2\17\63\3\2\2\2\21\65\3\2\2\2")
        buf.write("\238\3\2\2\2\25>\3\2\2\2\27\30\7u\2\2\30\31\7v\2\2\31")
        buf.write("\32\7t\2\2\32\33\7w\2\2\33\34\7e\2\2\34\35\7v\2\2\35\4")
        buf.write("\3\2\2\2\36\37\7k\2\2\37 \7p\2\2 !\7v\2\2!\6\3\2\2\2\"")
        buf.write("#\7h\2\2#$\7n\2\2$%\7q\2\2%&\7c\2\2&\'\7v\2\2\'\b\3\2")
        buf.write("\2\2()\7}\2\2)\n\3\2\2\2*+\7\177\2\2+\f\3\2\2\2,\60\t")
        buf.write("\2\2\2-/\t\3\2\2.-\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60")
        buf.write("\61\3\2\2\2\61\16\3\2\2\2\62\60\3\2\2\2\63\64\7.\2\2\64")
        buf.write("\20\3\2\2\2\65\66\7=\2\2\66\22\3\2\2\2\679\t\4\2\28\67")
        buf.write("\3\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2;<\3\2\2\2<=\b\n")
        buf.write("\2\2=\24\3\2\2\2>?\13\2\2\2?\26\3\2\2\2\5\2\60:\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STRUCT = 1
    INTTYPE = 2
    FLOATTYPE = 3
    LB = 4
    RB = 5
    ID = 6
    COMMA = 7
    SEMI = 8
    WS = 9
    ERROR_CHAR = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'struct'", "'int'", "'float'", "'{'", "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "STRUCT", "INTTYPE", "FLOATTYPE", "LB", "RB", "ID", "COMMA", 
            "SEMI", "WS", "ERROR_CHAR" ]

    ruleNames = [ "STRUCT", "INTTYPE", "FLOATTYPE", "LB", "RB", "ID", "COMMA", 
                  "SEMI", "WS", "ERROR_CHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


