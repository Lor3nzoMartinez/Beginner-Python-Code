
L = ['dog', 3, 7, 2, 'cat','5']


def sep_ints_strgs (L):
    L_str = []
    L_int = []
    for element in L:
        if (type(element) == str):
            L_str.append(element)
        elif (type(element) == int):
            L_int.append(element)
    return L_str, L_int

L_s ,L_n = sep_ints_strgs(L)


print(L_s, 'is', (len(L_s)), ' characters long')

print(L_n, 'is', (len(L_n)), ' characters long')





def theFunc (L_s, L_n):
    for i in (L_s, L_n):
        print(L_s)


theFunc(L_s, L_n)
