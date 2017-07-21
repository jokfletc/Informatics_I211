#! /usr/bin/env python3

print ('Content-type: text/html\n')
import cgi
import MySQLdb
form = cgi.FieldStorage()

html ="""
<html>
<head><title>Robot Fight!</title></head><body>
            <H1>Choose two robots to face off!</H1><hr />
            <FORM method="post" action="robot_fight.cgi">
            <H3>Please select robots:</H3>
            <p> Robot Name:
            <select name="robot1"><option>BB-8</option><option>Megatron</option><option>Commander Data</option><option>Terminator</option><option>Roomba</option></select><select name="robot2"><option>BB-8</option><option>Megatron</option><option>Commander Data</option><option>Terminator</option><option>Roomba</option></select></p> <input type="submit" value="Fight!" /> </FORM> <hr /></body></html>
"""



print(html)