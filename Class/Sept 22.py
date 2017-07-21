import csv

def state_company(user_input):
    data = csv.DictReader(open("companies.csv","r"))
    company_list = []

    for company in data:
        if company["state"] == user_input:
            company_list.append((company["company_name"],company["web"]))
    print("-"*70)
    for company in sorted(company_list):
        name,web = company
        pad = 30 - len(name)
        
        print(name," "*pad,web)


state = input("Search for companies in which state?: ")
result = state_company(state)
