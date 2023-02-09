def zadacha_10(num):
    print('Zadacha 10:', num % 100 // 10)

def zadacha_13(num):
    if -100 < num < 100:
        print('Number is one- or two-digit')
        return
    print('Zadacha 13:', str(num)[2])

def zadacha_15(day):
    print('Zadacha 15:', end=' ')
    if day < 1 or 7 < day:
        print('Impossible day of week')
        return
    print('Yes' if day == 6 or day == 7 else 'No')


zadacha_10(456)
zadacha_13(84921)
zadacha_15(6)