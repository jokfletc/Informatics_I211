#Question 1 (Two Vowels v3)


all_lines = [line.strip() for line in open("lines.txt", "r")]

two_v_words = [word for line in all_lines for word in line.split(" ") if len([let for let in word if let in "aeiou"])>=2]
print("All lines in the file: ", all_lines)
print(two_v_words)
##
##words = []
##vowels = 0
##for i in line_list:
##    i = i.split(" ")
##    for letter in i:
##        for char in letter:
##            if char in 'aeiou':
##                vowels += 1
##                if vowels >= int(2):
##                    if letter not in words:
##                    
##                    
##                        words.append(letter)
##                    vowels = 0
##            
##print(words)


# Group Work 2

##code = {1:'i',3:'e',4:'a',5:'g',7:'t'}
####code = ('num','let')
##print(code)
##phrase = eval("7h15 15 4 t357")
##print("output:",".join([ch if ch.isaplpha() or ch == " "\
##else leet_dict[ch] for ch
##leet = input phrase
##      leet_dict = code
##      leet_dict.get(ch,ch) for ch in leet]))
