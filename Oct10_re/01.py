import re

pattern = r'a{1,2}...e'
text = 'I ahave an apple'
matched = re.search(pattern, text)
if matched:
    print(f'Find:', matched.group())

matches = re.findall(pattern, text)
if matches:
    print(f'Find:', matches)