# ДЗ №4
from my_pack import *
from pathlib import Path
# Функції модуля

# ----------------------------------------------------
# Головна програма
def main():
    data_dir = Path('data')
    data_file = Path('contacts.txt')
    data_path = data_dir / data_file
    contacts = get_data_from_file(data_path)
    
    changes = False
    
    menu_file = 'cli_menu.txt'
    menu_path = data_dir / menu_file
    menu = get_menu_from_file(menu_path)
    
    print_tytle('Консольний бот-помічник')
    
    section_name ='Робота з базою даних:\n'+ data_path.__str__()
    print_section(section_name)
    print_tytle('Вітаємо в консольному боті-помічникові!')
    # Основний цикл програми
    while True:    
        print_menu(menu)
        user_input = input('Введіть команду: ')
        command, *args = parse_input(user_input)
        if command in ['close', 'exit']:
                if changes:
                    rewrite_contacts(data_path, contacts)
                print_end("До побачення!")
                break
        elif command == 'hello':
            print('Чим я можу допомогти?\n')
        elif command == 'all':
            print_contacts(contacts)
        elif command == 'add':
            print(add_contact(args, contacts))
            changes = True
        elif command == 'change':
            print(change_contact(args, contacts))
            changes = True
        elif command == 'del' and args:
            print(del_contact(args, contacts))
            changes = True
        else:
            print('Невірна команда\n')
    
    
# ----------------------------------------------------   
# Точка входу
# print_serv_msg(f'Check: __name__ = {__name__}') # Перевірка коректності входу, для головного скрипта - "__main__"
if __name__ == '__main__':
    main()
else:
    print_error('Помилка виконання скрипта!')