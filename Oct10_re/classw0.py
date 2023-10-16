import re 

pattern = r'\d[A-Z]{2,4}...e'

text = 'I 1DOhave an 156546545TTTTDgere'
matched = re.search(pattern, text)
if matched:
    print('Найдено совпадение: ', matched.group())

matches = re.findall(pattern, text)
print("Совпадения: ", matches)

