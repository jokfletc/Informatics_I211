#! /usr/bin/env python3

print 'Content-type: text/html\n'

import MySQLdb
import cgi



string = "i211f16_jokfletc" 			#change username to yours!!!
password = "my+sql=i211f16_jokfletc" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)

cursor = db_con.cursor()

form = cgi.FieldStorage()

form_name = form.getvalue("name","")
form_address1 = form.getvalue("address1","")
form_address2 = form.getvalue("address2","")
form_city = form.getvalue("city","")
form_state = form.getvalue("state","")
form_zip = form.getvalue("zip","")
		
try:		
	SQL = "INSERT INTO Addresses (Name,Address1,Address2,City,State,Zip) VALUES (%s,%s,%s,%s,%s,%s)"
	cursor.execute(SQL, (form_name,form_address1,form_address2,form_city,form_state,form_zip))

	db_con.commit()
	db_con.close()

except Exception, e:		#Here we handle the error
        print('<p>Something went wrong with the SQL!</p>')
        print(SQL, "Error:", e)
else:
	print('<p>Address added to Addresses Table within your database.</p>')
