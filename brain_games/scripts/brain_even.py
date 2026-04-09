#!/usr/bin/env python3


import random
import sys


def welcome_user() -> str:

    print("Welcome to the Brain Games!")
    name = input("May I have your name? ").strip()
    print(f"Hello, {name}!")
    return name


def ask_question(question: str) -> str:

    print(f"Question: {question}")
    return input("Your answer: ").strip().lower()


def is_even(number: int) -> bool:

    return number % 2 == 0


def main():
    
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_count = 0
    total_questions = 3

    while correct_count < total_questions:
        number = random.randint(1, 100)
        correct_answer = "yes" if is_even(number) else "no"
        user_answer = ask_question(str(number))

        if user_answer == correct_answer:
            print("Correct!")
            correct_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(.")
	    print(" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            sys.exit(1)

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
