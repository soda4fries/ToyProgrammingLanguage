# Generated from ./SimpleLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,53,270,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,5,0,43,8,0,10,0,12,0,46,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,54,8,
        1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,64,8,2,10,2,12,2,67,9,2,1,
        3,1,3,1,3,1,3,1,3,3,3,74,8,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,82,8,4,
        1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,5,7,96,8,7,10,7,
        12,7,99,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,3,8,115,8,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,123,8,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,10,3,10,132,8,10,1,10,1,10,1,10,1,10,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,163,8,11,
        1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,3,12,182,8,12,1,12,1,12,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,3,13,193,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,
        1,15,3,15,203,8,15,1,15,1,15,1,16,1,16,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,5,17,218,8,17,10,17,12,17,221,9,17,3,17,223,
        8,17,1,17,1,17,1,17,1,17,1,17,3,17,230,8,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        5,17,249,8,17,10,17,12,17,252,9,17,1,18,1,18,1,18,1,18,1,18,5,18,
        259,8,18,10,18,12,18,262,9,18,3,18,264,8,18,1,18,1,18,1,19,1,19,
        1,19,0,1,34,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,0,6,1,0,46,47,1,0,37,38,2,0,36,36,39,39,2,0,13,14,40,43,1,
        0,44,45,1,0,48,52,294,0,44,1,0,0,0,2,49,1,0,0,0,4,60,1,0,0,0,6,68,
        1,0,0,0,8,81,1,0,0,0,10,83,1,0,0,0,12,88,1,0,0,0,14,93,1,0,0,0,16,
        114,1,0,0,0,18,116,1,0,0,0,20,126,1,0,0,0,22,137,1,0,0,0,24,166,
        1,0,0,0,26,185,1,0,0,0,28,194,1,0,0,0,30,200,1,0,0,0,32,206,1,0,
        0,0,34,229,1,0,0,0,36,253,1,0,0,0,38,267,1,0,0,0,40,43,3,2,1,0,41,
        43,3,16,8,0,42,40,1,0,0,0,42,41,1,0,0,0,43,46,1,0,0,0,44,42,1,0,
        0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,44,1,0,0,0,47,48,5,0,0,1,48,1,
        1,0,0,0,49,50,5,1,0,0,50,51,5,52,0,0,51,53,5,2,0,0,52,54,3,4,2,0,
        53,52,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,5,3,0,0,56,57,5,
        4,0,0,57,58,3,8,4,0,58,59,3,14,7,0,59,3,1,0,0,0,60,65,3,6,3,0,61,
        62,5,5,0,0,62,64,3,6,3,0,63,61,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,
        0,65,66,1,0,0,0,66,5,1,0,0,0,67,65,1,0,0,0,68,69,5,52,0,0,69,70,
        5,6,0,0,70,73,3,8,4,0,71,72,5,7,0,0,72,74,3,34,17,0,73,71,1,0,0,
        0,73,74,1,0,0,0,74,7,1,0,0,0,75,82,5,8,0,0,76,82,5,9,0,0,77,82,5,
        10,0,0,78,82,5,11,0,0,79,82,3,10,5,0,80,82,3,12,6,0,81,75,1,0,0,
        0,81,76,1,0,0,0,81,77,1,0,0,0,81,78,1,0,0,0,81,79,1,0,0,0,81,80,
        1,0,0,0,82,9,1,0,0,0,83,84,5,12,0,0,84,85,5,13,0,0,85,86,3,8,4,0,
        86,87,5,14,0,0,87,11,1,0,0,0,88,89,5,15,0,0,89,90,5,13,0,0,90,91,
        3,8,4,0,91,92,5,14,0,0,92,13,1,0,0,0,93,97,5,16,0,0,94,96,3,16,8,
        0,95,94,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,100,
        1,0,0,0,99,97,1,0,0,0,100,101,5,17,0,0,101,15,1,0,0,0,102,115,3,
        18,9,0,103,115,3,20,10,0,104,105,3,36,18,0,105,106,5,18,0,0,106,
        115,1,0,0,0,107,115,3,30,15,0,108,115,3,26,13,0,109,115,3,32,16,
        0,110,115,3,22,11,0,111,115,3,24,12,0,112,115,3,28,14,0,113,115,
        3,14,7,0,114,102,1,0,0,0,114,103,1,0,0,0,114,104,1,0,0,0,114,107,
        1,0,0,0,114,108,1,0,0,0,114,109,1,0,0,0,114,110,1,0,0,0,114,111,
        1,0,0,0,114,112,1,0,0,0,114,113,1,0,0,0,115,17,1,0,0,0,116,117,5,
        19,0,0,117,118,5,52,0,0,118,119,5,6,0,0,119,122,3,8,4,0,120,121,
        5,7,0,0,121,123,3,34,17,0,122,120,1,0,0,0,122,123,1,0,0,0,123,124,
        1,0,0,0,124,125,5,18,0,0,125,19,1,0,0,0,126,131,5,52,0,0,127,128,
        5,20,0,0,128,129,3,34,17,0,129,130,5,21,0,0,130,132,1,0,0,0,131,
        127,1,0,0,0,131,132,1,0,0,0,132,133,1,0,0,0,133,134,5,7,0,0,134,
        135,3,34,17,0,135,136,5,18,0,0,136,21,1,0,0,0,137,138,5,52,0,0,138,
        162,5,22,0,0,139,140,5,23,0,0,140,141,5,2,0,0,141,163,5,3,0,0,142,
        143,5,24,0,0,143,144,5,2,0,0,144,163,5,3,0,0,145,146,5,25,0,0,146,
        147,5,2,0,0,147,163,5,3,0,0,148,149,5,26,0,0,149,150,5,2,0,0,150,
        163,5,3,0,0,151,152,5,27,0,0,152,153,5,2,0,0,153,163,5,3,0,0,154,
        155,5,28,0,0,155,156,5,2,0,0,156,163,5,3,0,0,157,158,5,29,0,0,158,
        159,5,2,0,0,159,160,3,34,17,0,160,161,5,3,0,0,161,163,1,0,0,0,162,
        139,1,0,0,0,162,142,1,0,0,0,162,145,1,0,0,0,162,148,1,0,0,0,162,
        151,1,0,0,0,162,154,1,0,0,0,162,157,1,0,0,0,163,164,1,0,0,0,164,
        165,5,18,0,0,165,23,1,0,0,0,166,167,5,52,0,0,167,181,5,22,0,0,168,
        169,5,30,0,0,169,170,5,2,0,0,170,171,3,34,17,0,171,172,5,3,0,0,172,
        182,1,0,0,0,173,174,5,31,0,0,174,175,5,2,0,0,175,176,3,34,17,0,176,
        177,5,3,0,0,177,182,1,0,0,0,178,179,5,23,0,0,179,180,5,2,0,0,180,
        182,5,3,0,0,181,168,1,0,0,0,181,173,1,0,0,0,181,178,1,0,0,0,182,
        183,1,0,0,0,183,184,5,18,0,0,184,25,1,0,0,0,185,186,5,32,0,0,186,
        187,5,2,0,0,187,188,3,34,17,0,188,189,5,3,0,0,189,192,3,14,7,0,190,
        191,5,33,0,0,191,193,3,14,7,0,192,190,1,0,0,0,192,193,1,0,0,0,193,
        27,1,0,0,0,194,195,5,34,0,0,195,196,5,2,0,0,196,197,3,34,17,0,197,
        198,5,3,0,0,198,199,3,14,7,0,199,29,1,0,0,0,200,202,5,35,0,0,201,
        203,3,34,17,0,202,201,1,0,0,0,202,203,1,0,0,0,203,204,1,0,0,0,204,
        205,5,18,0,0,205,31,1,0,0,0,206,207,7,0,0,0,207,33,1,0,0,0,208,209,
        6,17,-1,0,209,230,3,36,18,0,210,230,3,38,19,0,211,212,5,36,0,0,212,
        230,3,34,17,8,213,222,5,20,0,0,214,219,3,34,17,0,215,216,5,5,0,0,
        216,218,3,34,17,0,217,215,1,0,0,0,218,221,1,0,0,0,219,217,1,0,0,
        0,219,220,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,222,214,1,0,0,
        0,222,223,1,0,0,0,223,224,1,0,0,0,224,230,5,21,0,0,225,226,5,2,0,
        0,226,227,3,34,17,0,227,228,5,3,0,0,228,230,1,0,0,0,229,208,1,0,
        0,0,229,210,1,0,0,0,229,211,1,0,0,0,229,213,1,0,0,0,229,225,1,0,
        0,0,230,250,1,0,0,0,231,232,10,6,0,0,232,233,7,1,0,0,233,249,3,34,
        17,7,234,235,10,5,0,0,235,236,7,2,0,0,236,249,3,34,17,6,237,238,
        10,4,0,0,238,239,7,3,0,0,239,249,3,34,17,5,240,241,10,3,0,0,241,
        242,7,4,0,0,242,249,3,34,17,4,243,244,10,7,0,0,244,245,5,20,0,0,
        245,246,3,34,17,0,246,247,5,21,0,0,247,249,1,0,0,0,248,231,1,0,0,
        0,248,234,1,0,0,0,248,237,1,0,0,0,248,240,1,0,0,0,248,243,1,0,0,
        0,249,252,1,0,0,0,250,248,1,0,0,0,250,251,1,0,0,0,251,35,1,0,0,0,
        252,250,1,0,0,0,253,254,5,52,0,0,254,263,5,2,0,0,255,260,3,34,17,
        0,256,257,5,5,0,0,257,259,3,34,17,0,258,256,1,0,0,0,259,262,1,0,
        0,0,260,258,1,0,0,0,260,261,1,0,0,0,261,264,1,0,0,0,262,260,1,0,
        0,0,263,255,1,0,0,0,263,264,1,0,0,0,264,265,1,0,0,0,265,266,5,3,
        0,0,266,37,1,0,0,0,267,268,7,5,0,0,268,39,1,0,0,0,21,42,44,53,65,
        73,81,97,114,122,131,162,181,192,202,219,222,229,248,250,260,263
    ]

