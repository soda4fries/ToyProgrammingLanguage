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

// Matrix operations
let matrix1: array<array<float>> = [[1.0, 2.0], [3.0, 4.0]];
let matrix2: array<array<float>> = [[5.0, 6.0], [7.0, 8.0]];

matrix1.add(matrix2);
print("Matrix Addition Result:", matrix1_add);

matrix1.multiply(matrix2);
print("Matrix Multiplication Result:", matrix1_multiply);

matrix1.invert();
print("Matrix Inversion Result:", matrix1_invert);

matrix1.transpose();
print("Matrix Transpose Result:", matrix1_transpose);

"""

if __name__ == "__main__":
    interpreter = run_code(test_code)