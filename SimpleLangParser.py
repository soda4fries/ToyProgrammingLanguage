# Generated from SimpleLang.g4 by ANTLR 4.13.2
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
        4,1,36,164,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,5,0,33,8,0,10,0,12,0,36,9,0,1,0,1,0,1,1,1,1,1,
        1,1,1,3,1,44,8,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,54,8,2,10,2,
        12,2,57,9,2,1,3,1,3,1,3,1,3,1,3,3,3,64,8,3,1,4,1,4,1,5,1,5,5,5,70,
        8,5,10,5,12,5,73,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,3,6,91,8,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,99,8,
        7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,112,8,9,1,10,1,
        10,3,10,116,8,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,3,12,129,8,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,5,12,143,8,12,10,12,12,12,146,9,12,1,13,1,13,1,
        13,1,13,1,13,5,13,153,8,13,10,13,12,13,156,9,13,3,13,158,8,13,1,
        13,1,13,1,14,1,14,1,14,0,1,24,15,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,0,7,1,0,8,10,1,0,30,31,1,0,19,20,2,0,18,18,21,21,1,0,22,
        27,1,0,28,29,1,0,32,35,171,0,34,1,0,0,0,2,39,1,0,0,0,4,50,1,0,0,
        0,6,58,1,0,0,0,8,65,1,0,0,0,10,67,1,0,0,0,12,90,1,0,0,0,14,92,1,
        0,0,0,16,100,1,0,0,0,18,104,1,0,0,0,20,113,1,0,0,0,22,117,1,0,0,
        0,24,128,1,0,0,0,26,147,1,0,0,0,28,161,1,0,0,0,30,33,3,2,1,0,31,
        33,3,12,6,0,32,30,1,0,0,0,32,31,1,0,0,0,33,36,1,0,0,0,34,32,1,0,
        0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,34,1,0,0,0,37,38,5,0,0,1,38,1,
        1,0,0,0,39,40,5,1,0,0,40,41,5,35,0,0,41,43,5,2,0,0,42,44,3,4,2,0,
        43,42,1,0,0,0,43,44,1,0,0,0,44,45,1,0,0,0,45,46,5,3,0,0,46,47,5,
        4,0,0,47,48,3,8,4,0,48,49,3,10,5,0,49,3,1,0,0,0,50,55,3,6,3,0,51,
        52,5,5,0,0,52,54,3,6,3,0,53,51,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,
        0,55,56,1,0,0,0,56,5,1,0,0,0,57,55,1,0,0,0,58,59,5,35,0,0,59,60,
        5,6,0,0,60,63,3,8,4,0,61,62,5,7,0,0,62,64,3,24,12,0,63,61,1,0,0,
        0,63,64,1,0,0,0,64,7,1,0,0,0,65,66,7,0,0,0,66,9,1,0,0,0,67,71,5,
        11,0,0,68,70,3,12,6,0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,
        71,72,1,0,0,0,72,74,1,0,0,0,73,71,1,0,0,0,74,75,5,12,0,0,75,11,1,
        0,0,0,76,77,3,14,7,0,77,78,5,13,0,0,78,91,1,0,0,0,79,80,3,16,8,0,
        80,81,5,13,0,0,81,91,1,0,0,0,82,83,3,26,13,0,83,84,5,13,0,0,84,91,
        1,0,0,0,85,86,3,20,10,0,86,87,5,13,0,0,87,91,1,0,0,0,88,91,3,18,
        9,0,89,91,3,22,11,0,90,76,1,0,0,0,90,79,1,0,0,0,90,82,1,0,0,0,90,
        85,1,0,0,0,90,88,1,0,0,0,90,89,1,0,0,0,91,13,1,0,0,0,92,93,5,14,
        0,0,93,94,5,35,0,0,94,95,5,6,0,0,95,98,3,8,4,0,96,97,5,7,0,0,97,
        99,3,24,12,0,98,96,1,0,0,0,98,99,1,0,0,0,99,15,1,0,0,0,100,101,5,
        35,0,0,101,102,5,7,0,0,102,103,3,24,12,0,103,17,1,0,0,0,104,105,
        5,15,0,0,105,106,5,2,0,0,106,107,3,24,12,0,107,108,5,3,0,0,108,111,
        3,10,5,0,109,110,5,16,0,0,110,112,3,10,5,0,111,109,1,0,0,0,111,112,
        1,0,0,0,112,19,1,0,0,0,113,115,5,17,0,0,114,116,3,24,12,0,115,114,
        1,0,0,0,115,116,1,0,0,0,116,21,1,0,0,0,117,118,7,1,0,0,118,23,1,
        0,0,0,119,120,6,12,-1,0,120,129,3,26,13,0,121,129,3,28,14,0,122,
        123,5,18,0,0,123,129,3,24,12,6,124,125,5,2,0,0,125,126,3,24,12,0,
        126,127,5,3,0,0,127,129,1,0,0,0,128,119,1,0,0,0,128,121,1,0,0,0,
        128,122,1,0,0,0,128,124,1,0,0,0,129,144,1,0,0,0,130,131,10,5,0,0,
        131,132,7,2,0,0,132,143,3,24,12,6,133,134,10,4,0,0,134,135,7,3,0,
        0,135,143,3,24,12,5,136,137,10,3,0,0,137,138,7,4,0,0,138,143,3,24,
        12,4,139,140,10,2,0,0,140,141,7,5,0,0,141,143,3,24,12,3,142,130,
        1,0,0,0,142,133,1,0,0,0,142,136,1,0,0,0,142,139,1,0,0,0,143,146,
        1,0,0,0,144,142,1,0,0,0,144,145,1,0,0,0,145,25,1,0,0,0,146,144,1,
        0,0,0,147,148,5,35,0,0,148,157,5,2,0,0,149,154,3,24,12,0,150,151,
        5,5,0,0,151,153,3,24,12,0,152,150,1,0,0,0,153,156,1,0,0,0,154,152,
        1,0,0,0,154,155,1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,157,149,
        1,0,0,0,157,158,1,0,0,0,158,159,1,0,0,0,159,160,5,3,0,0,160,27,1,
        0,0,0,161,162,7,6,0,0,162,29,1,0,0,0,15,32,34,43,55,63,71,90,98,
        111,115,128,142,144,154,157
    ]

