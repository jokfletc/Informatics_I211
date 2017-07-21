
##import urllib.request, ssl,re,webbrowser,random
##
##context = ssl._create_unverified_context()
##
##web_page = urllib.request.urlopen ("https://en.wikipedia.org/wiki/Abbeville_and_Waycross_Railroad", context=context)
##
##lines = web_page.read().decode(errors="replace")
##
##web_page.close()
##hits = re.findall('(?<=href=").+?(?=")', lines,re.DOTALL)
##print(hits)
##body = re.findall('(?<=<body).+(?=</body>)', lines, re.DOTALL)[0]
##hits = re.findall('(?<=href=").+?(?=")', body)
##wiki_links = [link for link in hits if "wiki" in link and ".org" not in link]
##print(wiki_links)
##for i in range(int(3)):
##
##    choice = random.choice(wiki_links)
##    print(choice)
##    webbrowser.open_new_tab("http://en.wikipedia.org"+choice)



import os

os.chdir('C:\\Users\\Fletcher\\Desktop')
os.makedirs('C:\\Users\\Fletcher\\Desktop\\Pictures')



def image_list(url):
    
    context = ssl._create_unverified_context()

    web_page = urllib.request.urlopen ("https://en.wikipedia.org/wiki/Abbeville_and_Waycross_Railroad", context=context)

    lines = web_page.read().decode(errors="replace")

    web_page.close()

    images = re.findall('(?<=img").+?(?=")', lines,re.DOTALL)

    print(images)
