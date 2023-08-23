# Два слова похожи, если отличаются только одной буквой. Функция проверяет, похожи строки, или нет.
def is_similar(word1, word2):
    pass #len



def test_is_similar():
    assert is_similar('пень', 'лень') == True
    assert is_similar('вторник', 'вторнек') == True
    assert is_similar('город', 'огород') == True
    assert is_similar('перец', 'конец') == False
    assert is_similar('вор', 'ворон') == False
    assert is_similar('перец') == False

test_is_similar()