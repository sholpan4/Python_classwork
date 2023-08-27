# Функция принимает двумерный массив, содержащий буквы, и выводит два слова, составленные из букв главной и побочной диагоналей.
def get_diag_words(array):
    first_list = ''
    second_list = ''
    if not array:
        return ''
    for r in range(len(array)):
        #print(array[i])
        for c in range(len(array[r])):
            if r == c:
                first_list += array[r][c]
            if c == len(array[r])-1-r:
                second_list += array[r][c]    
                
            
    return first_list + ' ' + second_list
   
   
def test_get_diag_words():
    input = [['ж','ф','л'],
             ['р','и','а'],
             ['с','з','л']]
    expect = "жил лис"
    assert get_diag_words(input) == expect

    input = [['б','ф','л','т',']','в'],
             ['р','е','а','о','о','щ'],
             ['е','и','л','р','э','к'],
             ['г','ы','о','а','ф','о'],
             ['н','н','а','а','я','ч'],
             ['а','з','л','ц','в',' ']]
    expect = "белая  ворона"
    assert get_diag_words(input) == expect

    input = []
    expect = ""
    assert get_diag_words(input) == expect

test_get_diag_words()