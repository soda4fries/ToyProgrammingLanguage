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

Arithmetic (+,-,\*,/), comparisons (>,<,>=,<=,==,!=), logical (and,or), parentheses grouping

Defined with 'func', support parameters with default values, explicit return types, and return statements

Lexical scoping with global and local environments, variables must be declared before use

Supports both single-line (//) and multi-line (/\* \*/) comment

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
"""
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

// Pattern matching example
let value: int = 42;
match value {
    case 0 => print("Value is zero");
    case 42 => print("Value is forty two");
    case _ => print("Value is something else");
}

// Array pattern matching
let arr: array<int> = [1, 2, 3];
match arr {
    case [1, 2, 3] => print("Array matches [1, 2, 3]");
    case _ => print("Array does not match");
}

let numbers: array<int> = [1, 2, 3, 4, 5];
numbers.filter(x => x % 2 == 0);
print(numbers_filter);

let numbers: array<int> = [1, 2, 3, 4, 5];
numbers.map(x => x * x);
print(numbers_map);

// Array rotation and shifting
let nums: array<int> = [1, 2, 3, 4, 5];
nums.rotate(1);
print("Rotated Array (by 1):", nums_rotate);

nums.rotate(2);
print("Rotated Array (by 2):", nums_rotate);

nums.rotate(3);
print("Rotated Array (by 3):", nums_rotate);

nums.shift(2);
print("Shifted Array (by 2):", nums_shift);

// "Mary Had a Little Lamb" (complete)
let melody1: array<float> = [3,2,1,2,3,3,3, 2,2,2, 3,5,5, 3,2,1,2,3,3,3, 3,2,2,3,2,1];
print("Playing Mary Had a Little Lamb...");
melody1.play();

// "Twinkle Twinkle Little Star" (complete)
let melody2: array<float> = [0,0,4,4,5,5,4, 3,3,2,2,1,1,0, 4,4,3,3,2,2,1, 4,4,3,3,2,2,1, 0,0,4,4,5,5,4, 3,3,2,2,1,1,0];
print("Playing Twinkle Twinkle...");
melody2.play();

// "Row Row Row Your Boat" (complete with rounds)
let melody3: array<float> = [0,0,0,1,2, 2,1,2,3,4, 7,7,7,4,4,4, 2,2,2,1,1,1, 4,4,4,2,2,2, 0,0,0,1,2, 2,1,2,3,4];
print("Playing Row Row Row Your Boat...");
melody3.play();

// "Hot Cross Buns" (complete with repeats)
let melody4: array<float> = [3,2,1, 3,2,1, 1,1,1,1, 2,2,2,2, 3,2,1, 3,2,1, 3,2,1, 1,1,1,1, 2,2,2,2, 3,2,1];
print("Playing Hot Cross Buns...");
melody4.play();

// "Frère Jacques" (complete with repeats)
let melody5: array<float> = [0,1,2,0, 0,1,2,0, 2,3,4, 2,3,4, 4,5,4,3,2,0, 4,5,4,3,2,0, 0,4,0, 0,4,0, 0,1,2,0, 0,1,2,0];
print("Playing Frère Jacques...");
melody5.play();

// "London Bridge" (complete)
let melody6: array<float> = [4,5,4,3,2,3,4, 2,3,4,3,4,5, 4,5,4,3,2,3,4, 2,4,0, 4,5,4,3,2,3,4, 2,3,4,3,4,5, 4,5,4,3,2,3,4, 2,4,0];
print("Playing London Bridge...");
melody6.play();

// "Baa Baa Black Sheep" (complete)
let melody7: array<float> = [0,0,4,4,5,5,4, 3,3,2,2,1,1,0, 4,4,3,3,2, 4,4,3,3,2, 0,0,4,4,5,5,4, 3,3,2,2,1,1,0];
print("Playing Baa Baa Black Sheep...");
melody7.play();
"""

```
