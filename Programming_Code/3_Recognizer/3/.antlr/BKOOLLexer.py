# Generated from d:\HCMUT\Semester 212\Principles of Programming Languages\HK212_CO3005_PPL\Quiz\3_Recognizer\3\BKOOL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("k\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\5\5:\n\5\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\6\bG\n\b\r\b\16\bH\3\t\6\tL\n\t\r")
        buf.write("\t\16\tM\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3")
        buf.write("\17\3\17\3\20\3\20\3\21\6\21_\n\21\r\21\16\21`\3\21\3")
        buf.write("\21\3\22\3\22\3\22\3\23\3\23\3\24\3\24\2\2\25\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25\3\2\5\3\2\62;\4\2C\\c|\5")
        buf.write("\2\13\f\17\17\"\"\2n\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3)\3\2\2\2\5\60")
        buf.write("\3\2\2\2\7\62\3\2\2\2\t9\3\2\2\2\13;\3\2\2\2\r?\3\2\2")
        buf.write("\2\17F\3\2\2\2\21K\3\2\2\2\23O\3\2\2\2\25Q\3\2\2\2\27")
        buf.write("S\3\2\2\2\31U\3\2\2\2\33W\3\2\2\2\35Y\3\2\2\2\37[\3\2")
        buf.write("\2\2!^\3\2\2\2#d\3\2\2\2%g\3\2\2\2\'i\3\2\2\2)*\7t\2\2")
        buf.write("*+\7g\2\2+,\7v\2\2,-\7w\2\2-.\7t\2\2./\7p\2\2/\4\3\2\2")
        buf.write("\2\60\61\7?\2\2\61\6\3\2\2\2\62\63\7g\2\2\63\64\7z\2\2")
        buf.write("\64\65\7r\2\2\65\66\7t\2\2\66\b\3\2\2\2\67:\5\13\6\28")
        buf.write(":\5\r\7\29\67\3\2\2\298\3\2\2\2:\n\3\2\2\2;<\7k\2\2<=")
        buf.write("\7p\2\2=>\7v\2\2>\f\3\2\2\2?@\7h\2\2@A\7n\2\2AB\7q\2\2")
        buf.write("BC\7c\2\2CD\7v\2\2D\16\3\2\2\2EG\t\2\2\2FE\3\2\2\2GH\3")
        buf.write("\2\2\2HF\3\2\2\2HI\3\2\2\2I\20\3\2\2\2JL\t\3\2\2KJ\3\2")
        buf.write("\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2N\22\3\2\2\2OP\7*\2")
        buf.write("\2P\24\3\2\2\2QR\7+\2\2R\26\3\2\2\2ST\7}\2\2T\30\3\2\2")
        buf.write("\2UV\7\177\2\2V\32\3\2\2\2WX\7=\2\2X\34\3\2\2\2YZ\7.\2")
        buf.write("\2Z\36\3\2\2\2[\\\7\60\2\2\\ \3\2\2\2]_\t\4\2\2^]\3\2")
        buf.write("\2\2_`\3\2\2\2`^\3\2\2\2`a\3\2\2\2ab\3\2\2\2bc\b\21\2")
        buf.write("\2c\"\3\2\2\2de\13\2\2\2ef\b\22\3\2f$\3\2\2\2gh\13\2\2")
        buf.write("\2h&\3\2\2\2ij\13\2\2\2j(\3\2\2\2\7\29HM`\4\b\2\2\3\22")
        buf.write("\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    DATA_TYPE = 4
    INT = 5
    FLOAT = 6
    INTLIT = 7
    ID = 8
    LB = 9
    RB = 10
    LP = 11
    RP = 12
    SEMI = 13
    COMMA = 14
    DOT = 15
    WS = 16
    ERROR_CHAR = 17
    UNCLOSE_STRING = 18
    ILLEGAL_ESCAPE = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'='", "'expr'", "'int'", "'float'", "'('", "')'", 
            "'{'", "'}'", "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "DATA_TYPE", "INT", "FLOAT", "INTLIT", "ID", "LB", "RB", "LP", 
            "RP", "SEMI", "COMMA", "DOT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "DATA_TYPE", "INT", "FLOAT", "INTLIT", 
                  "ID", "LB", "RB", "LP", "RP", "SEMI", "COMMA", "DOT", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[16] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


