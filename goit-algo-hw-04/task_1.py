def total_salary(file_path):
    total_salary = 0
    num_developers = 0
    try:
        with open(file_path, "r", encoding = "UTF-8") as list_salary:
            for line in list_salary:
                parts = line.split(",")
                if len(parts)==2:                    
                    salary = int(parts[1].strip()) 
                    total_salary += salary
                    num_developers += 1
    except FileNotFoundError:
        print(f"file  {file_path} not found.")
        return None
    if num_developers == 0:
        print("The file is in the wrong format or is empty.")
        return None
    average_salary = int(total_salary / num_developers)
    print (f"Загальна сума заробітної плати: {total_salary}\nСередня заробітна плата розробників: {average_salary}")

total_salary("list_salary.txt")
