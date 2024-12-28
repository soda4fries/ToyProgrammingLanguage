from contextlib import contextmanager
import random
from antlr4 import *
from SimpleLangVisitor import SimpleLangVisitor
from typing import Any, Dict, List, Optional
from typing import List, Dict, Union
from typing import Any, List, Tuple, Union
from dataclasses import dataclass
from enum import Enum, auto
import operator
import numpy as np
from scipy import stats
import simpleaudio as sa
import time
import pygame.midi


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
    env: "Environment"


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


class StatisticalFunctions:
    @staticmethod
    def mean(array: Union[List[Union[int, float]], np.ndarray]) -> float:
        if isinstance(array, np.ndarray):
            if array.size == 0:
                raise ValueError("Cannot calculate mean of an empty array.")
            return float(np.mean(array))
        elif isinstance(array, list):
            if not array:
                raise ValueError("Cannot calculate mean of an empty list.")
            assert all(isinstance(x, (int, float)) for x in array), "Array elements must be int or float"
            return float(sum(array)) / len(array)
        else:
            raise TypeError("Input must be a list or numpy array.")

    @staticmethod
    def median(array: Union[List[Union[int, float]], np.ndarray]) -> float:
        if isinstance(array, np.ndarray):
            if array.size == 0:
                raise ValueError("Cannot calculate median of an empty array.")
            return float(np.median(array))
        elif isinstance(array, list):
            if not array:
                raise ValueError("Cannot calculate median of an empty list.")
            assert all(isinstance(x, (int, float)) for x in array), "Array elements must be int or float"
            sorted_array = sorted(array)
            n = len(sorted_array)
            if n % 2 == 0:
                return (sorted_array[n // 2 - 1] + sorted_array[n // 2]) / 2
            return sorted_array[n // 2]
        else:
            raise TypeError("Input must be a list or numpy array.")

    @staticmethod
    def variance(array: Union[List[Union[int, float]], np.ndarray]) -> float:
        if isinstance(array, np.ndarray):
            if array.size == 0:
                raise ValueError("Cannot calculate variance of an empty array.")
            return float(np.var(array))
        elif isinstance(array, list):
            if not array:
                raise ValueError("Cannot calculate variance of an empty list.")
            assert all(isinstance(x, (int, float)) for x in array), "Array elements must be int or float"
            mean = StatisticalFunctions.mean(array)
            return sum((x - mean) ** 2 for x in array) / len(array)
        else:
            raise TypeError("Input must be a list or numpy array.")

    @staticmethod
    def std_dev(array: Union[List[Union[int, float]], np.ndarray]) -> float:
        if isinstance(array, np.ndarray):
            if array.size == 0:
                raise ValueError("Cannot calculate standard deviation of an empty array.")
            return float(np.std(array))
        elif isinstance(array, list):
            if not array:
                raise ValueError("Cannot calculate standard deviation of an empty list.")
            assert all(isinstance(x, (int, float)) for x in array), "Array elements must be int or float"
            return StatisticalFunctions.variance(array) ** 0.5
        else:
            raise TypeError("Input must be a list or numpy array.")

    @staticmethod
    def linear_regression(x: List[Union[int, float]], y: List[Union[int, float]]) -> Dict[str, float]:
        assert all(isinstance(i, (int, float)) for i in x), "X elements must be int or float"
        assert all(isinstance(i, (int, float)) for i in y), "Y elements must be int or float"
        if len(x) != len(y):
            raise ValueError("Arrays must be of equal length")

        n = len(x)
        mean_x = StatisticalFunctions.mean(x)
        mean_y = StatisticalFunctions.mean(y)

        numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        denominator = sum((x[i] - mean_x) ** 2 for i in range(n))
        slope = numerator / denominator
        intercept = mean_y - slope * mean_x

        y_pred = [slope * x_val + intercept for x_val in x]
        ss_tot = sum((y_val - mean_y) ** 2 for y_val in y)
        ss_res = sum((y[i] - y_pred[i]) ** 2 for i in range(n))
        r_squared = 1 - (ss_res / ss_tot)

        return {"slope": slope, "intercept": intercept, "r_squared": r_squared}


class MusicPlayer:
    # Note mappings (C major scale)
    NOTE_MAPPING = {
        0: 60,  # Middle C
        1: 62,  # D
        2: 64,  # E
        3: 65,  # F
        4: 67,  # G
        5: 69,  # A
        6: 71,  # B
        7: 72,  # High C
    }

    # More interesting instrument selection
    INSTRUMENTS = [
        0,  # Piano
        4,  # Electric Piano
        13,  # Xylophone
        19,  # Church Organ
        24,  # Acoustic Guitar
        26,  # Electric Guitar
        46,  # Orchestral Harp
        66,  # Alto Sax
        68,  # Oboe
        71,  # Clarinet
        73,  # Flute
        108,  # Kalimba
        109,  # Bagpipe
        114,  # Steel Drums
    ]

    @staticmethod
    @contextmanager
    def _midi_context():
        """Context manager for MIDI resources"""
        pygame.midi.init()

        print("Available MIDI devices:")
        for i in range(pygame.midi.get_count()):
            info = pygame.midi.get_device_info(i)
            print(f"Device {i}: {info}")

        output_id = pygame.midi.get_default_output_id()

        if output_id == -1: 
            print("Warning: No MIDI output devices available")
            yield None 
        else:
            try:
                player = pygame.midi.Output(output_id)
                yield player  
            finally:
                if 'player' in locals(): 
                    player.close()

        pygame.midi.quit()

    @classmethod
    def play(cls, values):
        """Static method to play array of values with a single random instrument"""
        with cls._midi_context() as player:
            if player is None: 
                print("Skipping MIDI playback: No output device available")
                return

            instrument = random.choice(cls.INSTRUMENTS)
            player.set_instrument(instrument)
            print(f"Playing with instrument {instrument}")

            for i, value in enumerate(values):

                note = cls.NOTE_MAPPING[value % 8]

                velocity = 120 if i % 4 == 0 else 90

                player.note_on(note, velocity)
                time.sleep(0.3)
                player.note_off(note, velocity)
                time.sleep(0.1)


class Interpreter(SimpleLangVisitor):
    def __init__(self):
        self.global_env = Environment()
        self.current_env = self.global_env
        self.global_env.define("print", print)
        self.global_env.define("len", len)
        self.music_player = MusicPlayer()

    def visitProgram(self, ctx):
        for child in ctx.children[:-1]:
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
            env=self.current_env,
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
        if type_text == "int":
            return Type.INT
        elif type_text == "bool":
            return Type.BOOL
        elif type_text == "string":
            return Type.STRING
        elif type_text == "float":
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
            if isinstance(var_type, ArrayType) and var_type.element_type == ArrayType(Type.FLOAT):
                value = np.array(value)
            elif isinstance(var_type, ArrayType) and var_type.element_type == Type.FLOAT:
                value = np.array(value)
        else:
            if var_type == Type.FLOAT:
                value = 0.0
            elif var_type == Type.INT:
                value = 0
            elif var_type == Type.BOOL:
                value = False
            elif var_type == Type.STRING:
                value = ""
            elif isinstance(var_type, ArrayType):
                if isinstance(var_type.element_type, ArrayType) and var_type.element_type.element_type == Type.FLOAT:
                    value = np.array([])
                elif var_type.element_type == Type.FLOAT:
                    value = np.array([])
                else:
                    value = []
            elif isinstance(var_type, ListType):
                value = []

        self.current_env.define(name, value)

    def visitAssignment(self, ctx):
        name = ctx.IDENTIFIER().getText()
        exprs = ctx.expr()
        if len(exprs) > 1:  # Array/List indexing
            container = self.current_env.get(name)
            index = self.visit(exprs[0])
            value = self.visit(exprs[1])

            # Ensure the container is a list or array
            if not isinstance(container, (list, np.ndarray)):
                raise TypeError(f"Variable '{name}' is expected to be a list or array, got {type(container)}")

            # Ensure index is an integer
            if not isinstance(index, int):
                raise TypeError(f"Index must be an integer, got {type(index)}")

            container[index] = value
        else:
            value = self.visit(exprs[0])
            self.current_env.assign(name, value)

    def visitArrayOp(self, ctx):
        array_name = ctx.IDENTIFIER().getText()
        array = self.current_env.get(array_name)
        op_text = ctx.getText()

        # Check if the variable is a list or array
        if not isinstance(array, (list, np.ndarray)):
            raise TypeError(f"Variable '{array_name}' is not an array or list")

        if "sort" in op_text:
            desc = "desc" in op_text
            if isinstance(array, list):
                array.sort(reverse=desc)
            elif isinstance(array, np.ndarray):
                if desc:
                    array = np.sort(array)[::-1] 
                else:
                    array = np.sort(array)
                self.current_env.assign(array_name, array.tolist())
            else:
                raise TypeError(f"Unsupported type for sorting: {type(array)}")

        elif "mean" in op_text:
            # Ensure it's a numerical array for statistical functions
            if not all(isinstance(elem, (int, float)) for elem in array):
                raise TypeError(f"Mean can only be applied to numerical arrays, but got elements of different types")
            result = StatisticalFunctions.mean(array)
            result_var = array_name + "_mean"
            self.current_env.define(result_var, result)
            return result

        elif "median" in op_text:
            if not all(isinstance(elem, (int, float)) for elem in array):
                raise TypeError(f"Median can only be applied to numerical arrays, but got elements of different types")
            result = StatisticalFunctions.median(array)
            result_var = array_name + "_median"
            self.current_env.define(result_var, result)
            return result

        elif "variance" in op_text:
            if not all(isinstance(elem, (int, float)) for elem in array):
                raise TypeError(f"Variance can only be applied to numerical arrays, but got elements of different types")
            result = StatisticalFunctions.variance(array)
            result_var = array_name + "_variance"
            self.current_env.define(result_var, result)
            return result

        elif "stddev" in op_text:
            if not all(isinstance(elem, (int, float)) for elem in array):
                raise TypeError(f"Standard deviation can only be applied to numerical arrays, but got elements of different types")
            result = StatisticalFunctions.std_dev(array)
            result_var = array_name + "_stddev"
            self.current_env.define(result_var, result)
            return result

        elif "play" in op_text:
            # Play operation on array
            MusicPlayer.play(array)

        elif "linreg" in op_text:
            y_array = self.visit(ctx.expr())
            if not isinstance(y_array, (list, np.ndarray)) or not all(isinstance(elem, (int, float)) for elem in y_array):
                raise TypeError(f"Expected numerical array (list or numpy array) for linear regression, but got {type(y_array)}")
            result = StatisticalFunctions.linear_regression(array, y_array)
            self.current_env.define(array_name + "_slope", result["slope"])
            self.current_env.define(array_name + "_intercept", result["intercept"])
            self.current_env.define(array_name + "_r_squared", result["r_squared"])
            return result

        elif "rotate" in op_text:
            positions_expr = ctx.expr()
            if not positions_expr:
                raise ValueError("Missing number of positions for rotate operation")
            positions = int(self.visit(positions_expr))
            if not isinstance(array, list):
                raise TypeError("Rotate operation requires a list")
            rotated_array = array[-positions:] + array[:-positions]
            result_var = array_name + "_rotate"
            self.current_env.define(result_var, rotated_array)
            return rotated_array

        elif "shift" in op_text:
            positions_expr = ctx.expr()
            if not positions_expr:
                raise ValueError("Missing number of positions for shift operation")
            
            positions = int(self.visit(positions_expr))
            array_length = len(array)
            
            if array_length == 0:
                shifted_array = []
            else:
                if positions > 0:
                    positions %= array_length
                    shifted_array = [0] * positions + array[:array_length - positions]
                elif positions < 0:
                    positions = abs(positions) % array_length
                    shifted_array = array[positions:] + [0] * positions
                else:
                    shifted_array = array[:]

            result_var = array_name + "_shift"
            self.current_env.define(result_var, shifted_array)
            return shifted_array

        elif "filter" in op_text:
            lambda_expr = ctx.lambdaExpr()
            if not lambda_expr:
                raise ValueError("Missing lambda expression for filter operation")
            lambda_param = lambda_expr.IDENTIFIER().getText()
            lambda_body = lambda_expr.expr()
            filtered_array = [element for element in array if self._evaluate_lambda(lambda_param, lambda_body, element)]
            result_var = array_name + "_filter"
            self.current_env.define(result_var, filtered_array)
            return filtered_array

        elif "map" in op_text:
            lambda_expr = ctx.lambdaExpr()
            if not lambda_expr:
                raise ValueError("Missing lambda expression for map operation")
            lambda_param = lambda_expr.IDENTIFIER().getText()
            lambda_body = lambda_expr.expr()
            mapped_array = [self._evaluate_lambda(lambda_param, lambda_body, element) for element in array]
            result_var = array_name + "_map"
            self.current_env.define(result_var, mapped_array)
            return mapped_array


    def _evaluate_lambda(self, param_name, lambda_body, value):
        previous_env = self.current_env
        self.current_env = Environment(previous_env)

        try:
            self.current_env.define(param_name, value)
            result = self.visit(lambda_body)
        finally:
            self.current_env = previous_env

        return result

        
    def _evaluate_lambda(self, param_name, lambda_body, value):
        previous_env = self.current_env
        self.current_env = Environment(previous_env)

        try:
            self.current_env.define(param_name, value)
            result = self.visit(lambda_body)
        finally:
            self.current_env = previous_env

        return result

    def visitListOp(self, ctx):
        list_name = ctx.IDENTIFIER().getText()
        lst = self.current_env.get(list_name)

        if not isinstance(lst, list):
            raise TypeError(f"Variable '{list_name}' is not a list")

        op_text = ctx.getText()

        if "append" in op_text:
            value = self.visit(ctx.expr())
            lst.append(value)
        elif "remove" in op_text:
            value = self.visit(ctx.expr())
            if value in lst:
                lst.remove(value)
            else:
                raise ValueError(f"Value '{value}' not found in the list")
        elif "sort" in op_text:
            desc = "desc" in op_text
            lst.sort(reverse=desc)
        else:
            raise ValueError(f"Unsupported operation on list: {op_text}")


    def visitMatrixOp(self, ctx):
        matrix_name = ctx.IDENTIFIER().getText()
        matrix = self.current_env.get(matrix_name)

        if not isinstance(matrix, np.ndarray):
            try:
                matrix = np.array(matrix)
                self.current_env.assign(matrix_name, matrix)
            except Exception as e:
                raise TypeError(f"Variable '{matrix_name}' cannot be converted to a numpy matrix: {e}")

        op_text = ctx.getText()

        if "add" in op_text:
            other_matrix = self.visit(ctx.expr())
            other_matrix = np.array(other_matrix)
            if matrix.size == 0 or other_matrix.size == 0:
                raise ValueError("Matrix addition requires non-empty matrices.")
            if matrix.shape != other_matrix.shape:
                raise ValueError("Matrix addition requires matrices of the same shape.")
            result = np.add(matrix, other_matrix)
            result_var = f"{matrix_name}_add"
            self.current_env.define(result_var, result)
            return result

        elif "multiply" in op_text:
            other_matrix = self.visit(ctx.expr())
            other_matrix = np.array(other_matrix)

            if matrix.size == 0 or other_matrix.size == 0:
                raise ValueError("Matrix multiplication requires non-empty matrices.")

            if matrix.shape[1] != other_matrix.shape[0]:
                raise ValueError(
                    f"Matrix multiplication requires the number of columns in the first matrix "
                    f"({matrix.shape[1]}) to match the number of rows in the second matrix "
                    f"({other_matrix.shape[0]})."
                )
            result = np.matmul(matrix, other_matrix)
            result_var = matrix_name + "_multiply"
            self.current_env.define(result_var, result)
            return result

        elif "invert" in op_text:
            if matrix.size == 0: 
                raise ValueError("Matrix size should not be zero for inversion")

            if matrix.shape[0] != matrix.shape[1]:
                raise ValueError("Matrix inversion requires a square matrix")
            try:
                result = np.linalg.inv(matrix)
                result_var = matrix_name + "_invert"
                self.current_env.define(result_var, result)
                return result
            except np.linalg.LinAlgError:
                raise ValueError(f"Matrix '{matrix_name}' is singular and cannot be inverted")

        elif "transpose" in op_text:
            result = np.transpose(matrix)
            result_var = matrix_name + "_transpose"
            self.current_env.define(result_var, result)
            return result
        
    def visitMatchStatement(self, ctx):
        value = self.visit(ctx.expr())
        for case in ctx.matchCase():
            pattern = self.visit(case.pattern())
            if self._match_pattern(value, pattern):
                return self.visit(case.statement())
        raise ValueError(f"No matching pattern for value: {value}")

    def _match_pattern(self, value, pattern):
        if pattern == "_":  # Wildcard matches anything
            return True
        if isinstance(pattern, list):  # Array pattern matching
            if not isinstance(value, list) or len(value) != len(pattern):
                return False
            return all(self._match_pattern(v, p) for v, p in zip(value, pattern))
        # Add type checking for mismatched types
        if type(value) != type(pattern):
            return False  # Types don't match
        return value == pattern  # Exact match


    def visitMatchCase(self, ctx):
        pattern = self.visit(ctx.pattern())  # Visit pattern
        statement = self.visit(ctx.statement())  # Visit statement
        return {"pattern": pattern, "statement": statement}

    def visitPattern(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        elif ctx.BOOL():
            return ctx.BOOL().getText() == "true"
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]  # Remove quotes
        elif ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()  # Identifiers match variable values
        elif ctx.getChild(0).getText() == "_":  # Wildcard
            return "_"
        elif ctx.getChild(0).getText() == "[":  # Array pattern
            return [self.visit(child) for child in ctx.pattern()]
        elif ctx.getChild(0).getText() == "{":  # Object pattern
            obj_pattern = {}
            for child in ctx.children[1:-1]:  # Skip '{' and '}'
                key = child.IDENTIFIER().getText()
                value = self.visit(child.pattern())
                obj_pattern[key] = value
            return obj_pattern

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
        elif ctx.getChildCount() == 2 and ctx.getChild(0).getText() == "-":
            return -self.visit(ctx.expr(0))
        elif ctx.getChild(0).getText() == "[":  # Array/List literal
            exprs = ctx.expr()
            return [self.visit(e) for e in exprs]
        elif (
            ctx.getChildCount() == 4 and ctx.getChild(1).getText() == "["
        ):  
            container = self.visit(ctx.expr(0))
            index = self.visit(ctx.expr(1))
            return container[index]
        elif ctx.op:  # Binary operation
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.op.text

            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                ops = {
                    "*": operator.mul,
                    "/": operator.truediv,
                    "%": operator.mod,
                    "+": operator.add,
                    "-": operator.sub,
                    ">": operator.gt,
                    "<": operator.lt,
                    ">=": operator.ge,
                    "<=": operator.le,
                    "==": operator.eq,
                    "!=": operator.ne,
                    "and": operator.and_,
                    "or": operator.or_,
                }
                return ops[op](left, right)
            else:
                # Raise error for unsupported types in binary operations
                raise TypeError(
                    f"Unsupported operation '{op}' between {type(left)} and {type(right)}"
                )
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

        
            for (param_name, param_type, default_value), arg in zip(
                function.params, args
            ):
                self.current_env.define(param_name, arg)

            result = self.visit(function.body)
            self.current_env = previous_env

            if isinstance(result, ReturnValue):
                return result.value
            return result
        else: 
            return function(*args)

    def visitPrimary(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        elif ctx.BOOL():
            return ctx.BOOL().getText() == "true"
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]  # Remove quotes
        elif ctx.IDENTIFIER():
            return self.current_env.get(ctx.IDENTIFIER().getText())
