from antlr4 import *
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor
from typing import Dict, Any, List, Tuple, Callable, Union
import operator


class Function:
    def __init__(
        self,
        params: List[Tuple[str, str, Any]],
        return_type: str,
        block: Union[Any, Callable],
        env: Dict[str, Any],
        is_builtin: bool = False,
    ):
        self.params = params  # [(name, type, default_value), ...]
        self.return_type = return_type
        self.block = block
        self.env = env
        self.is_builtin = is_builtin

class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value


class Interpreter(SimpleLangVisitor):
    def __init__(self):
        self.global_env = {}
        self.current_env = [self.global_env]

       
        self.global_env["print"] = Function(
            [("value", "any", None)],
            "void",
            lambda args: print(args[0]),
            self.global_env,
            is_builtin=True,
        )

    def get_var(self, name: str) -> Any:
        
        for env in reversed(self.current_env):
            if name in env:
                return env[name]
        raise Exception(f"Variable or function '{name}' not defined")

    def visitProgram(self, ctx):
        for child in ctx.children:
            if child is not None and not isinstance(child, TerminalNode):
                self.visit(child)

    def visitFunctionDecl(self, ctx):
        name = ctx.IDENTIFIER().getText()
        params = []
        if ctx.paramList():
            for param in ctx.paramList().parameter():
                param_name = param.IDENTIFIER().getText()
                param_type = param.type_().getText()
                default_value = None
                if param.expr():
                    default_value = self.visit(param.expr())
                params.append((param_name, param_type, default_value))
        return_type = ctx.type_().getText()

        
        self.global_env[name] = Function(
            params, return_type, ctx.block(), self.global_env
        )

    def visitFunctionCall(self, ctx):
        name = ctx.IDENTIFIER().getText()
        try:
            func = self.get_var(name)
        except Exception as e:
            raise Exception(f"Function {name} not defined")

        args = []
        if ctx.expr():
            args = [self.visit(expr) for expr in ctx.expr()]

        if len(args) > len(func.params):
            raise Exception(f"Too many arguments for function {name}")

        while len(args) < len(func.params):
            default_value = func.params[len(args)][2]
            if default_value is None:
                raise Exception(f"Missing required argument for function {name}")
            args.append(default_value)

        if func.is_builtin:

            return func.block(args)
        else:

            new_env = dict(func.env)
            for (param_name, param_type, _), arg in zip(func.params, args):
                new_env[param_name] = arg
            self.current_env.append(new_env)
            # funny
            try:
                self.visit(func.block)
                return_value = None
            except ReturnValue as ret:
                return_value = ret.value
            finally:
                self.current_env.pop()

            return return_value

    def visitBlock(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitVarDecl(self, ctx):
        name = ctx.IDENTIFIER().getText()
        var_type = ctx.type_().getText()
        if ctx.expr():
            value = self.visit(ctx.expr())
            self.current_env[-1][name] = value

    def visitAssignment(self, ctx):
        name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expr())

        for env in reversed(self.current_env):
            if name in env:
                env[name] = value
                return
        self.current_env[-1][name] = value

    def visitIfStatement(self, ctx):
        condition = self.visit(ctx.expr())
        if condition:
            self.visit(ctx.block(0))
        elif len(ctx.block()) > 1:
            self.visit(ctx.block(1))

    def visitReturnStmt(self, ctx):
        value = None
        if ctx.expr():
            value = self.visit(ctx.expr())
        raise ReturnValue(value)

    def visitExpr(self, ctx):
        if len(ctx.children) == 1:
            return self.visit(ctx.children[0])
        elif len(ctx.children) == 2:
            # Unary minus operation
            if ctx.children[0].getText() == "-":
                value = self.visit(ctx.expr(0))
                return -value
        elif len(ctx.children) == 3:
            if ctx.expr(0):
                left = self.visit(ctx.expr(0))
                right = self.visit(ctx.expr(1))
                op = ctx.op.text

                ops = {
                    "+": operator.add,
                    "-": operator.sub,
                    "*": operator.mul,
                    "/": operator.truediv,
                    ">": operator.gt,
                    "<": operator.lt,
                    ">=": operator.ge,
                    "<=": operator.le,
                    "==": operator.eq,
                    "!=": operator.ne,
                    "and": lambda x, y: x and y,
                    "or": lambda x, y: x or y,
                }

                return ops[op](left, right)
            else:
                return self.visit(ctx.expr(0))

    def visitPrimary(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.BOOL():
            return ctx.BOOL().getText() == "true"
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        elif ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            return self.get_var(name)
