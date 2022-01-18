# Generated from d:\HCMUT\Semester 212\Principles of Programming Languages\HK212_CO3005_PPL\Quiz\3_Recognizer\2\BKOOL.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("A\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\6\2\21\n\2\r\2\16\2\22\3\2\3\2\3\3\3\3\6\3\31\n\3")
        buf.write("\r\3\16\3\32\3\3\3\3\3\4\3\4\3\4\3\4\5\4#\n\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\6\5*\n\5\r\5\16\5+\3\5\3\5\3\5\6\5\61\n\5")
        buf.write("\r\5\16\5\62\7\5\65\n\5\f\5\16\58\13\5\3\6\3\6\3\6\5\6")
        buf.write("=\n\6\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\2\2B\2\20\3\2\2")
        buf.write("\2\4\26\3\2\2\2\6\36\3\2\2\2\b\'\3\2\2\2\n<\3\2\2\2\f")
        buf.write(">\3\2\2\2\16\21\5\4\3\2\17\21\5\6\4\2\20\16\3\2\2\2\20")
        buf.write("\17\3\2\2\2\21\22\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2")
        buf.write("\23\24\3\2\2\2\24\25\7\2\2\3\25\3\3\2\2\2\26\30\7\4\2")
        buf.write("\2\27\31\5\n\6\2\30\27\3\2\2\2\31\32\3\2\2\2\32\30\3\2")
        buf.write("\2\2\32\33\3\2\2\2\33\34\3\2\2\2\34\35\7\r\2\2\35\5\3")
        buf.write("\2\2\2\36\37\7\4\2\2\37 \7\7\2\2 \"\7\t\2\2!#\5\b\5\2")
        buf.write("\"!\3\2\2\2\"#\3\2\2\2#$\3\2\2\2$%\7\n\2\2%&\5\f\7\2&")
        buf.write("\7\3\2\2\2\')\7\4\2\2(*\5\n\6\2)(\3\2\2\2*+\3\2\2\2+)")
        buf.write("\3\2\2\2+,\3\2\2\2,\66\3\2\2\2-.\7\r\2\2.\60\7\4\2\2/")
        buf.write("\61\5\n\6\2\60/\3\2\2\2\61\62\3\2\2\2\62\60\3\2\2\2\62")
        buf.write("\63\3\2\2\2\63\65\3\2\2\2\64-\3\2\2\2\658\3\2\2\2\66\64")
        buf.write("\3\2\2\2\66\67\3\2\2\2\67\t\3\2\2\28\66\3\2\2\29=\7\7")
        buf.write("\2\2:;\7\16\2\2;=\7\7\2\2<9\3\2\2\2<:\3\2\2\2=\13\3\2")
        buf.write("\2\2>?\7\3\2\2?\r\3\2\2\2\n\20\22\32\"+\62\66<")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'body'", "<INVALID>", "'int'", "'float'", 
                     "<INVALID>", "<INVALID>", "'('", "')'", "'{'", "'}'", 
                     "';'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "DATA_TYPE", "INT", "FLOAT", 
                      "ID", "INTLIT", "LB", "RB", "LP", "RP", "SEMI", "COMMA", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_vardecl = 1
    RULE_funcdecl = 2
    RULE_param_list = 3
    RULE_param = 4
    RULE_body = 5

    ruleNames =  [ "program", "vardecl", "funcdecl", "param_list", "param", 
                   "body" ]

    EOF = Token.EOF
    T__0=1
    DATA_TYPE=2
    INT=3
    FLOAT=4
    ID=5
    INTLIT=6
    LB=7
    RB=8
    LP=9
    RP=10
    SEMI=11
    COMMA=12
    WS=13
    ERROR_CHAR=14
    UNCLOSE_STRING=15
    ILLEGAL_ESCAPE=16

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
            self.state = 14 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 12
                    self.vardecl()
                    pass

                elif la_ == 2:
                    self.state = 13
                    self.funcdecl()
                    pass


                self.state = 16 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.DATA_TYPE):
                    break

            self.state = 18
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
            self.state = 20
            self.match(BKOOLParser.DATA_TYPE)
            self.state = 22 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 21
                self.param()
                self.state = 24 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.ID or _la==BKOOLParser.COMMA):
                    break

            self.state = 26
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
            self.state = 28
            self.match(BKOOLParser.DATA_TYPE)
            self.state = 29
            self.match(BKOOLParser.ID)
            self.state = 30
            self.match(BKOOLParser.LB)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.DATA_TYPE:
                self.state = 31
                self.param_list()


            self.state = 34
            self.match(BKOOLParser.RB)
            self.state = 35
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
            self.state = 37
            self.match(BKOOLParser.DATA_TYPE)
            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self.param()
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.ID or _la==BKOOLParser.COMMA):
                    break

            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.SEMI:
                self.state = 43
                self.match(BKOOLParser.SEMI)

                self.state = 44
                self.match(BKOOLParser.DATA_TYPE)
                self.state = 46 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 45
                    self.param()
                    self.state = 48 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==BKOOLParser.ID or _la==BKOOLParser.COMMA):
                        break

                self.state = 54
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
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.COMMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(BKOOLParser.COMMA)
                self.state = 57
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


        def getRuleIndex(self):
            return BKOOLParser.RULE_body




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(BKOOLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





