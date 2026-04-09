"""Brain GCD game logic."""

import math
import random


def get_question_and_answer():
    """Generate two random numbers and return question with GCD answer."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    
    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))
    
    return question, correct_answer
