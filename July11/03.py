my_file = open("123.txt", encoding="utf-8")
text = my_file.read()
my_file.close()

text = text.split()

for x in text:
    if x.isdigit():
        msg = len(x)

print(msg)
