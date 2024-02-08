from collections import Counter

file_to_path = 'log_file.txt' 

def parse_log_line(line: str) -> dict: # приймає рядок з логу як вхідний параметр і повертає словник з розібраними компонентами: дата, час, рівень, повідомлення.
    line = line.split(" ")
    message = " ".join(line[3:])
    outdict = {"data": line[0], "time": line[1], "level": line[2], "message": message }
    return outdict

def load_logs(file_path: str) -> list: #відкриває файл, читає кожен рядок і застосовує на нього функцію parse_log_line
    outlist = []
    with open(file_path, "r", encoding = "UTF-8") as log_line:        
        for line in log_line:
            parse_line = parse_log_line(line)
            outlist.append(parse_line)
    return outlist     
   
outlist_1 = load_logs(file_to_path)


def filter_logs_by_level(logs: list, level: str) -> list: # Фільтрація за рівнем логування
    level_finde ="level"
    return [item[level_finde] for item in logs]

print(filter_logs_by_level(outlist_1, "ERROR"))  
    



def count_logs_by_level(outlist: list) -> dict: # проходить по всім записам і підраховує кількість записів для кожного рівня логування
    count_dict_key = "level"
    count_dict = Counter(item[count_dict_key] for item in outlist)
    return (count_dict)

# print(count_logs_by_level(outlist_1))

# def display_log_counts(counts: dict): # форматує та виводить результати підрахунку в читабельній формі.
#     return 

if __name__ == "__main__":    
    path_to_file = 'log_file.txt'     
    


# # Ваш скрипт повинен вміти обробляти різні види помилок, такі як відсутність файлу або помилки при його читанні. Використовуйте блоки try/except для обробки виняткових ситуацій.

