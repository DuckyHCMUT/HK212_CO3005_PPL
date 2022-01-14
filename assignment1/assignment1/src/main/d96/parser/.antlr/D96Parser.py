# Generated from d:\HCMUT\Semester 212\Principles of Programming Languages\HK212_CO3005_PPL\assignment1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3H")
        buf.write("}\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\5\2-\n\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\5\6>\n\6\3\6")
        buf.write("\5\6A\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\3\13\3\13\3\f\5\fT\n\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\7\17h\n\17\f\17\16\17k\13\17\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\22\3\22\5\22t\n\22\3\23\3\23\3\23\5\23y\n\23\3")
        buf.write("\23\3\23\3\23\2\2\24\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$\2\3\3\2\7\b\2q\2&\3\2\2\2\4\61\3\2\2\2\6\63")
        buf.write("\3\2\2\2\b9\3\2\2\2\n=\3\2\2\2\fH\3\2\2\2\16J\3\2\2\2")
        buf.write("\20L\3\2\2\2\22N\3\2\2\2\24P\3\2\2\2\26S\3\2\2\2\30[\3")
        buf.write("\2\2\2\32a\3\2\2\2\34i\3\2\2\2\36l\3\2\2\2 n\3\2\2\2\"")
        buf.write("s\3\2\2\2$u\3\2\2\2&\'\5\4\3\2\'(\7\3\2\2()\7\66\2\2)")
        buf.write("*\7\67\2\2*,\7:\2\2+-\5 \21\2,+\3\2\2\2,-\3\2\2\2-.\3")
        buf.write("\2\2\2./\7;\2\2/\60\7\2\2\3\60\3\3\2\2\2\61\62\t\2\2\2")
        buf.write("\62\5\3\2\2\2\63\64\7\26\2\2\64\65\7\r\2\2\65\66\7:\2")
        buf.write("\2\66\67\5\b\5\2\678\7;\2\28\7\3\2\2\29:\7\r\2\2:\t\3")
        buf.write("\2\2\2;>\5\f\7\2<>\5\16\b\2=;\3\2\2\2=<\3\2\2\2>@\3\2")
        buf.write("\2\2?A\5\20\t\2@?\3\2\2\2@A\3\2\2\2AB\3\2\2\2BC\7\4\2")
        buf.write("\2CD\5\22\n\2DE\7-\2\2EF\5\24\13\2FG\7<\2\2G\13\3\2\2")
        buf.write("\2HI\7\33\2\2I\r\3\2\2\2JK\7 \2\2K\17\3\2\2\2LM\7\5\2")
        buf.write("\2M\21\3\2\2\2NO\7\20\2\2O\23\3\2\2\2PQ\3\2\2\2Q\25\3")
        buf.write("\2\2\2RT\5\20\t\2SR\3\2\2\2ST\3\2\2\2TU\3\2\2\2UV\7\r")
        buf.write("\2\2VW\7\66\2\2WX\5\34\17\2XY\7\67\2\2YZ\5\36\20\2Z\27")
        buf.write("\3\2\2\2[\\\7\22\2\2\\]\7\66\2\2]^\5\34\17\2^_\7\67\2")
        buf.write("\2_`\5\36\20\2`\31\3\2\2\2ab\7\27\2\2bc\7\66\2\2cd\7\67")
        buf.write("\2\2de\5\36\20\2e\33\3\2\2\2fh\7\6\2\2gf\3\2\2\2hk\3\2")
        buf.write("\2\2ig\3\2\2\2ij\3\2\2\2j\35\3\2\2\2ki\3\2\2\2lm\3\2\2")
        buf.write("\2m\37\3\2\2\2no\5$\23\2op\7<\2\2p!\3\2\2\2qt\5$\23\2")
        buf.write("rt\7\f\2\2sq\3\2\2\2sr\3\2\2\2t#\3\2\2\2uv\7\13\2\2vx")
        buf.write("\7\66\2\2wy\5\"\22\2xw\3\2\2\2xy\3\2\2\2yz\3\2\2\2z{\7")
        buf.write("\67\2\2{%\3\2\2\2\t,=@Sisx")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "':'", "'$'", "'wtf'", "'int'", 
                     "'void'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'Break'", "'Foreach'", "'Int'", "'Null'", 
                     "'Constructor'", "'Continue'", "'True'", "'Float'", 
                     "'Class'", "'Destructor'", "'If'", "'False'", "'Boolean'", 
                     "'Val'", "'New'", "'Elseif'", "'Array'", "'String'", 
                     "'Var'", "'By'", "'Else'", "'In'", "'Return'", "'+'", 
                     "'-'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'='", "'!='", "'<'", "'<='", "'>'", "'>='", "'==.'", 
                     "'.'", "'::'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "';'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INTTYPE", "VOIDTYPE", "WS", "BLOCK_COMMENT", 
                      "ALPHABET", "INTLIT", "ID", "BREAK", "FOREACH", "INT", 
                      "NULL", "CONSTRUCTOR", "CONTINUE", "TRUE", "FLOAT", 
                      "CLASS", "DESTRUCTOR", "IF", "FALSE", "BOOLEAN", "VAL", 
                      "NEW", "ELSEIF", "ARRAY", "STRING", "VAR", "BY", "ELSE", 
                      "IN", "RETURN", "ADD", "SUBTRACT", "MULTIPLY", "MODULO", 
                      "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", 
                      "LESS_THAN", "LEQ", "GREATER_THAN", "GEQ", "EQUAL_WHAT", 
                      "DOT", "SUPER_CLASS", "LB", "RB", "LS", "RS", "LP", 
                      "RP", "SEMI", "COMMA", "LITERAL_INT_DEC", "LITERAL_INT_HEX", 
                      "LITERAL_INT_OCT", "LITERAL_INT_BIN", "LITERAL_STRING", 
                      "LITERAL_IDX_ARRAY", "LITERAL_MTD_ARRAY", "DOUBLE_QUOTE", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_mptype = 1
    RULE_class_declaration = 2
    RULE_class_body = 3
    RULE_attribute = 4
    RULE_immuttable = 5
    RULE_muttable = 6
    RULE_static = 7
    RULE_data_type = 8
    RULE_data = 9
    RULE_method = 10
    RULE_constructor = 11
    RULE_destructor = 12
    RULE_params = 13
    RULE_stmt = 14
    RULE_body = 15
    RULE_exp = 16
    RULE_funcall = 17

    ruleNames =  [ "program", "mptype", "class_declaration", "class_body", 
                   "attribute", "immuttable", "muttable", "static", "data_type", 
                   "data", "method", "constructor", "destructor", "params", 
                   "stmt", "body", "exp", "funcall" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    INTTYPE=5
    VOIDTYPE=6
    WS=7
    BLOCK_COMMENT=8
    ALPHABET=9
    INTLIT=10
    ID=11
    BREAK=12
    FOREACH=13
    INT=14
    NULL=15
    CONSTRUCTOR=16
    CONTINUE=17
    TRUE=18
    FLOAT=19
    CLASS=20
    DESTRUCTOR=21
    IF=22
    FALSE=23
    BOOLEAN=24
    VAL=25
    NEW=26
    ELSEIF=27
    ARRAY=28
    STRING=29
    VAR=30
    BY=31
    ELSE=32
    IN=33
    RETURN=34
    ADD=35
    SUBTRACT=36
    MULTIPLY=37
    MODULO=38
    NOT=39
    AND=40
    OR=41
    EQUAL=42
    ASSIGN=43
    NOT_EQUAL=44
    LESS_THAN=45
    LEQ=46
    GREATER_THAN=47
    GEQ=48
    EQUAL_WHAT=49
    DOT=50
    SUPER_CLASS=51
    LB=52
    RB=53
    LS=54
    RS=55
    LP=56
    RP=57
    SEMI=58
    COMMA=59
    LITERAL_INT_DEC=60
    LITERAL_INT_HEX=61
    LITERAL_INT_OCT=62
    LITERAL_INT_BIN=63
    LITERAL_STRING=64
    LITERAL_IDX_ARRAY=65
    LITERAL_MTD_ARRAY=66
    DOUBLE_QUOTE=67
    ERROR_CHAR=68
    UNCLOSE_STRING=69
    ILLEGAL_ESCAPE=70

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def body(self):
            return self.getTypedRuleContext(D96Parser.BodyContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.mptype()
            self.state = 37
            self.match(D96Parser.T__0)
            self.state = 38
            self.match(D96Parser.LB)
            self.state = 39
            self.match(D96Parser.RB)
            self.state = 40
            self.match(D96Parser.LP)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ALPHABET:
                self.state = 41
                self.body()


            self.state = 44
            self.match(D96Parser.RP)
            self.state = 45
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MptypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(D96Parser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(D96Parser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_mptype




    def mptype(self):

        localctx = D96Parser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mptype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            _la = self._input.LA(1)
            if not(_la==D96Parser.INTTYPE or _la==D96Parser.VOIDTYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def class_body(self):
            return self.getTypedRuleContext(D96Parser.Class_bodyContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_declaration




    def class_declaration(self):

        localctx = D96Parser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(D96Parser.CLASS)
            self.state = 50
            self.match(D96Parser.ID)
            self.state = 51
            self.match(D96Parser.LP)
            self.state = 52
            self.class_body()
            self.state = 53
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_body




    def class_body(self):

        localctx = D96Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def data(self):
            return self.getTypedRuleContext(D96Parser.DataContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def immuttable(self):
            return self.getTypedRuleContext(D96Parser.ImmuttableContext,0)


        def muttable(self):
            return self.getTypedRuleContext(D96Parser.MuttableContext,0)


        def static(self):
            return self.getTypedRuleContext(D96Parser.StaticContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute




    def attribute(self):

        localctx = D96Parser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL]:
                self.state = 57
                self.immuttable()
                pass
            elif token in [D96Parser.VAR]:
                self.state = 58
                self.muttable()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.T__2:
                self.state = 61
                self.static()


            self.state = 64
            self.match(D96Parser.T__1)
            self.state = 65
            self.data_type()
            self.state = 66
            self.match(D96Parser.ASSIGN)
            self.state = 67
            self.data()
            self.state = 68
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmuttableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_immuttable




    def immuttable(self):

        localctx = D96Parser.ImmuttableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_immuttable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(D96Parser.VAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MuttableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_muttable




    def muttable(self):

        localctx = D96Parser.MuttableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_muttable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(D96Parser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_static




    def static(self):

        localctx = D96Parser.StaticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_static)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(D96Parser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_data_type




    def data_type(self):

        localctx = D96Parser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_data_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(D96Parser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_data




    def data(self):

        localctx = D96Parser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_data)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def params(self):
            return self.getTypedRuleContext(D96Parser.ParamsContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(D96Parser.StmtContext,0)


        def static(self):
            return self.getTypedRuleContext(D96Parser.StaticContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method




    def method(self):

        localctx = D96Parser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.T__2:
                self.state = 80
                self.static()


            self.state = 83
            self.match(D96Parser.ID)
            self.state = 84
            self.match(D96Parser.LB)
            self.state = 85
            self.params()
            self.state = 86
            self.match(D96Parser.RB)
            self.state = 87
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def params(self):
            return self.getTypedRuleContext(D96Parser.ParamsContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(D96Parser.StmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 90
            self.match(D96Parser.LB)
            self.state = 91
            self.params()
            self.state = 92
            self.match(D96Parser.RB)
            self.state = 93
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(D96Parser.StmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(D96Parser.DESTRUCTOR)
            self.state = 96
            self.match(D96Parser.LB)
            self.state = 97
            self.match(D96Parser.RB)
            self.state = 98
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_params




    def params(self):

        localctx = D96Parser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.T__3:
                self.state = 100
                self.match(D96Parser.T__3)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


        def getRuleIndex(self):
            return D96Parser.RULE_stmt




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)

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

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_body




    def body(self):

        localctx = D96Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.funcall()
            self.state = 109
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exp)
        try:
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ALPHABET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.funcall()
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.match(D96Parser.INTLIT)
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


    class FuncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALPHABET(self):
            return self.getToken(D96Parser.ALPHABET, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_funcall




    def funcall(self):

        localctx = D96Parser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(D96Parser.ALPHABET)
            self.state = 116
            self.match(D96Parser.LB)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ALPHABET or _la==D96Parser.INTLIT:
                self.state = 117
                self.exp()


            self.state = 120
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