class SimpleLangParser ( Parser ):

    grammarFileName = "SimpleLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'func'", "'('", "')'", "'->'", "','", 
                     "':'", "'='", "'int'", "'bool'", "'string'", "'{'", 
                     "'}'", "';'", "'let'", "'if'", "'else'", "'return'", 
                     "'-'", "'*'", "'/'", "'+'", "'>'", "'<'", "'>='", "'<='", 
                     "'=='", "'!='", "'and'", "'or'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", 
                      "INT", "BOOL", "STRING", "IDENTIFIER", "WS" ]

    RULE_program = 0
    RULE_functionDecl = 1
    RULE_paramList = 2
    RULE_parameter = 3
    RULE_type = 4
    RULE_block = 5
    RULE_statement = 6
    RULE_varDecl = 7
    RULE_assignment = 8
    RULE_ifStatement = 9
    RULE_returnStmt = 10
    RULE_commentStmt = 11
    RULE_expr = 12
    RULE_functionCall = 13
    RULE_primary = 14

    ruleNames =  [ "program", "functionDecl", "paramList", "parameter", 
                   "type", "block", "statement", "varDecl", "assignment", 
                   "ifStatement", "returnStmt", "commentStmt", "expr", "functionCall", 
                   "primary" ]

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
    SINGLE_LINE_COMMENT=30
    MULTI_LINE_COMMENT=31
    INT=32
    BOOL=33
    STRING=34
    IDENTIFIER=35
    WS=36

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
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 37581144066) != 0):
                self.state = 32
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 30
                    self.functionDecl()
                    pass
                elif token in [14, 15, 17, 30, 31, 35]:
                    self.state = 31
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
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
            self.state = 39
            self.match(SimpleLangParser.T__0)
            self.state = 40
            self.match(SimpleLangParser.IDENTIFIER)
            self.state = 41
            self.match(SimpleLangParser.T__1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 42
                self.paramList()


            self.state = 45
            self.match(SimpleLangParser.T__2)
            self.state = 46
            self.match(SimpleLangParser.T__3)
            self.state = 47
            self.type_()
            self.state = 48
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
            self.state = 50
            self.parameter()
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 51
                self.match(SimpleLangParser.T__4)
                self.state = 52
                self.parameter()
                self.state = 57
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
            self.state = 58
            self.match(SimpleLangParser.IDENTIFIER)
            self.state = 59
            self.match(SimpleLangParser.T__5)
            self.state = 60
            self.type_()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 61
                self.match(SimpleLangParser.T__6)
                self.state = 62
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0)):
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
        self.enterRule(localctx, 10, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(SimpleLangParser.T__10)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 37581144064) != 0):
                self.state = 68
                self.statement()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(SimpleLangParser.T__11)
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
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.varDecl()
                self.state = 77
                self.match(SimpleLangParser.T__12)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.assignment()
                self.state = 80
                self.match(SimpleLangParser.T__12)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.functionCall()
                self.state = 83
                self.match(SimpleLangParser.T__12)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 85
                self.returnStmt()
                self.state = 86
                self.match(SimpleLangParser.T__12)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 88
                self.ifStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 89
                self.commentStmt()
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
        self.enterRule(localctx, 14, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(SimpleLangParser.T__13)
            self.state = 93
            self.match(SimpleLangParser.IDENTIFIER)
            self.state = 94
            self.match(SimpleLangParser.T__5)
            self.state = 95
            self.type_()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 96
                self.match(SimpleLangParser.T__6)
                self.state = 97
                self.expr(0)


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

        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


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
        self.enterRule(localctx, 16, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(SimpleLangParser.IDENTIFIER)
            self.state = 101
            self.match(SimpleLangParser.T__6)
            self.state = 102
            self.expr(0)
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
        self.enterRule(localctx, 18, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(SimpleLangParser.T__14)
            self.state = 105
            self.match(SimpleLangParser.T__1)
            self.state = 106
            self.expr(0)
            self.state = 107
            self.match(SimpleLangParser.T__2)
            self.state = 108
            self.block()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 109
                self.match(SimpleLangParser.T__15)
                self.state = 110
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
        self.enterRule(localctx, 20, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(SimpleLangParser.T__16)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 64424771588) != 0):
                self.state = 114
                self.expr(0)


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
        self.enterRule(localctx, 22, self.RULE_commentStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            _la = self._input.LA(1)
            if not(_la==30 or _la==31):
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 120
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 121
                self.primary()
                pass

            elif la_ == 3:
                self.state = 122
                self.match(SimpleLangParser.T__17)
                self.state = 123
                self.expr(6)
                pass

            elif la_ == 4:
                self.state = 124
                self.match(SimpleLangParser.T__1)
                self.state = 125
                self.expr(0)
                self.state = 126
                self.match(SimpleLangParser.T__2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 144
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 142
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = SimpleLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 130
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 131
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 132
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = SimpleLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 133
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 134
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==21):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 135
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = SimpleLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 136
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 137
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 264241152) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 138
                        self.expr(4)
                        pass

                    elif la_ == 4:
                        localctx = SimpleLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 139
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 140
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==28 or _la==29):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 141
                        self.expr(3)
                        pass

             
                self.state = 146
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self.enterRule(localctx, 26, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(SimpleLangParser.IDENTIFIER)
            self.state = 148
            self.match(SimpleLangParser.T__1)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 64424771588) != 0):
                self.state = 149
                self.expr(0)
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 150
                    self.match(SimpleLangParser.T__4)
                    self.state = 151
                    self.expr(0)
                    self.state = 156
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 159
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
        self.enterRule(localctx, 28, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 64424509440) != 0)):
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
        self._predicates[12] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




