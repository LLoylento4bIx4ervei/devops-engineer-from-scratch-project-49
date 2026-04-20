"""Game engine."""


def run_game(game_logic, instruction):
    """
    Universal game engine.
    
    Args:
        game_logic: function that returns (question, correct_answer)
        instruction: string with game rules/instructions
    """
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ").strip()
    print(f"Hello, {name}!")
    print(instruction)
    
    total_rounds = 3
    
    for round_num in range(total_rounds):
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")
