def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if contacts == {}:
        contacts[name] = phone
        return "Contact added."
    else:
        for key in contacts.keys():
            if key == name:               
                return f"Введений контакт з ім'ям {name} вже існує." 
            else:
                contacts[name] = phone
                return "Contact added."           
    
def change_contact(args, contacts):
    name, phone = args
    for key in contacts.keys():
        if  key == name:
            contacts[name] = phone
            return f'Контакт {name} змінено.'
        else:
            return 'Вказаного користувача не існує'
    
def del_contact(args, contacts):
    try:
        name, = args
        contacts.pop(name)
        return f"Контакт {name} видалено"        
    except: 
        return f"Контакт {name} не знайдено"

def main():
    contacts = {} 
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "all":
            print(contacts)
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "del" and args:
            print(del_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()