#!/usr/bin/env python3
"""Brain Calculator game entry point."""

from brain_games.engine import run_game
from brain_games.games.brain_calc import get_question_and_answer


def main():
    """Run brain-calc game."""
    instruction = 'What is the result of the expression?'
    run_game(get_question_and_answer, instruction)


if __name__ == "__main__":
    main()
