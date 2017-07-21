#! /usr/bin/env python3
print('Content-type: text/html\n')

import cgi
form = cgi.FieldStorage()


html = """
<!doctype html>
<html>
<head><meta charset="utf-8"><title>Stock Compare</title></head>
<body>
<table border=1>
{content}
</table>

</body>
</html>"""

info = getfirst('comp')

import urllib.request, ssl,re,webbrowser

symbols = form.getfirst('symbols')
symbols = symbols.split('\r\n')
for item in symbols:
	item = item.strip()
tables=""
for item in symbols:

	info = form.getfirst('comp')

	context = ssl._create_unverified_context()
	url =("https://finance.yahoo.com/quote/"+item+"?p="+item)
	web_page = urllib.request.urlopen(url , context=context)

	lines = web_page.read().decode(errors="replace")

	web_page.close()
	if info == 'close':
		result = re.findall('(?=<td class="Ta(end) Fw(b)" data-test="PREV_CLOSE-value" data-reactid=".1ll933j0pwg.0.$0.0.1.3.1.$main-0-Quote-Proxy.$main-0-Quote.2.0.0.0.1.0.0.0.$PREV_CLOSE.1">).+?(?=</td>)',lines,re.DOTALL)
	if info == 'opn':
		result = re.findall('(?=<td class="Ta(end) Fw(b)" data-test="OPEN-value" data-reactid=".1ll933j0pwg.0.$0.0.1.3.1.$main-0-Quote-Proxy.$main-0-Quote.2.0.0.0.1.0.0.0.$OPEN.1">).+?(?=</td>)',lines,re.DOTALL)
	if info == 'peRatio':
		result = re.findall('(?=<td class="Ta(end) Fw(b)" data-test="PE_RATIO-value" data-reactid=".1ll933j0pwg.0.$0.0.1.3.1.$main-0-Quote-Proxy.$main-0-Quote.2.0.0.0.1.0.0.0.$PE_RATIO.1">).+?(?=</td>)',lines,re.DOTALL)
	table += "<tr>"
	table += "<td>"+item+"</td>"
	table +="<td>"+result+"</td>"
	table += "</tr>"



print(html.format(content=table))

