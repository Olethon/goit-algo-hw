from AddressBook import *

def parse_input(user_input: str): # Парсинг введених даних
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):    # Декоратор для функцій
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "The data is not entered correctly" 
        except IndexError: 
            return "The data is not entered correctlyadd"
        except SyntaxError: 
            return "This number exists"               
    return inner

@input_error
def show_phone(args, contacts:AddressBook):
    name = args[0]
    return contacts[name] if name in contacts.keys() else "Not found"

@input_error                                           
def add_contact(args, contacts:AddressBook): # Функія додавання контактів
    name, phone = args
    name_found = contacts.find_records(name)      
    if name_found:
        name_found.add_phone(phone)
        return f'Контакт {name} оновлено'
    else:
        new_record = Record(name)
        new_record.add_phone(phone)
        contacts.add_record(new_record)
        return f'Контакт {name} додано'       
             
@input_error   
def change_contact(args: str, contacts:AddressBook): # Функія заміни контактів
    name, phone, new_phone  = args     
    rec_find = contacts.find_records(name)
    if rec_find:
        return rec_find.edit_phone(phone, new_phone)         
    else:
       return f'Контакт {name} не знайдено.'

@input_error    
def del_contact(args: str, contacts:AddressBook): # Функія видалення контактів
        name, = args
        return contacts.delete_record(name)
               
@input_error
def add_birthday(args:str, contacts:AddressBook):
    name, birthday = args    
    rec_find = contacts.find_records(name)
    if rec_find:
        rec_find.add_birthday(birthday)
        contacts.add_record(rec_find)
        return f'birthday {name} додано'
 
@input_error
def show_birthday(args:str, contacts:AddressBook):
    name = args[0]
    rec_find = contacts.find_records(name)
    if rec_find:
        return rec_find.birthday
    else: 
        return "Not found"

@input_error
def birthdays (contacts: AddressBook):
    now_birthdays = contacts.calculate_birthdays()
    return now_birthdays    

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
           print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(book)
        
        elif command == "delete":
            print(del_contact(args, book))

        elif command == "add_birthday":
             print(add_birthday(args, book))

        elif command == "show_birthday":
             print(show_birthday(args, book))

        elif command == "birthdays":
             print(birthdays(book))

        else:
            print("Invalid command.")
if __name__ == "__main__":
    main()
    

# add [ім'я] [телефон]:                                 Додати новий контакт з іменем та телефонним номером.
# change [ім'я] [існуючий телефон] [новий телефон]:     Змінити телефонний номер для вказаного контакту.
# phone [ім'я]:                                         Показати телефонний номер для вказаного контакту.
# all:                                                  Показати всі контакти в адресній книзі
# add_birthday [ім'я] [дата народження]:                Додати дату народження для вказаного контакту.
# show_birthday [ім'я]:                                 Показати дату народження для вказаного контакту.
# birthdays:                                            Показати дні народження, які відбудуться протягом наступного тижня.
# hello:                                                Отримати вітання від бота
# close або exit:                                       Закрити програму.
    
     # номери телефонів у виведенні представлені згідно методу валідації з класу Phone із AddressBook