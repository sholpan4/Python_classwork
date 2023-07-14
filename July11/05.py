
2
3
4
5
6
7
8
9
str = 'йцуйцуфыва'

def first_last(letter, st):
    _first = st.find(letter)
    _last = st.rfind(letter)

    return (None, None) if _last == -1 else (_first, _last)

print(first_last('у', str)) # (2, 5)




def first_last(let, s):
    if ( lis := [ i for i in range( len(s) ) if s[i] == let ] ):
        return lis[0], lis[-1]
    return None, None
#==============================================================================
print( *first_last( 'а', 'абракадабра' ) )