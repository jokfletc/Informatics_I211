import xml.etree.ElementTree as ET



##def id_find(num):
##    root = ET.parse(source="students.xml")
##    try:
##        students = root.iter("Student")
##        for student in students:
##            if num == student.find("id").text:
##                value = student.find("name/first").text+" "+student.find("name/last").text
##                return value
##    except ValueError:
##     
##    else:
##        print("Not Found")
##    
##
##
###Main
##result = ("0119846789")
##print(id_find(result))



##def fee_find(name):
##    root = ET.parse(source="students.xml")
##    students = root.iter("Student")
##    for student in students:
##        if name == (student.find("name/first").text+" "+student.find("name/last").text):
##            fee = student.find("fees")
##            units =(fee.attrib['units'])
##            country =(fee.attrib['c'])
##           
##            return(name +" owes "+ fee.text+" "+ country+" "+ units+ " in fees.")
##        
##    return("Not Found")
##
##
###Main
##print(fee_find("Jason Bourne"))
##print(fee_find("Jack Sparrow"))
##print(fee_find("No Body"))





