# Generated from ./SimpleLang.g4 by ANTLR 4.13.2
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


    # Enter a parse tree produced by SimpleLangParser#type.
    def enterType(self, ctx:SimpleLangParser.TypeContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#type.
    def exitType(self, ctx:SimpleLangParser.TypeContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#arrayType.
    def enterArrayType(self, ctx:SimpleLangParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#arrayType.
    def exitArrayType(self, ctx:SimpleLangParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#listType.
    def enterListType(self, ctx:SimpleLangParser.ListTypeContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#listType.
    def exitListType(self, ctx:SimpleLangParser.ListTypeContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#block.
    def enterBlock(self, ctx:SimpleLangParser.BlockContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#block.
    def exitBlock(self, ctx:SimpleLangParser.BlockContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#statement.
    def enterStatement(self, ctx:SimpleLangParser.StatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#statement.
    def exitStatement(self, ctx:SimpleLangParser.StatementContext):
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


    # Enter a parse tree produced by SimpleLangParser#arrayOp.
    def enterArrayOp(self, ctx:SimpleLangParser.ArrayOpContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#arrayOp.
    def exitArrayOp(self, ctx:SimpleLangParser.ArrayOpContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#listOp.
    def enterListOp(self, ctx:SimpleLangParser.ListOpContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#listOp.
    def exitListOp(self, ctx:SimpleLangParser.ListOpContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#ifStatement.
    def enterIfStatement(self, ctx:SimpleLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#ifStatement.
    def exitIfStatement(self, ctx:SimpleLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#whileStatement.
    def enterWhileStatement(self, ctx:SimpleLangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#whileStatement.
    def exitWhileStatement(self, ctx:SimpleLangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#returnStmt.
    def enterReturnStmt(self, ctx:SimpleLangParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#returnStmt.
    def exitReturnStmt(self, ctx:SimpleLangParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#commentStmt.
    def enterCommentStmt(self, ctx:SimpleLangParser.CommentStmtContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#commentStmt.
    def exitCommentStmt(self, ctx:SimpleLangParser.CommentStmtContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#expr.
    def enterExpr(self, ctx:SimpleLangParser.ExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#expr.
    def exitExpr(self, ctx:SimpleLangParser.ExprContext):
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