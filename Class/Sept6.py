###Squares[Group Work]
##
##def squares(number):
##    num_list=[i*i for i in range(0,number+1)]
##    print(num_list)
###main
##user_input = eval(input("Enter an integer: "))
##result = squares(user_input)
##
##
###Divisible By [Group Work]
##def divisible(num_1,num_2):
##    num_list = [num for num in range(num_1, num_2 +1) if num %2 == 0]
##    print("All of the even numbers between",num_1,"and",num_2,":",num_list)
##    div_num = eval(input("Please enter a number to divide by: "))
##    div_list = [num for num in num_list if num %div_num == 0]
##    print("All of the even numbers between",num_1,"and",num_2,"that are divisible by",div_num,":",div_list)
##
###main
##first_num  = eval(input("Please enter a lower bound(int): "))
##sec_num = eval(input("Please enter an upper bound(int): "))
##result = divisible(first_num,sec_num)
##
##







let_num = 0
word_list = []
file_contents = [line.split() for line in open("words.txt","r") ]
for line in file_contents:
    
    for word in line:
        let_num = 0
        
        for letter in word:
            
            if letter in "aeiou":
                let_num +=1
        if let_num >= 2:
            word_list.append(word)
print(word_list[0])
            
       

