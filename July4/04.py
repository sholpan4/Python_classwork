from functools import reduce
my_file = open("book.txt", encoding="utf-8")

text = my_file.read()
my_file.close()

print(text)


address = list(reduce(lambda acc, x: acc + [x] for x in range(len(word[i])) == ".com", text.split(), []))
print(address)
