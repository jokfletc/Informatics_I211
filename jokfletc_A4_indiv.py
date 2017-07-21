#Name: John Fletcher
#Group: 98



#Phase 1 (30 points)
#import String module
import string
#Create function
def pl_words(user_string):
#Create empty list to save translated words into
    string_list = []
#Split words with in each string from eachother
    user_string = user_string.split()
    
# use for loop to designate each word within the list
    for i in range(len(user_string)):
#assign variable to each word by placement of i
        word = user_string[i]
#pre is the first letter in each word
        pre = word[0]
#Suf is evaerything from the second letter and on
        suf = word[1:]
           
#if length of word is less than or equal to 1 then    
        if len(word) <= 1:
                    
#tranlation is word plus "yay"      
            word = word+"yay"
#If a character in the word is an ending punctuation
#mark then remove it and add it t the end of the translated word
            for ch in word:
                if ch in ".,?!":
                    word = word.replace(ch,'')+ch
#Add the translated word to the translated list
            string_list.append(word)
                    
                
#If the first letter in a word that is greater than one then variable
#cap is True
        if pre.upper() == pre:
            cap = True
        
            
#esle variable cap is False
        else:
            cap = False
#If cap is False word is the Suffix + the preffix lower case + "ay"
            word = suf + pre.lower() + "ay"
#If a character in the word is an ending punctuation
#mark then remove it and add it t the end of the translated word
            for ch in word:
                if ch in ".,?!":
                    word = word.replace(ch,'')+ch
#Add the translated word to the translated list
            string_list.append(word)
#If cap is True word = capitalized first letter from the word iteration above
# plus the suffix of the iteration from above
        if cap:
            word = suf + pre.lower() + "ay"
            word =word[0].upper() + word[1:]
#If a character in the word is an ending punctuation
#mark then remove it and add it t the end of the translated word
            for ch in word:
                if ch in ".,?!":
                    word = word.replace(ch,'')+ch
#Add the translated word to the translated list
            string_list.append(word)
    


#return the string of the tranlated words for given line
    return(' '.join(string_list))









#Phase 2(25 points)

def pl_converter(user_reader,user_writer):
#open the user inputed file to read
    contents = open(user_reader,"r")
#open the file designated to write within
    writer = open(user_writer,"w")
    
#for line in the opened file to read..
    for line in contents:
#send each line to the function"pl_words" for translation
        result = pl_words(line)
#result = initial translated string plus line break for upcoming string
        result = str(result + "\n")
#write translated lines to writer file
        writer.write(result)
#Close the files
    contents.close()
    writer.close()
#return result
    return result



    



#Phase 3(25 points)

#import needed modules
import os
import csv
from os import listdir
from os.path import isfile, join


#get home path for device being used
home = os.getcwd()

#Have user input desired directory
user_dictionary = input("Please enter a directory you would like to access for a file to translate to pig latin: ")

#create list of all files within directory that are text files
file_names = [file for file in listdir(user_dictionary) if isfile(join(user_dictionary, file)) if file.endswith(".txt")]

#print file list for directory
print("Files in the "+user_dictionary+" directory:")
print(file_names)

#have user input file name from list above to translate
user_input = input("From these choices please select a file name: ")

#assign variable to the path of the desired file
read_file = os.path.join(home,user_dictionary,user_input)

#make sure path exists for file or folder errors
if os.path.exists(read_file):

#assign path to the tranlations directory within current directory
    dir_path = os.path.join(home,user_dictionary,"translations")
#check to see if directory already exists
    if not os.path.exists(dir_path):
#if not create directory
        new_directory = os.makedirs(dir_path)

#Assign the file to write in to the tranlations directory with the same file name
#as the file initially chosen
    write_file = os.path.join(dir_path,user_input+"(pig).txt")
#Send the file paths to the function "pl_converter to begin translation process
    answer = pl_converter(read_file,write_file)
else:
#If file name doesn't exist print Error message
    print("ERROR: File chosen doesn't exist! ")
    

#Phase 4(20 points)
    
#Import needed modules
import datetime

#asign variable to date function to get todays date information
now = datetime.datetime.today()

#create date string for requested format
today = now.strftime("%A,the %d"+"th"+ " of %B,%y,%H:%M")

#check if initial file exists                    
if os.path.exists(read_file):
    
#if so open file to write date information
    with open(write_file, "r+") as phase_4:
        
#assign variable to all content in file initially
        content = phase_4.read()
        
#locate first position in file
        phase_4.seek(0,0)
        
#Strip the date information of all none needed characters
#add a line break and add content below
        phase_4.write(today.rstrip('\r\n')+ '\n' +"\n" + content)

#open the write file
    f = open(write_file,"a")
    
#write the requested message at the bottom of the text file
    f.write("\n"+"Thank you for using the Pig Latin Translator")
    
#close the file
    f.close()
    
else:
#If initial file doesn't exist print an Error message
    print("Re-run program and Try Again.")



