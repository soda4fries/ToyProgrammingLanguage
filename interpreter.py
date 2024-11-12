from antlr4 import *
from typing import Dict, Any, List, Tuple, Union, Callable
import operator
from decimal import Decimal, ROUND_HALF_UP

from SimpleLangVisitor import SimpleLangVisitor


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


class SimpleLangInterpreter(SimpleLangVisitor):
    def __init__(self):
        self.global_env = {}
        self.current_env = [self.global_env]
        
        # Built-in functions
        self.global_env["print"] = Function(
            [("value", "Any", None)],
            "Void",
            lambda args: (print(args[0]), None)[-1],
            self.global_env,
            is_builtin=True,
        )
        
        
        self.setup_builtin_functions()

    def setup_builtin_functions(self):
        # Math functions
        self.global_env["abs"] = Function(
            [("x", "Any", None)],
            "Any",
            lambda args: abs(args[0]),
            self.global_env,
            is_builtin=True,
        )
        
        self.global_env["round"] = Function(
            [("x", "Float", None), ("places", "Int", 0)],
            "Float",
            lambda args: float(Decimal(str(args[0])).quantize(
                Decimal('0.' + '0' * args[1]),
                rounding=ROUND_HALF_UP
            )),
            self.global_env,
            is_builtin=True,
        )

    def type_cast(self, value: Any, target_type: str) -> Any:
        try:
            if target_type == "Int":
                if isinstance(value, bool):
                    return 1 if value else 0
                elif isinstance(value, str):
                    if value.lower() == "true":
                        return 1
                    elif value.lower() == "false":
                        return 0
                    else:
                        return int(float(value))
                elif isinstance(value, float):
                    return int(value)
                return int(value)
            
            elif target_type == "Float":
                if isinstance(value, bool):
                    return 1.0 if value else 0.0
                elif isinstance(value, str):
                    if value.lower() == "true":
                        return 1.0
                    elif value.lower() == "false":
                        return 0.0
                    else:
                        return float(value)
                return float(value)
            
            elif target_type == "Bool":
                if isinstance(value, str):
                    return value.lower() == "true"
                return bool(value)
            
            elif target_type == "String":
                if isinstance(value, float):
                    return f"{value:g}"
                return str(value)
            
            else:
                raise Exception(f"Unsupported type cast to {target_type}")
        except ValueError:
            raise Exception(f"Cannot cast {value} to {target_type}")

    def get_var(self, name: str) -> Any:
        for env in reversed(self.current_env):
            if name in env:
                return env[name]
        raise Exception(f"Variable or function '{name}' not defined")

    def visitProgram(self, ctx):
        last_value = None
        for expr in ctx.expr():
            last_value = self.visit(expr)
        return last_value

    def visitBlock(self, ctx):
        last_value = None
        self.current_env.append({})
        try:
            for expr in ctx.expr():
                last_value = self.visit(expr)
            return last_value
        finally:
            self.current_env.pop()

    def visitFunctionDecl(self, ctx):
        name = ctx.IDENTIFIER().getText()
        params = []
        if ctx.paramList():
            for param in ctx.paramList().parameter():
                param_name = param.IDENTIFIER().getText()
                param_type = param.Type().getText()
                default_value = None
                if param.expr():
                    default_value = self.visit(param.expr())
                params.append((param_name, param_type, default_value))
        
        func = Function(params, ctx.Type().getText(), ctx.block(), dict(self.current_env[-1]))
        self.current_env[-1][name] = func
        return func

    def visitFunctionCall(self, ctx):
        name = ctx.IDENTIFIER().getText()
        func = self.get_var(name)

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
            for (param_name, _, _), arg in zip(func.params, args):
                new_env[param_name] = arg
            self.current_env.append(new_env)
            try:
                return self.visit(func.block)
            finally:
                self.current_env.pop()

    def visitVarDecl(self, ctx):
        name = ctx.IDENTIFIER().getText()
        value = None
        if ctx.expr():
            value = self.visit(ctx.expr())
        self.current_env[-1][name] = value
        return value

    def visitAssignment(self, ctx):
        name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expr())
        
        if ctx.assignOp():
            current_value = self.get_var(name)
            op = ctx.assignOp().getText()
            ops = {
                "+=": operator.add,
                "-=": operator.sub,
                "*=": operator.mul,
                "/=": operator.truediv,
            }
            value = ops[op](current_value, value)
            
        for env in reversed(self.current_env):
            if name in env:
                env[name] = value
                return value
        
        self.current_env[-1][name] = value
        return value

    def visitIfExpr(self, ctx):
        condition = self.visit(ctx.expr())
        if condition:
            return self.visit(ctx.block(0))
        elif len(ctx.block()) > 1:
            return self.visit(ctx.block(1))
        return None

    def visitTypeCast(self, ctx):
        value = self.visit(ctx.expr())
        target_type = ctx.Type().getText()
        return self.type_cast(value, target_type)

    def visitExpr(self, ctx):
        if len(ctx.children) == 1:
            return self.visit(ctx.children[0])
        elif len(ctx.children) == 2:
            op = ctx.children[0].getText()
            if op == "-":
                value = self.visit(ctx.expr(0))
                return -value
            elif op == "not":
                value = self.visit(ctx.expr(0))
                return not value
        elif len(ctx.children) == 3:
            if ctx.expr(0):
                left = self.visit(ctx.expr(0))
                right = self.visit(ctx.expr(1))
                op = ctx.op.text

                # Handle type promotion
                if (isinstance(left, (int, float)) and 
                    isinstance(right, (int, float))):
                    if isinstance(left, float) or isinstance(right, float):
                        left = float(left)
                        right = float(right)

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
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        elif ctx.BOOL():
            return ctx.BOOL().getText() == "true"
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        elif ctx.IDENTIFIER():
            return self.get_var(ctx.IDENTIFIER().getText())