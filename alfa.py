a = input('Введите слово:')
s = input('Введите проверку буквы:')
su = 0
for i in a:
    if i == s:
        su += 1
print('В вашем слове', su, 'букв', s)
