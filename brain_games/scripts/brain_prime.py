#!/usr/bin/env python3
"""Brain Prime game entry point."""

from brain_games.engine import run_game
from brain_games.games.brain_prime import get_question_and_answer


def main():
    """Run brain-prime game."""
    instruction = (
        'Answer "yes" if given number is prime. '
        'Otherwise answer "no".'
    )
    run_game(get_question_and_answer, instruction)


if __name__ == "__main__":
    main()
