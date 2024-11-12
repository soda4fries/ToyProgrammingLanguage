from antlr4 import *
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from interpreter import Interpreter

def run_code(code):
    input_stream = InputStream(code)
    lexer = SimpleLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SimpleLangParser(stream)
    tree = parser.program()
    interpreter = Interpreter()
    interpreter.visit(tree)

example_code = """
// Function with type and default parameter
func greet(name: string = "World") -> string {
    return "Hello, " + name;
}

// Function overloading with different types
func add(x: int, y: int) -> int {
    return x + y;
}

func add(x: string, y: string) -> string {
    return x + y;
}

// Recursive function
func factorial(n: int) -> int {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

// Function returning boolean for if condition
func isPositive(n: int) -> bool {
    return n > 0;
}

/* Testing all features */
let result: string = greet();  // Uses default parameter
print(result);

let sum1: int = add(5, 3);    // Calls int version
print(sum1);

let sum2: string = add("Hello, ", "World");  // Calls string version
print(sum2);

let fact: int = factorial(5);  // Tests recursion
print(fact);
print(isPositive(-120));

// Testing if condition with function return
if (isPositive(-120)) {
    print("Number is positive!");
} else {
    print("Number is negative!");
}
"""

if __name__ == "__main__":
    run_code(example_code)