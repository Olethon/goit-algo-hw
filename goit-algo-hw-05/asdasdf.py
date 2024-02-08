from collections import Counter

list_of_dicts = [
    {'колір': 'червоний', 'форма': 'кругла'},
    {'колір': 'синій', 'форма': 'кругла'},
    {'колір': 'червоний', 'форма': 'кругла'},
    {'колір': 'рожевий', 'форма': 'кругла'},
    {'колір': 'синій', 'форма': 'кругла'}
]
count_key = 'колір' 
count_dict = Counter( for item in list_of_dicts)

print(count_dict)