# Generated from d:\HCMUT\Semester 212\Principles of Programming Languages\HK212_CO3005_PPL\Quiz\3_Recognizer\2\BKOOL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("Z\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\5\3+\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\6\68\n\6\r\6\16\69\3\7\6\7=\n\7\r\7\16\7>\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\6\16N\n\16\r\16\16\16O\3\16\3\16\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\21\3\21\2\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22\3\2\5\4")
        buf.write("\2C\\c|\3\2\62;\5\2\13\f\17\17\"\"\2]\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5*\3\2\2\2\7,\3\2")
        buf.write("\2\2\t\60\3\2\2\2\13\67\3\2\2\2\r<\3\2\2\2\17@\3\2\2\2")
        buf.write("\21B\3\2\2\2\23D\3\2\2\2\25F\3\2\2\2\27H\3\2\2\2\31J\3")
        buf.write("\2\2\2\33M\3\2\2\2\35S\3\2\2\2\37V\3\2\2\2!X\3\2\2\2#")
        buf.write("$\7d\2\2$%\7q\2\2%&\7f\2\2&\'\7{\2\2\'\4\3\2\2\2(+\5\7")
        buf.write("\4\2)+\5\t\5\2*(\3\2\2\2*)\3\2\2\2+\6\3\2\2\2,-\7k\2\2")
        buf.write("-.\7p\2\2./\7v\2\2/\b\3\2\2\2\60\61\7h\2\2\61\62\7n\2")
        buf.write("\2\62\63\7q\2\2\63\64\7c\2\2\64\65\7v\2\2\65\n\3\2\2\2")
        buf.write("\668\t\2\2\2\67\66\3\2\2\289\3\2\2\29\67\3\2\2\29:\3\2")
        buf.write("\2\2:\f\3\2\2\2;=\t\3\2\2<;\3\2\2\2=>\3\2\2\2><\3\2\2")
        buf.write("\2>?\3\2\2\2?\16\3\2\2\2@A\7*\2\2A\20\3\2\2\2BC\7+\2\2")
        buf.write("C\22\3\2\2\2DE\7}\2\2E\24\3\2\2\2FG\7\177\2\2G\26\3\2")
        buf.write("\2\2HI\7=\2\2I\30\3\2\2\2JK\7.\2\2K\32\3\2\2\2LN\t\4\2")
        buf.write("\2ML\3\2\2\2NO\3\2\2\2OM\3\2\2\2OP\3\2\2\2PQ\3\2\2\2Q")
        buf.write("R\b\16\2\2R\34\3\2\2\2ST\13\2\2\2TU\b\17\3\2U\36\3\2\2")
        buf.write("\2VW\13\2\2\2W \3\2\2\2XY\13\2\2\2Y\"\3\2\2\2\7\2*9>O")
        buf.write("\4\b\2\2\3\17\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    DATA_TYPE = 2
    INT = 3
    FLOAT = 4
    ID = 5
    INTLIT = 6
    LB = 7
    RB = 8
    LP = 9
    RP = 10
    SEMI = 11
    COMMA = 12
    WS = 13
    ERROR_CHAR = 14
    UNCLOSE_STRING = 15
    ILLEGAL_ESCAPE = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'body'", "'int'", "'float'", "'('", "')'", "'{'", "'}'", "';'", 
            "','" ]

    symbolicNames = [ "<INVALID>",
            "DATA_TYPE", "INT", "FLOAT", "ID", "INTLIT", "LB", "RB", "LP", 
            "RP", "SEMI", "COMMA", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "DATA_TYPE", "INT", "FLOAT", "ID", "INTLIT", "LB", 
                  "RB", "LP", "RP", "SEMI", "COMMA", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[13] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


