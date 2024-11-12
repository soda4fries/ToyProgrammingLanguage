# Generated from SimpleLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete generic visitor for a parse tree produced by SimpleLangParser.

class SimpleLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleLangParser#program.
    def visitProgram(self, ctx:SimpleLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#functionDecl.
    def visitFunctionDecl(self, ctx:SimpleLangParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#paramList.
    def visitParamList(self, ctx:SimpleLangParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#parameter.
    def visitParameter(self, ctx:SimpleLangParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#type.
    def visitType(self, ctx:SimpleLangParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#block.
    def visitBlock(self, ctx:SimpleLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#statement.
    def visitStatement(self, ctx:SimpleLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#varDecl.
    def visitVarDecl(self, ctx:SimpleLangParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#assignment.
    def visitAssignment(self, ctx:SimpleLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#ifStatement.
    def visitIfStatement(self, ctx:SimpleLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#returnStmt.
    def visitReturnStmt(self, ctx:SimpleLangParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#commentStmt.
    def visitCommentStmt(self, ctx:SimpleLangParser.CommentStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#expr.
    def visitExpr(self, ctx:SimpleLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#functionCall.
    def visitFunctionCall(self, ctx:SimpleLangParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#primary.
    def visitPrimary(self, ctx:SimpleLangParser.PrimaryContext):
        return self.visitChildren(ctx)



del SimpleLangParser