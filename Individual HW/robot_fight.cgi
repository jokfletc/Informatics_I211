#! /usr/bin/env python3

print ('Content-type: text/html\n')
import cgi
import MySQLdb
import random
form = cgi.FieldStorage()
robot1 = form.getfirst("robot1")
robot2 = form.getfirst("robot2")
damage_list = {'sword':'20','sarcasm':'5','laser gun':'20','machine gun':'25','vaccum':'10'}
string = "i211f16_jokfletc" 		#change username to yours!!!
password = "my+sql=i211f16_jokfletc" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

def get_info(cursor,robot1,robot2):
	try:
		SQL = """SELECT RobotID,Name, Weapon, HitPoint, Wins FROM Robot WHERE Name = '%s'""" % (robot1)
		SQL2 = """SELECT RobotID,Name, Weapon, HitPoint, Wins FROM Robot WHERE Name = '%s'""" % (robot2)
		cursor.execute(SQL)
		bot1 = cursor.fetchall()
		cursor.execute(SQL2)
		bot2 = cursor.fetchall()
		for bot in bot1:
			name1 = bot[1]
			weapon1 = bot[2]
			hp1 = int(bot[3])
		for bott in bot2:
			name2 = bott[1]
			weapon2 = bott[2]
			hp2 = int(bott[3])
	except:
		print('<p>Something went wrong with the SQL!</p>')
		print(SQL)
	print(name1,weapon1,hp1,name2,weapon2,hp2)
	return name1,weapon1,hp1,name2,weapon2,hp2
try:				#Always surround .execute with a try!
	results = get_info()
	print(results)
except:		#Here we handle the error
		print('<p>Something went wrong with the SQL!</p>')
else:
		robots = [name1, name2]
		while hp1 != 0 or hp2 != 0:
			attack = random.choice(robots)
			if attack == name1:
				defend = name2
				hp2 -= int(damage_list[weapon1])
				print(attack + " hits " + defend +"!" + "\n")
			else:
				defend = name1
				hp1 -= int(damage_list[weapon2])
				print(attack + " hits " + defend +"!" + "\n")
		else:
			if hp2 == 0:
				print(name1 + " wins the round with its " + weapon1 + " "+name2+" is destroyed!"+"\n")
				SQL3 = "Update Robot set Wins = Wins + 1 Where Name = '" + name1 + "';"
				cursor.execute(SQL3)
				db_con.commit()
			elif hp1 == 0:
				print(name2 + " wins the round with its " + weapon2 + " "+name1+" is destroyed!"+"\n")
				SQL3 = "Update Robot set Wins = Wins + 1 Where Name = '" + name2 + "';"
				cursor.execute(SQL3)
				db_con.commit()
            
           