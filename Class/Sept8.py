#Question 1

num_list = [num*2 for num in range(10)]
print(num_list)


#Question 2

div_list = [num for num in range(100) if num %10 == 0]
print(div_list)


#Question 3

words = ["apple","ball","candle","dog","egg","frog"]

new_list = [words[i].upper()  if len(words[i]) < 4 else words[i] for i in range(len(words)) ]

sec_list = [words[i].upper() for i in range(len(words))  if len(words[i]) < 4]
print(new_list)
print(sec_list)


#Question 4

message = input("Please enter the secret: ")
secret_list = ["-" * len(message[i]) if message[i].isalpha() else message[i] for i in range(len(message))]
print(''.join(secret_list))
