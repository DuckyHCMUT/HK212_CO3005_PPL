# Generated from d:\HCMUT\Semester 212\Principles of Programming Languages\HK212_CO3005_PPL\Quiz\3_Recognizer\exercises\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32")
        buf.write("\u00a0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\6\2%\n\2\r")
        buf.write("\2\16\2&\3\2\3\2\3\3\3\3\6\3-\n\3\r\3\16\3.\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\5\4\67\n\4\3\4\3\4\3\4\3\5\3\5\6\5>\n\5")
        buf.write("\r\5\16\5?\3\5\3\5\3\5\6\5E\n\5\r\5\16\5F\7\5I\n\5\f\5")
        buf.write("\16\5L\13\5\3\6\3\6\3\6\5\6Q\n\6\3\7\3\7\3\7\7\7V\n\7")
        buf.write("\f\7\16\7Y\13\7\3\7\3\7\3\b\3\b\3\b\5\b`\n\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\5\tg\n\t\3\t\3\t\3\n\3\n\3\n\7\nn\n\n\f\n\16")
        buf.write("\nq\13\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\5\r\177\n\r\3\16\3\16\3\16\3\16\3\16\5\16\u0086")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u008e\n\17\f")
        buf.write("\17\16\17\u0091\13\17\3\20\3\20\3\20\3\20\3\20\5\20\u0098")
        buf.write("\n\20\3\21\3\21\3\21\3\21\5\21\u009e\n\21\3\21\2\3\34")
        buf.write("\22\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \2\3\3\2\n")
        buf.write("\13\2\u00a4\2$\3\2\2\2\4*\3\2\2\2\6\62\3\2\2\2\b;\3\2")
        buf.write("\2\2\nP\3\2\2\2\fR\3\2\2\2\16_\3\2\2\2\20c\3\2\2\2\22")
        buf.write("j\3\2\2\2\24r\3\2\2\2\26u\3\2\2\2\30~\3\2\2\2\32\u0085")
        buf.write("\3\2\2\2\34\u0087\3\2\2\2\36\u0097\3\2\2\2 \u009d\3\2")
        buf.write("\2\2\"%\5\4\3\2#%\5\6\4\2$\"\3\2\2\2$#\3\2\2\2%&\3\2\2")
        buf.write("\2&$\3\2\2\2&\'\3\2\2\2\'(\3\2\2\2()\7\2\2\3)\3\3\2\2")
        buf.write("\2*,\7\5\2\2+-\5\n\6\2,+\3\2\2\2-.\3\2\2\2.,\3\2\2\2.")
        buf.write("/\3\2\2\2/\60\3\2\2\2\60\61\7\24\2\2\61\5\3\2\2\2\62\63")
        buf.write("\7\5\2\2\63\64\7\17\2\2\64\66\7\20\2\2\65\67\5\b\5\2\66")
        buf.write("\65\3\2\2\2\66\67\3\2\2\2\678\3\2\2\289\7\21\2\29:\5\f")
        buf.write("\7\2:\7\3\2\2\2;=\7\5\2\2<>\5\n\6\2=<\3\2\2\2>?\3\2\2")
        buf.write("\2?=\3\2\2\2?@\3\2\2\2@J\3\2\2\2AB\7\24\2\2BD\7\5\2\2")
        buf.write("CE\5\n\6\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2GI\3")
        buf.write("\2\2\2HA\3\2\2\2IL\3\2\2\2JH\3\2\2\2JK\3\2\2\2K\t\3\2")
        buf.write("\2\2LJ\3\2\2\2MQ\7\17\2\2NO\7\25\2\2OQ\7\17\2\2PM\3\2")
        buf.write("\2\2PN\3\2\2\2Q\13\3\2\2\2RW\7\22\2\2SV\5\4\3\2TV\5\16")
        buf.write("\b\2US\3\2\2\2UT\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2")
        buf.write("XZ\3\2\2\2YW\3\2\2\2Z[\7\23\2\2[\r\3\2\2\2\\`\5\20\t\2")
        buf.write("]`\5\24\13\2^`\5\26\f\2_\\\3\2\2\2_]\3\2\2\2_^\3\2\2\2")
        buf.write("`a\3\2\2\2ab\7\24\2\2b\17\3\2\2\2cd\7\17\2\2df\7\20\2")
        buf.write("\2eg\5\22\n\2fe\3\2\2\2fg\3\2\2\2gh\3\2\2\2hi\7\21\2\2")
        buf.write("i\21\3\2\2\2jo\5\30\r\2kl\7\25\2\2ln\5\30\r\2mk\3\2\2")
        buf.write("\2nq\3\2\2\2om\3\2\2\2op\3\2\2\2p\23\3\2\2\2qo\3\2\2\2")
        buf.write("rs\7\3\2\2st\5\30\r\2t\25\3\2\2\2uv\7\17\2\2vw\7\4\2\2")
        buf.write("wx\5\30\r\2x\27\3\2\2\2yz\5\32\16\2z{\7\b\2\2{|\5\30\r")
        buf.write("\2|\177\3\2\2\2}\177\5\32\16\2~y\3\2\2\2~}\3\2\2\2\177")
        buf.write("\31\3\2\2\2\u0080\u0081\5\34\17\2\u0081\u0082\7\t\2\2")
        buf.write("\u0082\u0083\5\34\17\2\u0083\u0086\3\2\2\2\u0084\u0086")
        buf.write("\5\34\17\2\u0085\u0080\3\2\2\2\u0085\u0084\3\2\2\2\u0086")
        buf.write("\33\3\2\2\2\u0087\u0088\b\17\1\2\u0088\u0089\5\36\20\2")
        buf.write("\u0089\u008f\3\2\2\2\u008a\u008b\f\4\2\2\u008b\u008c\t")
        buf.write("\2\2\2\u008c\u008e\5\36\20\2\u008d\u008a\3\2\2\2\u008e")
        buf.write("\u0091\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2")
        buf.write("\u0090\35\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0093\7\20")
        buf.write("\2\2\u0093\u0094\5\36\20\2\u0094\u0095\7\21\2\2\u0095")
        buf.write("\u0098\3\2\2\2\u0096\u0098\5 \21\2\u0097\u0092\3\2\2\2")
        buf.write("\u0097\u0096\3\2\2\2\u0098\37\3\2\2\2\u0099\u009e\7\17")
        buf.write("\2\2\u009a\u009e\7\r\2\2\u009b\u009e\7\f\2\2\u009c\u009e")
        buf.write("\5\20\t\2\u009d\u0099\3\2\2\2\u009d\u009a\3\2\2\2\u009d")
        buf.write("\u009b\3\2\2\2\u009d\u009c\3\2\2\2\u009e!\3\2\2\2\24$")
        buf.write("&.\66?FJPUW_fo~\u0085\u008f\u0097\u009d")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'return'", "'='", "<INVALID>", "'int'", 
                     "'float'", "'+'", "'-'", "'*'", "'/'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "DATA_TYPE", 
                      "INT", "FLOAT", "ADD", "SUBTRACT", "MULTIPLY", "DIVISION", 
                      "FLOAT_LITERAL", "INTEGER_LITERAL", "INTLIT", "ID", 
                      "LB", "RB", "LP", "RP", "SEMI", "COMMA", "DOT", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_vardecl = 1
    RULE_funcdecl = 2
    RULE_param_list = 3
    RULE_param = 4
    RULE_body = 5
    RULE_stmt = 6
    RULE_call = 7
    RULE_list_of_expr = 8
    RULE_return_stmt = 9
    RULE_assign_stmt = 10
    RULE_expr = 11
    RULE_expr1 = 12
    RULE_expr2 = 13
    RULE_expr3 = 14
    RULE_operands = 15

    ruleNames =  [ "program", "vardecl", "funcdecl", "param_list", "param", 
                   "body", "stmt", "call", "list_of_expr", "return_stmt", 
                   "assign_stmt", "expr", "expr1", "expr2", "expr3", "operands" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    DATA_TYPE=3
    INT=4
    FLOAT=5
    ADD=6
    SUBTRACT=7
    MULTIPLY=8
    DIVISION=9
    FLOAT_LITERAL=10
    INTEGER_LITERAL=11
    INTLIT=12
    ID=13
    LB=14
    RB=15
    LP=16
    RP=17
    SEMI=18
    COMMA=19
    DOT=20
    WS=21
    ERROR_CHAR=22
    UNCLOSE_STRING=23
    ILLEGAL_ESCAPE=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.VardeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.VardeclContext,i)


        def funcdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.FuncdeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.FuncdeclContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 32
                    self.vardecl()
                    pass

                elif la_ == 2:
                    self.state = 33
                    self.funcdecl()
                    pass


                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.DATA_TYPE):
                    break

            self.state = 38
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA_TYPE(self):
            return self.getToken(BKOOLParser.DATA_TYPE, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ParamContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ParamContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(BKOOLParser.DATA_TYPE)
            self.state = 42 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 41
                self.param()
                self.state = 44 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.ID or _la==BKOOLParser.COMMA):
                    break

            self.state = 46
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA_TYPE(self):
            return self.getToken(BKOOLParser.DATA_TYPE, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


        def param_list(self):
            return self.getTypedRuleContext(BKOOLParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_funcdecl




    def funcdecl(self):

        localctx = BKOOLParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(BKOOLParser.DATA_TYPE)
            self.state = 49
            self.match(BKOOLParser.ID)
            self.state = 50
            self.match(BKOOLParser.LB)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.DATA_TYPE:
                self.state = 51
                self.param_list()


            self.state = 54
            self.match(BKOOLParser.RB)
            self.state = 55
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA_TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.DATA_TYPE)
            else:
                return self.getToken(BKOOLParser.DATA_TYPE, i)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.SEMI)
            else:
                return self.getToken(BKOOLParser.SEMI, i)

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ParamContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ParamContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param_list




    def param_list(self):

        localctx = BKOOLParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(BKOOLParser.DATA_TYPE)
            self.state = 59 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 58
                self.param()
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.ID or _la==BKOOLParser.COMMA):
                    break

            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.SEMI:
                self.state = 63
                self.match(BKOOLParser.SEMI)

                self.state = 64
                self.match(BKOOLParser.DATA_TYPE)
                self.state = 66 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 65
                    self.param()
                    self.state = 68 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==BKOOLParser.ID or _la==BKOOLParser.COMMA):
                        break

                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_param




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_param)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.COMMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.match(BKOOLParser.COMMA)
                self.state = 77
                self.match(BKOOLParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.VardeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.VardeclContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_body




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(BKOOLParser.LP)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.T__0) | (1 << BKOOLParser.DATA_TYPE) | (1 << BKOOLParser.ID))) != 0):
                self.state = 83
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.DATA_TYPE]:
                    self.state = 81
                    self.vardecl()
                    pass
                elif token in [BKOOLParser.T__0, BKOOLParser.ID]:
                    self.state = 82
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def call(self):
            return self.getTypedRuleContext(BKOOLParser.CallContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Return_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Assign_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 90
                self.call()
                pass

            elif la_ == 2:
                self.state = 91
                self.return_stmt()
                pass

            elif la_ == 3:
                self.state = 92
                self.assign_stmt()
                pass


            self.state = 95
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def list_of_expr(self):
            return self.getTypedRuleContext(BKOOLParser.List_of_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_call




    def call(self):

        localctx = BKOOLParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(BKOOLParser.ID)
            self.state = 98
            self.match(BKOOLParser.LB)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.FLOAT_LITERAL) | (1 << BKOOLParser.INTEGER_LITERAL) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.LB))) != 0):
                self.state = 99
                self.list_of_expr()


            self.state = 102
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_list_of_expr




    def list_of_expr(self):

        localctx = BKOOLParser.List_of_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list_of_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.expr()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 105
                self.match(BKOOLParser.COMMA)
                self.state = 106
                self.expr()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_return_stmt




    def return_stmt(self):

        localctx = BKOOLParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(BKOOLParser.T__0)
            self.state = 113
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = BKOOLParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(BKOOLParser.ID)
            self.state = 116
            self.match(BKOOLParser.T__1)
            self.state = 117
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(BKOOLParser.Expr1Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr)
        try:
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.expr1()
                self.state = 120
                self.match(BKOOLParser.ADD)
                self.state = 121
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr2Context,i)


        def SUBTRACT(self):
            return self.getToken(BKOOLParser.SUBTRACT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr1




    def expr1(self):

        localctx = BKOOLParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr1)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.expr2(0)
                self.state = 127
                self.match(BKOOLParser.SUBTRACT)
                self.state = 128
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def MULTIPLY(self):
            return self.getToken(BKOOLParser.MULTIPLY, 0)

        def DIVISION(self):
            return self.getToken(BKOOLParser.DIVISION, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.expr3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 141
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 136
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 137
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.MULTIPLY or _la==BKOOLParser.DIVISION):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 138
                    self.expr3() 
                self.state = 143
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def operands(self):
            return self.getTypedRuleContext(BKOOLParser.OperandsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr3




    def expr3(self):

        localctx = BKOOLParser.Expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expr3)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(BKOOLParser.LB)
                self.state = 145
                self.expr3()
                self.state = 146
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.FLOAT_LITERAL, BKOOLParser.INTEGER_LITERAL, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.operands()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(BKOOLParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(BKOOLParser.FLOAT_LITERAL, 0)

        def call(self):
            return self.getTypedRuleContext(BKOOLParser.CallContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_operands




    def operands(self):

        localctx = BKOOLParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_operands)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(BKOOLParser.INTEGER_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.match(BKOOLParser.FLOAT_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 154
                self.call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expr2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




