#John Fletcher
#Team 98
#9/14/2016

#Question 1

teams = []
#Ask user input for a file name
user_file = input("Please enter a file name(no quotes): ")

#Assign variable to openinging file and reading in while nesting the each team
#with their score within the list and stripping of extra punctuations
file_contents = [str(line.strip().split(",")) for line in open(user_file,"r")]
#Assign variable to list to seperate the team from score in the range of the
# opened file "file_contents"
#to use in printed statement and strip of extra punctuations
score_list = [file_contents[i].strip("[]").strip("'").split(" ") for i in range(len(file_contents))]
#Create a for loop to assign the seperated elements to the specified printed statement
#using indexing
for i in score_list:
    score = i[0],"have won",i[1],"games"
#assign a variable to join each teams statement going through the for loop
    new = ' '.join(score)
#Add the teams statemnet to a list to be saved
    teams.append(new)
#assign a variable to joing the list of all the teams statements so they
#are on seperate lines
    final_list = ('\n'.join(teams))
#Print the final result to the user
print(final_list)


#Question 2

#Assign variable to a list to sort names with less than 5 letters
names = [score_list[i][0] for i in range(len(score_list))  if len(score_list[i][0]) < 5 ]
#print statement with variable
print("Teams with names shorter than 5 letters: ",names)


#Question 3

#Import itemgetter from operator
from operator import itemgetter
#use for loop to set score as an integer
for i in score_list:
    i[1] = eval(i[1])
#set variable to order list of teams in reverse by wins
names = sorted(score_list, key =itemgetter(1), reverse = True)
#assign variable to list to contain only the three highest winning teams
high_scores = [names[i][0] for i in range(0,3)]
#print out statement with variable
print("The three teams with the highest wins are: ",high_scores)



