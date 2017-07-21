import csv
import datetime
def date_format(yearmonth,day):
    year_month = int(yearmonth)
    year = str(year_month//100)
    month = str(year_month%100)
    return month+'/'+day+'/'+year

def date_parse(date):
    parts = user_date.split('/')
    try:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
    except ValueError:
        return ''
    return datetime.date(year,month,day)


def date_str(date):
    return str(date.month)+'/'+str(date.day)+'/'+str(date.year)


def storm_by_event(event):
    data = csv.reader(open("Indiana_Storms.csv","r"))
    for entry in data:
        if entry[12] == event:
            
                print("A "+event+" happened on "+date_format(entry[0],entry[1])+" in "+entry[15]+" county.")
            

#Main



def storm_by_date(date):
    
    with open('Indiana_Storms.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for entry in reader:
            if(date_str(date) == date_format(entry['BEGIN_YEARMONTH'],entry['BEGIN_DAY'])):
                print("a "+entry['EVENT_TYPE'] + ' happened on '+
                      date_format(entry['BEGIN_YEARMONTH'],entry['BEGIN_DAY'])+
                      ' in ' + entry['CZ_NAME'] + ' county.')        
        



#Main
event_date = ''

while event_date == '':
    event_date = input("Would you like to search by date or by event?")
    if event_date not in "date,event":
        print('That is not a valid selection. Please try again.')
        event_date = ''

    
if event_date == "date":
    user_date = ''
    while user_date =='':
        user_date= input("Enter a date in YYYY/MM/DD format: ")
        if user_date == '':
            print("Invalid date")
    storm_by_date(date_parse(user_date))
if event_date == "event":
    user_event = input("Enter an event to search: ")
    if user_event != '':
        
        storm_by_event(user_event)
    
    
    


