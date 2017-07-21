web_page = urllib.request.urlopen(url)
lines = web_page.read().decode(errors="replace")
web_page.close()
re.findall('[\w]
