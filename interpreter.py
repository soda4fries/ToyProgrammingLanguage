from antlr4 import *
from SimpleLangVisitor import SimpleLangVisitor
from typing import Any, Dict, List, Optional
from dataclasses import dataclass
from enum import Enum, auto
import operator

class Type(Enum):
    INT = auto()
    FLOAT = auto()
    BOOL = auto()
    STRING = auto()
    ARRAY = auto()
    LIST = auto()

@dataclass
class ArrayType:
    element_type: Type

@dataclass
class ListType:
    element_type: Type

@dataclass
class Function:
    params: List[tuple]
    return_type: Type
    body: Any
    env: 'Environment'

class ReturnValue:
    def __init__(self, value):
        self.value = value

class Environment:
    def __init__(self, parent=None):
        self.values: Dict[str, Any] = {}
        self.parent = parent

    def define(self, name: str, value: Any):
        self.values[name] = value

    def get(self, name: str) -> Any:
        if name in self.values:
            return self.values[name]
        if self.parent:
            return self.parent.get(name)
        raise NameError(f"Variable '{name}' is not defined")

    def assign(self, name: str, value: Any):
        if name in self.values:
            self.values[name] = value
            return
        if self.parent:
            self.parent.assign(name, value)
            return
        raise NameError(f"Variable '{name}' is not defined")

class Interpreter(SimpleLangVisitor):
    def __init__(self):
        self.global_env = Environment()
        self.current_env = self.global_env
        
        # Add built-in functions
        self.global_env.define('print', print)
        self.global_env.define('len', len)

    def visitProgram(self, ctx):
        for child in ctx.children[:-1]:  # Skip EOF
            self.visit(child)

    def visitFunctionDecl(self, ctx):
        name = ctx.IDENTIFIER().getText()
        params = []
        if ctx.paramList():
            params = self.visit(ctx.paramList())
        return_type = self.visit(ctx.type_())
        
        function = Function(
            params=params,
            return_type=return_type,
            body=ctx.block(),
            env=self.current_env
        )
        self.current_env.define(name, function)

    def visitParamList(self, ctx):
        return [self.visit(param) for param in ctx.parameter()]

    def visitParameter(self, ctx):
        name = ctx.IDENTIFIER().getText()
        param_type = self.visit(ctx.type_())
        default_value = None
        if ctx.expr():
            default_value = self.visit(ctx.expr())
        return (name, param_type, default_value)

    def visitType(self, ctx):
        type_text = ctx.getText()
        if type_text == 'int':
            return Type.INT
        elif type_text == 'bool':
            return Type.BOOL
        elif type_text == 'string':
            return Type.STRING
        elif type_text == 'float':
            return Type.FLOAT
        elif ctx.arrayType():
            return ArrayType(self.visit(ctx.arrayType().type_()))
        elif ctx.listType():
            return ListType(self.visit(ctx.listType().type_()))

    def visitVarDecl(self, ctx):
        name = ctx.IDENTIFIER().getText()
        var_type = self.visit(ctx.type_())
        value = None

        if ctx.expr():
            value = self.visit(ctx.expr())
        else:
            if var_type == Type.FLOAT:
                value = 0.0
            elif var_type == Type.INT:
                value = 0
            elif var_type == Type.BOOL:
                value = False
            elif var_type == Type.STRING:
                value = ""
            elif isinstance(var_type, (ArrayType, ListType)):
                value = []
                
        self.current_env.define(name, value)

    def visitAssignment(self, ctx):
        name = ctx.IDENTIFIER().getText()
        exprs = ctx.expr()
        if len(exprs) > 1:  # Array/List indexing
            container = self.current_env.get(name)
            index = self.visit(exprs[0])
            value = self.visit(exprs[1])
            container[index] = value
        else:
            value = self.visit(exprs[0])
            self.current_env.assign(name, value)

    def visitArrayOp(self, ctx):
        array_name = ctx.IDENTIFIER().getText()
        array = self.current_env.get(array_name)
        if 'sort' in ctx.getText():
            array.sort()

    def visitListOp(self, ctx):
        list_name = ctx.IDENTIFIER().getText()
        lst = self.current_env.get(list_name)
        op_text = ctx.getText()
        
        if 'append' in op_text:
            value = self.visit(ctx.expr())
            lst.append(value)
        elif 'remove' in op_text:
            value = self.visit(ctx.expr())
            lst.remove(value)
        elif 'sort' in op_text:
            lst.sort()

    def visitIfStatement(self, ctx):
        condition = self.visit(ctx.expr())
        if condition:
            result = self.visit(ctx.block(0))
            if isinstance(result, ReturnValue):
                return result
        elif ctx.block(1):
            result = self.visit(ctx.block(1))
            if isinstance(result, ReturnValue):
                return result

    def visitWhileStatement(self, ctx):
        while self.visit(ctx.expr()):
            result = self.visit(ctx.block())
            if isinstance(result, ReturnValue):
                return result

    def visitBlock(self, ctx):
        previous_env = self.current_env
        self.current_env = Environment(previous_env)
        
        for stmt in ctx.statement():
            result = self.visit(stmt)
            if isinstance(result, ReturnValue):
                self.current_env = previous_env
                return result
            
        self.current_env = previous_env

    def visitReturnStmt(self, ctx):
        value = None
        if ctx.expr():
            value = self.visit(ctx.expr())
        return ReturnValue(value)

    def visitExpr(self, ctx):
        if ctx.primary():
            return self.visit(ctx.primary())
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        elif ctx.getChildCount() == 2 and ctx.getChild(0).getText() == '-':
            return -self.visit(ctx.expr(0))
        elif ctx.getChild(0).getText() == '[':  # Array/List literal
            exprs = ctx.expr()
            return [self.visit(e) for e in exprs]
        elif ctx.getChildCount() == 4 and ctx.getChild(1).getText() == '[':  # Array/List indexing
            container = self.visit(ctx.expr(0))
            index = self.visit(ctx.expr(1))
            return container[index]
        elif ctx.op:  # Binary operation
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.op.text

            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                ops = {
                    '*': operator.mul,
                    '/': operator.truediv,
                    '+': operator.add,
                    '-': operator.sub,
                    '>': operator.gt,
                    '<': operator.lt,
                    '>=': operator.ge,
                    '<=': operator.le,
                    '==': operator.eq,
                    '!=': operator.ne,
                    'and': operator.and_,
                    'or': operator.or_
                }
                return ops[op](left, right)
            else:
                raise TypeError(f"Unsupported operation between {type(left)} and {type(right)}")
        elif ctx.expr(0):  # Parentheses
            return self.visit(ctx.expr(0))

    def visitFunctionCall(self, ctx):
        name = ctx.IDENTIFIER().getText()
        function = self.current_env.get(name)
        
        args = []
        if ctx.expr():
            args = [self.visit(expr) for expr in ctx.expr()]
            
        if isinstance(function, Function):
            previous_env = self.current_env
            self.current_env = Environment(function.env)
            
            # Bind parameters to arguments
            for (param_name, param_type, default_value), arg in zip(function.params, args):
                self.current_env.define(param_name, arg)
                
            result = self.visit(function.body)
            self.current_env = previous_env
            
            if isinstance(result, ReturnValue):
                return result.value
            return result
        else:  # Built-in function
            return function(*args)

    def visitPrimary(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        elif ctx.BOOL():
            return ctx.BOOL().getText() == 'true'
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]  # Remove quotes
        elif ctx.IDENTIFIER():
            return self.current_env.get(ctx.IDENTIFIER().getText())