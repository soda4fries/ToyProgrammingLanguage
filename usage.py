from antlr4 import *
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from interpreter import SimpleLangInterpreter

def run_program(source_code: str):
    input_stream = InputStream(source_code)
    lexer = SimpleLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SimpleLangParser(token_stream)
    tree = parser.program()
    
    interpreter = SimpleLangInterpreter()
    return interpreter.visit(tree)

comprehensive_example = """
/* Comprehensive test suite for SimpleLang
   Testing all features and their combinations */

// 1. Basic Math Functions
func square(x: Int) -> Int {
    x * x
}

func cube(x: Int) -> Int {
    x * x * x
}

// 2. Recursive Functions
func factorial(n: Int) -> Int {
    if (n <= 1) {
        1
    } else {
        n * factorial(n - 1)
    }
}

func fibonacci(n: Int, a: Int = 0, b: Int = 1) -> Int {
    if (n <= 0) {
        a
    } else {
        fibonacci(n - 1, b, a + b)
    }
}

// 3. String Processing
func repeat(s: String, n: Int) -> String {
    if (n <= 0) {
        ""
    } else {
        s + repeat(s, n - 1)
    }
}

// 4. Type Conversion Functions
func stringToNumber(s: String) -> Float {
    Float(s)
}

func roundToPrecision(n: Float, precision: Int) -> Float {
    round(n, precision)
}

// 5. Complex Return Types
func complexOperation(x: Float, flag: Bool) -> String {
    let result: Float = if (flag) {
        x * 2.0
    } else {
        x / 2.0
    };
    String(roundToPrecision(result, 2))
}

// 6. Nested Function Calls
func nestedOperation(x: Int) -> Int {
    square(cube(x)) + cube(square(x))
}

// 7. Block Return Functions
func createCounter(start: Int) -> Int {
    {
        let current: Int = start;
        current + 1
    }
}

// 8. Boolean Logic Functions
func analyzeBooleans(a: Bool, b: Bool) -> String {
    let andResult: Bool = a and b;
    let orResult: Bool = a or b;
    let notResult: Bool = not a;
    "AND=" + String(andResult) + 
    ", OR=" + String(orResult) + 
    ", NOT=" + String(notResult)
}

// Main test suite
{
    let testResults: String = "";
    
    // Test Section 1: Basic Arithmetic and Type Conversion
    {
        // Integer operations
        let x: Int = 5;
        let y: Int = 3;
        let sum: Int = x + y;
        let diff: Int = x - y;
        let prod: Int = x * y;
        let quot: Float = Float(x) / Float(y);
        
        testResults = testResults + "Basic Arithmetic: " +
            "sum=" + String(sum) + ", " +
            "diff=" + String(diff) + ", " +
            "prod=" + String(prod) + ", " +
            "quot=" + String(roundToPrecision(quot, 2));
    };
    print(testResults);
    testResults = "";

    // Test Section 2: Compound Assignments
    {
        let num: Float = 10.0;
        num += 5.0;
        num *= 2.0;
        num -= 7.0;
        num /= 2.0;
        testResults = testResults + "Compound Assignment: final=" + String(num);
    };
    print(testResults);
    testResults = "";

    // Test Section 3: Type Casting Chain
    {
        let strNum: String = "123.456";
        let floatNum: Float = Float(strNum);
        let intNum: Int = Int(floatNum);
        let backToString: String = String(intNum);
        
        testResults = testResults + "Type Casting: " +
            "string->float=" + String(floatNum) + ", " +
            "float->int=" + String(intNum) + ", " +
            "int->string=" + backToString;
    };
    print(testResults);
    testResults = "";

    // Test Section 4: Function Results and Composition
    {
        let squareOf5: Int = square(5);
        let cubeOf3: Int = cube(3);
        let fact5: Int = factorial(5);
        let fib7: Int = fibonacci(7);
        
        testResults = testResults + "Function Results: " +
            "square(5)=" + String(squareOf5) + ", " +
            "cube(3)=" + String(cubeOf3) + ", " +
            "factorial(5)=" + String(fact5) + ", " +
            "fibonacci(7)=" + String(fib7);
    };
    print(testResults);
    testResults = "";

    // Test Section 5: Complex Blocks and Nested Operations
    {
        let nested: Int = nestedOperation(2);
        let counter: Int = createCounter(10);
        let complex: Float = {
            let x: Float = 10.5;
            let y: Int = 2;
            x * Float(square(y))
        };
        
        testResults = testResults + "Complex Operations: " +
            "nested=" + String(nested) + ", " +
            "counter=" + String(counter) + ", " +
            "complex=" + String(complex);
    };
    print(testResults);
    testResults = "";

    // Test Section 6: Boolean Operations and Control Flow
    {
        let boolResult: String = analyzeBooleans(true, false);
        let controlFlow: String = if (10 > 5) {
            if (true and false) {
                "nested true"
            } else {
                "nested false"
            }
        } else {
            "outer false"
        };
        
        testResults = testResults + "Boolean and Control: " +
            "bools=" + boolResult + ", " +
            "flow=" + controlFlow;
    };
    print(testResults);
    testResults = "";

    // Test Section 7: String Operations
    {
        let str1: String = "Hello";
        let str2: String = "World";
        let combined: String = str1 + " " + str2;
        let repeated: String = repeat("*", 3);
        
        testResults = testResults + "String Operations: " +
            "combined='" + combined + "', " +
            "repeated='" + repeated + "'";
    };
    print(testResults);
    testResults = "";

    // Test Section 8: Mixed Type Operations
    {
        let intVal: Int = 42;
        let floatVal: Float = 3.14;
        let boolVal: Bool = true;
        let mixedResult: Float = if (boolVal) {
            Float(intVal) * floatVal
        } else {
            floatVal / Float(intVal)
        };
        
        testResults = testResults + "Mixed Types: " +
            "result=" + String(roundToPrecision(mixedResult, 2));
    };
    print(testResults);
    testResults = "";

    // Test Section 9: Complex Function Interactions
    {
        let f1: Int = factorial(3);
        let f2: Float = Float(f1) * 1.5;
        let f3: String = complexOperation(f2, true);
        let f4: Int = Int(stringToNumber(f3));
        
        testResults = testResults + "Function Chain: " +
            "result=" + String(f4);
    };
    print(testResults);

    "All tests completed successfully"
}
"""

def run_all_examples():
    print("Running SimpleLang examples...")
    print("=" * 50)
    
    result = run_program(comprehensive_example)
    
    print("\nFinal result:", result)
    print("=" * 50)

if __name__ == "__main__":
    run_all_examples()