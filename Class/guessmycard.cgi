#! /usr/bin/env python3
print('Content-type: text/html\n')

import cgi

form = cgi.FieldStorage()

html ="""
<!doctype html>
<html>
<head><meta charset="utf-8"><title>Guess My Card</title></head>
<body>
<h1>You guessed:</h1><br>
<p><img src="cards/{card}.jpg" height="200"></p>
<h1>Suit:</h1><br>
<p>{suit}</p>
<h1>Rank:</h1><br>
<p>{rank}</p>
</body>
</html>"""

if form.getfirst("suit") == "S":
	suit = "Correct suit!"
else:
	suit = "Wrong suit!"
	
if form.getfirst("rank") in ["K","Q","A"]:
	rank = "Too high!"
elif form.getfirst("rank") == "J":
	rank = "That is correct!"
else:
	rank = "Too low!"
	
if str(form.getfirst("rank")+form.getfirst("suit")) != "JS":
	html="""
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Guess My Card</title></head>
<body>
<h1>You guessed:</h1>
    <p><img src="cards/{card}.jpg" height="200"></p>
    <h1>Suit:</h1>
    <p>{suit}</p>
    <h1> Rank </h1>
    <p>{rank}</p>
    <form method="post" action="guessmycard.cgi">
    <H2>Try to guess the card!</H2>
	<p>Rank:
		<select name="rank">
			<option>2</option>
			<option>3</option>
			<option>4</option>
			<option>5</option>
			<option>6</option>
			<option>7</option>
			<option>8</option>
			<option>9</option>
			<option>10</option>
			<option>J</option>
			<option>Q</option>
			<option>K</option>
			<option>A</option>
		</select>
	</p>
	<p>Suit:
		<br /><input type="radio" name="suit" value="C" checked />Clubs
		<br /><input type="radio" name="suit" value="D" />Diamonds
		<br /><input type="radio" name="suit" value="H" />Hearts
		<br /><input type="radio" name="suit" value="S" />Spades
	</p>
	<button type="submit">Submit</button>
</form>
</body>
</html>"""

card = str(form.getfirst("rank")+form.getfirst("suit"))

print(html.format(card=card,rank=rank,suit=suit))