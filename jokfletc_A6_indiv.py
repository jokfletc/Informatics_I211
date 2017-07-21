# John Fletcher
# Group 98


import xml.etree.ElementTree as ET

def id_check(id_input):
    root = ET.parse(source="library.xml")
    catalog = root.iter('book')
    id_list = []
    for book in catalog:
        
        bk_id = (book.attrib['id'])
        id_list.append(bk_id)
    if id_input in id_list:
        print("The information for the book with ID# "+user_input+":")
        print("\n")
        display_book(id_input)
    else:
        print("ERROR: The book id entered does not exist in the document.")
    

def parse_date(date):
    parts = date.split('-')
    if(len(parts) != 3):
        return ''
    try:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
    except ValueError:
        return ''
    return month


#Part A



def display_book(book_id):

    root = ET.parse(source="library.xml")
    catalog = root.iter('book')
    for book in catalog:
        
        bk_id = (book.attrib['id'])
        if book_id == bk_id:
            
            print("Title: "+book.find("title").text)
            print("Author: "+book.find("author").text)
            print("Price: "+book.find("price").text)
            print("\n")







#Part B
import datetime

def book_date(genre,month):
    
    root = ET.parse(source="library.xml")
    catalog = root.iter('book')
    for book in catalog:
        if (book.find('genre').text) == genre:
            date = parse_date(str((book.find('publish_date').text)))
            if str(date) == str(month):
                display_book(book.attrib['id'])



def genre_info(genre):
    
    root = ET.parse(source="library.xml")
    catalog = root.iter('book')
    for book in catalog:
        if (book.find('genre').text) == genre:
            display_book(book.attrib['id'])

#PART C
                
def genre_search():
    root = ET.parse(source="library.xml")
    catalog = root.iter('book')
   
    genres_list = [(book.find('genre').text) for book in catalog]
    genres = [item for item in genres_list if  genres_list.count(item) == 1]
    
    for item in genres:
        genre_info(item)
        





        
#Main
user_input = input("What book ID would you like to look up?: ")
print("\n")
id_check(user_input)
print("\n")
print("The title, author, and price of each Computer book released in December are: ")
print("\n")
book_date('Computer','12')
print("\n")
print("The information for the books with unique genres are: ")
print("\n")
genre_search()
