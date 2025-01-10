import sys
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

if __name__ == "__main__":
    # Check if a filename is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python run.py [filename].txt")
        sys.exit(1)

    # Get the filename from the command-line arguments
    filename = sys.argv[1]
    
    try:
        # Open and read the file
        with open(filename, 'r') as file:
            code = file.read()
        
        # Pass the file content to the interpreter
        interpreter = run_code(code)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")