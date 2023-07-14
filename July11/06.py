



tr_ing = input("Type any word or sentence: ")

for i in str_ing:
if i not in Dict:
Dict[i]=1
else:
Dict[i]+=1
print(Dict)

s = 'Из входной строки определить 3 наиболее часто встречаемых символа в ней.'


def top3(s):
    t = ([(s.count(i), i) for i in s])
    return (sorted(set(t))[::-1][:3])


print(top3(s))





def top3(s):
    t = ([(s.count(i), i) for i in s if i != ' '])
    return (sorted(set(t))[::-1][:3])