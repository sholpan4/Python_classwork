# Функция принимает на вход словарь, содержащий ФИО и сумму задолженности за коммунальные услуги,
# а возвращает словарь с общим количеством должников и суммой всех долгов, с ключами debtors и total.
def get_debts(people):
    debtors = 0
    for value in people:
        total = sum(value)
        debtors += 1
    return {'debtors': debtors, 'total': total}



def test_get_debts():
    input = {'Сырым': 0, 'Адилхан': 100, 'Зульфия': 250}
    expect = {'debtors': 2, 'total': 350}
    assert get_debts(input) == expect

    input = {}
    expect = {'debtors': 0, 'total': 0}
    assert get_debts(input) == expect

test_get_debts()