import csv

    

out = open("template2.html", "w")

html = """<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<title>Google Link</title>
</head>
<body>
	<p>Paragraph 1</p>
	<p>Paragraph 2</p>
	<a href="http://www.google.com">This takes you to Google!</a>
</body>
</html>"""

out.write(html)
out.close()

print("Finished writing.")

