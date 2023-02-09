def zadacha_25(a, b):
    print('Zadacha 25:', end=' ')
    res = 1
    for i in range(b):
        res *= a
    print(res)

def zadacha_27(num):
    print('Zadacha 27:', end=' ')
    res = 0
    for i in str(num):
        res += int(i)
    print(res)

def zadacha_29(*nums):
    print('Zadacha 29:', end=' ')
    lst = []
    for i in nums:
        lst.append(i)
    print(lst)


zadacha_25(3, 5)
zadacha_27(452)
zadacha_29(3, 34, 28, 9)