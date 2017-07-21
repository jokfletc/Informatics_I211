from datetime import datetime
import datetime
import random

def date_run():
    while True:
        try:
            year = random.choice(range(1900,2000))
            month = random.choice(range(1,12))
            day = random.choice(range(1,29))
            date = datetime.date(year,month,day)
            print(date.strftime("%d %b %Y is a %A on the %d day of %B"))
            if date.strftime("%A") == "Thursday":
                if date.strftime("%B") == "February":
                    if year%7 == 0:
                        break
            
        except:
            print("Go")
            
               

                    
            

date_run()
