from functools import reduce

my_file = open("123.txt", encoding="utf-8")
text = my_file.read()
my_file.close()

text = text.split()
# smallest_len = 99999

# for x in text:
#     word_len = len(x)
#     if word_len < smallest_len:
#         smallest_len = word_len
# print(text)
# print(smallest_len)

shortest = reduce(lambda acc, x: len(x) if acc > len(x) else acc, text, 99999)
print(shortest)
# for x in text:
#     if len(x) <= 1:
#         msg = x
#     else:
#         msg = 'There is no short words'
# print(msg)

# def shortest(x, y):
#     if len(x) > len(y):
#         return y
#     else:
#         return x
# text = ' we love animals 2345'