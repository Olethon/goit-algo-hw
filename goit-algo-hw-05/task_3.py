from collections import Counter

file_to_path = 'log_file.log' 

def parse_log_line(line: str) -> dict: # приймає рядок з логу як вхідний параметр і повертає словник з розібраними компонентами: дата, час, рівень, повідомлення.
    line = line.split(" ")    
    message = " ".join(line[3:])
    modified_message = message.replace("\n", '')
    outdict = {"data": line[0], "time": line[1], "level": line[2], "message": modified_message }
    return outdict

def load_logs(file_path: str) -> list: #відкриває файл, читає кожен рядок і застосовує на нього функцію parse_log_line
    outlist = []
    with open(file_path, "r", encoding = "UTF-8") as log_line:        
        for line in log_line:
            parse_line = parse_log_line(line)
            outlist.append(parse_line)
    return outlist 

def filter_logs_by_level(logs: list, level: str) -> list: # Фільтрація за рівнем логування
    print(f"Деталі логів для рівня '{level}'")  
    filter_logs = [f"{log['data']} {log['time']} - {log['message']}" for log in logs if log.get("level") == level]       
    for  element in filter_logs:
        print(element)
           
def count_logs_by_level(outlist: list) -> dict: # проходить по всім записам і підраховує кількість записів для кожного рівня логування
    count_dict_key = "level"
    count_dict = dict(Counter(item[count_dict_key] for item in outlist))
    return count_dict


def display_log_counts(counts_dict: dict): # форматує та виводить результати підрахунку в читабельній формі.
    for level, count in counts_dict.items():
        print(f"{level.ljust(17)}| {str(count).rjust(9)}")

outlist_1 = load_logs(file_to_path)
# print(outlist_1)
# filter_logs_by_level(outlist_1, "INFO") 
qq = (count_logs_by_level(outlist_1))

if __name__ == "__main__":
    display_log_counts(qq)    














# Ваш скрипт повинен вміти обробляти різні види помилок, такі як відсутність файлу або помилки при його читанні. Використовуйте блоки try/except для обробки виняткових ситуацій.

