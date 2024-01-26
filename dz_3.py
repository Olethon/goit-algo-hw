from datetime import datetime 
from datetime import timedelta
import random
import re

#  Task_1

# some_date = '2020-10-09'

def get_days_from_today(date_object: str):
        try:
            date_parsing = datetime.strptime(date_object, "%Y-%m-%d")
            now_date = datetime.now() 
            days_since = now_date.toordinal() - date_parsing.toordinal()
            return (f'кількість днів між заданою  та поточною датами: {days_since} дні')
        except Exception:
            return('Ви ввели помилкові дані')
        
# print(get_days_from_today(some_date))


#  Task_2

def get_numbers_ticket(min: int, max: int, quantity: int):
    if min >= max or quantity > (max - min + 1):
        return([]) 
    else:
        unique_numbers = random.sample(range(min, max + 1), quantity)
        return(sorted(unique_numbers))

# print(get_numbers_ticket(1, 49, 6))



#  Task_3

# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

def normalize_phone(phone_number):
    p1=r"[\d\+]+"
    phone_number=''.join(re.findall(p1,phone_number))
    if phone_number.startswith('+38'):
        return phone_number
    elif phone_number.startswith('38') and len(phone_number) == 12:
        return '+' + phone_number
    elif phone_number.startswith('8') and len(phone_number) == 11:
        return '+3' + phone_number
    else:
        return '+38' + phone_number

# for phone in raw_numbers:
#     print(normalize_phone(phone))   



#  Task_4

# list_user = [
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.01.28"},
#     {"name": "Josdf Doe", "birthday": "1989.01.26"},
#     {"name": "Jsdfn Doe", "birthday": "1992.01.27"},
#     {"name": "sdfn Doe", "birthday": "2000.02.01"},
#     {"name": "Jsdfn Doe", "birthday": "1976.02.10"}
  
# ]

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
                sunday_day = birthday_parsing + timedelta(days=1)  
                birthdays_list.append({'name':user['name'], "birthday":datetime.strftime(sunday_day, "%Y.%m.%d")})                
            elif birthday_now_year_parsing.weekday() == 5:
                saturday_day = birthday_parsing + timedelta(days=2)  
                birthdays_list.append({'name':user['name'], "birthday":datetime.strftime(saturday_day, "%Y.%m.%d")})  
            else: 
                birthdays_list.append({'name':user['name'], 'birthday':birthday})    
    print (birthdays_list)

# get_upcoming_birthdays(list_user) 

        

