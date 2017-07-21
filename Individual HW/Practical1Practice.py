
#Question 1


with open("teams.txt","r") as file:
    team_list = [line.strip().split(" ") for line in file]
    score_list = ["The "+line[0] + "have won "+line[1]+" games" for line in team_list]
print('\n'.join(score_list))


#Question 2


name = [team_list[i][0] for i in range(len(score_list)) if len(team_list[i][0]) <5]
print(name)


#Question 3


from operator import itemgetter
for i in team_list:
    i[1] = eval(i[1])

score_sort = sorted(team_list, key = itemgetter(1), reverse = True)

score_list = [score_sort[i][0] for i in range(0,3)]
print(score_list)


#Question 4

file_read = [word for word in open("words.txt","r").read().split()]
vowels_2 = [word for word in file_read if len([let for let in word if let in 'aeiou'])>=2]
print(vowels_2)


#Question 5

def valid_div(bound):
    while True:
        try:
            user_input = int(input("Please enter"+ bound + "(int): "))

        except:
            print("That's not an integer")

        else:
            return user_input

#Main

lower = valid_div("a lower bound")
upper = valid_div("an upper bound")

num_list = [i for i in range(lower,upper + 1) if i %2 == 0]
print(num_list)
        
factor = valid_div("a number to divide by")

div_list = [num for num in num_list if num %factor == 0]

print("All of the even numbers between",lower,"and",upper,\
      "that are divisible by",factor,"are: ",div_list)



#Question 6

def vowel_three(file):
    file_contents =[line.strip() for line in open("lines.txt","r")]
    vowels = [word for line in file_contents for word in line.split(" ") if len([let for let in word if let in 'aeiou'])>=2]

    print(vowels)






