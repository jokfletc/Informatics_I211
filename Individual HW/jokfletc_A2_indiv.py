#John Fletcher
#Group 98



#Question 1
#1# Start function titling it "Fullweek" and taking a day as an arguement
def fullweek(day):
    
#2# Use a dictionary with the abbreviations as the keys and the full day as the set value
    week = {'M':'Monday','T':'Tuesday','W':'Wednesday','R':'Thursday','F':'Friday','S':'Saturday','U':'Sunday'}
#3# If input not in the dictionary the input is invalid
    if day in week:
#4# Print the value for the abbreviated day entered by using the key provided   
        print (week[day])
#5# If input is invalid the following message will be printed out to the user
    else:
        print("Invalid input! Please try again choosing from these options; M,T,W,R,F,S,U")
       

#Main
#6# Ask user input an abbreviated day of the week to return a result
user_input = input("Please input an abreviation for a day of the week; M,T,W,R,F,S,U: ")

#7# Set result to the function taking the user_input as the argument
result = fullweek(user_input)



#Question 2
#1# Create a function titled "fullweek_2"
def fullweek_2(day):
#2# assign a dictionary of the days of the week to their keys of one letter
#2# abbreviation to variable "week"
    week = {'M':'Monday','T':'Tuesday','W':'Wednesday','R':'Thursday','F':'Friday','S':'Saturday','U':'Sunday'}
#3# assign list of valid inputs to variable "valid_inputs"
    valid_inputs = ["M","T","W","R","F","S","U","DONE"]
#4# Create while loop so that while day is not equivalent to "Done"
    while day != "DONE":
#5# use if statement so that if day is in list valid_inputs
        if day in valid_inputs:
#6# print the day of the week associated with the entered one letter abbreviation
            print(week[day])
#7# ask the user for another input for the function fullweek_2
            day = input("Please input an abreviation for a day of the week; M,T,W,R,F,S,U,DONE: ").upper()
#8# Use else statement so that if user input is not in the list
        else:
#9# Print the input was invalid and ask user for another input
            print("Invalid input! Please try again choosing from these options; M,T,W,R,F,S,U,DONE")
            day = input("Please input an abreviation for a day of the week; M,T,W,R,F,S,U,DONE: ").upper()
#10# If the input is equivalent to "Done" print "Stop" to show the user
#10# the function has been instructed to end
    else:
        print("Stop")


#Main
#11# ask user input an abbreviated day of the week to return a result
user_input = input("Please input an abreviation for a day of the week; M,T,W,R,F,S,U,DONE: ").upper()

#12# set result to the function taking the user_input as the argument
result = fullweek_2(user_input)



#Question 3
#1# Create a function to start building the program to decide the statuse
#1# of the game titled "game" and argument titled "move"
def game(move):
#2# import random function
    import random
#2# Set the variable titled "game_options" to a list containing rock, paper,
#2# and scissors
    game_options = ["rock","paper","scissors"]
#3# set variable "game_decision" to nil and will be a value through the use
#3# of if statements later on
    game_decisions = ""
#4# Have the computer randomly choose one item from the "game_options" list
#4# using the random function
    computer_option = random.choice(game_options)
#5# Create a while loop so while the user input is one of the elements in the list
    while move in ["rock","paper","scissors","stop"]:
#6#   Initiate a while loop for while user_input is not set to "stop"
        while move != "stop":
#7# Implement if statement so that if user input and computers choice is
#7# equivalent the game_decision is set to "Game Tied"
            if move == computer_option:
                game_decision = "Game Tied"
#8# Use elif statement so that if user input is rock and computer's
#8# choice is paper, game_decision is set to "User Lost"
            elif move == "rock" and computer_option == "paper":
                game_decision = "User Lost"
#9# Use elif statement so that if user input is rock and computer's
#9# choice is scissors, game_decision is set to "User Won!"
            elif move == "rock" and computer_option == "scissors":
                game_decision = "User Won!"
#10# Use elif statement so that if user input is paper and computer's
#10# choice is rock, game_decision is set to "User Won!"
            elif move == "paper" and computer_option == "rock":
                game_decision = "User Won!"
#11# Use elif statement so that if user input is paper and computer's
#11# choice is scissors, game_decision is set to "User Lost"
            elif move == "paper" and computer_option == "scissors":
                game_decision = "User Lost"
#12# Use elif statement so that if user input is scissors and computer's
#12# choice is rock, game_decision is set to "User Lost"
            elif move == "scissors" and computer_option == "rock":
                game_decision = "User Lost"
#13# Use elif statement so that if user input is scissors and computer's
#13# choice is paper, game_decision is set to "User Won!"
            elif move == "scissors" and computer_option == "paper":
                game_decision = "User Won!"
#14# print variable game_decision to deliver the game's decision to the user
            print(game_decision)
#15# Ask the user to input another move for the game
            move = input("Please input a move from these choices; rock, paper, scissors, or stop: ")
        else:
#16# If the input is "stop" use else statement to print "Game Over" and end the game
            print("Game Over")
#17# Use break statement to end game
            break
#18# If input is not in the list above then use else statement to print
#18# "Invalid Input and ask the user to enter a new input for a move choice
#18# and run the game again
    else:
        print("invalid input!")
        re_input = input("Please input a move from these choices; rock, paper, scissors, or stop: ")
        game(re_input)

#Main
#19# Ask the user to input the initial move choice
user_input = input("Please input a move from these choices; rock, paper, scissors, or stop: ")
#20# Assign the variable user_input as the game function's arguement
result = game(user_input)



