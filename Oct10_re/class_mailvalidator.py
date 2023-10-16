import sys
import re

with open(sys.argv[1], 'r') as data_file:
    data = data_file.read().split()

pattern = r"\w[\w\.-_]+\w@\w[\w\.-_]+\.[a-zA-Z]{2,3}"
for email in data:
    matched = re.search(pattern, email)
    # Вариант 1
    # if not matched: 
    #     print("Некорректный адрес: ", email)

    # Вариант 2
    if matched:
        data[data.index(email)] = ''

data = list(filter(lambda x: x != '', data))
print(*data, sep="\n")


