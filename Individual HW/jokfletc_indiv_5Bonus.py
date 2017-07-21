#Name: John Fletcher
#Group: 98

#Phase 1

import urllib.request, re

web_page = urllib.request.urlopen("http://www.cbssports.com/nfl/scoreboard/all/2016/regular/5/")
lines = web_page.read().decode(errors="replace")
web_page.close()
body = re.findall('(?<=<body).+(?=</body>)', lines, re.DOTALL)[0]
contents = re.findall('(?<=<h1>).+?(?=</h1>)',body)

print("The heading tag on this page is:"+''.join(contents))
print("\n")

#Phase 2

links = []
image_links = re.findall('http://sports.cbsimg.net/images/nfl/logos/90x90/scoreboard/[A-Z]*.png', body)

print("A list of links to all the logo images on the page: ",'\n'.join(image_links))

#Phase 3

tables = re.findall('(?<=<table>).+?(?=</tr><tr><td class="team">)',lines,re.DOTALL)
print("\n")
games = [''.join(re.findall('(?<=<table>).+?(?=</tr><tr><td class="team">)',lines,re.DOTALL)).count("total-score")]
print("There were "+str(games).strip("[]")+" games this week,")

#Phase 4

print("\n")


scores = re.findall('(?<=<td class="total-score">).+?(?=</td>)',lines,re.DOTALL)

score_dif = []
for i in range(len(scores)+1):
    try:
        
        team1 = scores[0]
        team2 = scores[1]
    
        high = max(team1,team2)
        low = min(team1,team2)
        dif = int(high) - int(low)
        score_dif.append(dif)
        
        
        scores.remove(team1)
        scores.remove(team2)
    except:
        ValueError
       
   



print("\n")
print("The greatest points difference this week was ",max(score_dif)," points.")
    

