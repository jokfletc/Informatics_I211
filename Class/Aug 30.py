#Question 3

def game(move):
    import random
    game_options = ["rock","paper","scissors"]
    game_decisions = ""
    computer_option = random.choice(game_options)
    while move in ["rock","paper","scissors","stop"]:
        
        while move != "stop":
            if move == computer_option:
                game_decision = "Game Tied"
            elif move == "rock" and computer_option == "paper":
                game_decision = "User Lost"
            elif move == "rock" and computer_option == "scissors":
                game_decision = "User Won!"
            elif move == "paper" and computer_option == "rock":
                game_decision = "User Won!"
            elif move == "paper" and computer_option == "scissors":
                game_decision = "User Lost"
            elif move == "scissors" and computer_option == "rock":
                game_decision = "User Lost"
            elif move == "scissors" and computer_option == "paper":
                game_decision = "User Won!"
            print(game_decision)
            move = input("Please input a move from these choices; rock, paper, scissors, or stop: ")
        else:
            print("Game Over")
            break
    else:
        print("invalid input!")
        re_input = input("Please input a move from these choices; rock, paper, scissors, or stop: ")
        game(re_input)

#Main
user_input = input("Please input a move from these choices; rock, paper, scissors, or stop: ")
result = game(user_input)

