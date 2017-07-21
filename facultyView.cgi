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
form_name = form.getvalue("name","")
form_title = form.getvalue("title","")
form_email = form.getvalue("email","")
form_areas = form.getvalue("areas","")

try:				#Always surround .execute with a try!
		
        SQL = "SELECT * FROM Faculty"
        sql2 = "INSERT INTO Faculty(Name,Title,Email,Areas) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql2, (form_name,form_title, form_email, form_areas))
        db_con.commit()
        cursor.execute(SQL)
        results = cursor.fetchall()
except:		#Here we handle the error
        print('<p>Something went wrong with the SQL!</p>')
        print(SQL)
else:				#This runs if there was no error
		print('<p><a href="insertfaculty.html">Go Back</a></p>')
		print ("<table border = '1'><tr><th>FacultyID</th><th>Name</th><th>Title</th><th>Email</th><th>Areas</th></tr>")
		print('<tbody>')
		for row in results:
			fid = row[0]
			name = row[1]
			title = row[2]
			email = row[3]
			area = row[4]
			print ('<tr><td>' + str(row[0]) + '</td><td>' + name + '</td><td>' + title + '</td><td>' + email + '</td><td>' + area + "</td><td><a href='deletefaculty.cgi?fid="+ str(row[0])+"'>Delete</a></td</tr>")
		print('</tbody>')
		print('</table>')
		