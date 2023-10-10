import sys
import re
print(sys.argv)

with open(sys.argv[1]) as file:
    data = file.read().split()

pattern = r'\w[\w\.-]+\w@\w[\w\.-]+\.[a-zA-Z]{2,3}'
for email in data:
    matched = re.search(pattern, email)
    if matched:
        print("Find not matched address:", email)