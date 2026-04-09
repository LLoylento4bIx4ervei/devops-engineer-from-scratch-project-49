"""Brain Calculator game logic."""

import random


def calculate(num1: int, num2: int, operator: str) -> int:
    """Perform calculation based on operator."""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    else:
        raise ValueError(f"Unknown operator: {operator}")


def get_question_and_answer():
    """Generate random expression and correct answer."""
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(['+', '-', '*'])
    
    question = f"{num1} {operator} {num2}"
    correct_answer = str(calculate(num1, num2, operator))
    
    return question, correct_answer
