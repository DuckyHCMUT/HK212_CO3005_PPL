# Generated from d:\HCMUT\Semester 212\Principles of Programming Languages\HK212_CO3005_PPL\Quiz\3_Recognizer\exercises\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\32")
        buf.write("\u0088\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\5\4?\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\5\13T\n\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\7\f\\\n\f\f\f\16\f_\13\f\5\fa\n\f\3")
        buf.write("\r\6\rd\n\r\r\r\16\re\3\16\6\16i\n\16\r\16\16\16j\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\6\26|\n\26\r\26\16\26}\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\2\2\32\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\3\2\6\3")
        buf.write("\2\63;\3\2\62;\4\2C\\c|\5\2\13\f\17\17\"\"\2\u008e\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\3\63\3\2\2\2\5:\3\2\2\2\7>\3\2")
        buf.write("\2\2\t@\3\2\2\2\13D\3\2\2\2\rJ\3\2\2\2\17L\3\2\2\2\21")
        buf.write("N\3\2\2\2\23P\3\2\2\2\25S\3\2\2\2\27`\3\2\2\2\31c\3\2")
        buf.write("\2\2\33h\3\2\2\2\35l\3\2\2\2\37n\3\2\2\2!p\3\2\2\2#r\3")
        buf.write("\2\2\2%t\3\2\2\2\'v\3\2\2\2)x\3\2\2\2+{\3\2\2\2-\u0081")
        buf.write("\3\2\2\2/\u0084\3\2\2\2\61\u0086\3\2\2\2\63\64\7t\2\2")
        buf.write("\64\65\7g\2\2\65\66\7v\2\2\66\67\7w\2\2\678\7t\2\289\7")
        buf.write("p\2\29\4\3\2\2\2:;\7?\2\2;\6\3\2\2\2<?\5\t\5\2=?\5\13")
        buf.write("\6\2><\3\2\2\2>=\3\2\2\2?\b\3\2\2\2@A\7k\2\2AB\7p\2\2")
        buf.write("BC\7v\2\2C\n\3\2\2\2DE\7h\2\2EF\7n\2\2FG\7q\2\2GH\7c\2")
        buf.write("\2HI\7v\2\2I\f\3\2\2\2JK\7-\2\2K\16\3\2\2\2LM\7/\2\2M")
        buf.write("\20\3\2\2\2NO\7,\2\2O\22\3\2\2\2PQ\7\61\2\2Q\24\3\2\2")
        buf.write("\2RT\5\27\f\2SR\3\2\2\2ST\3\2\2\2TU\3\2\2\2UV\5)\25\2")
        buf.write("VW\5\31\r\2W\26\3\2\2\2Xa\7\62\2\2Y]\t\2\2\2Z\\\t\3\2")
        buf.write("\2[Z\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^a\3\2\2\2")
        buf.write("_]\3\2\2\2`X\3\2\2\2`Y\3\2\2\2a\30\3\2\2\2bd\t\3\2\2c")
        buf.write("b\3\2\2\2de\3\2\2\2ec\3\2\2\2ef\3\2\2\2f\32\3\2\2\2gi")
        buf.write("\t\4\2\2hg\3\2\2\2ij\3\2\2\2jh\3\2\2\2jk\3\2\2\2k\34\3")
        buf.write("\2\2\2lm\7*\2\2m\36\3\2\2\2no\7+\2\2o \3\2\2\2pq\7}\2")
        buf.write("\2q\"\3\2\2\2rs\7\177\2\2s$\3\2\2\2tu\7=\2\2u&\3\2\2\2")
        buf.write("vw\7.\2\2w(\3\2\2\2xy\7\60\2\2y*\3\2\2\2z|\t\5\2\2{z\3")
        buf.write("\2\2\2|}\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\177\3\2\2\2\177")
        buf.write("\u0080\b\26\2\2\u0080,\3\2\2\2\u0081\u0082\13\2\2\2\u0082")
        buf.write("\u0083\b\27\3\2\u0083.\3\2\2\2\u0084\u0085\13\2\2\2\u0085")
        buf.write("\60\3\2\2\2\u0086\u0087\13\2\2\2\u0087\62\3\2\2\2\n\2")
        buf.write(">S]`ej}\4\b\2\2\3\27\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    DATA_TYPE = 3
    INT = 4
    FLOAT = 5
    ADD = 6
    SUBTRACT = 7
    MULTIPLY = 8
    DIVISION = 9
    FLOAT_LITERAL = 10
    INTEGER_LITERAL = 11
    INTLIT = 12
    ID = 13
    LB = 14
    RB = 15
    LP = 16
    RP = 17
    SEMI = 18
    COMMA = 19
    DOT = 20
    WS = 21
    ERROR_CHAR = 22
    UNCLOSE_STRING = 23
    ILLEGAL_ESCAPE = 24

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'='", "'int'", "'float'", "'+'", "'-'", "'*'", 
            "'/'", "'('", "')'", "'{'", "'}'", "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "DATA_TYPE", "INT", "FLOAT", "ADD", "SUBTRACT", "MULTIPLY", 
            "DIVISION", "FLOAT_LITERAL", "INTEGER_LITERAL", "INTLIT", "ID", 
            "LB", "RB", "LP", "RP", "SEMI", "COMMA", "DOT", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "DATA_TYPE", "INT", "FLOAT", "ADD", "SUBTRACT", 
                  "MULTIPLY", "DIVISION", "FLOAT_LITERAL", "INTEGER_LITERAL", 
                  "INTLIT", "ID", "LB", "RB", "LP", "RP", "SEMI", "COMMA", 
                  "DOT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[21] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


