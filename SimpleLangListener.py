# Generated from SimpleLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete listener for a parse tree produced by SimpleLangParser.
class SimpleLangListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleLangParser#program.
    def enterProgram(self, ctx:SimpleLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#program.
    def exitProgram(self, ctx:SimpleLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#expr.
    def enterExpr(self, ctx:SimpleLangParser.ExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#expr.
    def exitExpr(self, ctx:SimpleLangParser.ExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#functionDecl.
    def enterFunctionDecl(self, ctx:SimpleLangParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#functionDecl.
    def exitFunctionDecl(self, ctx:SimpleLangParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#paramList.
    def enterParamList(self, ctx:SimpleLangParser.ParamListContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#paramList.
    def exitParamList(self, ctx:SimpleLangParser.ParamListContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#parameter.
    def enterParameter(self, ctx:SimpleLangParser.ParameterContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#parameter.
    def exitParameter(self, ctx:SimpleLangParser.ParameterContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#block.
    def enterBlock(self, ctx:SimpleLangParser.BlockContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#block.
    def exitBlock(self, ctx:SimpleLangParser.BlockContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#varDecl.
    def enterVarDecl(self, ctx:SimpleLangParser.VarDeclContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#varDecl.
    def exitVarDecl(self, ctx:SimpleLangParser.VarDeclContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#assignment.
    def enterAssignment(self, ctx:SimpleLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#assignment.
    def exitAssignment(self, ctx:SimpleLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#assignOp.
    def enterAssignOp(self, ctx:SimpleLangParser.AssignOpContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#assignOp.
    def exitAssignOp(self, ctx:SimpleLangParser.AssignOpContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#ifExpr.
    def enterIfExpr(self, ctx:SimpleLangParser.IfExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#ifExpr.
    def exitIfExpr(self, ctx:SimpleLangParser.IfExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#typeCast.
    def enterTypeCast(self, ctx:SimpleLangParser.TypeCastContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#typeCast.
    def exitTypeCast(self, ctx:SimpleLangParser.TypeCastContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#functionCall.
    def enterFunctionCall(self, ctx:SimpleLangParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#functionCall.
    def exitFunctionCall(self, ctx:SimpleLangParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#primary.
    def enterPrimary(self, ctx:SimpleLangParser.PrimaryContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#primary.
    def exitPrimary(self, ctx:SimpleLangParser.PrimaryContext):
        pass



del SimpleLangParser