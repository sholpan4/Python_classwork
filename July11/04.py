from functools import reduce
my_file = open("123.txt", encoding="utf-8")
text = my_file.read()
my_file.close()

text = text.split()
print(text)


def f(word):
    out = ''
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            out += word[i]
    if word[-1] != out[-1]:
        out += word[-1]
    return out

print(f(text))
