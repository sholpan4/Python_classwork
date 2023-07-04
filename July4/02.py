my_file = open("book.txt", encoding="utf-8")

#text = my_file.readlines()
text = my_file.read()
my_file.close()

print(text)

user_in_a = input("Укажите какое слово в тексте заменить:")
user_in_b = input("Укажите на какое слово заменить:")

# a = user_in_a.lower() and user_in_a.upper()
# b = user_in_b.lower() and user_in_b.upper()

# result = text.replace(a, b)
text = text.replace(user_in_a.lower(), user_in_b.lower())
text = text.replace(user_in_a.upper(), user_in_b.upper())
text = text.replace(user_in_a.capitalize(), user_in_b.capitalize())

print(text)