# Generated from d:\HCMUT\Semester 212\Principles of Programming Languages\Mid-term review\Mid term VNese\Coding\2019_Programming\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("D\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\7\3\30\n\3\f\3\16\3\33")
        buf.write("\13\3\3\4\3\4\3\4\3\4\3\4\5\4\"\n\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5)\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\62\n\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7?\n\7\f\7")
        buf.write("\16\7B\13\7\3\7\2\4\4\f\b\2\4\6\b\n\f\2\2\2D\2\16\3\2")
        buf.write("\2\2\4\21\3\2\2\2\6!\3\2\2\2\b(\3\2\2\2\n\61\3\2\2\2\f")
        buf.write("\63\3\2\2\2\16\17\5\4\3\2\17\20\7\2\2\3\20\3\3\2\2\2\21")
        buf.write("\22\b\3\1\2\22\23\5\6\4\2\23\31\3\2\2\2\24\25\f\4\2\2")
        buf.write("\25\26\7\3\2\2\26\30\5\6\4\2\27\24\3\2\2\2\30\33\3\2\2")
        buf.write("\2\31\27\3\2\2\2\31\32\3\2\2\2\32\5\3\2\2\2\33\31\3\2")
        buf.write("\2\2\34\35\5\b\5\2\35\36\7\4\2\2\36\37\5\b\5\2\37\"\3")
        buf.write("\2\2\2 \"\5\b\5\2!\34\3\2\2\2! \3\2\2\2\"\7\3\2\2\2#$")
        buf.write("\5\n\6\2$%\7\5\2\2%&\5\b\5\2&)\3\2\2\2\')\5\n\6\2(#\3")
        buf.write("\2\2\2(\'\3\2\2\2)\t\3\2\2\2*+\7\6\2\2+,\5\4\3\2,-\7\7")
        buf.write("\2\2-\62\3\2\2\2.\62\7\n\2\2/\62\7\13\2\2\60\62\5\f\7")
        buf.write("\2\61*\3\2\2\2\61.\3\2\2\2\61/\3\2\2\2\61\60\3\2\2\2\62")
        buf.write("\13\3\2\2\2\63\64\b\7\1\2\64\65\7\13\2\2\65\66\7\b\2\2")
        buf.write("\66\67\5\4\3\2\678\7\t\2\28@\3\2\2\29:\f\3\2\2:;\7\b\2")
        buf.write("\2;<\5\4\3\2<=\7\t\2\2=?\3\2\2\2>9\3\2\2\2?B\3\2\2\2@")
        buf.write(">\3\2\2\2@A\3\2\2\2A\r\3\2\2\2B@\3\2\2\2\7\31!(\61@")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'?'", "'^'", "'@'", "'('", "')'", "'['", 
                     "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "LP", "RP", "LB", "RB", "INT", "ID", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_expr = 1
    RULE_expr1 = 2
    RULE_expr2 = 3
    RULE_expr3 = 4
    RULE_element_op = 5

    ruleNames =  [ "program", "expr", "expr1", "expr2", "expr3", "element_op" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    LP=4
    RP=5
    LB=6
    RB=7
    INT=8
    ID=9
    WS=10
    ERROR_CHAR=11
    UNCLOSE_STRING=12
    ILLEGAL_ESCAPE=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.expr(0)
            self.state = 13
            self.match(BKITParser.EOF)
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
            return self.getTypedRuleContext(BKITParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expr



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.expr1()
            self._ctx.stop = self._input.LT(-1)
            self.state = 23
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 18
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 19
                    self.match(BKITParser.T__0)
                    self.state = 20
                    self.expr1() 
                self.state = 25
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Expr2Context)
            else:
                return self.getTypedRuleContext(BKITParser.Expr2Context,i)


        def getRuleIndex(self):
            return BKITParser.RULE_expr1




    def expr1(self):

        localctx = BKITParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr1)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.expr2()
                self.state = 27
                self.match(BKITParser.T__1)
                self.state = 28
                self.expr2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.expr2()
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
            return self.getTypedRuleContext(BKITParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(BKITParser.Expr2Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expr2




    def expr2(self):

        localctx = BKITParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr2)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.expr3()
                self.state = 34
                self.match(BKITParser.T__2)
                self.state = 35
                self.expr2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.expr3()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def INT(self):
            return self.getToken(BKITParser.INT, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def element_op(self):
            return self.getTypedRuleContext(BKITParser.Element_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expr3




    def expr3(self):

        localctx = BKITParser.Expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr3)
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(BKITParser.LP)
                self.state = 41
                self.expr(0)
                self.state = 42
                self.match(BKITParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(BKITParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.match(BKITParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.element_op(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def element_op(self):
            return self.getTypedRuleContext(BKITParser.Element_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_element_op



    def element_op(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Element_opContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_element_op, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(BKITParser.ID)
            self.state = 51
            self.match(BKITParser.LB)
            self.state = 52
            self.expr(0)
            self.state = 53
            self.match(BKITParser.RB)
            self._ctx.stop = self._input.LT(-1)
            self.state = 62
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Element_opContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_element_op)
                    self.state = 55
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 56
                    self.match(BKITParser.LB)
                    self.state = 57
                    self.expr(0)
                    self.state = 58
                    self.match(BKITParser.RB) 
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        self._predicates[5] = self.element_op_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def element_op_sempred(self, localctx:Element_opContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




