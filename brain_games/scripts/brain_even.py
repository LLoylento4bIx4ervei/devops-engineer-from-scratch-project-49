#!/usr/bin/env python3
"""Brain Even game entry point."""

from brain_games.engine import run_game
from brain_games.games.brain_even import get_question_and_answer


def main():
    """Run brain-even game."""
    instruction = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(get_question_and_answer, instruction)


if __name__ == "__main__":
    main()
