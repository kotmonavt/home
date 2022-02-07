# функция первого задания
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


# функция второго задания
def two(a, b, c, w, h):
    if (a <= h and b <= w) or (a <= w and b <= h) or (a <= h and c <= w) or (a <= w and c <= h) or (c <= h and b <= w) \
            or (c <= w and b <= h):
        print('true')
    else:
        print('false')


# третье до конца не удалось решить, но попытки ниже
# что-то даже считает, но в одном условии зацикливается, ментального здоровья не хватило на решение проблемы
# была идея разделить на несколько вариантов положения паука и мухи и от каждой ситуации отдельный алгоритм
# т.е. если мы на одной радиане или на не соседних (больше чем соседняя или через одну радиану)
# то мы приходим в центр и выходим на нужную радиану, так выгоднее
# если на соседних (соседняя и через одну), то выгоднее спуститься до номера мухи и по кругу пройти до нужной точки
# если муха выше паука - идем от мухи, а потом устраиваем реверс пути
# можно и по умному, но я таких способов не знаю( пыталась доступными для меня методами, как просто мат. задачу решить

def three(sp, fl):
    a_sp = sp[0]
    a_fl = fl[0]
    n_sp = int(sp[1])
    n_fl = int(fl[1])
    alfa = 'ABCDEFGH'
    s = alfa.find(sp[0])
    f = alfa.find(fl[0])
    # создаем стоку с путем:
    st = ''
    # если наш паук находится "выше" по цифре, чем муха:
    if n_sp >= n_fl:
        # если паук от мухи меньше, чем в трех радианах, т.е. в двух соседних либо, через одну радиану
        # в таком случае выгоднее спуститься до нужной цифры и пройти до нужной радианы по основанию треугольника
        if alfa[s+2] == a_fl or alfa[s-2] == a_fl or alfa[s+1] == a_fl or alfa[s-1] == a_fl or alfa[s+6] == a_fl or \
                alfa[s+7] == a_fl or alfa[s-6] == a_fl or alfa[s-7] == a_fl:
            print(alfa[s] + str(n_sp), end='-')
            while n_sp > n_fl:
                n_sp -= 1
                print(alfa[s]+str(n_sp), end='-')
            while s != f:
                if alfa[s+2] == a_fl or alfa[s+1] == a_fl or alfa[s-6] == a_fl or alfa[s-7] == a_fl:
                    s += 1
                    print(alfa[s] + str(n_sp), end='-')
                elif alfa[s-2] == a_fl or alfa[s-1] == a_fl or alfa[s+6] == a_fl or alfa[s+7] == a_fl:
                    s -= 1
                    print(alfa[s] + str(n_sp), end='-')
        else:
            # Если мы больше чем в двух радианах или на той же, или на продолжении нашей радианы
            for i in range(n_sp, -1, -1):
                print(alfa[s]+str(i), end='-')
            for i in range(1, n_fl+1):
                print(alfa[f]+str(i), end='-')
    # если паук ниже мухи, двигаемся от мухи к пауку по прошлой стратегии и потом реверсим путь
    # реверсим кроме последнего else, ибо там все равно мы по прямой двигаемся
    if n_sp < n_fl:
        if alfa[s+2] == a_fl or alfa[s-2] == a_fl or alfa[s+1] == a_fl or alfa[s-1] == a_fl or alfa[s+6] == a_fl or \
                alfa[s+7] == a_fl or alfa[s-6] == a_fl or alfa[s-7] == a_fl:
            st += alfa[f] + str(n_fl) + '-'
            while n_fl > n_sp:
                n_fl -= 1
                st += alfa[f]+str(n_fl) + '-'
            while f != s:
                if alfa[s+2] == a_fl or alfa[s+1] == a_fl or alfa[s-6] == a_fl or alfa[s-7] == a_fl:
                    f += 1
                    st += alfa[f] + str(n_sp) + '-'
                elif alfa[s - 2] == a_fl or alfa[s - 1] == a_fl or alfa[s + 6] == a_fl or alfa[s + 7] == a_fl:
                    f -= 1
                    st += alfa[f] + str(n_sp) + '-'
        else:
            for i in range(n_sp, -1, -1):
                print(alfa[s]+str(i), end='-')
            for i in range(1, n_fl+1):
                print(alfa[f]+str(i), end='-')
        print(st[::-1])
