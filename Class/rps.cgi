#! /usr/bin/env python3
print('Content-type: text/html\n')

import cgi, random
form = cgi.FieldStorage()


html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Rock Paper Scissors</title></head>
    <body>
        <p>You chose: <img src="{source1}" height="300"></p>
        <p>Computer chose: <img src="{source2}" height="300"></p>
	<h2>{result}</h2>
    </body>
</html>"""


options = ["Paper", "Rock", "Scissors"]

images = {"Paper": "http://images.clipartpanda.com/writing-on-paper-clipart-black-and-white-1206556249326967385nexxuz_Loose_Leaf_Paper.svg", "Rock": "http://icons.iconarchive.com/icons/raindropmemory/down-to-earth/256/G12-Rock-icon.png", "Scissors": "http://icons.iconarchive.com/icons/custom-icon-design/pretty-office-10/512/Scissors-icon.png"}

choice = random.choice(options)

user_choice = form.getfirst('weapon', 'Rock')

if user_choice == choice:
	status = "Tie"
elif (user_choice == "Rock" and choice == "Scissors") or (user_choice == "Paper" and choice == "Rock") or \
     (user_choice == "Scissors" and choice == "Paper"):
	status = "You Win!"
else:
	status = "You Lose!"

print(html.format(source1 = images[user_choice], source2 = images[choice], result = status))