from collections import UserDict
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value )
 
class Name(Field):
   def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Phone(Field):
    def __init__(self, value = None):
        super().__init__(value)   

    def normalize_phone (self, value):                                    # виведення введеного номеру у форматі (+38)+"10 цифр"
        number_template=r"[\d\+]+"
        phone_number=''.join(re.findall(number_template, value))
        if len(phone_number) == 10:
            phone = '+38' + phone_number
            return phone
        elif len(phone_number) == 11 and phone_number.startswith('8'):
            phone = '+3' + phone_number
            return phone
        elif len(phone_number) == 12 and phone_number.startswith('38'):
            phone = '+' + phone_number 
            return phone      
        elif len(phone_number) == 13 and phone_number.startswith('+38'):
            phone = phone_number
            return phone
        else:
            raise ValueError('невірний формат номеру')
 
class Record:
    def __init__(self, name):
        self.name = Name(name)       
        self.phones = []
        self.phone = Phone()

    def add_phone(self, number):
        if number in self.phones:
            raise ValueError("this phone exists")
        else:
            self.phones.append(self.phone.normalize_phone(number))         # додаєм номер в список використовуючи метод валідації з класу Phone               
    
    def remove_phone(self, phone:Phone):
        phone = self.phone.normalize_phone(phone)                          # валідуєм вхідний номер
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            raise ValueError("phone not found")         
    
    def edit_phone(self, phone:str, change_phone:str):
        phone = self.phone.normalize_phone(phone)                         
        change_phone = self.phone.normalize_phone(change_phone)             
        if phone in self.phones:
            index_to_replace = self.phones.index(phone)                     # знаходимо індекс елемента списку
            self.phones[index_to_replace] = change_phone                    # змінюємо номер у списку за індексом          
        else:
            raise ValueError("phone not found")      
    
    def find_phone(self, phone: Phone):
        phone = self.phone.normalize_phone(phone)
        return (phone if phone in self.phones else f" {phone} not found") 

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, user_name:str):
        for name, phone in self.data.items():
            if name == user_name:
                return phone
            else:
                return "not found"
   
    def delete_record(self, name: str):
        if name in self.data:
            del self.data[name]
        else:
            return(f"Record with name {name} not found in the address book.")
               
if __name__ == '__main__':
    # Створення нової адресної книги
    book = AddressBook()
    
    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)
    

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete_record("Jane")
    for name, record in book.data.items():
        print(record)
        
    # номери телефонів у виведенні представлені згідно методу валідації з класу Phone
   

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # # Знаходження та редагування телефону для John
    # john = book.find("John")
    # john.edit_phone("1234567890", "1112223333")

    # print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # # Пошук конкретного телефону у записі John
    # found_phone = john.find_phone("5555555555")
    # print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # # Видалення запису Jane
    # book.delete("Jane")

     
    
     