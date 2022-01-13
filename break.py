c = 1
summ = 0
while c > 0:
    num = input('Введите число:')
    if num == 'stop':
        c = 0
    else:
        num = int(num)
        if num % 2 == 0:
            summ += 1
print('четных:', summ)
