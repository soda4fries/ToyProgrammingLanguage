from antlr4 import *
from SimpleLangVisitor import SimpleLangVisitor
from typing import Any, Dict, List, Optional
from dataclasses import dataclass
from enum import Enum, auto
import operator
import numpy as np
from scipy import stats
import simpleaudio as sa
import time

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

class StatisticalFunctions:
    @staticmethod
    def mean(array):
        return float(sum(array)) / len(array)
    
    @staticmethod
    def median(array):
        sorted_array = sorted(array)
        n = len(sorted_array)
        if n % 2 == 0:
            return (sorted_array[n//2 - 1] + sorted_array[n//2]) / 2
        return sorted_array[n//2]
    
    @staticmethod
    def variance(array):
        mean = StatisticalFunctions.mean(array)
        return sum((x - mean) ** 2 for x in array) / len(array)
    
    @staticmethod
    def std_dev(array):
        return StatisticalFunctions.variance(array) ** 0.5
    
    @staticmethod
    def linear_regression(x, y):
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
        
        return {
            'slope': slope,
            'intercept': intercept,
            'r_squared': r_squared
        }

class MusicPlayer:
    # Piano note frequencies from C3 to C6
    PIANO_NOTES = {
        'C3': 130.81, 'C#3': 138.59, 'D3': 146.83, 'D#3': 155.56, 'E3': 164.81,
        'F3': 174.61, 'F#3': 185.00, 'G3': 196.00, 'G#3': 207.65, 'A3': 220.00,
        'A#3': 233.08, 'B3': 246.94,
        'C4': 261.63, 'C#4': 277.18, 'D4': 293.66, 'D#4': 311.13, 'E4': 329.63,
        'F4': 349.23, 'F#4': 369.99, 'G4': 392.00, 'G#4': 415.30, 'A4': 440.00,
        'A#4': 466.16, 'B4': 493.88,
        'C5': 523.25, 'C#5': 554.37, 'D5': 587.33, 'D#5': 622.25, 'E5': 659.26,
        'F5': 698.46, 'F#5': 739.99, 'G5': 783.99, 'G#5': 830.61, 'A5': 880.00,
        'A#5': 932.33, 'B5': 987.77,
        'C6': 1046.50
    }

    @staticmethod
    def create_reverb(audio, sample_rate=44100):
        """Create a fixed-length reverb effect"""
        audio_length = len(audio)
        num_delays = 3
        delay_samples = int(0.03 * sample_rate)  # 30ms delay
        decay = 0.5

        # Create reverb buffer of the same length as input
        reverb = np.copy(audio)
        
        # Add delayed copies
        for i in range(num_delays):
            delay = int((i + 1) * delay_samples)
            amplitude = decay ** (i + 1)
            
            # Ensure we don't exceed buffer length
            if delay < audio_length:
                reverb[delay:] += audio[:(audio_length - delay)] * amplitude

        # Normalize
        reverb = reverb / np.max(np.abs(reverb))
        return reverb

    @staticmethod
    def create_note_waveform(frequency, duration, velocity=0.8, sample_rate=44100):
        """Create a piano note with improved harmonics"""
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        
        
        harmonics = [
            (1.0, 0),    
            (0.6, 0),     
            (0.4, 0),    
            (0.25, 0),    
            (0.15, 0)     
        ]
        
        waveform = np.zeros_like(t)
        for amplitude, phase in harmonics:
            harmonic = amplitude * np.sin(2 * np.pi * frequency * (t + phase))
            # Add slight detuning for richness
            detuned = amplitude * 0.01 * np.sin(2 * np.pi * frequency * 1.001 * t)
            waveform += harmonic + detuned
        
        
        attack = 0.005
        decay = 0.1
        sustain_level = 0.7
        release = 0.3
        
        attack_samples = int(attack * sample_rate)
        decay_samples = int(decay * sample_rate)
        release_samples = int(release * sample_rate)
        
        envelope = np.ones(len(t))
        
        envelope[:attack_samples] = np.power(np.linspace(0, 1, attack_samples), 2)
       
        envelope[attack_samples:attack_samples+decay_samples] = \
            np.power(np.linspace(1, sustain_level, decay_samples), 0.5)
       
        envelope[-release_samples:] = \
            np.power(np.linspace(sustain_level, 0, release_samples), 0.3)
        
        return waveform * envelope * velocity

    @staticmethod
    def array_to_frequency(values, min_note='C3', max_note='C5'):
        """Convert array values to musical frequencies with improved note mapping"""
        min_freq = MusicPlayer.PIANO_NOTES[min_note]
        max_freq = MusicPlayer.PIANO_NOTES[max_note]
        
        min_val = min(values)
        max_val = max(values)
        
        if max_val == min_val:
            mid_freq = (min_freq + max_freq) / 2
            note_freqs = list(MusicPlayer.PIANO_NOTES.values())
            return [min(note_freqs, key=lambda x: abs(x - mid_freq))] * len(values)
            
        frequencies = []
        notes = list(MusicPlayer.PIANO_NOTES.values())
        
        for val in values:
            # Scale to 0-1 range
            normalized = (val - min_val) / (max_val - min_val)
            # Scale to frequency range
            target_freq = min_freq + (max_freq - min_freq) * normalized
            # Find nearest note
            nearest_freq = min(notes, key=lambda x: abs(x - target_freq))
            frequencies.append(nearest_freq)
            
        return frequencies

    @staticmethod
    def play_array(array, duration=5, min_note='C3', max_note='C5'):
        """Play array as musical notes with improved dynamics"""
        frequencies = MusicPlayer.array_to_frequency(array, min_note, max_note)
        sample_rate = 44100

        notes_played = [
            name for name, freq in MusicPlayer.PIANO_NOTES.items() 
            if any(abs(f - freq) < 0.1 for f in frequencies)
        ]
        print("Playing notes:", notes_played)
        
        for i, freq in enumerate(frequencies):
            # Vary velocity based on position for more musical expression
            velocity = 0.8 if i % 2 == 0 else 0.6
            if i % 4 == 0:  # Emphasize every fourth note
                velocity = 0.9
                
            # Create and process the note
            waveform = MusicPlayer.create_note_waveform(freq, duration, velocity, sample_rate)
            waveform = MusicPlayer.create_reverb(waveform, sample_rate)
            
            # Convert to 16-bit audio
            audio = np.int16(waveform * 32767)
            
            # Play the note
            play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
            play_obj.wait_done()
            
            if i % 4 == 3:  
                time.sleep(0.15)
            else:
                time.sleep(0.1)

class Interpreter(SimpleLangVisitor):
    def __init__(self):
        self.global_env = Environment()
        self.current_env = self.global_env
        self.global_env.define('print', print)
        self.global_env.define('len', len)

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
        op_text = ctx.getText()

        if 'sort' in op_text:
            array.sort()
        elif 'mean' in op_text:
            result = StatisticalFunctions.mean(array)
            result_var = array_name + '_mean'
            self.current_env.define(result_var, result)  # Define before assign
            return result
        elif 'median' in op_text:
            result = StatisticalFunctions.median(array)
            result_var = array_name + '_median'
            self.current_env.define(result_var, result)
            return result
        elif 'variance' in op_text:
            result = StatisticalFunctions.variance(array)
            result_var = array_name + '_variance'
            self.current_env.define(result_var, result)
            return result
        elif 'stddev' in op_text:
            result = StatisticalFunctions.std_dev(array)
            result_var = array_name + '_stddev'
            self.current_env.define(result_var, result)
            return result
        elif 'play' in op_text:
            MusicPlayer.play_array(array)
        elif 'linreg' in op_text:
            y_array = self.visit(ctx.expr())
            result = StatisticalFunctions.linear_regression(array, y_array)
            
            # Define before assign
            self.current_env.define(array_name + '_slope', result['slope'])
            self.current_env.define(array_name + '_intercept', result['intercept'])
            self.current_env.define(array_name + '_r_squared', result['r_squared'])
            
            return result

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