class SimpleLangParser ( Parser ):

    grammarFileName = "SimpleLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'func'", "'('", "')'", "'->'", "','", 
                     "':'", "'='", "'int'", "'bool'", "'string'", "'float'", 
                     "'array'", "'<'", "'>'", "'list'", "'{'", "'}'", "';'", 
                     "'let'", "'['", "']'", "'.'", "'sort'", "'mean'", "'median'", 
                     "'variance'", "'stddev'", "'play'", "'linreg'", "'append'", 
                     "'remove'", "'if'", "'else'", "'while'", "'return'", 
                     "'-'", "'*'", "'/'", "'+'", "'>='", "'<='", "'=='", 
                     "'!='", "'and'", "'or'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", 
                      "INT", "FLOAT", "BOOL", "STRING", "IDENTIFIER", "WS" ]

    RULE_program = 0
    RULE_functionDecl = 1
    RULE_paramList = 2
    RULE_parameter = 3
    RULE_type = 4
    RULE_arrayType = 5
    RULE_listType = 6
    RULE_block = 7
    RULE_statement = 8
    RULE_varDecl = 9
    RULE_assignment = 10
    RULE_arrayOp = 11
    RULE_listOp = 12
    RULE_ifStatement = 13
    RULE_whileStatement = 14
    RULE_returnStmt = 15
    RULE_commentStmt = 16
    RULE_expr = 17
    RULE_functionCall = 18
    RULE_primary = 19

    ruleNames =  [ "program", "functionDecl", "paramList", "parameter", 
                   "type", "arrayType", "listType", "block", "statement", 
                   "varDecl", "assignment", "arrayOp", "listOp", "ifStatement", 
                   "whileStatement", "returnStmt", "commentStmt", "expr", 
                   "functionCall", "primary" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    SINGLE_LINE_COMMENT=46
    MULTI_LINE_COMMENT=47
    INT=48
    FLOAT=49
    BOOL=50
    STRING=51
    IDENTIFIER=52
    WS=53

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SimpleLangParser.EOF, 0)

        def functionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.FunctionDeclContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.FunctionDeclContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.StatementContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SimpleLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4714761695068162) != 0):
                self.state = 42
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 40
                    self.functionDecl()
                    pass
                elif token in [16, 19, 32, 34, 35, 46, 47, 52]:
                    self.state = 41
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 47
            self.match(SimpleLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SimpleLangParser.IDENTIFIER, 0)

        def type_(self):
            return self.getTypedRuleContext(SimpleLangParser.TypeContext,0)


        def block(self):
            return self.getTypedRuleContext(SimpleLangParser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(SimpleLangParser.ParamListContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = SimpleLangParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(SimpleLangParser.T__0)
            self.state = 50
            self.match(SimpleLangParser.IDENTIFIER)
            self.state = 51
            self.match(SimpleLangParser.T__1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 52
                self.paramList()


            self.state = 55
            self.match(SimpleLangParser.T__2)
            self.state = 56
            self.match(SimpleLangParser.T__3)
            self.state = 57
            self.type_()
            self.state = 58
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ParameterContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ParameterContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = SimpleLangParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.parameter()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 61
                self.match(SimpleLangParser.T__4)
                self.state = 62
                self.parameter()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SimpleLangParser.IDENTIFIER, 0)

        def type_(self):
            return self.getTypedRuleContext(SimpleLangParser.TypeContext,0)


        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = SimpleLangParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(SimpleLangParser.IDENTIFIER)
            self.state = 69
            self.match(SimpleLangParser.T__5)
            self.state = 70
            self.type_()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 71
                self.match(SimpleLangParser.T__6)
                self.state = 72
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayType(self):
            return self.getTypedRuleContext(SimpleLangParser.ArrayTypeContext,0)


        def listType(self):
            return self.getTypedRuleContext(SimpleLangParser.ListTypeContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = SimpleLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.match(SimpleLangParser.T__7)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.match(SimpleLangParser.T__8)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.match(SimpleLangParser.T__9)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.match(SimpleLangParser.T__10)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 79
                self.arrayType()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 6)
                self.state = 80
                self.listType()
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


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(SimpleLangParser.TypeContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_arrayType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayType" ):
                listener.enterArrayType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayType" ):
                listener.exitArrayType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = SimpleLangParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(SimpleLangParser.T__11)
            self.state = 84
            self.match(SimpleLangParser.T__12)
            self.state = 85
            self.type_()
            self.state = 86
            self.match(SimpleLangParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(SimpleLangParser.TypeContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_listType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListType" ):
                listener.enterListType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListType" ):
                listener.exitListType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListType" ):
                return visitor.visitListType(self)
            else:
                return visitor.visitChildren(self)




    def listType(self):

        localctx = SimpleLangParser.ListTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_listType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(SimpleLangParser.T__14)
            self.state = 89
            self.match(SimpleLangParser.T__12)
            self.state = 90
            self.type_()
            self.state = 91
            self.match(SimpleLangParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.StatementContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = SimpleLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(SimpleLangParser.T__15)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4714761695068160) != 0):
                self.state = 94
                self.statement()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
            self.match(SimpleLangParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(SimpleLangParser.VarDeclContext,0)


        def assignment(self):
            return self.getTypedRuleContext(SimpleLangParser.AssignmentContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(SimpleLangParser.FunctionCallContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(SimpleLangParser.ReturnStmtContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(SimpleLangParser.IfStatementContext,0)


        def commentStmt(self):
            return self.getTypedRuleContext(SimpleLangParser.CommentStmtContext,0)


        def arrayOp(self):
            return self.getTypedRuleContext(SimpleLangParser.ArrayOpContext,0)


        def listOp(self):
            return self.getTypedRuleContext(SimpleLangParser.ListOpContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(SimpleLangParser.WhileStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(SimpleLangParser.BlockContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SimpleLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement)
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                self.functionCall()
                self.state = 105
                self.match(SimpleLangParser.T__17)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 107
                self.returnStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 108
                self.ifStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 109
                self.commentStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 110
                self.arrayOp()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 111
                self.listOp()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 112
                self.whileStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 113
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SimpleLangParser.IDENTIFIER, 0)

        def type_(self):
            return self.getTypedRuleContext(SimpleLangParser.TypeContext,0)


        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = SimpleLangParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(SimpleLangParser.T__18)
            self.state = 117
            self.match(SimpleLangParser.IDENTIFIER)
            self.state = 118
            self.match(SimpleLangParser.T__5)
            self.state = 119
            self.type_()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 120
                self.match(SimpleLangParser.T__6)
                self.state = 121
                self.expr(0)


            self.state = 124
            self.match(SimpleLangParser.T__17)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SimpleLangParser.IDENTIFIER, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = SimpleLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(SimpleLangParser.IDENTIFIER)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 127
                self.match(SimpleLangParser.T__19)
                self.state = 128
                self.expr(0)
                self.state = 129
                self.match(SimpleLangParser.T__20)


            self.state = 133
            self.match(SimpleLangParser.T__6)
            self.state = 134
            self.expr(0)
            self.state = 135
            self.match(SimpleLangParser.T__17)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SimpleLangParser.IDENTIFIER, 0)

        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_arrayOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayOp" ):
                listener.enterArrayOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayOp" ):
                listener.exitArrayOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayOp" ):
                return visitor.visitArrayOp(self)
            else:
                return visitor.visitChildren(self)




    def arrayOp(self):

        localctx = SimpleLangParser.ArrayOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arrayOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(SimpleLangParser.IDENTIFIER)
            self.state = 138
            self.match(SimpleLangParser.T__21)
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.state = 139
                self.match(SimpleLangParser.T__22)
                self.state = 140
                self.match(SimpleLangParser.T__1)
                self.state = 141
                self.match(SimpleLangParser.T__2)
                pass
            elif token in [24]:
                self.state = 142
                self.match(SimpleLangParser.T__23)
                self.state = 143
                self.match(SimpleLangParser.T__1)
                self.state = 144
                self.match(SimpleLangParser.T__2)
                pass
            elif token in [25]:
                self.state = 145
                self.match(SimpleLangParser.T__24)
                self.state = 146
                self.match(SimpleLangParser.T__1)
                self.state = 147
                self.match(SimpleLangParser.T__2)
                pass
            elif token in [26]:
                self.state = 148
                self.match(SimpleLangParser.T__25)
                self.state = 149
                self.match(SimpleLangParser.T__1)
                self.state = 150
                self.match(SimpleLangParser.T__2)
                pass
            elif token in [27]:
                self.state = 151
                self.match(SimpleLangParser.T__26)
                self.state = 152
                self.match(SimpleLangParser.T__1)
                self.state = 153
                self.match(SimpleLangParser.T__2)
                pass
            elif token in [28]:
                self.state = 154
                self.match(SimpleLangParser.T__27)
                self.state = 155
                self.match(SimpleLangParser.T__1)
                self.state = 156
                self.match(SimpleLangParser.T__2)
                pass
            elif token in [29]:
                self.state = 157
                self.match(SimpleLangParser.T__28)
                self.state = 158
                self.match(SimpleLangParser.T__1)
                self.state = 159
                self.expr(0)
                self.state = 160
                self.match(SimpleLangParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 164
            self.match(SimpleLangParser.T__17)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SimpleLangParser.IDENTIFIER, 0)

        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_listOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListOp" ):
                listener.enterListOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListOp" ):
                listener.exitListOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListOp" ):
                return visitor.visitListOp(self)
            else:
                return visitor.visitChildren(self)




    def listOp(self):

        localctx = SimpleLangParser.ListOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_listOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(SimpleLangParser.IDENTIFIER)
            self.state = 167
            self.match(SimpleLangParser.T__21)
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.state = 168
                self.match(SimpleLangParser.T__29)
                self.state = 169
                self.match(SimpleLangParser.T__1)
                self.state = 170
                self.expr(0)
                self.state = 171
                self.match(SimpleLangParser.T__2)
                pass
            elif token in [31]:
                self.state = 173
                self.match(SimpleLangParser.T__30)
                self.state = 174
                self.match(SimpleLangParser.T__1)
                self.state = 175
                self.expr(0)
                self.state = 176
                self.match(SimpleLangParser.T__2)
                pass
            elif token in [23]:
                self.state = 178
                self.match(SimpleLangParser.T__22)
                self.state = 179
                self.match(SimpleLangParser.T__1)
                self.state = 180
                self.match(SimpleLangParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 183
            self.match(SimpleLangParser.T__17)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.BlockContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = SimpleLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(SimpleLangParser.T__31)
            self.state = 186
            self.match(SimpleLangParser.T__1)
            self.state = 187
            self.expr(0)
            self.state = 188
            self.match(SimpleLangParser.T__2)
            self.state = 189
            self.block()
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 190
                self.match(SimpleLangParser.T__32)
                self.state = 191
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(SimpleLangParser.BlockContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = SimpleLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(SimpleLangParser.T__33)
            self.state = 195
            self.match(SimpleLangParser.T__1)
            self.state = 196
            self.expr(0)
            self.state = 197
            self.match(SimpleLangParser.T__2)
            self.state = 198
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = SimpleLangParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(SimpleLangParser.T__34)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8725792998555652) != 0):
                self.state = 201
                self.expr(0)


            self.state = 204
            self.match(SimpleLangParser.T__17)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_LINE_COMMENT(self):
            return self.getToken(SimpleLangParser.SINGLE_LINE_COMMENT, 0)

        def MULTI_LINE_COMMENT(self):
            return self.getToken(SimpleLangParser.MULTI_LINE_COMMENT, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_commentStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentStmt" ):
                listener.enterCommentStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentStmt" ):
                listener.exitCommentStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommentStmt" ):
                return visitor.visitCommentStmt(self)
            else:
                return visitor.visitChildren(self)




    def commentStmt(self):

        localctx = SimpleLangParser.CommentStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_commentStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            _la = self._input.LA(1)
            if not(_la==46 or _la==47):
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def functionCall(self):
            return self.getTypedRuleContext(SimpleLangParser.FunctionCallContext,0)


        def primary(self):
            return self.getTypedRuleContext(SimpleLangParser.PrimaryContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 209
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 210
                self.primary()
                pass

            elif la_ == 3:
                self.state = 211
                self.match(SimpleLangParser.T__35)
                self.state = 212
                self.expr(8)
                pass

            elif la_ == 4:
                self.state = 213
                self.match(SimpleLangParser.T__19)
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8725792998555652) != 0):
                    self.state = 214
                    self.expr(0)
                    self.state = 219
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==5:
                        self.state = 215
                        self.match(SimpleLangParser.T__4)
                        self.state = 216
                        self.expr(0)
                        self.state = 221
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 224
                self.match(SimpleLangParser.T__20)
                pass

            elif la_ == 5:
                self.state = 225
                self.match(SimpleLangParser.T__1)
                self.state = 226
                self.expr(0)
                self.state = 227
                self.match(SimpleLangParser.T__2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 250
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 248
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = SimpleLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 231
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 232
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==37 or _la==38):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 233
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = SimpleLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 234
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 235
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==36 or _la==39):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 236
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = SimpleLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 237
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 238
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16492674441216) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 239
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = SimpleLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 240
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 241
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==44 or _la==45):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 242
                        self.expr(4)
                        pass

                    elif la_ == 5:
                        localctx = SimpleLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 243
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 244
                        self.match(SimpleLangParser.T__19)
                        self.state = 245
                        self.expr(0)
                        self.state = 246
                        self.match(SimpleLangParser.T__20)
                        pass

             
                self.state = 252
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SimpleLangParser.IDENTIFIER, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = SimpleLangParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(SimpleLangParser.IDENTIFIER)
            self.state = 254
            self.match(SimpleLangParser.T__1)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8725792998555652) != 0):
                self.state = 255
                self.expr(0)
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 256
                    self.match(SimpleLangParser.T__4)
                    self.state = 257
                    self.expr(0)
                    self.state = 262
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 265
            self.match(SimpleLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(SimpleLangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(SimpleLangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(SimpleLangParser.BOOL, 0)

        def STRING(self):
            return self.getToken(SimpleLangParser.STRING, 0)

        def IDENTIFIER(self):
            return self.getToken(SimpleLangParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = SimpleLangParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8725724278030336) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         




