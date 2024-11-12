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
        4,1,39,156,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,5,0,
        28,8,0,10,0,12,0,31,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,53,8,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,67,8,1,10,1,12,1,70,9,1,1,
        2,1,2,1,2,1,2,3,2,76,8,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,86,
        8,3,10,3,12,3,89,9,3,1,4,1,4,1,4,1,4,1,4,3,4,96,8,4,1,5,1,5,5,5,
        100,8,5,10,5,12,5,103,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,113,
        8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,122,8,7,1,8,1,8,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,3,9,133,8,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,
        11,1,11,1,11,5,11,145,8,11,10,11,12,11,148,9,11,3,11,150,8,11,1,
        11,1,11,1,12,1,12,1,12,0,1,2,13,0,2,4,6,8,10,12,14,16,18,20,22,24,
        0,6,1,0,3,4,2,0,1,1,5,5,1,0,6,11,1,0,12,13,1,0,25,28,1,0,32,36,167,
        0,29,1,0,0,0,2,52,1,0,0,0,4,71,1,0,0,0,6,82,1,0,0,0,8,90,1,0,0,0,
        10,97,1,0,0,0,12,106,1,0,0,0,14,121,1,0,0,0,16,123,1,0,0,0,18,125,
        1,0,0,0,20,134,1,0,0,0,22,139,1,0,0,0,24,153,1,0,0,0,26,28,3,2,1,
        0,27,26,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,32,
        1,0,0,0,31,29,1,0,0,0,32,33,5,0,0,1,33,1,1,0,0,0,34,35,6,1,-1,0,
        35,53,3,4,2,0,36,53,3,12,6,0,37,53,3,14,7,0,38,53,3,18,9,0,39,53,
        3,10,5,0,40,53,3,22,11,0,41,53,3,24,12,0,42,43,5,1,0,0,43,53,3,2,
        1,9,44,45,5,2,0,0,45,53,3,2,1,8,46,53,3,20,10,0,47,53,5,14,0,0,48,
        49,5,15,0,0,49,50,3,2,1,0,50,51,5,16,0,0,51,53,1,0,0,0,52,34,1,0,
        0,0,52,36,1,0,0,0,52,37,1,0,0,0,52,38,1,0,0,0,52,39,1,0,0,0,52,40,
        1,0,0,0,52,41,1,0,0,0,52,42,1,0,0,0,52,44,1,0,0,0,52,46,1,0,0,0,
        52,47,1,0,0,0,52,48,1,0,0,0,53,68,1,0,0,0,54,55,10,6,0,0,55,56,7,
        0,0,0,56,67,3,2,1,7,57,58,10,5,0,0,58,59,7,1,0,0,59,67,3,2,1,6,60,
        61,10,4,0,0,61,62,7,2,0,0,62,67,3,2,1,5,63,64,10,3,0,0,64,65,7,3,
        0,0,65,67,3,2,1,4,66,54,1,0,0,0,66,57,1,0,0,0,66,60,1,0,0,0,66,63,
        1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,3,1,0,0,0,70,
        68,1,0,0,0,71,72,5,17,0,0,72,73,5,36,0,0,73,75,5,15,0,0,74,76,3,
        6,3,0,75,74,1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,78,5,16,0,0,78,
        79,5,18,0,0,79,80,5,31,0,0,80,81,3,10,5,0,81,5,1,0,0,0,82,87,3,8,
        4,0,83,84,5,19,0,0,84,86,3,8,4,0,85,83,1,0,0,0,86,89,1,0,0,0,87,
        85,1,0,0,0,87,88,1,0,0,0,88,7,1,0,0,0,89,87,1,0,0,0,90,91,5,36,0,
        0,91,92,5,20,0,0,92,95,5,31,0,0,93,94,5,21,0,0,94,96,3,2,1,0,95,
        93,1,0,0,0,95,96,1,0,0,0,96,9,1,0,0,0,97,101,5,22,0,0,98,100,3,2,
        1,0,99,98,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,
        102,104,1,0,0,0,103,101,1,0,0,0,104,105,5,23,0,0,105,11,1,0,0,0,
        106,107,5,24,0,0,107,108,5,36,0,0,108,109,5,20,0,0,109,112,5,31,
        0,0,110,111,5,21,0,0,111,113,3,2,1,0,112,110,1,0,0,0,112,113,1,0,
        0,0,113,13,1,0,0,0,114,115,5,36,0,0,115,116,5,21,0,0,116,122,3,2,
        1,0,117,118,5,36,0,0,118,119,3,16,8,0,119,120,3,2,1,0,120,122,1,
        0,0,0,121,114,1,0,0,0,121,117,1,0,0,0,122,15,1,0,0,0,123,124,7,4,
        0,0,124,17,1,0,0,0,125,126,5,29,0,0,126,127,5,15,0,0,127,128,3,2,
        1,0,128,129,5,16,0,0,129,132,3,10,5,0,130,131,5,30,0,0,131,133,3,
        10,5,0,132,130,1,0,0,0,132,133,1,0,0,0,133,19,1,0,0,0,134,135,5,
        31,0,0,135,136,5,15,0,0,136,137,3,2,1,0,137,138,5,16,0,0,138,21,
        1,0,0,0,139,140,5,36,0,0,140,149,5,15,0,0,141,146,3,2,1,0,142,143,
        5,19,0,0,143,145,3,2,1,0,144,142,1,0,0,0,145,148,1,0,0,0,146,144,
        1,0,0,0,146,147,1,0,0,0,147,150,1,0,0,0,148,146,1,0,0,0,149,141,
        1,0,0,0,149,150,1,0,0,0,150,151,1,0,0,0,151,152,5,16,0,0,152,23,
        1,0,0,0,153,154,7,5,0,0,154,25,1,0,0,0,13,29,52,66,68,75,87,95,101,
        112,121,132,146,149
    ]

