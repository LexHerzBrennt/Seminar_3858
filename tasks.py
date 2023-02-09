def zadacha_2(a, b):
    print('Zadacha 2:', end=' ')
    if a > b:
        return print('max =', a)
    elif a < b:
        return print('max =', b)
    else:
        return print('Numbers are equal')

def zadacha_4(a, b, c):
    print('Zadacha 4:', end=' ')
    lst = [a, b, c]

    #partially use bubble sorting
    for i in range(2):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]

    return print('max =', lst[-1])

def zadacha_6(a):
    print('Zadacha 6:', end=' ')
    return print('Yes' if a % 2 == 0 else 'No')

def zadacha_8(a):
    print('Zadacha 8:', end=' ')
    for i in range(1, a + 1):
        print(f'{i} ' if i % 2 == 0 else '', end='')


zadacha_2(5, 7)
zadacha_4(44, 5, 78)
zadacha_6(4)
zadacha_8(8)