#getContent (Group Work)

import urllib.request

web_page = urllib.request.urlopen("http://www.cnn.com/")
contents = web_page.read().decode(errors="replace")
web_page.close()

file_out = open("page.html", "w", encoding="utf-8")
file_out.write(contents)
file_out.close()

print("All done! Open page.html in your browser! ")

import os
def getContent(website):

    web_page = urllib.request.urlopen(website)
    
    contents = web_page.read().decode(errors="replace")

    file_name = os.path.basename(website)
    while True:
        try:
            file_out = open(file_name, "w", encoding="utf-8")
            file_out.write(contents)
            file_out.close()
        except:
           file_name = "index.html"



