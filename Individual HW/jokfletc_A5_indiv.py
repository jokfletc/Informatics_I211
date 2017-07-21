#John Fletcher
#Group 98


#Part 1 (30 points)
import csv
import urllib.request,os
def getQuakeData(url,orderby,limit):
    part2_url = ("http://earthquake.usgs.gov/fdsnws/event/1/query.csv?starttime=2016-09-23%2000:00:00&endtime=2016-09-30%2023:59:59&minmagnitude=4.5&eventtype=earthquake&orderby="+orderby+"&"+"limit"+"="+limit)
    

    web_page = urllib.request.urlopen(part2_url)
    lines = web_page.read().decode(errors="replace")
    web_page.close()
    quake_list = lines.split('\n')
    for line in quake_list:
        isinstance(line,str)
    print(quake_list)
    getTopQuakes(quake_list)
    

                  

#Part 3 (25 points)
import csv
def getTopQuakes(data):
    
    
    print("ID"+(" "*11)+"Mag"+(" "*4)+"Location"+(" "*38)+"Time")
    print("-"*90)
    reader = csv.DictReader(data)
    
    
    
    for entry in reader:
        
        
        mag_id = entry['id']
        mag = entry['mag']
        location = entry['place']
        if len(mag) == 1:
            mag = (entry['mag']+".0")
        time = entry['time']
        output = "{0}"+(" "*3)+"{1}"+(" "*4)+"{2}"+" "*(90-(len(mag_id)+len(mag)+len(location)+len(time)+3+4))+"{3}"
        print(output.format(mag_id,mag,location,time))

#main


user_url = ("http://earthquake.usgs.gov/fdsnws/event/1/query.csv?starttime=2016-09-23%2000:00:00&endtime=2016-09-30%2023:59:59&minmagnitude=4.5&eventtype=earthquake&orderby=time")
user_orderby = input("Please enter whether you would like your data to be ordered by 'time' or 'magnitude': ")
user_limit = input("Please enter the amount of earthquake records you would like returned to your system: ")

result = getQuakeData(user_url,user_orderby,user_limit)
