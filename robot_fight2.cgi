#! /usr/bin/env python3
									#John Fletcher
import cgi, random, MySQLdb         #Group:98
print ('Content-type: text/html\n')
form = cgi.FieldStorage()
string = "i211f16_jokfletc" 		#change username to yours!!!
password = "my+sql=i211f16_jokfletc" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

def get_weapon(cursor,winner):
	try:
		SQL ="""SELECT Weapon FROM Robot WHERE Name='%s'"""%(winner)
		cursor.execute(SQL)
		weapon=cursor.fetchall()[0][0]
	except:
		weapon="Something went wrong with the weapon SQL"
	return weapon

def get_hp(cursor,robot):
	try:
		SQL="""SELECT HitPoint FROM Robot WHERE Name='%s'"""%(robot)
		cursor.execute(SQL)
		hp=cursor.fetchall()[0][0]
	except:
		hp="Something went wrong with the hp SQL"
	return hp

def update_winner(cursor,winner):
	try:
		SQL="""UPDATE Robot SET Wins = Wins + 1 WHERE Name='%s'"""%(winner)
		cursor.execute(SQL)
		db_con.commit()
	except:
		print("Winner not updated!")

def robot_fight(cursor,robot1,robot2):
	hp1=get_hp(cursor,robot1)
	hp2=get_hp(cursor,robot2)
	weapon1=get_weapon(cursor,robot1)
	weapon2=get_weapon(cursor,robot2)
	while hp1 >0 and hp2>0:
		attack=random.choice([robot1,robot2])
		if attack == robot1:
			defend = robot2
			hp2 -= 1
			print(attack + " hits " + defend +"!"+"<br>")
			if hp2 ==0:
				print(robot1 + " wins the round with its " + weapon1 + " "+robot2+" is destroyed!")
				update_winner(cursor,robot1)
		else:
			defend = robot1
			hp1 -= 1
			print(attack + " hits " + defend +"!"+"<br>")
			if hp1 == 0:
				print(robot2 + " wins the round with its " + weapon2 + " "+robot1+" is destroyed!")
				update_winner(cursor,robot2)





html="""<html>
<head><title>Robot Fight!</title></head>"""
try:
    SQL = "SELECT Name FROM Robot;"
    cursor.execute(SQL)
    names = cursor.fetchall()
except Exception as e:
    print('<p>Something went wrong with the SQL!</p>')
    print(SQL, "Error:", e)
else:   #This runs if there was no error
    if not form.getfirst("robot1",None):
        html += """<body>
            <H1>Choose two robots to face off!</H1><hr />
            <FORM method="post" action="robot_fight2.cgi">
            <H3>Please select robots:</H3>
            <p> Robot Name:
            <select name="robot1">"""
        for name in names:
            html+="<option>"+name[0]+"</option>"
        html+="</select>"
        html+="""<select name="robot2">"""
        for name in names:
            html+="<option>"+name[0]+"</option>"
        html+="""</select></p> <input type="submit" value="Fight!" /> </FORM> <hr />"""
    else:
        robot1=form.getfirst("robot1", "")
        robot2=form.getfirst("robot2", "")
        html+=robot_fight(cursor, robot1, robot2)
html+="""</body></html>"""
print(html)
				
	
	