def format_string(string, length):
    number_of_seats = (length - len(string)) // 2
    if len(string) < int(length):
        return f"{'9'*number_of_seats}{string}"
    else:
        return string
    

print(format_string("12345", 15))