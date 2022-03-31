# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("+\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\5\4\32\n\4\3")
        buf.write("\5\6\5\35\n\5\r\5\16\5\36\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\5\6)\n\6\3\6\2\2\7\2\4\6\b\n\2\2\2)\2\f\3\2\2\2\4")
        buf.write("\17\3\2\2\2\6\31\3\2\2\2\b\34\3\2\2\2\n(\3\2\2\2\f\r\5")
        buf.write("\4\3\2\r\16\7\2\2\3\16\3\3\2\2\2\17\20\7\7\2\2\20\21\7")
        buf.write("\t\2\2\21\22\5\b\5\2\22\23\7\n\2\2\23\24\7\b\2\2\24\25")
        buf.write("\5\6\4\2\25\5\3\2\2\2\26\32\7\3\2\2\27\32\7\4\2\2\30\32")
        buf.write("\5\4\3\2\31\26\3\2\2\2\31\27\3\2\2\2\31\30\3\2\2\2\32")
        buf.write("\7\3\2\2\2\33\35\5\n\6\2\34\33\3\2\2\2\35\36\3\2\2\2\36")
        buf.write("\34\3\2\2\2\36\37\3\2\2\2\37\t\3\2\2\2 !\7\5\2\2!\"\7")
        buf.write("\f\2\2\")\7\5\2\2#$\7\5\2\2$%\7\f\2\2%&\7\5\2\2&\'\7\13")
        buf.write("\2\2\')\5\n\6\2( \3\2\2\2(#\3\2\2\2)\13\3\2\2\2\5\31\36")
        buf.write("(")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "<INVALID>", "'-'", 
                     "'array'", "'of'", "'['", "']'", "','", "'..'" ]

    symbolicNames = [ "<INVALID>", "INTTYPE", "FLOATTYPE", "INT", "SUB", 
                      "ARRAY", "OF", "LS", "RS", "COMMA", "DOTDOT", "STRING", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_array_type = 1
    RULE_data_type = 2
    RULE_domain_list = 3
    RULE_domain = 4

    ruleNames =  [ "program", "array_type", "data_type", "domain_list", 
                   "domain" ]

    EOF = Token.EOF
    INTTYPE=1
    FLOATTYPE=2
    INT=3
    SUB=4
    ARRAY=5
    OF=6
    LS=7
    RS=8
    COMMA=9
    DOTDOT=10
    STRING=11
    WS=12
    ERROR_CHAR=13
    UNCLOSE_STRING=14
    ILLEGAL_ESCAPE=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(BKITParser.Array_typeContext,0)


        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.array_type()
            self.state = 11
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(BKITParser.ARRAY, 0)

        def LS(self):
            return self.getToken(BKITParser.LS, 0)

        def domain_list(self):
            return self.getTypedRuleContext(BKITParser.Domain_listContext,0)


        def RS(self):
            return self.getToken(BKITParser.RS, 0)

        def OF(self):
            return self.getToken(BKITParser.OF, 0)

        def data_type(self):
            return self.getTypedRuleContext(BKITParser.Data_typeContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = BKITParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(BKITParser.ARRAY)
            self.state = 14
            self.match(BKITParser.LS)
            self.state = 15
            self.domain_list()
            self.state = 16
            self.match(BKITParser.RS)
            self.state = 17
            self.match(BKITParser.OF)
            self.state = 18
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(BKITParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(BKITParser.FLOATTYPE, 0)

        def array_type(self):
            return self.getTypedRuleContext(BKITParser.Array_typeContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = BKITParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_data_type)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.match(BKITParser.INTTYPE)
                pass
            elif token in [BKITParser.FLOATTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.match(BKITParser.FLOATTYPE)
                pass
            elif token in [BKITParser.ARRAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.array_type()
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


    class Domain_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def domain(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.DomainContext)
            else:
                return self.getTypedRuleContext(BKITParser.DomainContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_domain_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDomain_list" ):
                return visitor.visitDomain_list(self)
            else:
                return visitor.visitChildren(self)




    def domain_list(self):

        localctx = BKITParser.Domain_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_domain_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 25
                self.domain()
                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.INT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DomainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INT)
            else:
                return self.getToken(BKITParser.INT, i)

        def DOTDOT(self):
            return self.getToken(BKITParser.DOTDOT, 0)

        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def domain(self):
            return self.getTypedRuleContext(BKITParser.DomainContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_domain

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDomain" ):
                return visitor.visitDomain(self)
            else:
                return visitor.visitChildren(self)




    def domain(self):

        localctx = BKITParser.DomainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_domain)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(BKITParser.INT)
                self.state = 31
                self.match(BKITParser.DOTDOT)
                self.state = 32
                self.match(BKITParser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.match(BKITParser.INT)
                self.state = 34
                self.match(BKITParser.DOTDOT)
                self.state = 35
                self.match(BKITParser.INT)
                self.state = 36
                self.match(BKITParser.COMMA)
                self.state = 37
                self.domain()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





