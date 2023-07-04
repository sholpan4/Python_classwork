my_file = open("book.txt", encoding="utf-8")

text = my_file.read()
my_file.close()

print(text)

# a = list(text)
# a.reverse()
# a = "".join(a)
# list_a = a.split(",")
# words = text.split()

polindrome = " ".join(list(filter(lambda x: x == x[::-1], text.split())))  #можно лист не писать
print(polindrome)

# def is_polindrome(word):
#     return word == "".join(reversed(word))
#
# a = list(filter(is_polindrome, text.split())
# print(a)

