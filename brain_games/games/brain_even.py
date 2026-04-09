"""Brain Even game logic."""

import random


def is_even(number: int) -> bool:
    """Return True if number is even."""
    return number % 2 == 0


def get_question_and_answer():
    """Generate question and correct answer for brain-even."""
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer
