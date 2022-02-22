# Generated from main/mp/parser/MP.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\5\3\5\3\6\6\6 \n\6\r\6\16\6!\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\6\t\62\n\t\r\t\16\t\63")
        buf.write("\3\t\3\t\3\n\3\n\2\2\13\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\3\2\4\3\2\62;\5\2\13\f\17\17\"\"\2:\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\3\25\3\2\2\2\5\27\3\2\2\2\7\32\3\2\2\2\t\34\3\2\2\2\13")
        buf.write("\37\3\2\2\2\r#\3\2\2\2\17+\3\2\2\2\21\61\3\2\2\2\23\67")
        buf.write("\3\2\2\2\25\26\7]\2\2\26\4\3\2\2\2\27\30\7\60\2\2\30\31")
        buf.write("\7\60\2\2\31\6\3\2\2\2\32\33\7_\2\2\33\b\3\2\2\2\34\35")
        buf.write("\7/\2\2\35\n\3\2\2\2\36 \t\2\2\2\37\36\3\2\2\2 !\3\2\2")
        buf.write("\2!\37\3\2\2\2!\"\3\2\2\2\"\f\3\2\2\2#$\7k\2\2$%\7p\2")
        buf.write("\2%&\7v\2\2&\'\7g\2\2\'(\7i\2\2()\7g\2\2)*\7t\2\2*\16")
        buf.write("\3\2\2\2+,\7t\2\2,-\7g\2\2-.\7c\2\2./\7n\2\2/\20\3\2\2")
        buf.write("\2\60\62\t\3\2\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61\3\2")
        buf.write("\2\2\63\64\3\2\2\2\64\65\3\2\2\2\65\66\b\t\2\2\66\22\3")
        buf.write("\2\2\2\678\13\2\2\28\24\3\2\2\2\5\2!\63\3\b\2\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    INTLIT = 5
    INTTYPE = 6
    FLOATTYPE = 7
    WS = 8
    ERROR_CHAR = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "'..'", "']'", "'-'", "'integer'", "'real'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "INTTYPE", "FLOATTYPE", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "INTLIT", "INTTYPE", "FLOATTYPE", 
                  "WS", "ERROR_CHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


