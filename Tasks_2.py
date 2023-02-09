def zadacha_19(num):
    print('Zadacha 19:', end=' ')
    if num < 10000 or 99999 < num:
        print('Number is not five-digit')
        return
    num_str = str(num)
    if num_str[0] == num_str[-1] and num_str[1] == num_str[-2]:
        print('Yes')
        return
    print('No')

def zadacha_21(a, b):
    print('Zadacha 21:', end=' ')
    distance = pow((pow(a[0] - b[0], 2) +
                    pow(a[1] - b[1], 2) +
                    pow(a[2] - b[2], 2)), 0.5)
    print(round(distance, 2))

def zadacha_23(num):
    print('Zadacha 23:', end=' ')
    for i in range(1, num + 1):
        print(pow(i, 3), end=' ')


A = [3, 6, 8]
B = [2, 1, -7]

zadacha_19(14741)
zadacha_21(A, B)
zadacha_23(5)