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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("k\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\4\5\4/\n\4\3\4\3\4\3\4\7\4\64")
        buf.write("\n\4\f\4\16\4\67\13\4\5\49\n\4\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\7\fT\n\f\f\f\16\fW\13\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\16\6\16_\n\16\r\16\16\16`\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\21\3\21\2\2\22\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\2\33\16\35")
        buf.write("\17\37\20!\21\3\2\6\3\2\63;\3\2\62;\3\2$$\4\2\13\f\"\"")
        buf.write("\2o\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5\'\3\2\2\2")
        buf.write("\7.\3\2\2\2\t:\3\2\2\2\13<\3\2\2\2\rB\3\2\2\2\17E\3\2")
        buf.write("\2\2\21G\3\2\2\2\23I\3\2\2\2\25K\3\2\2\2\27N\3\2\2\2\31")
        buf.write("[\3\2\2\2\33^\3\2\2\2\35d\3\2\2\2\37g\3\2\2\2!i\3\2\2")
        buf.write("\2#$\7k\2\2$%\7p\2\2%&\7v\2\2&\4\3\2\2\2\'(\7h\2\2()\7")
        buf.write("n\2\2)*\7q\2\2*+\7c\2\2+,\7v\2\2,\6\3\2\2\2-/\5\t\5\2")
        buf.write(".-\3\2\2\2./\3\2\2\2/8\3\2\2\2\609\7\62\2\2\61\65\t\2")
        buf.write("\2\2\62\64\t\3\2\2\63\62\3\2\2\2\64\67\3\2\2\2\65\63\3")
        buf.write("\2\2\2\65\66\3\2\2\2\669\3\2\2\2\67\65\3\2\2\28\60\3\2")
        buf.write("\2\28\61\3\2\2\29\b\3\2\2\2:;\7/\2\2;\n\3\2\2\2<=\7c\2")
        buf.write("\2=>\7t\2\2>?\7t\2\2?@\7c\2\2@A\7{\2\2A\f\3\2\2\2BC\7")
        buf.write("q\2\2CD\7h\2\2D\16\3\2\2\2EF\7]\2\2F\20\3\2\2\2GH\7_\2")
        buf.write("\2H\22\3\2\2\2IJ\7.\2\2J\24\3\2\2\2KL\7\60\2\2LM\7\60")
        buf.write("\2\2M\26\3\2\2\2NO\t\4\2\2OU\t\4\2\2PQ\t\4\2\2QT\5\31")
        buf.write("\r\2RT\5\31\r\2SP\3\2\2\2SR\3\2\2\2TW\3\2\2\2US\3\2\2")
        buf.write("\2UV\3\2\2\2VX\3\2\2\2WU\3\2\2\2XY\t\4\2\2YZ\t\4\2\2Z")
        buf.write("\30\3\2\2\2[\\\n\4\2\2\\\32\3\2\2\2]_\t\5\2\2^]\3\2\2")
        buf.write("\2_`\3\2\2\2`^\3\2\2\2`a\3\2\2\2ab\3\2\2\2bc\b\16\2\2")
        buf.write("c\34\3\2\2\2de\13\2\2\2ef\b\17\3\2f\36\3\2\2\2gh\13\2")
        buf.write("\2\2h \3\2\2\2ij\13\2\2\2j\"\3\2\2\2\t\2.\658SU`\4\b\2")
        buf.write("\2\3\17\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTTYPE = 1
    FLOATTYPE = 2
    INT = 3
    SUB = 4
    ARRAY = 5
    OF = 6
    LS = 7
    RS = 8
    COMMA = 9
    DOTDOT = 10
    STRING = 11
    WS = 12
    ERROR_CHAR = 13
    UNCLOSE_STRING = 14
    ILLEGAL_ESCAPE = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'-'", "'array'", "'of'", "'['", "']'", 
            "','", "'..'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "FLOATTYPE", "INT", "SUB", "ARRAY", "OF", "LS", "RS", 
            "COMMA", "DOTDOT", "STRING", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTTYPE", "FLOATTYPE", "INT", "SUB", "ARRAY", "OF", "LS", 
                  "RS", "COMMA", "DOTDOT", "STRING", "STRING_CHAR", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
     


