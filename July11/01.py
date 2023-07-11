str = 'rtijf'

if str.startswith('abc'):
    result = str.replace('abc', 'www')
else:
    result = str + '.com'

print(result)