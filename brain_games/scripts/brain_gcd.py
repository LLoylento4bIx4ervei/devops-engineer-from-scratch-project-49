#!/usr/bin/env python3
"""Brain GCD game entry point."""

from brain_games.engine import run_game
from brain_games.games.brain_gcd import get_question_and_answer


def main():
    """Run brain-gcd game."""
    instruction = "Find the greatest common divisor of given numbers."
    run_game(get_question_and_answer, instruction)


if __name__ == "__main__":
    main()
