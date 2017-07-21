#Name: John Fletcher
#Username: jokfletc




###Question 1###


#1# Create a function to start building the program to decide the statuse
#1# of the game titled "decision" and argument titled "move"
#2# Set the variable titled "game_options" to a list containing rock, paper,
#2# and scissors
#3# set variable "game_decision" to nil and will be a value through the use
#3# of if statements later on
#4# Initiate a while loop for while user_input is not set to "stop"
#5# Import "random"
#6# Have the computer randomly choose one item from the "game_options" list
#6# using the random function
#7# Set this item to varable titled "computer_option"
#8# Create if and elif statements to compare the computer_option and user_input
#9# If user_input's string value is equal to "rock" and computer_option is
#9# equal to "rock", set variable "game_decision" to "Game Tied"
#10# Elif user_input is equal to "rock" and game_option is equal to "paper",
#10# set variable "game_decision" to "User Lost"
#11# Elif user_input is equal to "rock" and game_option is equal to "scissors",
#11# set variable "game_decision" to "User Won!"
#12# Elif user_input is equal to "paper" and game_option is equal to "rock",
#12# set variable "game_decision" to "User won!"
#13# Elif user_input is equal to "paper" and game_option is equal to "paper",
#13# set variable "game_decision" to "Game Tied"
#14# Elif user_input is equal to "paper" and game_option is equal to "scissors",
#14# set variable "game_decision" to "User Lost"
#15# Elif user_input is equal to "scissors" and game_option is equal to "rock",
#15# set variable "game_decision" to "User Lost"
#16# Elif user_input is equal to "scissors" and game_option is equal to "paper",
#16# set variable "game_decision" to "User Won!"
#17# Elif user_input is equal to "scissors" and game_option is equal to
#17# "scissors", set variable "game_decision" to "Game Tied"
#18# Elif user_input is equal to "stop" set variable "game_decision" to
#18# "Game Over"
#19# Create else statement to the end of the initial while loop, requesting
#19# a user to input either rock, paper, scissors, or stop(to end game)
#20# Return the variable "game_decision"

#21# Start the main section of your function
#22# Set a variable titled "user_move" to input("rock, paper, scissors,
#22# or stop(to end game: ")
#23# Set variable titled "result" to the function assigning the variable
#23# "user_move" as the functions argument
#24# Print the variable "result" to print the return value of the function





###Question 2###


#1# Create function to start building the program to compare the two
#1# lists titled "compare"
def compare(list_one,list_two):
#2# Set variable result to an empty array to hold common elements if any exist
    common_numbers = []
    list_decision = ""
#3# Create a for loop to run through "list_1" and identify the elements it
#3# contains
    for number in list_1:
#4# Create an if statement to see if the current number the program is
#4# evaluating from "list_1" is within "list_2"
        if number in list_2:
#5# If the number is also within "list_2" add it to the "common_numbers" array
            common_numbers.append(number)
#6# Identify the number of elements the have in common if any by using the "len"
#6# function to find the number of elements in the "common_numbers" array and
#6# an equal to or great than symbol to one to discover if any common elements
#6# exist 
    if len(common_numbers) >= 1:
#7# Use the return command to save True as the function's value if the "if"
#7# statement is True
        return True
#8# use the return command to save False as the function"s value if the "if"
#8# statement is False
    return False
   
    
#main
#7# Set list one to variable "list_1"
list_1 = [1,2,3,4,5]
#8# set list two to variable "list_2"
list_2 = [2,3,6,7,8]
#9# Set variable "result" to the function assigning the variables "list_1"
#10# and "list_2" as the functions arguments
result = compare(list_1,list_2)
#11# Print the variable "result" to print the return value of the function
print(result)







###Question 3###


#1# Create a function to start building the program to reverse the order
#1# of the string titled "reverse"
def reverse(string):
    
#2# Set variable "reverse_string" to an empty array
    reverse_string = []
#3# Set variable "string_range" to the number of characters in the string
#3# using the "len" function
    string_range = len(user_string)
#4# Create a while loop for string_range is not nil to perform an action
    while string_range:
#5# subtract 1 from the strings range to move down 1 position closer to
#5# the beginning of the string
        string_range -= 1
#6# Add the character at this current position to the "reverse_string" array
        reverse_string.append(user_string[string_range])
#7# Once the variable "string_range" is nil, return "reverse_string" to save
#7# the value of the reversed order of the original string the user input so
#7# it may be printed later 
    return ''.join(reverse_string)


#main
#8# Request an input from the user for a string and set it to the variable
#8# "user_string"
user_string = input("Please enter a string: ")
#9# Set variable "result" to the function assigning the variable "user_string"
#9# as the argument
result = reverse(user_string)
#10# Print the variable "result" to send the reversed string of the user's
#10# orginal string back to the user
print(result)

