from functools import reduce
my_file = open("123.txt", encoding="utf-8")
text = my_file.read()
my_file.close()

text = text.split()
print(text)

s = 'aaaabbbaccccdd'
new_s = [s[0]]
for i in s[1:]:
    if True:
        new_s.append(i)

print(''.join(new_s))

>> >

def f(s):
    out = ''
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]: out += s[i]
    if s[-1] != out[-1]: out += s[-1]
    return out

>> > f('qqqwwwqw')
'qwqw'
>> >



s = "wfewgefedgfggf"
r = "".join(set(s))
print(r)



s_in = 'aaaabbbaccccdd'
r = [None]
for c in s_in:
    if c != r[-1]: r.append(c)
s_out = ''.join(r[1:])
print(s_out)



x = 'aaaabbbaccccdd'
y = []
for i in x :
    if i not in y:
        y.append(i)
print(''.join(y))

x = 'aaaabbbaccccdd'
y = []
for i in x:
    if i not in y:
        y.append(i)
print(''.join(y))

print(''.join(set(x)))
abcd

dabc