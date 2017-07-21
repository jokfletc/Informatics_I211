#! /usr/bin/env python
print('Content-type: text/html\n')

import cgi

html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Dropdown in CGI</title></head>
    <body>
	<p>{content}</p>
    </body>
</html>"""

form = cgi.FieldStorage()
