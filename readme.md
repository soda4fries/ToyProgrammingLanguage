install antler python runtime

pip install antlr4-python3-runtime==4.13.0

generate antler lexer and parser with visitor pattern (java must be installed). visitor is easier for expression, return values, and functional things kinda

java -jar antlr.jar -Dlanguage=Python3 -visitor SimpleLang.g4

only the interpreter.py SimpleLang.g4, usage.py are not auto-generated. Rest can be deleted if buggy


Three primitive types - int, bool, string with static typing
Variable declarations (let), assignments, if/else control flow, returns, and function calls
Arithmetic (+,-,*,/), comparisons (>,<,>=,<=,==,!=), logical (and,or), parentheses grouping
Defined with 'func', support parameters with default values, explicit return types, and return statements
Lexical scoping with global and local environments, variables must be declared before use
Supports both single-line (//) and multi-line (/* */) comments

negative number handling a bit bad.
need to add type checking but will crash since python will not execute using wrong type (maybe)
uses exceptions to get return value 
