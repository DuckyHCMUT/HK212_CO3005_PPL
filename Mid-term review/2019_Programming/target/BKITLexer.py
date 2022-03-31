# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("o\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\t\7\t9\n\t\f\t\16\t<\13\t\5\t>\n\t\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\5\fO\n\f\3\r\3\r\3\r\3\r\5\rU\n\r\3\16\3\16\3\16")
        buf.write("\3\16\5\16[\n\16\3\16\3\16\3\16\3\17\3\17\3\20\6\20c\n")
        buf.write("\20\r\20\16\20d\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\2\2\24\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\2\31\2\33\2\35\2\37\r!\16#\17%\20\3\2\r\3\2\63")
        buf.write(";\3\2\62;\3\2c|\6\2\62;C\\aac|\3\2\62\62\3\2\63\64\3\2")
        buf.write("\65\65\3\2\62\63\3\2\63\63\3\2\62\64\4\2\13\f\"\"\2q\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\3\'\3\2\2\2\5)\3\2\2\2\7+\3\2\2\2\t-\3\2\2\2")
        buf.write("\13/\3\2\2\2\r\61\3\2\2\2\17\63\3\2\2\2\21=\3\2\2\2\23")
        buf.write("?\3\2\2\2\25B\3\2\2\2\27N\3\2\2\2\31T\3\2\2\2\33Z\3\2")
        buf.write("\2\2\35_\3\2\2\2\37b\3\2\2\2!h\3\2\2\2#k\3\2\2\2%m\3\2")
        buf.write("\2\2\'(\7A\2\2(\4\3\2\2\2)*\7`\2\2*\6\3\2\2\2+,\7B\2\2")
        buf.write(",\b\3\2\2\2-.\7*\2\2.\n\3\2\2\2/\60\7+\2\2\60\f\3\2\2")
        buf.write("\2\61\62\7]\2\2\62\16\3\2\2\2\63\64\7_\2\2\64\20\3\2\2")
        buf.write("\2\65>\7\62\2\2\66:\t\2\2\2\679\t\3\2\28\67\3\2\2\29<")
        buf.write("\3\2\2\2:8\3\2\2\2:;\3\2\2\2;>\3\2\2\2<:\3\2\2\2=\65\3")
        buf.write("\2\2\2=\66\3\2\2\2>\22\3\2\2\2?@\t\4\2\2@A\t\5\2\2A\24")
        buf.write("\3\2\2\2BC\5\27\f\2CD\5\35\17\2DE\5\31\r\2EF\5\35\17\2")
        buf.write("FG\5\33\16\2G\26\3\2\2\2HI\t\6\2\2IO\t\2\2\2JK\t\7\2\2")
        buf.write("KO\t\3\2\2LM\t\b\2\2MO\t\t\2\2NH\3\2\2\2NJ\3\2\2\2NL\3")
        buf.write("\2\2\2O\30\3\2\2\2PQ\t\6\2\2QU\t\2\2\2RS\t\n\2\2SU\t\13")
        buf.write("\2\2TP\3\2\2\2TR\3\2\2\2U\32\3\2\2\2VW\7\63\2\2W[\7;\2")
        buf.write("\2XY\7\64\2\2Y[\7\62\2\2ZV\3\2\2\2ZX\3\2\2\2[\\\3\2\2")
        buf.write("\2\\]\t\3\2\2]^\t\3\2\2^\34\3\2\2\2_`\7\61\2\2`\36\3\2")
        buf.write("\2\2ac\t\f\2\2ba\3\2\2\2cd\3\2\2\2db\3\2\2\2de\3\2\2\2")
        buf.write("ef\3\2\2\2fg\b\20\2\2g \3\2\2\2hi\13\2\2\2ij\b\21\3\2")
        buf.write("j\"\3\2\2\2kl\13\2\2\2l$\3\2\2\2mn\13\2\2\2n&\3\2\2\2")
        buf.write("\t\2:=NTZd\4\b\2\2\3\21\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    LP = 4
    RP = 5
    LB = 6
    RB = 7
    INT = 8
    ID = 9
    DATE = 10
    WS = 11
    ERROR_CHAR = 12
    UNCLOSE_STRING = 13
    ILLEGAL_ESCAPE = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'?'", "'^'", "'@'", "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "LP", "RP", "LB", "RB", "INT", "ID", "DATE", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "LP", "RP", "LB", "RB", "INT", 
                  "ID", "DATE", "DAY", "MONTH", "YEAR", "DASH", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[15] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


