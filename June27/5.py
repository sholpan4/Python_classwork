names = ["Артём", "Руслан", "Ансар", "Глеб", "Шолпан", "Латифа", "Даниил"]
marks = [10, 1, 11, 5, 3, 4, 7]
num = [int(x) for x in marks]
pairs = list(zip(names, marks))
group_a = []
group_c = []

def makes_groups(marks):
    for x in marks:
        if x >= 5:
            group_a.append(x)
        else:
            group_c.append(x)

makes_groups(marks)

print(group_a, group_c, pairs)

