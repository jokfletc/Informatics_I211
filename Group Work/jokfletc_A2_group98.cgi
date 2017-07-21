#! /usr/bin/env python3
print('Content-type: text/html\n')

import cgi
import re
import urllib.request

form = cgi.FieldStorage()
html ="""
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Stock Compare</title></head>
    <body>
    <table border = 1>{contents}</table>
    </body>
</html>"""

def stockinfo(symbol, option):
    url = "https://finance.yahoo.com/quote/"+symbol+"?p="+symbol
    try:
        web_page = urllib.request.urlopen(url)
        lines = web_page.read().decode(errors="replace")
        web_page.close()
    except:
        return "Invalid Stock Symbol"
    else:
        if option == "opn":
            result = re.findall('(?=<td).+?(?=</td>)', lines, re.DOTALL)
            for item in result:
                 if "$OPEN.1" in item:
                     placement=(item.index(">"))
                     value = item[placement+1:]
                     return value
        elif option == "close":
            result = re.findall('(?=<td).+?(?=</td>)', lines, re.DOTALL)
            for item in result:
                 if "$PREV_CLOSE.1" in item:
                     placement=(item.index(">"))
                     value = item[placement+1:]
                     return value
        else:
            result = re.findall('(?=<td).+?(?=</td>)', lines, re.DOTALL)
            for item in result:
                 if "$PE_RATIO.1" in item:
                     placement=(item.index(">"))
                     value = item[placement+1:]
                     return value
            
option = form.getfirst("comp", "opn")
stocksymbols = form.getfirst("symbols", "GOOG")
stocksymbols = stocksymbols.split("\r\n")
table = ""
for symbol in stocksymbols:
    value = stockinfo(symbol, option)
    table += "<tr>"
    table += "<td>"+symbol+"</td>"
    table += "<td>"+value+"</td>"
    table += "</tr>"
    
    
print(html.format(contents = table))

