#! /usr/bin/env python3
print('Content-type: text/html\n')

import cgi
import MySQLdb
string = "i211f16_jokfletc" 			#change username to yours!!!
password = "my+sql=i211f16_jokfletc" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)

cursor = db_con.cursor()

form = cgi.FieldStorage()
fid = form.getfirst('fid',"")


try:		
	SQL = """DELETE FROM Faculty WHERE FacultyID = '%s'""" % ("+"+str(fid)+"+")
	
	cursor.execute(SQL)

	db_con.commit()
	db_con.close()

except :		#Here we handle the error
        print('<p>Something went wrong with the SQL!</p>')
        print(SQL)
else:
	print("Entry deleted from Table")