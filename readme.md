## **Setup for the program**

install antlr python runtime

```
pip install antlr4-python3-runtime==4.13.0
```

generate antlr lexer and parser with visitor pattern (java must be installed). visitor is easier for expression, return values, and functional things kinda

```
java -jar antlr.jar -Dlanguage=Python3 -visitor SimpleLang.g4
```

!!!NOTES!!!
only the interpreter.py SimpleLang.g4, usage.py are not auto-generated. Rest can be deleted if buggy

##Information about the program

Three primitive types - int, bool, string with static typing

Variable declarations (let), assignments, if/else control flow, returns, and function calls

Arithmetic (+,-,*,/), comparisons (>,<,>=,<=,==,!=), logical (and,or), parentheses grouping

Defined with 'func', support parameters with default values, explicit return types, and return statements

Lexical scoping with global and local environments, variables must be declared before use

Supports both single-line (//) and multi-line (/* */) comment

uses exceptions to get return value 

## **How to run this program**

1. Open terminal
2. Go to the path of the program
   ```
    cd <pathname>
   ```
3. Run the run.py file by passing the filename of the .txt
   ```
    python run.py <filename>.txt
   ```

## **Example Syntax:**

```
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

```
