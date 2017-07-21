import csv
import datetime

def format_date(raw_yearmonth, day):
    yearmonth = int(raw_yearmonth)
    year = str(yearmonth//100)
    month = str(yearmonth%100)
    return month+'/'+day+'/'+year

def parse_date(date):
    parts = date.split('/')
    if(len(parts) != 3):
        return ''
    try:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
    except ValueError:
        return ''
    return datetime.date(year,month,day)
    

def date_str(date):
    return str(date.month)+'/'+str(date.day)+'/'+str(date.year)

def format_event(event):
    if event[0] in 'aeiouAEIOU':
        return 'An ' + event
    else:
        return 'A ' + event


def storm_by_event(event):
    with open('Indiana_Storms.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row['EVENT_TYPE'].lower() == event.lower() or event == '*'):
                print(format_event(row['EVENT_TYPE']) + ' happened on '+
                      format_date(row['BEGIN_YEARMONTH'],row['BEGIN_DAY'])+
                      ' in ' + row['CZ_NAME'] + ' county.')


def storm_by_date(date):
    with open('Indiana_Storms.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(date_str(date) == format_date(row['BEGIN_YEARMONTH'],row['BEGIN_DAY'])):
                print(format_event(row['EVENT_TYPE']) + ' happened on '+
                      format_date(row['BEGIN_YEARMONTH'],row['BEGIN_DAY'])+
                      ' in ' + row['CZ_NAME'] + ' county.')

#main
search_type = ''
while(search_type == ''):
    search_type = input("Would you like to search by date or event? ").lower()
    if(search_type != 'date' and search_type.lower() != 'event'):
        print('That is not a valid selection. Please try again.')
        search_type = ''
if(search_type == 'event'):
    search_event = input("Please enter the type of weather you are searching for: ")
    storm_by_event(search_event)
if(search_type == 'date'):
    date = ''
    while(date == ''):
        search_date = input("please enter your date in YYYY/MM/DD format: ")
        date = parse_date(search_date)
        if(date == ''):
            print("invalid date")
    storm_by_date(date)
