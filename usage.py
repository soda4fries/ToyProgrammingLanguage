# usage.py
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

# Test code
test_code = """
// Basic variable declarations and operations
let x: int = 10;
let y: int = 20;
print(x + y);

// Array operations
let numbers: array<int> = [1, 5, 3, 2, 4];
numbers.sort();
print(numbers);

// List operations
let fruits: list<string> = ["apple", "banana"];
fruits.append("orange");
print(fruits);
fruits.remove("banana");
print(fruits);
fruits.sort();
print(fruits);

// Function with recursion
func factorial(n: int) -> int {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

// Test factorial function
let fact5: int = factorial(5);
print(fact5);

// Array indexing and modification
let arr: array<int> = [1, 2, 3];
arr[1] = 5;
print(arr);
print(arr[1]);

// While loop
let i: int = 0;
while (i < 5) {
    print(i);
    i = i + 1;
}

// Test float variable declaration and arithmetic
let a: float = 3.14;
print(a); // 3.14

// Float arithmetic
let b: float = 2.5;
print(b); // 2.5
let c: float = a + b;
print(c); // 5.64
c = a * b;
print(c); // 7.85

// Mixed-type arithmetic (int and float)
let d: int = 10;
let e: float = d * a;
print(e); // 31.4

// Float comparison
let isGreater: bool = a > b;
print(isGreater); // true

// Default float value
let f: float;
print(f); // 0.0
"""

if __name__ == "__main__":
    interpreter = run_code(test_code)