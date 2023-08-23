# Функция возвращает аббревиатуру от переданной строки
def get_abbr(phrase):
    if phrase == '':
        return ''
    abr = ''
    text = phrase.title()
    a = text.split(' ')
    for x in a:
        if x[0].isupper():
            abr += x[0]
        elif x[0] == '-':
            abr += x[0]
    return abr



def test_get_abbr():
    assert get_abbr('семь раз отмерь - один раз отрежь') == 'СРО-ОРО'
    assert get_abbr("don't repeat yourself") == 'DRY'
    assert get_abbr('') == ''

test_get_abbr()