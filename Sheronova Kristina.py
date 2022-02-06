from math import *
def one(s):
    words = s.split(' ')
    k = 0
    for i in range(1, len(words)+1):
        for j in range(k, len(words)):
            if str(i) in words[j]:
                words[i-1], words[j] = words[j], words[i-1]
                print(str(words[i-1]).replace(str(i), ''), end=' ')
                break
        k += 1


def two(a, b, c, w, h):
    if (a <= h and b <= w) or (a <= w and b <= h) or (a <= h and c <= w) or (a <= w and c <= h) or (c <= h and b <= w) or (c <= w and b <= h):
        print('true')
    else:
        print('false')

# третья задача не вышла. были идеи считать через выбор удобного варианта
# или, как ниже, через несколько случаев расположения
# ни один вариант не имел успеха в реализации
sp = input()
fl = input()
a_sp = sp[0]
a_fl = fl[0]
n_sp = int(sp[1])
n_fl = int(sp[1])
alfa = 'ABCDEFGH'
s = alfa.find(sp[0])
f = alfa.find(fl[0])
print(n_sp, n_fl, s, f, alfa[s-1])
if n_fl == n_sp and ((s - 1 == f) or (s-2 == f) or (s+1 == f) or (s+2 == f)):
    if s - 1 == f or (s+1 == f):
        print(fl)
    elif s-2 == f:
        print(alfa[s-1] + str(n_fl), fl, sep='-')
    elif s+2 == f:
        print(alfa[s+1] + str(n_fl), fl, sep='-')
elif abs(s-f) == 4:
    for i in range(n_sp, -1, -1):
        print(a_sp + str(i), end='-')
    for i in range(1, n_fl):
        print(a_fl + str(i), end='-')
elif s - f == 0:
    if n_sp > n_fl:
        for i in range(n_sp, n_fl-1, -1):
            print(a_sp + str(i), end='-')
    else:
        for i in range(n_sp, n_fl+1):
            print(a_sp + str(i), end='-')
else:
    if n_sp > n_fl:
        for i in range(n_sp, n_fl-1, -1):
            print(a_sp + str(i), end='-')
        for i in range()






