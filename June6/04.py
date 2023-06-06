import random

def get_random_int(min, max):
    
    result = random.random() * (max - min) + min

    return int(result)

#num = random.random()
num = get_random_int (1000, 10000)
print(num)