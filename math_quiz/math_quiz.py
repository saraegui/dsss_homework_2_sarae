import random

def get_random_number(min_val, max_val):
    """
    Returns a random integer between min_val and max_val.
    """
    return random.randint(min_val, max_val)

def choose_operator():
    """
    Randomly selects a math operator: +, -, or *.
    """
    return random.choice(['+', '-', '*'])

def formulate_problem(num1, num2, operator):
    """
    Creates a math problem and calculates the answer.
    """
    problem_text = f"{num1} {operator} {num2}"
    if operator == '+':
        solution = num1 + num2
    elif operator == '-':
        solution = num1 - num2
    else:
        solution = num1 * num2
    return problem_text, solution

def start_quiz():
    """
    Runs a math quiz with multiple questions.
    """
    score = 0
    total_questions = 3  # Number of questions in the quiz

    print("Welcome to Math Quiz!")
    print("Solve the math problems to score points.")

    for _ in range(total_questions):
        # Generate operands and operator
        num1 = get_random_number(1, 10)
        num2 = get_random_number(1, 5)
        operator = choose_operator()

        # Get problem and solution
        problem_text, correct_answer = formulate_problem(num1, num2, operator)
        print(f"\nProblem: {problem_text}")

        # User input with error check
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue  # Move to the next question

        # Check answer
        if user_answer == correct_answer:
            print("Right answer! +1 point.")
            score += 1
        else:
            print(f"Incorrect. The answer was {correct_answer}.")

    print(f"\nQuiz complete! Final score: {score}/{total_questions}")

if __name__ == "__main__":
    start_quiz()

