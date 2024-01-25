from datetime import datetime
from datetime import timedelta

list = [
    {"name": "John Doe", "birthday": "2000.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.25"},
    {"name": "Josdf Doe", "birthday": "1985.01.28"},
    {"name": "Jsdfn Doe", "birthday": "1985.01.27"},
    {"name": "sdfn Doe", "birthday": "1985.02.01"},
    {"name": "Jsdfn Doe", "birthday": "1985.02.10"}
  
]



def get_upcoming_birthdays(users=None):
    today = datetime.today().date()
    birthdays_list = []
    for user in users:
        birthday = user['birthday']
        birthday_parsing =datetime.strptime(birthday, "%Y.%m.%d").date() 
        birthday_now_year=str(today.year)+birthday[4:]
        birthday_now_year_parsing = datetime.strptime(birthday_now_year, "%Y.%m.%d").date()
        if birthday_now_year_parsing.toordinal() - today.toordinal() > 7 or birthday_now_year_parsing.toordinal() - today.toordinal() <= 0:
            pass
        else:
            if birthday_now_year_parsing.weekday() == 6:
                sunday_day = birthday_parsing  + timedelta(days=1)  
                birthdays_list.append({'name':user['name'], "birthday":datetime.strftime(sunday_day, "%Y.%m.%d")})                
            elif birthday_now_year_parsing.weekday() == 5:
                saturday_day = birthday_parsing  + timedelta(days=2)  
                birthdays_list.append({'name':user['name'], "birthday":datetime.strftime(saturday_day, "%Y.%m.%d")})  
            else: 
                birthdays_list.append({'name':user['name'], 'birthday':birthday})    
    return birthdays_list


print(get_upcoming_birthdays(list))