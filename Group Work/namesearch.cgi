#! /usr/bin/env python3

print ('Content-type: text/html\n')
import cgi
import MySQLdb
form = cgi.FieldStorage()
form_name = form.getfirst("name")
string = "i211f16_jokfletc" 		#change username to yours!!!
password = "my+sql=i211f16_jokfletc" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

try:				#Always surround .execute with a try!
        SQL = """SELECT * FROM Addresses WHERE Name = %s ;"
        cursor.execute(SQL,(form_name))
        results = cursor.fetchall()
except:		#Here we handle the error
        print('<p>Something went wrong with the SQL!</p>')
        print(SQL, "Error:", e)
else:				#This runs if there was no error
        result = ""
        for row in results:
                result += row+'<br>'
        print(result)