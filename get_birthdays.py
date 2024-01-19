from datetime import date, timedelta

user_list = [
    {"name": "Bill", "birthday": date(1970, 1, 12)},
    {"name": "Jill", "birthday": date(1982, 1, 14)},
    {"name": "Stan", "birthday": date(1963, 1, 1)},
    {"name": "Jan", "birthday": date(1992, 1, 16)},
    {"name": "Joe", "birthday": date(2000, 10, 31)},
    {"name": "Zoe", "birthday": date(2009, 1, 17)},
    {"name": "Kim", "birthday": date(1975, 1, 4)},
    {"name": "Jim", "birthday": date(1985, 1, 20)},
    {"name": "Ann", "birthday": date(1991, 2, 28)},
    {"name": "Liu", "birthday": date(1997, 5, 22)},
    {"name": "Meg", "birthday": date(2003, 1, 15)},
    {"name": "Zeb", "birthday": date(1969, 6, 2)},
    {"name": "Mario", "birthday": date(1944, 3, 2)},
    {"name": "Dario", "birthday": date(1956, 1, 9)},
    {"name": "Zigi", "birthday": date(2001, 1, 13)},
    {"name": "Zibi", "birthday": date(2003, 1, 19)},
    {"name": "Zenon", "birthday": date(1955, 1, 21)},
    {"name": "Leon", "birthday": date(1966, 1, 15)},
    {"name": "Maria", "birthday": date(1977, 12, 8)},
    {"name": "Grazia", "birthday": date(1947, 4, 12)},
    {"name": "Tom", "birthday": date(2013, 1, 18)},
    {"name": "Bob", "birthday": date(1960, 9, 22)},
]

def get_birthdays_per_week(user_list):
    monday = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []

    current_date = date.today()
    print(f'{current_date} - This is current date (today)')

    start_date = current_date - timedelta(weeks=1)
    print(f'{start_date} - Starting from this date we will remind about comming employee birthdays')
    print("*" * 24)

    for entry in user_list:
        birthday = entry.get("birthday")
        person = entry.get("name")
        # mapping of the birthday to the current year for proper calculating of the time period (7 days)
        mapped_birthday = date(current_date.year, birthday.month, birthday.day)
        
        period = (mapped_birthday - start_date).total_seconds() 
        
        if 0 <= period <= 604800: # 604800 s == 7 days
            
            if birthday.strftime("%A") == "Tuesday":
                tuesday.append(person)
            elif birthday.strftime("%A") == "Wednesday":
                wednesday.append(person)
            elif birthday.strftime("%A") == "Thursday":
                thursday.append(person)
            elif birthday.strftime("%A") == "Friday":
                friday.append(person)
            else:
                monday.append(person)
           
    if len(monday) > 0:
        joined_names = ", ".join(monday)
        x = f"Monday: " + joined_names
        print(x)

    if len(tuesday) > 0:
        joined_names = ", ".join(tuesday)
        x = f"Tuesday: " + joined_names
        print(x)

    if len(wednesday) > 0:
        joined_names = ", ".join(wednesday)
        x = f"Wednesday: " + joined_names
        print(x)

    if len(thursday) > 0:
        joined_names = ", ".join(thursday)
        x = f"Thursday: " + joined_names
        print(x)

    if len(friday) > 0:
        joined_names = ", ".join(friday)
        x = f"Friday: " + joined_names
        print(x)

    # if len(saturday) > 0:
    #     joined_names = ", ".join(saturday)
    #     x = f"Saturday: " + joined_names
    #     print(x)

    # if len(sunday) > 0:
    #     joined_names = ", ".join(sunday)
    #     x = f"Sunday: " + joined_names
    #     print(x)

    print("*" * 24)
    
       
        
if __name__ == '__main__':
    get_birthdays_per_week(user_list)