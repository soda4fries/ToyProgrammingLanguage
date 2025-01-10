import unittest
from interpreter import Interpreter
from antlr4 import InputStream, CommonTokenStream
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser

class TestSimpleLangInterpreter(unittest.TestCase):
    def setUp(self):
        self.interpreter = Interpreter()

    def run_code(self, code):
        input_stream = InputStream(code)
        lexer = SimpleLangLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = SimpleLangParser(token_stream)
        tree = parser.program()
        self.interpreter.visit(tree)

    def test_basic_types(self):
        code = """
        // Test basic types
        let a: int = 5;
        let b: float = 3.14;
        let c: bool = true;
        let d: string = "hello";

        // Test arrays
        let e: array<int> = [1, 2, 3];
        let f: array<float> = [1.1, 2.2, 3.3];
        let g: array<bool> = [true, false, true];
        let h: array<string> = ["one", "two", "three"];

        // Test lists
        let i: list<int> = [4, 5, 6];
        let j: list<float> = [4.4, 5.5, 6.6];
        let k: list<bool> = [false, true, false];
        let l: list<string> = ["four", "five", "six"];
        """
        self.run_code(code)


    def test_invalid_assignments(self):
        invalid_assignments = [
            # Assigning a string to an integer variable
            {
                "code": """
                let a: int = 5;
                a = "text"; // Should raise a type error
                """,
                "expected_error": TypeError
            },
            # Assigning a float to an integer variable
            {
                "code": """
                let b: int = 10;
                b = 3.14; // Should raise a type error
                """,
                "expected_error": TypeError
            },
            # Assigning an integer to a boolean variable
            {
                "code": """
                let c: bool = true;
                c = 42; // Should raise a type error
                """,
                "expected_error": TypeError
            },
            # Assigning a string to a boolean variable
            {
                "code": """
                let d: bool = false;
                d = "true"; // Should raise a type error
                """,
                "expected_error": TypeError
            },
            # Assigning a boolean to a string variable
            {
                "code": """
                let e: string = "hello";
                e = false; // Should raise a type error
                """,
                "expected_error": TypeError
            },
            # Assigning a list to an integer variable
            {
                "code": """
                let f: int = 100;
                f = [1, 2, 3]; // Should raise a type error
                """,
                "expected_error": TypeError
            },
            # Assigning an array of wrong type
            {
                "code": """
                let g: array<int> = [1, 2, 3];
                g = ["a", "b", "c"]; // Should raise a type error
                """,
                "expected_error": TypeError
            },
            # Assigning a mismatched type in array elements
            {
                "code": """
                let h: array<int> = [1, 2, 3];
                h[0] = "text"; // Should raise a type error
                """,
                "expected_error": TypeError
            },
            # Assigning an array to a float variable
            {
                "code": """
                let i: float = 2.5;
                i = [3.14, 2.71]; // Should raise a type error
                """,
                "expected_error": TypeError
            }
        ]

        for test_case in invalid_assignments:
            with self.assertRaises(test_case["expected_error"], msg=f"Failed for code: {test_case['code']}"):
                self.run_code(test_case["code"])

    def test_array_map_default(self):
        code = """
        let nums: array<int> = [1, 2, 3, 4, 5];
        nums.map(x => x * x);
        """
        self.run_code(code)
        result = self.interpreter.global_env.get("nums_map")
        self.assertEqual(result, [1, 4, 9, 16, 25])

    def test_array_map_mutate(self):
        code = """
        let nums: array<int> = [1, 2, 3, 4, 5];
        nums.map(x => x * x, mutate=true);
        """
        self.run_code(code)
        result = self.interpreter.global_env.get("nums")
        self.assertEqual(result, [1, 4, 9, 16, 25])


    def test_linear_regression(self):
        code = """
        let x: array<float> = [1.0, 2.0, 3.0, 4.0, 5.0];
        let y: array<float> = [2.1, 4.0, 6.3, 8.0, 9.9];
        x.linreg(y);
        """
        self.run_code(code)

        # Retrieve results from the environment
        slope = self.interpreter.global_env.get("x_slope")
        intercept = self.interpreter.global_env.get("x_intercept")
        r_squared = self.interpreter.global_env.get("x_r_squared")

        # Assert expected results (calculated externally or using a known library)
        self.assertAlmostEqual(slope, 1.960, places=2)
        self.assertAlmostEqual(intercept, 0.18, places=2)
        self.assertAlmostEqual(r_squared, 0.9980, places=2)


if __name__ == "__main__":
    unittest.main()
