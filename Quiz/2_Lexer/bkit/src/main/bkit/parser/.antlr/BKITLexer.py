# Generated from d:\HCMUT\Semester 212\Principles of Programming Languages\1_Lexer_Exercise\bkit\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("\60\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\5\4\32\n\4")
        buf.write("\7\4\34\n\4\f\4\16\4\37\13\4\5\4!\n\4\3\5\6\5$\n\5\r\5")
        buf.write("\16\5%\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\b\3\b\2\2\t\3\2\5")
        buf.write("\2\7\3\t\4\13\5\r\6\17\7\3\2\6\4\2\62;aa\3\2\63;\3\2\62")
        buf.write("\62\5\2\13\f\17\17\"\"\2\62\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\3\21\3\2\2\2\5\23")
        buf.write("\3\2\2\2\7 \3\2\2\2\t#\3\2\2\2\13)\3\2\2\2\r,\3\2\2\2")
        buf.write("\17.\3\2\2\2\21\22\t\2\2\2\22\4\3\2\2\2\23\24\t\3\2\2")
        buf.write("\24\6\3\2\2\2\25!\t\4\2\2\26\35\5\5\3\2\27\34\5\3\2\2")
        buf.write("\30\32\7a\2\2\31\30\3\2\2\2\31\32\3\2\2\2\32\34\3\2\2")
        buf.write("\2\33\27\3\2\2\2\33\31\3\2\2\2\34\37\3\2\2\2\35\33\3\2")
        buf.write("\2\2\35\36\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2 \25\3\2\2")
        buf.write("\2 \26\3\2\2\2!\b\3\2\2\2\"$\t\5\2\2#\"\3\2\2\2$%\3\2")
        buf.write("\2\2%#\3\2\2\2%&\3\2\2\2&\'\3\2\2\2\'(\b\5\2\2(\n\3\2")
        buf.write("\2\2)*\13\2\2\2*+\b\6\3\2+\f\3\2\2\2,-\13\2\2\2-\16\3")
        buf.write("\2\2\2./\13\2\2\2/\20\3\2\2\2\b\2\31\33\35 %\4\b\2\2\3")
        buf.write("\6\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PHP_DIGIT = 1
    WS = 2
    ERROR_CHAR = 3
    UNCLOSE_STRING = 4
    ILLEGAL_ESCAPE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "PHP_DIGIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "DIGIT", "NATURAL_DIGIT", "PHP_DIGIT", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[4] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


