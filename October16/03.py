import os
from functools import lru_cache

@lru_cache
def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()

print(read_file('text.txt'))
os.remove('text.txt')
print(read_file('text.txt'))