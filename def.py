def f(a,b,z):
    if z == '+':
        s = a + b
    elif z == '/':
        s = a / b
    else:
        if z == '-':
            s = a - b
        elif z == '*':
            s = a*b
        else:
            return 'Неверный ввод данных'

    return s

d = f(10, 10, '+')
print(d)
