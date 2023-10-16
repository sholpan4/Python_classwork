import re

pattern = r'(?P<month>[A-Za-z]+) (?P<day>\d+)'
text = "June 24, Seprember 20, October 10"

matched = re.search(pattern, text)
if matched:
    print("Группа 0", matched.group(0))
    print("Группа 1", matched.group('month'))
    print("Группа 2", matched.group('day'))