#! /usr/bin/env python3

print('Content-type: text/html\n')

import cgi

form = cgi.FieldStorage()

html ="""
<!doctype html>
<html>
<head><meta charset="utf-8"><title>Robot Delivery System Confirmation</title></head>
<body>
<h1>Robot Delivery System Confirmation</h1>
<p>You have selected to have a {item} delivered by 
{delivery} with {shipping}.</p>
<p>Your total delivery fee comes to: ${total}</p></body>
</html>"""

values = {"drone" : 10, "self driving car": 20, "giant robot": 1000, "Express Delivery": 30,
          "Mostly Not Broken" : 20, "With a Smile": 1}

count = values[form.getfirst('delivery_method')]

for addon in form.getlist('addons'):
    count += values[addon]

print(html.format(item = form.getfirst("delivery"), delivery = form.getfirst("delivery_method"), shipping = form.getfirst("addons"), total =str( count)))
