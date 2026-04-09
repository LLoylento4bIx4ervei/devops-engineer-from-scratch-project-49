#!/usr/bin/env python3
"""Brain Progression game entry point."""

from brain_games.engine import run_game
from brain_games.games.brain_progression import get_question_and_answer


def main():
    
    instruction = "What number is missing in the progression?"
    run_game(get_question_and_answer, instruction)


if __name__ == "__main__":
    main()
