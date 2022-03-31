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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("J\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\t\7\t/\n\t\f\t\16\t\62\13\t\5\t\64")
        buf.write("\n\t\3\n\3\n\7\n8\n\n\f\n\16\n;\13\n\3\13\6\13>\n\13\r")
        buf.write("\13\16\13?\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16\2\2")
        buf.write("\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\3\2\7\3\2\63;\3\2\62;\3\2c|\6\2\62;C\\aa")
        buf.write("c|\4\2\13\f\"\"\2M\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\37\3\2\2\2\7!\3\2\2")
        buf.write("\2\t#\3\2\2\2\13%\3\2\2\2\r\'\3\2\2\2\17)\3\2\2\2\21\63")
        buf.write("\3\2\2\2\23\65\3\2\2\2\25=\3\2\2\2\27C\3\2\2\2\31F\3\2")
        buf.write("\2\2\33H\3\2\2\2\35\36\7A\2\2\36\4\3\2\2\2\37 \7`\2\2")
        buf.write(" \6\3\2\2\2!\"\7B\2\2\"\b\3\2\2\2#$\7*\2\2$\n\3\2\2\2")
        buf.write("%&\7+\2\2&\f\3\2\2\2\'(\7]\2\2(\16\3\2\2\2)*\7_\2\2*\20")
        buf.write("\3\2\2\2+\64\7\62\2\2,\60\t\2\2\2-/\t\3\2\2.-\3\2\2\2")
        buf.write("/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\64\3\2\2\2\62")
        buf.write("\60\3\2\2\2\63+\3\2\2\2\63,\3\2\2\2\64\22\3\2\2\2\659")
        buf.write("\t\4\2\2\668\t\5\2\2\67\66\3\2\2\28;\3\2\2\29\67\3\2\2")
        buf.write("\29:\3\2\2\2:\24\3\2\2\2;9\3\2\2\2<>\t\6\2\2=<\3\2\2\2")
        buf.write(">?\3\2\2\2?=\3\2\2\2?@\3\2\2\2@A\3\2\2\2AB\b\13\2\2B\26")
        buf.write("\3\2\2\2CD\13\2\2\2DE\b\f\3\2E\30\3\2\2\2FG\13\2\2\2G")
        buf.write("\32\3\2\2\2HI\13\2\2\2I\34\3\2\2\2\7\2\60\639?\4\b\2\2")
        buf.write("\3\f\2")
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
    WS = 10
    ERROR_CHAR = 11
    UNCLOSE_STRING = 12
    ILLEGAL_ESCAPE = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'?'", "'^'", "'@'", "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "LP", "RP", "LB", "RB", "INT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "LP", "RP", "LB", "RB", "INT", 
                  "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
     


