from functools import reduce

my_file = open("123.txt", encoding="utf-8")
text = my_file.read()
my_file.close()

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
text = text.split()
smallest_len = []

for x in text:
    word_len = len(x)
    if word_len < smallest_len:

        return word_len
    else:
        return smallest_len

print(smallest_len)
# shortest = reduce(lambda acc, x: acc + [x] if len(acc) > len(x) else acc, text, [])


# print(a)