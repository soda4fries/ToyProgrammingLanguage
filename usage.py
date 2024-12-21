from antlr4 import *
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from interpreter import Interpreter

def run_code(code: str):
    input_stream = InputStream(code)
    lexer = SimpleLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SimpleLangParser(token_stream)
    tree = parser.program()
    
    interpreter = Interpreter()
    return interpreter.visit(tree)

test_code = """
// Statistical operations
let data: array<float> = [1.0, 2.0, 3.0, 4.0, 5.0];
data.mean();  
print("Mean:", data_mean);

// Test other operations
data.median();
print("Median:", data_median);

data.variance();
print("Variance:", data_variance);

data.stddev();
print("Standard Deviation:", data_stddev);

// Linear regression
let x: array<float> = [1.0, 2.0, 3.0, 4.0, 5.0];
let y: array<float> = [2.1, 4.0, 6.3, 8.0, 9.9];
x.linreg(y);
print("Linear Regression Results:");
print("Slope:", x_slope);
print("Intercept:", x_intercept);
print("R-squared:", x_r_squared);

let melody1: array<float> = [0, 2, 4, 5, 7, 9, 11, 12, 11, 9, 7, 5, 4, 2, 0];
print("Playing major scale melody...");
melody1.play();
"""

if __name__ == "__main__":
    interpreter = run_code(test_code)