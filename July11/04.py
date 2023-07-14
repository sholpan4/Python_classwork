from functools import reduce
my_file = open("123.txt", encoding="utf-8")
text = my_file.read()
my_file.close()

text = text.split()
print(text)

_in = 'aaaabbbaccccdd'
r = [None]
for c in s_in:
    if c != r[-1]: r.append(c)
s_out = ''.join(r[1:])
print(s_out)