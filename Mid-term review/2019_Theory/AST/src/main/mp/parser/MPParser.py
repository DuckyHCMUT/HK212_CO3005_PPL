# Generated from main/mp/parser/MP.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("\'\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\6\3\21\n\3\r\3\16\3\22\3\3\3\3\3\4\3\4\3\4\3\4\7")
        buf.write("\4\33\n\4\f\4\16\4\36\13\4\3\4\3\4\3\5\3\5\3\5\5\5%\n")
        buf.write("\5\3\5\2\2\6\2\4\6\b\2\2\2&\2\n\3\2\2\2\4\r\3\2\2\2\6")
        buf.write("\26\3\2\2\2\b$\3\2\2\2\n\13\5\4\3\2\13\f\7\2\2\3\f\3\3")
        buf.write("\2\2\2\r\16\7\3\2\2\16\20\7\6\2\2\17\21\5\6\4\2\20\17")
        buf.write("\3\2\2\2\21\22\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2\23")
        buf.write("\24\3\2\2\2\24\25\7\7\2\2\25\5\3\2\2\2\26\27\5\b\5\2\27")
        buf.write("\34\7\b\2\2\30\31\7\t\2\2\31\33\7\b\2\2\32\30\3\2\2\2")
        buf.write("\33\36\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35\37\3\2\2")
        buf.write("\2\36\34\3\2\2\2\37 \7\n\2\2 \7\3\2\2\2!%\7\4\2\2\"%\7")
        buf.write("\5\2\2#%\5\4\3\2$!\3\2\2\2$\"\3\2\2\2$#\3\2\2\2%\t\3\2")
        buf.write("\2\2\5\22\34$")
        return buf.getvalue()


class MPParser ( Parser ):

    grammarFileName = "MP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'struct'", "'int'", "'float'", "'{'", 
                     "'}'", "<INVALID>", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "STRUCT", "INTTYPE", "FLOATTYPE", "LB", 
                      "RB", "ID", "COMMA", "SEMI", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_struct = 1
    RULE_mem = 2
    RULE_data_type = 3

    ruleNames =  [ "program", "struct", "mem", "data_type" ]

    EOF = Token.EOF
    STRUCT=1
    INTTYPE=2
    FLOATTYPE=3
    LB=4
    RB=5
    ID=6
    COMMA=7
    SEMI=8
    WS=9
    ERROR_CHAR=10

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

        def struct(self):
            return self.getTypedRuleContext(MPParser.StructContext,0)


        def EOF(self):
            return self.getToken(MPParser.EOF, 0)

        def getRuleIndex(self):
            return MPParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.struct()
            self.state = 9
            self.match(MPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(MPParser.STRUCT, 0)

        def LB(self):
            return self.getToken(MPParser.LB, 0)

        def RB(self):
            return self.getToken(MPParser.RB, 0)

        def mem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.MemContext)
            else:
                return self.getTypedRuleContext(MPParser.MemContext,i)


        def getRuleIndex(self):
            return MPParser.RULE_struct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct" ):
                return visitor.visitStruct(self)
            else:
                return visitor.visitChildren(self)




    def struct(self):

        localctx = MPParser.StructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_struct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.match(MPParser.STRUCT)
            self.state = 12
            self.match(MPParser.LB)
            self.state = 14 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 13
                self.mem()
                self.state = 16 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MPParser.STRUCT) | (1 << MPParser.INTTYPE) | (1 << MPParser.FLOATTYPE))) != 0)):
                    break

            self.state = 18
            self.match(MPParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_type(self):
            return self.getTypedRuleContext(MPParser.Data_typeContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.ID)
            else:
                return self.getToken(MPParser.ID, i)

        def SEMI(self):
            return self.getToken(MPParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.COMMA)
            else:
                return self.getToken(MPParser.COMMA, i)

        def getRuleIndex(self):
            return MPParser.RULE_mem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMem" ):
                return visitor.visitMem(self)
            else:
                return visitor.visitChildren(self)




    def mem(self):

        localctx = MPParser.MemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.data_type()
            self.state = 21
            self.match(MPParser.ID)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MPParser.COMMA:
                self.state = 22
                self.match(MPParser.COMMA)
                self.state = 23
                self.match(MPParser.ID)
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.match(MPParser.SEMI)
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
            return self.getToken(MPParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MPParser.FLOATTYPE, 0)

        def struct(self):
            return self.getTypedRuleContext(MPParser.StructContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = MPParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_data_type)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MPParser.INTTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.match(MPParser.INTTYPE)
                pass
            elif token in [MPParser.FLOATTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.match(MPParser.FLOATTYPE)
                pass
            elif token in [MPParser.STRUCT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.struct()
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