class SimpleLangParser ( Parser ):

    grammarFileName = "SimpleLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'not'", "'*'", "'/'", "'+'", "'>'", 
                     "'<'", "'>='", "'<='", "'=='", "'!='", "'and'", "'or'", 
                     "';'", "'('", "')'", "'func'", "'->'", "','", "':'", 
                     "'='", "'{'", "'}'", "'let'", "'+='", "'-='", "'*='", 
                     "'/='", "'if'", "'else'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "Type", "FLOAT", 
                      "INT", "BOOL", "STRING", "IDENTIFIER", "SINGLE_LINE_COMMENT", 
                      "MULTI_LINE_COMMENT", "WS" ]

    RULE_program = 0
    RULE_expr = 1
    RULE_functionDecl = 2
    RULE_paramList = 3
    RULE_parameter = 4
    RULE_block = 5
    RULE_varDecl = 6
    RULE_assignment = 7
    RULE_assignOp = 8
    RULE_ifExpr = 9
    RULE_typeCast = 10
    RULE_functionCall = 11
    RULE_primary = 12

    ruleNames =  [ "program", "expr", "functionDecl", "paramList", "parameter", 
                   "block", "varDecl", "assignment", "assignOp", "ifExpr", 
                   "typeCast", "functionCall", "primary" ]

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
    Type=31
    FLOAT=32
    INT=33
    BOOL=34
    STRING=35
    IDENTIFIER=36
    SINGLE_LINE_COMMENT=37
    MULTI_LINE_COMMENT=38
    WS=39

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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


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
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 135849492486) != 0):
                self.state = 26
                self.expr(0)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self.match(SimpleLangParser.EOF)
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

        def functionDecl(self):
            return self.getTypedRuleContext(SimpleLangParser.FunctionDeclContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(SimpleLangParser.VarDeclContext,0)


        def assignment(self):
            return self.getTypedRuleContext(SimpleLangParser.AssignmentContext,0)


        def ifExpr(self):
            return self.getTypedRuleContext(SimpleLangParser.IfExprContext,0)


        def block(self):
            return self.getTypedRuleContext(SimpleLangParser.BlockContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(SimpleLangParser.FunctionCallContext,0)


        def primary(self):
            return self.getTypedRuleContext(SimpleLangParser.PrimaryContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def typeCast(self):
            return self.getTypedRuleContext(SimpleLangParser.TypeCastContext,0)


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
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 35
                self.functionDecl()
                pass

            elif la_ == 2:
                self.state = 36
                self.varDecl()
                pass

            elif la_ == 3:
                self.state = 37
                self.assignment()
                pass

            elif la_ == 4:
                self.state = 38
                self.ifExpr()
                pass

            elif la_ == 5:
                self.state = 39
                self.block()
                pass

            elif la_ == 6:
                self.state = 40
                self.functionCall()
                pass

            elif la_ == 7:
                self.state = 41
                self.primary()
                pass

            elif la_ == 8:
                self.state = 42
                self.match(SimpleLangParser.T__0)
                self.state = 43
                self.expr(9)
                pass

            elif la_ == 9:
                self.state = 44
                self.match(SimpleLangParser.T__1)
                self.state = 45
                self.expr(8)
                pass

            elif la_ == 10:
                self.state = 46
                self.typeCast()
                pass

            elif la_ == 11:
                self.state = 47
                self.match(SimpleLangParser.T__13)
                pass

            elif la_ == 12:
                self.state = 48
                self.match(SimpleLangParser.T__14)
                self.state = 49
                self.expr(0)
                self.state = 50
                self.match(SimpleLangParser.T__15)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 66
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = SimpleLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 54
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 55
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 56
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = SimpleLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 57
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 58
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==5):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 59
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = SimpleLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 60
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 61
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4032) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 62
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = SimpleLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 63
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 64
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 65
                        self.expr(4)
                        pass

             
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SimpleLangParser.IDENTIFIER, 0)

        def Type(self):
            return self.getToken(SimpleLangParser.Type, 0)

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
        self.enterRule(localctx, 4, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(SimpleLangParser.T__16)
            self.state = 72
            self.match(SimpleLangParser.IDENTIFIER)
            self.state = 73
            self.match(SimpleLangParser.T__14)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 74
                self.paramList()


            self.state = 77
            self.match(SimpleLangParser.T__15)
            self.state = 78
            self.match(SimpleLangParser.T__17)
            self.state = 79
            self.match(SimpleLangParser.Type)
            self.state = 80
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
        self.enterRule(localctx, 6, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.parameter()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 83
                self.match(SimpleLangParser.T__18)
                self.state = 84
                self.parameter()
                self.state = 89
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

        def Type(self):
            return self.getToken(SimpleLangParser.Type, 0)

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
        self.enterRule(localctx, 8, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(SimpleLangParser.IDENTIFIER)
            self.state = 91
            self.match(SimpleLangParser.T__19)
            self.state = 92
            self.match(SimpleLangParser.Type)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 93
                self.match(SimpleLangParser.T__20)
                self.state = 94
                self.expr(0)


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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


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
            self.state = 97
            self.match(SimpleLangParser.T__21)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 135849492486) != 0):
                self.state = 98
                self.expr(0)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self.match(SimpleLangParser.T__22)
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

        def Type(self):
            return self.getToken(SimpleLangParser.Type, 0)

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
        self.enterRule(localctx, 12, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(SimpleLangParser.T__23)
            self.state = 107
            self.match(SimpleLangParser.IDENTIFIER)
            self.state = 108
            self.match(SimpleLangParser.T__19)
            self.state = 109
            self.match(SimpleLangParser.Type)
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 110
                self.match(SimpleLangParser.T__20)
                self.state = 111
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


        def assignOp(self):
            return self.getTypedRuleContext(SimpleLangParser.AssignOpContext,0)


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
        self.enterRule(localctx, 14, self.RULE_assignment)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.match(SimpleLangParser.IDENTIFIER)
                self.state = 115
                self.match(SimpleLangParser.T__20)
                self.state = 116
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(SimpleLangParser.IDENTIFIER)
                self.state = 118
                self.assignOp()
                self.state = 119
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_assignOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignOp" ):
                listener.enterAssignOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignOp" ):
                listener.exitAssignOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignOp" ):
                return visitor.visitAssignOp(self)
            else:
                return visitor.visitChildren(self)




    def assignOp(self):

        localctx = SimpleLangParser.AssignOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 503316480) != 0)):
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


    class IfExprContext(ParserRuleContext):
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
            return SimpleLangParser.RULE_ifExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfExpr" ):
                listener.enterIfExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfExpr" ):
                listener.exitIfExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfExpr" ):
                return visitor.visitIfExpr(self)
            else:
                return visitor.visitChildren(self)




    def ifExpr(self):

        localctx = SimpleLangParser.IfExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(SimpleLangParser.T__28)
            self.state = 126
            self.match(SimpleLangParser.T__14)
            self.state = 127
            self.expr(0)
            self.state = 128
            self.match(SimpleLangParser.T__15)
            self.state = 129
            self.block()
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 130
                self.match(SimpleLangParser.T__29)
                self.state = 131
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeCastContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Type(self):
            return self.getToken(SimpleLangParser.Type, 0)

        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_typeCast

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeCast" ):
                listener.enterTypeCast(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeCast" ):
                listener.exitTypeCast(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeCast" ):
                return visitor.visitTypeCast(self)
            else:
                return visitor.visitChildren(self)




    def typeCast(self):

        localctx = SimpleLangParser.TypeCastContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_typeCast)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(SimpleLangParser.Type)
            self.state = 135
            self.match(SimpleLangParser.T__14)
            self.state = 136
            self.expr(0)
            self.state = 137
            self.match(SimpleLangParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 22, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(SimpleLangParser.IDENTIFIER)
            self.state = 140
            self.match(SimpleLangParser.T__14)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135849492486) != 0):
                self.state = 141
                self.expr(0)
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==19:
                    self.state = 142
                    self.match(SimpleLangParser.T__18)
                    self.state = 143
                    self.expr(0)
                    self.state = 148
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 151
            self.match(SimpleLangParser.T__15)
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
        self.enterRule(localctx, 24, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 133143986176) != 0)):
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
        self._predicates[1] = self.expr_sempred
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
         




