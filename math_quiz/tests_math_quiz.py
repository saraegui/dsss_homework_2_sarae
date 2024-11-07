import unittest
from math_quiz import generate_random_value, select_operator, create_math_problem


class TestMathQuizGame(unittest.TestCase):

    def test_generate_random_value(self):
        # Test if random values are within the specified boundaries
        lower_bound = 1
        upper_bound = 10
        for _ in range(100):  # Run the test multiple times for variability
            outcome = generate_random_value(lower_bound, upper_bound)
            self.assertTrue(lower_bound <= outcome <= upper_bound, f"Out of range: {outcome}")

    def test_select_operator(self):
        # Test if the chosen operator is one of the predefined options
        valid_operators = {'+', '-', '*'}
        for _ in range(100):  # Run multiple checks to ensure randomness
            operator = select_operator()
            self.assertIn(operator, valid_operators, f"Unexpected operator: {operator}")

    def test_create_math_problem(self):
        # Verify that math problems and corresponding answers are accurate
        test_scenarios = [
            (5, 3, '+', "5 + 3", 8),
            (15, 7, '-', "15 - 7", 8),
            (8, 2, '*', "8 * 2", 16),
        ]

        for operand1, operand2, operator, expected_problem, expected_answer in test_scenarios:
            problem, answer = create_math_problem(operand1, operand2, operator)
            self.assertEqual(problem, expected_problem, f"Problem mismatch: {problem}")
            self.assertEqual(answer, expected_answer, f"Answer mismatch: {answer}")


if __name__ == "__main__":
    unittest.main()
