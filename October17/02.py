def my_func():
    yield 'hello'
    yield 'how r u?'
    yield 'bye'
    yield 'Yooooo'

# it = my_func()
# next(it)

for x in my_func():
    print(x)

it = my_func()
a = tuple(map(lambda x: x.upper(), it))
print(a)