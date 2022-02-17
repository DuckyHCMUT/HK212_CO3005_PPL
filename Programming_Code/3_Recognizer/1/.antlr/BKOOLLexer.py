# Generated from d:\HCMUT\Semester 212\Principles of Programming Languages\HK212_CO3005_PPL\Quiz\3_Recognizer\1\BKOOL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("P\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\6\4\60\n\4\r\4\16\4\61\3\5\6")
        buf.write("\5\65\n\5\r\5\16\5\66\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\13\6\13D\n\13\r\13\16\13E\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\3\2\5\4\2C\\c|")
        buf.write("\3\2\62;\5\2\13\f\17\17\"\"\2R\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5%\3\2\2")
        buf.write("\2\7/\3\2\2\2\t\64\3\2\2\2\138\3\2\2\2\r:\3\2\2\2\17<")
        buf.write("\3\2\2\2\21>\3\2\2\2\23@\3\2\2\2\25C\3\2\2\2\27I\3\2\2")
        buf.write("\2\31L\3\2\2\2\33N\3\2\2\2\35\36\7x\2\2\36\37\7c\2\2\37")
        buf.write(" \7t\2\2 !\7f\2\2!\"\7g\2\2\"#\7e\2\2#$\7n\2\2$\4\3\2")
        buf.write("\2\2%&\7h\2\2&\'\7w\2\2\'(\7p\2\2()\7e\2\2)*\7f\2\2*+")
        buf.write("\7g\2\2+,\7e\2\2,-\7n\2\2-\6\3\2\2\2.\60\t\2\2\2/.\3\2")
        buf.write("\2\2\60\61\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\b\3\2")
        buf.write("\2\2\63\65\t\3\2\2\64\63\3\2\2\2\65\66\3\2\2\2\66\64\3")
        buf.write("\2\2\2\66\67\3\2\2\2\67\n\3\2\2\289\7*\2\29\f\3\2\2\2")
        buf.write(":;\7+\2\2;\16\3\2\2\2<=\7}\2\2=\20\3\2\2\2>?\7\177\2\2")
        buf.write("?\22\3\2\2\2@A\7=\2\2A\24\3\2\2\2BD\t\4\2\2CB\3\2\2\2")
        buf.write("DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2FG\3\2\2\2GH\b\13\2\2H\26")
        buf.write("\3\2\2\2IJ\13\2\2\2JK\b\f\3\2K\30\3\2\2\2LM\13\2\2\2M")
        buf.write("\32\3\2\2\2NO\13\2\2\2O\34\3\2\2\2\6\2\61\66E\4\b\2\2")
        buf.write("\3\f\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    ID = 3
    INTLIT = 4
    LB = 5
    RB = 6
    LP = 7
    RP = 8
    SEMI = 9
    WS = 10
    ERROR_CHAR = 11
    UNCLOSE_STRING = 12
    ILLEGAL_ESCAPE = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'vardecl'", "'funcdecl'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INTLIT", "LB", "RB", "LP", "RP", "SEMI", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "ID", "INTLIT", "LB", "RB", "LP", "RP", 
                  "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[10] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


